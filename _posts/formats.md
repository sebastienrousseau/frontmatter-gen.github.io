---
name: "Frontmatter Gen"
short_name: "frontmatter-gen"
title: "Supported Formats: YAML 1.2, TOML 1.1 & JSON Frontmatter"
description: "Specification and delimiter reference for YAML 1.2 (noyalib), TOML 1.1 (toml), and JSON (serde_json) frontmatter extraction and serialization in Rust."
keywords: "yaml 1.2 frontmatter, toml 1.1 frontmatter, json frontmatter, noyalib yaml 1.2, norway problem yaml, hugo toml frontmatter"
author: "Sebastien Rousseau"
date: "2026-10-31"
language: "en-GB"
layout: "page"
permalink: "https://frontmatter-gen.com/formats/"
logo: "https://cloudcdn.pro/clients/frontmatter-gen/v1/logos/frontmatter-gen.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Frontmatter Gen: Zero-Copy Frontmatter Extraction and Parsing in Rust"
eyebrow: "Specifications Matrix"
headline: "Supported Frontmatter Formats & Specifications"
lead: "Full YAML 1.2, TOML 1.1, and JSON frontmatter extraction, automatic format detection, and lossless cross-format conversion."
category: "Documentation"
changefreq: "weekly"
date_published: "2026-01-15T00:00:00Z"
date_modified: "2026-10-31T00:00:00Z"
priority: "0.9"
slug: "formats"
url: "/formats/"
apple_touch_icon_sizes: "192x192"
schema_type: "TechArticle"
theme_color: "#22242f"
---

Frontmatter Gen supports the three primary frontmatter formats used across static site generators, documentation engines, and content management systems. All three formats deserialize into the same `Frontmatter` (`HashMap<String, Value>`) representation and can be converted into one another via `frontmatter_gen::parser::to_string`.

<div class="table-responsive my-4">
<table class="visage-table">
<thead>
<tr>
<th>Format</th>
<th>Fence / Delimiter</th>
<th>Underlying Parser</th>
<th>Specification &amp; Key Guarantees</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>YAML 1.2</strong></td>
<td><code>---</code> ... <code>---</code></td>
<td><code>noyalib</code> (Pure Rust)</td>
<td>YAML 1.2 Core Schema; no Norway problem; explicit tags preserved as <code>Value::Tagged</code>.</td>
</tr>
<tr>
<td><strong>TOML 1.1</strong></td>
<td><code>+++</code> ... <code>+++</code></td>
<td><code>toml</code></td>
<td>TOML 1.1 tables, inline tables, arrays of tables, and ISO 8601 datetimes converted to strings.</td>
</tr>
<tr>
<td><strong>JSON</strong></td>
<td><code>{ ... }</code> or fenced JSON</td>
<td><code>serde_json</code></td>
<td>RFC 8259 balanced brace tracking with string-literal and escape-sequence awareness.</td>
</tr>
</tbody>
</table>
</div>

<h2>1. YAML 1.2 Frontmatter (<code>---</code>) via <code>noyalib</code></h2>

<p>YAML is the default frontmatter format across Jekyll, Astro, Docusaurus, Eleventy, and Markdown documentation portals. Unlike legacy Rust crates built on archived <code>serde_yaml</code> (YAML 1.1), <code>frontmatter-gen</code> uses <strong><code>noyalib</code></strong>, a pure-Rust YAML 1.2 parser with zero <code>unsafe</code> code:</p>

<ul>
<li><strong>No YAML 1.1 Norway Problem:</strong> In YAML 1.1, unquoted strings like <code>NO</code>, <code>no</code>, <code>on</code>, and <code>off</code> silently coerce into booleans. Under YAML 1.2, only <code>true</code> and <code>false</code> resolve as booleans, keeping country codes and short tokens intact as <code>Value::String</code>.</li>
<li><strong>Explicit YAML Tag Preservation:</strong> Tagged scalars and mappings (such as <code>!custom value</code> or <code>!include path.yaml</code>) are preserved losslessly as <code>Value::Tagged(tag_name, Box&lt;Value&gt;)</code> and accessible via <code>Value::as_tagged()</code>.</li>
<li><strong>Root Mapping Requirement:</strong> The top-level YAML value must be a mapping; scalar or sequence roots return <code>ParseError::InvalidYaml</code>.</li>
</ul>

<div class="terminal-box my-3">
<div class="terminal-bar">
<span class="terminal-dot dot-red"></span>
<span class="terminal-dot dot-yellow"></span>
<span class="terminal-dot dot-green"></span>
<span class="terminal-title">markdown — YAML 1.2 frontmatter</span>
</div>
<div class="terminal-body">
<div class="t-line"><span class="t-comment">---</span></div>
<div class="t-line"><span class="t-key">title:</span> <span class="t-val">&quot;Deterministic YAML 1.2&quot;</span></div>
<div class="t-line"><span class="t-key">country:</span> <span class="t-val">NO</span></div>
<div class="t-line"><span class="t-key">published:</span> <span class="t-val">true</span></div>
<div class="t-line"><span class="t-key">custom:</span> <span class="t-val">!slug my-article-slug</span></div>
<div class="t-line"><span class="t-comment">---</span></div>
<div class="t-line">&#35; Article Body</div>
</div>
</div>

<h2>2. TOML 1.1 Frontmatter (<code>+++</code>) via <code>toml</code></h2>

<p>TOML frontmatter is standard in Hugo, Zola, and Rust documentation pipelines. A TOML header opens with <code>+++</code> on the first line and closes with a matching <code>+++</code> fence:</p>

<ul>
<li><strong>Native Datetime Normalization:</strong> TOML native datetimes (<code>toml::Value::Datetime</code>) are automatically converted into their canonical ISO 8601 string representation (<code>Value::String</code>) for uniform downstream template rendering.</li>
<li><strong>Nested Tables &amp; Arrays:</strong> Dotted keys, inline tables, and nested sections map directly to nested <code>Value::Object(Box&lt;Frontmatter&gt;)</code> structures.</li>
</ul>

<div class="terminal-box my-3">
<div class="terminal-bar">
<span class="terminal-dot dot-red"></span>
<span class="terminal-dot dot-yellow"></span>
<span class="terminal-dot dot-green"></span>
<span class="terminal-title">markdown — TOML 1.1 frontmatter</span>
</div>
<div class="terminal-body">
<div class="t-line"><span class="t-comment">+++</span></div>
<div class="t-line"><span class="t-key">title</span> = <span class="t-val">&quot;TOML 1.1 Frontmatter&quot;</span></div>
<div class="t-line"><span class="t-key">weight</span> = <span class="t-val">10</span></div>
<div class="t-line"><span class="t-key">date</span> = <span class="t-val">2026-10-31T12:00:00Z</span></div>
<div class="t-line"><span class="t-key">[taxonomies]</span></div>
<div class="t-line"><span class="t-key">categories</span> = [<span class="t-val">&quot;systems&quot;</span>, <span class="t-val">&quot;rust&quot;</span>]</div>
<div class="t-line"><span class="t-comment">+++</span></div>
<div class="t-line">&#35; TOML Document Body</div>
</div>
</div>

<h2>3. JSON Frontmatter (<code>{ ... }</code>) via <code>serde_json</code></h2>

<p>JSON frontmatter is widely used in automated CMS exports and machine-generated Markdown documents. <code>frontmatter-gen</code> supports both standalone leading JSON objects and fenced JSON blocks:</p>

<ul>
<li><strong>Balanced Brace Scanner:</strong> <code>extract_json_frontmatter</code> tracks brace depth while respecting quoted string literals and backslash escapes (<code>\&quot;</code>), ensuring braces inside string values never prematurely terminate extraction.</li>
<li><strong>Exact Numeric Representation:</strong> Numbers are stored as <code>serde_json::Number</code> inside <code>Value::Number</code>, preserving 64-bit signed/unsigned integers and IEEE 754 floats.</li>
</ul>

<h2>4. Cross-Format Serialization (<code>parser::to_string</code>)</h2>

<p>Because all three formats deserialize into <code>Frontmatter</code>, converting between YAML, TOML, and JSON requires a single call to <code>frontmatter_gen::parser::to_string(&amp;fm, target_format)</code>:</p>

<div class="terminal-box my-3">
<div class="terminal-bar">
<span class="terminal-dot dot-red"></span>
<span class="terminal-dot dot-yellow"></span>
<span class="terminal-dot dot-green"></span>
<span class="terminal-title">rust — cross-format conversion</span>
</div>
<div class="terminal-body">
<div class="t-line"><span class="t-key">use</span> frontmatter_gen::{extract, Format};</div>
<div class="t-line"><span class="t-key">use</span> frontmatter_gen::parser::to_string;</div>
<div class="t-line">&nbsp;</div>
<div class="t-line"><span class="t-key">let</span> (fm, _body) = extract(<span class="t-val">&quot;---\ntitle: Convert Me\ncount: 42\n---\nBody&quot;</span>)?;</div>
<div class="t-line"><span class="t-key">let</span> as_toml = to_string(&amp;fm, Format::Toml)?;</div>
<div class="t-line"><span class="t-key">let</span> as_json = to_string(&amp;fm, Format::Json)?;</div>
</div>
</div>
