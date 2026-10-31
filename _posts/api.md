---
name: "Frontmatter Gen"
short_name: "frontmatter-gen"
title: "API & CLI Reference: Rust Types, Functions & fmg Commands"
description: "Complete API reference for frontmatter-gen v0.0.15: Frontmatter, Value, Format, ParseOptions, extract_raw_frontmatter, generate_metatags, and the fmg CLI."
keywords: "frontmatter_gen api, Frontmatter struct, Value enum, ParseOptions, generate_metatags, fmg cli reference, rust docs"
author: "Sebastien Rousseau"
date: "2026-10-31"
language: "en-GB"
layout: "page"
permalink: "https://frontmatter-gen.com/api/"
logo: "https://cloudcdn.pro/clients/frontmatter-gen/v1/logos/frontmatter-gen.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Frontmatter Gen: Zero-Copy Frontmatter Extraction and Parsing in Rust"
eyebrow: "Developer Reference"
headline: "Rust API & CLI Reference"
lead: "Public types, zero-copy extractor functions, budget-guarded parsers, HTML meta tag synthesis, and CLI flags."
category: "Documentation"
changefreq: "weekly"
date_published: "2026-01-15T00:00:00Z"
date_modified: "2026-10-31T00:00:00Z"
priority: "0.9"
slug: "api"
url: "/api/"
apple_touch_icon_sizes: "192x192"
schema_type: "TechArticle"
theme_color: "#22242f"
---

Frontmatter Gen exposes a compact, strongly-typed Rust API alongside the `fmg` command-line binary. Every public function returns explicit `Result` types (`ParseError`, `MetaError`, `ConfigError`, `EngineError`) with zero panics on malformed user input. Full generated rustdoc is hosted on [docs.rs/frontmatter-gen](https://docs.rs/frontmatter-gen).

<div class="step-item">
<div class="step-header">
<span class="step-badge">01</span>
<h2 class="step-title">Core Library Interface &amp; Value Model</h2>
</div>
<p>Extract and inspect frontmatter values using the unified <code>Frontmatter</code> map and recursive <code>Value</code> enum across YAML 1.2, TOML 1.1, and JSON:</p>

<div class="terminal-box my-3">
<div class="terminal-bar">
<span class="terminal-dot dot-red"></span>
<span class="terminal-dot dot-yellow"></span>
<span class="terminal-dot dot-green"></span>
<span class="terminal-title">rust — frontmatter_gen::extract &amp; Value</span>
</div>
<div class="terminal-body">
<div class="t-line"><span class="t-key">use</span> frontmatter_gen::{extract, Format, Frontmatter, Value};</div>
<div class="t-line"><span class="t-key">use</span> frontmatter_gen::parser::to_string;</div>
<div class="t-line">&nbsp;</div>
<div class="t-line"><span class="t-comment">&#35; Extract Frontmatter map and borrowed Markdown body</span></div>
<div class="t-line"><span class="t-key">let</span> (fm, body): (Frontmatter, &amp;str) = extract(content)?;</div>
<div class="t-line">&nbsp;</div>
<div class="t-line"><span class="t-comment">&#35; Inspect typed scalars, arrays, objects, or YAML 1.2 tags</span></div>
<div class="t-line"><span class="t-key">let</span> title: Option&lt;&amp;str&gt; = fm.get(<span class="t-val">&quot;title&quot;</span>).and_then(Value::as_str);</div>
<div class="t-line"><span class="t-key">let</span> draft: Option&lt;bool&gt; = fm.get(<span class="t-val">&quot;draft&quot;</span>).and_then(Value::as_bool);</div>
<div class="t-line"><span class="t-key">let</span> tagged = fm.get(<span class="t-val">&quot;custom&quot;</span>).and_then(Value::as_tagged);</div>
<div class="t-line">&nbsp;</div>
<div class="t-line"><span class="t-comment">&#35; Serialize Frontmatter into YAML, TOML, or JSON</span></div>
<div class="t-line"><span class="t-key">let</span> json_out: String = to_string(&amp;fm, Format::Json)?;</div>
</div>
</div>

<p>Core types and helper methods exported at the crate root:</p>

<div class="table-responsive my-3">
<table class="visage-table">
<thead>
<tr>
<th>Type / Method</th>
<th>Signature</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>extract</code></td>
<td><code>fn(&amp;str) -&gt; Result&lt;(Frontmatter, &amp;str), ParseError&gt;</code></td>
<td>Extracts and parses frontmatter in one pass, returning the parsed map and borrowed body slice.</td>
</tr>
<tr>
<td><code>Frontmatter</code></td>
<td><code>pub struct Frontmatter(pub HashMap&lt;String, Value&gt;)</code></td>
<td>Case-sensitive map implementing <code>Deref</code> and <code>DerefMut</code> to <code>HashMap&lt;String, Value&gt;</code>.</td>
</tr>
<tr>
<td><code>Value</code></td>
<td><code>Null | Bool | Number | String | Array | Object | Tagged</code></td>
<td>Format-agnostic recursive value enum with <code>Value::Tagged(String, Box&lt;Value&gt;)</code> for YAML 1.2 tags.</td>
</tr>
<tr>
<td><code>Value::as_str</code> / <code>as_bool</code></td>
<td><code>fn(&amp;self) -&gt; Option&lt;...&gt;</code></td>
<td>Borrows the underlying string, boolean, <code>f64</code>, <code>i64</code>, <code>u64</code>, array, object, or tagged pair.</td>
</tr>
<tr>
<td><code>Format</code></td>
<td><code>Yaml | Toml | Json | Unsupported</code></td>
<td>Identifies the detected or target serialization format for frontmatter blocks.</td>
</tr>
</tbody>
</table>
</div>
</div>

<div class="step-item">
<div class="step-header">
<span class="step-badge">02</span>
<h2 class="step-title">Zero-Copy Extractor &amp; Budgeted Parser Modules</h2>
</div>
<p>The <code>extractor</code>, <code>parser</code>, and <code>meta</code> modules give fine-grained control over zero-copy slicing, structural DoS budgets, and HTML meta tag generation:</p>

<div class="table-responsive my-3">
<table class="visage-table">
<thead>
<tr>
<th>Module Function</th>
<th>Signature</th>
<th>Purpose &amp; Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>extractor::extract_raw_frontmatter</code></td>
<td><code>fn(&amp;str) -&gt; Result&lt;(&amp;str, &amp;str), ParseError&gt;</code></td>
<td>Zero-copy split returning <code>(raw_frontmatter, body)</code> borrowed directly from <code>content</code>.</td>
</tr>
<tr>
<td><code>extractor::detect_format</code></td>
<td><code>fn(&amp;str) -&gt; Format</code></td>
<td>Classifies raw frontmatter as <code>Format::Json</code>, <code>Format::Toml</code>, <code>Format::Yaml</code>, or <code>Format::Unsupported</code>.</td>
</tr>
<tr>
<td><code>parser::parse</code></td>
<td><code>fn(&amp;str, Format) -&gt; Result&lt;Frontmatter, ParseError&gt;</code></td>
<td>Parses a raw frontmatter slice using default <code>ParseOptions</code>.</td>
</tr>
<tr>
<td><code>parser::parse_with_options</code></td>
<td><code>fn(&amp;str, Format, &amp;ParseOptions) -&gt; Result&lt;Frontmatter, ParseError&gt;</code></td>
<td>Parses raw frontmatter while enforcing <code>validate</code>, <code>max_depth</code>, and <code>max_keys</code> limits.</td>
</tr>
<tr>
<td><code>parser::to_string</code></td>
<td><code>fn(&amp;Frontmatter, Format) -&gt; Result&lt;String, ParseError&gt;</code></td>
<td>Serializes a <code>Frontmatter</code> map into YAML, TOML, or pretty-printed JSON.</td>
</tr>
<tr>
<td><code>meta::generate_metatags</code></td>
<td><code>fn(&amp;Frontmatter) -&gt; MetaResult&lt;String&gt;</code></td>
<td>Synthesizes entity-escaped HTML <code>&lt;meta&gt;</code>, Open Graph (<code>og:*</code>), and Twitter Card tags.</td>
</tr>
</tbody>
</table>
</div>
</div>

<div class="step-item">
<div class="step-header">
<span class="step-badge">03</span>
<h2 class="step-title">Command-Line Interface (fmg) &amp; Error Diagnostics</h2>
</div>
<p>Compile with <code>--features cli</code> to use the <code>fmg</code> binary for extracting metadata or building static sites:</p>

<div class="terminal-box my-3">
<div class="terminal-bar">
<span class="terminal-dot dot-red"></span>
<span class="terminal-dot dot-yellow"></span>
<span class="terminal-dot dot-green"></span>
<span class="terminal-title">bash — fmg subcommands</span>
</div>
<div class="terminal-body">
<div class="t-line"><span class="t-comment">&#35; Extract frontmatter from an input file in JSON, YAML, or TOML format</span></div>
<div class="t-line"><span class="t-prompt">$</span>fmg extract &lt;INPUT&gt; [--format json|yaml|toml] [--output &lt;FILE&gt;]</div>
<div class="t-line">&nbsp;</div>
<div class="t-line"><span class="t-comment">&#35; Build a static site from Markdown content and Tera templates (requires --features cli,ssg)</span></div>
<div class="t-line"><span class="t-prompt">$</span>fmg build --content-dir &lt;DIR&gt; --output-dir &lt;DIR&gt; [--template-dir &lt;DIR&gt;] [--base-url &lt;URL&gt;]</div>
</div>
</div>

<p>Structured error types returned across the crate:</p>

<div class="table-responsive my-3">
<table class="visage-table">
<thead>
<tr>
<th>Error Type</th>
<th>Module</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>error::Error</code></td>
<td><code>frontmatter_gen::error</code></td>
<td>Crate-wide error enum covering extraction, parsing (`yaml_line`, `toml_line`), and I/O errors.</td>
</tr>
<tr>
<td><code>error::ParseError</code></td>
<td><code>frontmatter_gen::error</code></td>
<td>Returned by <code>extract</code>, <code>extractor</code>, and <code>parser</code> for missing fences, format errors, or budget violations.</td>
</tr>
<tr>
<td><code>meta::MetaError</code></td>
<td><code>frontmatter_gen::meta</code></td>
<td>Returned when a frontmatter key or value fails HTML meta tag validation.</td>
</tr>
<tr>
<td><code>config::ConfigError</code></td>
<td><code>frontmatter_gen::config</code></td>
<td>Returned when <code>ConfigBuilder</code> validation fails (empty site name or invalid directory paths).</td>
</tr>
</tbody>
</table>
</div>
</div>

<div class="step-item">
<div class="step-header">
<span class="step-badge">04</span>
<h2 class="step-title">Stability &amp; SemVer Contract</h2>
</div>
<p>In addition to Rust type and function signature stability, any change to the observable output of <code>extract_metadata</code> or <code>generate_metatags</code> for existing inputs is treated as a breaking change.</p>

<div class="doc-visual-card">
<picture>
<source media="(max-width: 40rem)" srcset="https://cloudcdn.pro/stocks/images/quantum-computer-room-320.webp 320w, https://cloudcdn.pro/stocks/images/quantum-computer-room-640.webp 640w, https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp 1200w" sizes="100vw">
<img src="https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp" alt="Deterministic Rust API and CLI architecture for frontmatter-gen" width="1200" height="675" loading="lazy" />
</picture>
<div class="doc-visual-caption">Predictable API contract: zero-copy borrowing, budget-guarded parsing, and deterministic HTML meta tag emission.</div>
</div>
</div>
