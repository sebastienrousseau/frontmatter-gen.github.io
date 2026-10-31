---
name: "Frontmatter Gen"
short_name: "frontmatter-gen"
title: "Pipeline Architecture: Zero-Copy Slicing & Parsing in Rust"
description: "Explore the four-stage architecture of frontmatter-gen: zero-copy fence extraction, format detection, budget-guarded parsing, and HTML meta tag synthesis."
keywords: "frontmatter-gen architecture, zero copy rust parser, noyalib yaml 1.2, ParseOptions budget, rust ssg engine"
author: "Sebastien Rousseau"
date: "2026-10-31"
language: "en-GB"
layout: "page"
permalink: "https://frontmatter-gen.com/architecture/"
logo: "https://cloudcdn.pro/clients/frontmatter-gen/v1/logos/frontmatter-gen.svg"
banner: "https://cloudcdn.pro/stocks/images/vadim-sherbakov-xS_RzdD5CFE-1200.webp"
banner_alt: "Frontmatter Gen: Pipeline Architecture and Zero-Copy Execution"
eyebrow: "Engine Internals"
headline: "Architecture & Pipeline Specifications"
lead: "How frontmatter-gen separates zero-copy slice extraction, format detection, DoS-guarded deserialization, and HTML meta tag synthesis."
category: "Documentation"
changefreq: "weekly"
date_published: "2026-01-15T00:00:00Z"
date_modified: "2026-10-31T00:00:00Z"
priority: "0.9"
slug: "architecture"
url: "/architecture/"
apple_touch_icon_sizes: "192x192"
schema_type: "TechArticle"
theme_color: "#22242f"
---

Frontmatter Gen is architected around a deterministic, four-stage pipeline that strictly decouples **zero-copy boundary slicing** from **typed deserialization** and **downstream synthesis**. Callers that only need to strip or inspect raw frontmatter pay zero heap allocation costs.

<h2>Four-Stage Processing Pipeline</h2>

<div class="process-grid my-4">
<article>
<b>01</b>
<h3>Boundary Slice</h3>
<p>Strip optional UTF-8 BOM (<code>\u{FEFF}</code>) and split <code>(raw_frontmatter, body)</code> as borrowed <code>&amp;str</code> slices in a single forward scan.</p>
<small>Zero Heap Allocations</small>
</article>
<article>
<b>02</b>
<h3>Format Classifier</h3>
<p>Classify raw header slices as <code>Format::Yaml</code>, <code>Format::Toml</code>, <code>Format::Json</code>, or <code>Format::Unsupported</code> without regex overhead.</p>
<small>O(n) Lexical Inspection</small>
</article>
<article>
<b>03</b>
<h3>Guarded Parser</h3>
<p>Deserialize into <code>Frontmatter</code> via <code>noyalib</code>, <code>toml</code>, or <code>serde_json</code> while enforcing <code>max_depth</code> and <code>max_keys</code> budgets.</p>
<small>Bounded Memory &amp; Depth</small>
</article>
<article>
<b>04</b>
<h3>Meta &amp; SSG Emit</h3>
<p>Synthesize entity-escaped HTML <code>&lt;meta&gt;</code> tags, round-trip between formats via <code>to_string</code>, or render Tera templates.</p>
<small>Deterministic Output</small>
</article>
</div>

<h2>Deterministic Pipeline Execution Trace</h2>

<p>The trace below illustrates how an input Markdown document flows through the four modules from raw <code>&amp;str</code> slice to escaped HTML meta tags:</p>

<div class="terminal-box my-4">
<div class="terminal-bar">
<span class="terminal-dot dot-red"></span>
<span class="terminal-dot dot-yellow"></span>
<span class="terminal-dot dot-green"></span>
<span class="terminal-title">pipeline-trace — frontmatter-gen v0.0.15</span>
</div>
<div class="terminal-body">
<div class="t-line"><span class="t-key">Input:</span> &amp;str (<span class="t-val">&quot;---\ntitle: Hello\ncountry: NO\n---\n# Markdown Body&quot;</span>)</div>
<div class="t-line"><span class="t-comment">[Stage 1: extractor::extract_raw_frontmatter] Strip optional UTF-8 BOM • Locate closing --- fence</span></div>
<div class="t-line"><span class="t-comment">[Stage 1: zero-copy output] raw = &quot;title: Hello\ncountry: NO&quot; | body = &quot;\n# Markdown Body&quot; (0 heap allocs)</span></div>
<div class="t-line"><span class="t-comment">[Stage 2: extractor::detect_format] Heuristic scan -&gt; Format::Yaml</span></div>
<div class="t-line"><span class="t-comment">[Stage 3: parser::parse_with_options] noyalib YAML 1.2 parse • Check max_depth &amp; max_keys invariants</span></div>
<div class="t-line"><span class="t-comment">[Stage 4: meta::generate_metatags] Emit escaped &lt;meta name=&quot;title&quot;&gt; and &lt;meta name=&quot;country&quot; content=&quot;NO&quot;&gt;</span></div>
<div class="t-line"><span class="t-key">Status:</span> <span class="t-val">OK</span> • <span class="t-key">Extractor Latency:</span> <span class="t-val">~120 ns</span> • <span class="t-key">Unsafe Blocks:</span> <span class="t-val">0</span></div>
</div>
</div>

<h2>Stage 1: Zero-Copy Boundary Slicing (<code>src/extractor.rs</code>)</h2>

<p><code>extractor::extract_raw_frontmatter(content: &amp;str) -&gt; Result&lt;(&amp;str, &amp;str), ParseError&gt;</code> operates directly on the caller's UTF-8 string slice:</p>

<ul>
<li><strong>UTF-8 BOM Handling:</strong> Automatically strips a leading <code>\u{FEFF}</code> byte-order mark before inspecting opening delimiters.</li>
<li><strong>Fence Scanning:</strong> Recognizes <code>---</code> (YAML) and <code>+++</code> (TOML) across both LF (<code>\n</code>) and CRLF (<code>\r\n</code>) line endings.</li>
<li><strong>Balanced JSON Braces:</strong> Tracks nesting depth for leading <code>{ ... }</code> blocks while ignoring braces inside string literals and escape sequences.</li>
</ul>

<h2>Stage 2 &amp; 3: Format Detection &amp; Budgeted Parsing (<code>src/parser.rs</code>)</h2>

<p>Once extracted, <code>detect_format</code> routes the raw slice to one of three pure-Rust parsers while <code>ParseOptions</code> enforces structural invariants:</p>

<ul>
<li><strong>YAML 1.2 Engine (<code>noyalib</code>):</strong> Preserves explicit YAML tags as <code>Value::Tagged(tag, Box&lt;Value&gt;)</code> and avoids YAML 1.1 boolean coercion.</li>
<li><strong>TOML 1.1 Engine (<code>toml</code>):</strong> Converts TOML tables and native ISO 8601 datetimes into canonical <code>Frontmatter</code> entries.</li>
<li><strong>JSON Engine (<code>serde_json</code>):</strong> Parses RFC 8259 JSON objects with exact integer and floating-point preservation.</li>
<li><strong>DoS Budget Checks:</strong> <code>check_depth</code> and <code>count_keys</code> validate nesting depth and total key counts against <code>ParseOptions</code>.</li>
</ul>

<div class="doc-visual-card">
<picture>
<source media="(max-width: 40rem)" srcset="https://cloudcdn.pro/stocks/images/vadim-sherbakov-xS_RzdD5CFE-320.webp 320w, https://cloudcdn.pro/stocks/images/vadim-sherbakov-xS_RzdD5CFE-640.webp 640w, https://cloudcdn.pro/stocks/images/vadim-sherbakov-xS_RzdD5CFE-1200.webp 1200w" sizes="100vw">
<img src="https://cloudcdn.pro/stocks/images/vadim-sherbakov-xS_RzdD5CFE-1200.webp" alt="Frontmatter Gen pipeline architecture and deterministic execution" width="1200" height="675" loading="lazy" />
</picture>
<div class="doc-visual-caption">Modular compilation: zero-copy slicing, YAML 1.2 / TOML 1.1 / JSON parsing, and opt-in CLI and SSG feature flags.</div>
</div>

<h2>Stage 4: Meta Synthesis &amp; Feature Isolation</h2>

<p>To keep compile times and dependency trees minimal for library consumers, heavy application dependencies are gated behind Cargo features:</p>

<div class="table-responsive my-3">
<table class="visage-table">
<thead>
<tr>
<th>Feature Flag</th>
<th>Default</th>
<th>Included Modules &amp; Dependencies</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>default = []</code></td>
<td>Yes</td>
<td>Core library (<code>extractor</code>, <code>parser</code>, <code>meta</code>, <code>error</code>, <code>noyalib</code>, <code>toml</code>, <code>serde_json</code>).</td>
</tr>
<tr>
<td><code>cli</code></td>
<td>Opt-in</td>
<td>Adds the <code>fmg</code> binary target, <code>clap</code> CLI parser, <code>tokio</code> async runtime, and structured logging.</td>
</tr>
<tr>
<td><code>ssg</code></td>
<td>Opt-in</td>
<td>Adds <code>config</code>, <code>engine</code>, <code>fs</code>, <code>markdown</code>, and <code>template</code> modules (<code>tera</code> + <code>comrak</code>).</td>
</tr>
</tbody>
</table>
</div>
