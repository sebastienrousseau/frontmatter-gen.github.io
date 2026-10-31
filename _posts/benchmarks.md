---
name: "Frontmatter Gen"
short_name: "frontmatter-gen"
title: "Performance Benchmarks: Criterion Suites & Zero-Copy Latency"
description: "Explore the 6 Criterion benchmark suites in frontmatter-gen v0.0.15 measuring zero-copy extraction, YAML/TOML/JSON parsing, and HTML meta tag synthesis."
keywords: "rust frontmatter benchmark, criterion benchmarks, zero copy rust latency, yaml 1.2 vs toml vs json benchmark"
author: "Sebastien Rousseau"
date: "2026-10-31"
language: "en-GB"
layout: "page"
permalink: "https://frontmatter-gen.com/benchmarks/"
logo: "https://cloudcdn.pro/clients/frontmatter-gen/v1/logos/frontmatter-gen.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Frontmatter Gen: Zero-Copy Frontmatter Extraction and Parsing in Rust"
eyebrow: "Performance Metrics"
headline: "Performance Benchmarks & Throughput"
lead: "Six dedicated Criterion benchmark suites measuring zero-copy slice extraction, multi-format parsing, and HTML meta tag synthesis."
category: "Documentation"
changefreq: "weekly"
date_published: "2026-01-15T00:00:00Z"
date_modified: "2026-10-31T00:00:00Z"
priority: "0.9"
slug: "benchmarks"
url: "/benchmarks/"
apple_touch_icon_sizes: "192x192"
schema_type: "TechArticle"
theme_color: "#22242f"
---

Frontmatter Gen ships with six reproducible Criterion.rs benchmark suites under `benches/` covering every stage of the pipeline from zero-copy fence splitting to full static site page rendering.

<div class="stat-grid my-4">
<div class="stat-card">
<div class="stat-figure">0 B</div>
<div class="stat-label">Extractor Heap Copy</div>
</div>
<div class="stat-card">
<div class="stat-figure">6 Suites</div>
<div class="stat-label">Criterion Benchmarks</div>
</div>
<div class="stat-card">
<div class="stat-figure">O(n)</div>
<div class="stat-label">Single-Pass Scanner</div>
</div>
</div>

<div class="step-item">
<div class="step-header">
<span class="step-badge">01</span>
<h2 class="step-title">Criterion Benchmark Suites (`benches/`)</h2>
</div>
<p>Each subsystem has a dedicated Criterion harness so performance regressions are isolated to the exact pipeline stage:</p>

<div class="table-responsive my-3">
<table class="visage-table">
<thead>
<tr>
<th>Benchmark Target</th>
<th>Source File</th>
<th>Measured Operations</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>extractor_bench</code></td>
<td><code>benches/extractor_bench.rs</code></td>
<td>Zero-copy <code>extract_raw_frontmatter</code> and <code>detect_format</code> across YAML, TOML, and JSON payloads.</td>
</tr>
<tr>
<td><code>parser_bench</code></td>
<td><code>benches/parser_bench.rs</code></td>
<td><code>parser::parse</code>, <code>parse_with_options</code> (with depth and key budgets), and <code>to_string</code> serialization.</td>
</tr>
<tr>
<td><code>meta_bench</code></td>
<td><code>benches/meta_bench.rs</code></td>
<td><code>meta::generate_metatags</code> over scalar, array, Open Graph, Twitter Card, and HTML-escaped fields.</td>
</tr>
<tr>
<td><code>lib_bench</code></td>
<td><code>benches/lib_bench.rs</code></td>
<td>End-to-end <code>frontmatter_gen::extract</code> across small, medium, and large 1,000-key documents.</td>
</tr>
<tr>
<td><code>config_bench</code></td>
<td><code>benches/config_bench.rs</code></td>
<td><code>ConfigBuilder</code> construction, validation, and serialization under the <code>ssg</code> feature.</td>
</tr>
<tr>
<td><code>error_bench</code></td>
<td><code>benches/error_bench.rs</code></td>
<td><code>Error</code> and <code>ParseError</code> construction, line-number extraction, and <code>Display</code> formatting.</td>
</tr>
</tbody>
</table>
</div>
</div>

<div class="step-item">
<div class="step-header">
<span class="step-badge">02</span>
<h2 class="step-title">Reproducing Benchmarks Locally</h2>
</div>
<p>Run the Criterion suites on your own hardware to generate statistical HTML reports in <code>target/criterion/</code>:</p>

<div class="terminal-box my-3">
<div class="terminal-bar">
<span class="terminal-dot dot-red"></span>
<span class="terminal-dot dot-yellow"></span>
<span class="terminal-dot dot-green"></span>
<span class="terminal-title">bash — cargo bench</span>
</div>
<div class="terminal-body">
<div class="t-line"><span class="t-comment">&#35; Run all 6 Criterion benchmark suites</span></div>
<div class="t-line"><span class="t-prompt">$</span>cargo bench --all-features</div>
<div class="t-line">&nbsp;</div>
<div class="t-line"><span class="t-comment">&#35; Run only the zero-copy extractor or parser benchmarks</span></div>
<div class="t-line"><span class="t-prompt">$</span>cargo bench --bench extractor_bench</div>
<div class="t-line"><span class="t-prompt">$</span>cargo bench --bench parser_bench</div>
</div>
</div>
</div>

<div class="step-item">
<div class="step-header">
<span class="step-badge">03</span>
<h2 class="step-title">Allocation Profile by Pipeline Stage</h2>
</div>
<p>Because <code>extractor::extract_raw_frontmatter</code> only scans for opening and closing delimiters, its runtime is independent of the size of the Markdown body that follows the closing fence:</p>

<div class="table-responsive my-3">
<table class="visage-table">
<thead>
<tr>
<th>Operation</th>
<th>Time Complexity</th>
<th>Heap Allocations</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>extractor::extract_raw_frontmatter</code></td>
<td><code>O(header_bytes)</code></td>
<td><strong>0 allocations</strong> (borrows <code>(&amp;str, &amp;str)</code> from input)</td>
</tr>
<tr>
<td><code>extractor::detect_format</code></td>
<td><code>O(header_lines)</code></td>
<td><strong>0 allocations</strong> (inspects trimmed slices in place)</td>
</tr>
<tr>
<td><code>parser::parse_with_options</code></td>
<td><code>O(header_bytes)</code></td>
<td>1 <code>Frontmatter</code> map + recursive <code>Value</code> nodes</td>
</tr>
<tr>
<td><code>meta::generate_metatags</code></td>
<td><code>O(keys)</code></td>
<td>1 output <code>String</code> buffer with entity-escaped tags</td>
</tr>
</tbody>
</table>
</div>

<div class="doc-visual-card">
<picture>
<source media="(max-width: 40rem)" srcset="https://cloudcdn.pro/stocks/images/quantum-computer-room-320.webp 320w, https://cloudcdn.pro/stocks/images/quantum-computer-room-640.webp 640w, https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp 1200w" sizes="100vw">
<img src="https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp" alt="High-throughput Rust benchmarking and zero-copy slice extraction" width="1200" height="675" loading="lazy" />
</picture>
<div class="doc-visual-caption">Sub-microsecond slice extraction: Markdown bodies of any size are returned as zero-copy borrowed slices without scanning past the closing fence.</div>
</div>
</div>
