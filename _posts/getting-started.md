---
name: "Frontmatter Gen"
short_name: "frontmatter-gen"
title: "Getting Started: Install Frontmatter Gen Crate & CLI"
description: "Install frontmatter-gen v0.0.15 via Cargo, extract YAML 1.2, TOML, and JSON frontmatter in Rust, generate HTML meta tags, and run the fmg CLI."
keywords: "install frontmatter-gen, cargo add frontmatter-gen, fmg cli, rust frontmatter quickstart, extract_raw_frontmatter"
author: "Sebastien Rousseau"
date: "2026-10-31"
language: "en-GB"
layout: "page"
permalink: "https://frontmatter-gen.com/getting-started/"
logo: "https://cloudcdn.pro/clients/frontmatter-gen/v1/logos/frontmatter-gen.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Frontmatter Gen: Zero-Copy Frontmatter Extraction and Parsing in Rust"
eyebrow: "Installation & Guide"
headline: "Getting Started with Frontmatter Gen"
lead: "Install the library crate or standalone CLI, extract YAML 1.2, TOML 1.1, and JSON headers, and synthesize HTML meta tags."
category: "Documentation"
changefreq: "weekly"
date_published: "2026-01-15T00:00:00Z"
date_modified: "2026-10-31T00:00:00Z"
priority: "0.9"
slug: "getting-started"
url: "/getting-started/"
apple_touch_icon_sizes: "192x192"
schema_type: "TechArticle"
theme_color: "#22242f"
---

Frontmatter Gen (`frontmatter-gen`) is an open-source, pure-Rust library and CLI for extracting and parsing YAML 1.2, TOML 1.1, and JSON frontmatter from Markdown and text documents. Follow this guide to add the crate, run the `fmg` binary, or enforce DoS limits on untrusted inputs.

<div class="install-grid">
<div class="install-card">
<div class="install-card-header">
<h2 class="install-card-title">Core Library</h2>
<span class="install-card-tag">Crate v0.0.15</span>
</div>
<p class="install-card-desc">Zero-copy extractor, YAML 1.2 / TOML 1.1 / JSON parsers, and HTML meta tag generator with minimal dependencies.</p>
<pre><code>cargo add frontmatter-gen</code></pre>
</div>

<div class="install-card">
<div class="install-card-header">
<h2 class="install-card-title">Standalone CLI</h2>
<span class="install-card-tag">Binary (fmg)</span>
</div>
<p class="install-card-desc">Install the standalone <code>fmg</code> command-line binary with <code>clap</code> and <code>tokio</code> for terminal and CI workflows.</p>
<pre><code>cargo install frontmatter-gen --features cli</code></pre>
</div>

<div class="install-card">
<div class="install-card-header">
<h2 class="install-card-title">SSG Engine</h2>
<span class="install-card-tag">Feature Flag</span>
</div>
<p class="install-card-desc">Enable the static site generation engine powered by <code>tera</code> templates and <code>comrak</code> Markdown rendering.</p>
<pre><code>cargo add frontmatter-gen --features ssg</code></pre>
</div>

<div class="install-card">
<div class="install-card-header">
<h2 class="install-card-title">Rust Toolchain</h2>
<span class="install-card-tag">MSRV 1.85.0+</span>
</div>
<p class="install-card-desc">Requires Rust 1.85.0 or newer (Edition 2024) and compiles cleanly across Linux, macOS, and Windows with zero unsafe code.</p>
<pre><code>rustup update stable</code></pre>
</div>
</div>

<div class="step-item">
<div class="step-header">
<span class="step-badge">01</span>
<h2 class="step-title">Extract &amp; Parse Frontmatter in One Call</h2>
</div>
<p>The top-level <code>frontmatter_gen::extract</code> function detects the frontmatter format automatically, parses the header into a <code>Frontmatter</code> map, and returns the remaining Markdown body as a borrowed <code>&amp;str</code> slice:</p>

<div class="terminal-box my-3">
<div class="terminal-bar">
<span class="terminal-dot dot-red"></span>
<span class="terminal-dot dot-yellow"></span>
<span class="terminal-dot dot-green"></span>
<span class="terminal-title">rust — src/main.rs</span>
</div>
<div class="terminal-body">
<div class="t-line"><span class="t-key">use</span> frontmatter_gen::{extract, Value};</div>
<div class="t-line">&nbsp;</div>
<div class="t-line"><span class="t-key">fn</span> <span class="t-val">main</span>() -&gt; Result&lt;(), Box&lt;<span class="t-key">dyn</span> std::error::Error&gt;&gt; {</div>
<div class="t-line">&nbsp;&nbsp;&nbsp;&nbsp;<span class="t-key">let</span> doc = <span class="t-val">&quot;---\ntitle: Zero-Copy Rust\npublished: true\n---\n# Welcome\n&quot;</span>;</div>
<div class="t-line">&nbsp;&nbsp;&nbsp;&nbsp;<span class="t-key">let</span> (fm, body) = extract(doc)?;</div>
<div class="t-line">&nbsp;</div>
<div class="t-line">&nbsp;&nbsp;&nbsp;&nbsp;assert_eq!(fm.get(<span class="t-val">&quot;title&quot;</span>), Some(&amp;Value::String(<span class="t-val">&quot;Zero-Copy Rust&quot;</span>.into())));</div>
<div class="t-line">&nbsp;&nbsp;&nbsp;&nbsp;assert_eq!(fm.get(<span class="t-val">&quot;published&quot;</span>), Some(&amp;Value::Bool(<span class="t-val">true</span>)));</div>
<div class="t-line">&nbsp;&nbsp;&nbsp;&nbsp;assert!(body.starts_with(<span class="t-val">&quot;# Welcome&quot;</span>));</div>
<div class="t-line">&nbsp;&nbsp;&nbsp;&nbsp;Ok(())</div>
<div class="t-line">}</div>
</div>
</div>
</div>

<div class="step-item">
<div class="step-header">
<span class="step-badge">02</span>
<h2 class="step-title">Zero-Copy Raw Slicing &amp; DoS Budget Guardrails</h2>
</div>
<p>When processing untrusted Markdown uploads or inspecting raw slices before allocation, pair <code>extractor::extract_raw_frontmatter</code> with <code>parser::parse_with_options</code>:</p>

<div class="terminal-box my-3">
<div class="terminal-bar">
<span class="terminal-dot dot-red"></span>
<span class="terminal-dot dot-yellow"></span>
<span class="terminal-dot dot-green"></span>
<span class="terminal-title">rust — zero-copy &amp; ParseOptions</span>
</div>
<div class="terminal-body">
<div class="t-line"><span class="t-key">use</span> frontmatter_gen::extractor::{detect_format, extract_raw_frontmatter};</div>
<div class="t-line"><span class="t-key">use</span> frontmatter_gen::parser::{parse_with_options, ParseOptions};</div>
<div class="t-line">&nbsp;</div>
<div class="t-line"><span class="t-comment">&#35; 1. Borrow (raw_header, body) without heap allocation</span></div>
<div class="t-line"><span class="t-key">let</span> (raw_header, body) = extract_raw_frontmatter(input)?;</div>
<div class="t-line"><span class="t-key">let</span> format = detect_format(raw_header);</div>
<div class="t-line">&nbsp;</div>
<div class="t-line"><span class="t-comment">&#35; 2. Enforce structural depth and key-count budgets</span></div>
<div class="t-line"><span class="t-key">let</span> options = ParseOptions {</div>
<div class="t-line">&nbsp;&nbsp;&nbsp;&nbsp;validate: <span class="t-val">true</span>,</div>
<div class="t-line">&nbsp;&nbsp;&nbsp;&nbsp;max_depth: Some(<span class="t-val">8</span>),</div>
<div class="t-line">&nbsp;&nbsp;&nbsp;&nbsp;max_keys: Some(<span class="t-val">64</span>),</div>
<div class="t-line">};</div>
<div class="t-line"><span class="t-key">let</span> fm = parse_with_options(raw_header, format, &amp;options)?;</div>
</div>
</div>
</div>

<div class="step-item">
<div class="step-header">
<span class="step-badge">03</span>
<h2 class="step-title">Generate Escaped HTML Meta Tags &amp; Use the CLI</h2>
</div>
<p>Convert parsed frontmatter into HTML <code>&lt;meta&gt;</code>, Open Graph, and Twitter Card tags, or invoke the <code>fmg</code> binary directly from your shell:</p>

<div class="terminal-box my-3">
<div class="terminal-bar">
<span class="terminal-dot dot-red"></span>
<span class="terminal-dot dot-yellow"></span>
<span class="terminal-dot dot-green"></span>
<span class="terminal-title">bash — fmg cli quickstart</span>
</div>
<div class="terminal-body">
<div class="t-line"><span class="t-comment">&#35; Extract frontmatter from a Markdown file and print as formatted JSON</span></div>
<div class="t-line"><span class="t-prompt">$</span>fmg extract content/post.md --format json</div>
<div class="t-line">&nbsp;</div>
<div class="t-line"><span class="t-comment">&#35; Write extracted frontmatter to a YAML file</span></div>
<div class="t-line"><span class="t-prompt">$</span>fmg extract content/post.md --format yaml --output build/meta.yaml</div>
<div class="t-line">&nbsp;</div>
<div class="t-line"><span class="t-comment">&#35; Build a static site from content/ and templates/ into public/</span></div>
<div class="t-line"><span class="t-prompt">$</span>fmg build --content-dir content --template-dir templates --output-dir public</div>
</div>
</div>
</div>

<div class="step-item">
<div class="step-header">
<span class="step-badge">04</span>
<h2 class="step-title">Memory-Safe Execution Guarantees</h2>
</div>
<p>Every extraction and parsing pass executes strictly in local memory with <code>#![forbid(unsafe_code)]</code>, verified under Miri Tree Borrows and continuous fuzzing:</p>

<div class="doc-visual-card">
<picture>
<source media="(max-width: 40rem)" srcset="https://cloudcdn.pro/stocks/images/quantum-computer-room-320.webp 320w, https://cloudcdn.pro/stocks/images/quantum-computer-room-640.webp 640w, https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp 1200w" sizes="100vw">
<img src="https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp" alt="Deterministic Rust document metadata extraction and parsing architecture" width="1200" height="675" loading="lazy" />
</picture>
<div class="doc-visual-caption">Zero-copy architecture: frontmatter boundaries are sliced in a single forward scan and parsed into strongly-typed Rust values with zero unsafe code.</div>
</div>
</div>
