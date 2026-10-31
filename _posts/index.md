---
name: "Frontmatter Gen"
short_name: "frontmatter-gen"
title: "Frontmatter Gen: Zero-Copy YAML 1.2, TOML & JSON in Rust"
description: "Zero-copy frontmatter extraction and multi-format parsing library and CLI for YAML 1.2, TOML 1.1, and JSON in Rust with HTML meta tag synthesis and zero unsafe code."
keywords: "rust frontmatter parser, yaml 1.2 frontmatter, toml frontmatter, json frontmatter, static site generator rust, meta tag generator, noyalib, zero copy rust"
author: "Sebastien Rousseau"
date: "2026-10-31"
language: "en-GB"
layout: "index"
permalink: "https://frontmatter-gen.com/"
logo: "https://cloudcdn.pro/clients/frontmatter-gen/v1/logos/frontmatter-gen.svg"
banner: "https://cloudcdn.pro/stocks/images/corporate-finance-1200.webp"
banner_alt: "Frontmatter Gen: Zero-Copy Frontmatter Extraction and Parsing in Rust"
eyebrow: "Rust Frontmatter Engine · v0.0.15"
headline: "Front matter in, typed values out."
lead: "Extract and parse YAML 1.2, TOML 1.1, and JSON document headers in one pass with zero-copy body slicing, configurable DoS budgets, and HTML meta tag synthesis."
category: "Documentation"
changefreq: "daily"
date_published: "2026-01-15T00:00:00Z"
date_modified: "2026-10-31T00:00:00Z"
priority: "1.0"
slug: "index"
url: "/"
apple_touch_icon_sizes: "192x192"
schema_type: "SoftwareSourceCode"
theme_color: "#22242f"
---

<section class="visage-intro" aria-labelledby="hero-heading">
<div class="wrap">
<p class="lilac-label">Rust Document Engineering · v0.0.15 · Open Source</p>
<h1 id="hero-heading">Front matter in, <em>typed values out.</em><br>Zero-copy slicing. Zero unsafe code.</h1>
<p>A pure-Rust library and CLI for extracting and parsing YAML 1.2, TOML 1.1, and JSON frontmatter from Markdown and text documents. Built for static site generators, documentation engines, and content pipelines with configurable DoS budgets, HTML meta tag synthesis, Miri Tree Borrows verification, and 100% unit test coverage.</p>
<div class="actions">
<a class="primary" href="/getting-started/index.html">Install Crate &amp; CLI</a>
<a href="/formats/index.html">Explore Supported Formats</a>
</div>
<ul class="hero-assurances">
<li>YAML 1.2, TOML 1.1 &amp; JSON</li>
<li>Zero-Copy Body Slicing</li>
<li>#![forbid(unsafe_code)] + Miri Verified</li>
</ul>
</div>
</section>

<section class="trust-strip" aria-label="Platform guarantees">
<div class="wrap">
<ul>
<li>
<b>3 Native Formats</b>
<span>YAML 1.2 (<code>---</code> via <code>noyalib</code>), TOML 1.1 (<code>+++</code>), and JSON (<code>{ ... }</code>) enabled by default.</span>
</li>
<li>
<b>0 B Copy Slice</b>
<span><code>extract_raw_frontmatter</code> borrows <code>(&amp;str, &amp;str)</code> slices directly from your input buffer.</span>
</li>
<li>
<b>100% Coverage</b>
<span>Every module verified by <code>cargo-llvm-cov</code>, <code>proptest</code>, Miri Tree Borrows, and 4 fuzz targets.</span>
</li>
<li>
<b>DoS Guardrails</b>
<span>Configurable <code>max_depth</code>, <code>max_keys</code>, and required-key validation via <code>ParseOptions</code>.</span>
</li>
</ul>
</div>
</section>

<section class="analysis-stage" id="workflows" aria-labelledby="workflows-heading">
<div class="wrap image-shell">
<picture>
<source media="(max-width: 40rem)" srcset="https://cloudcdn.pro/stocks/images/getty-images-LaU3HadwEeE-unsplash-320.webp 320w, https://cloudcdn.pro/stocks/images/getty-images-LaU3HadwEeE-unsplash-640.webp 640w, https://cloudcdn.pro/stocks/images/getty-images-LaU3HadwEeE-unsplash-1200.webp 1200w" sizes="100vw">
<img src="https://cloudcdn.pro/stocks/images/getty-images-LaU3HadwEeE-unsplash-1200.webp" srcset="https://cloudcdn.pro/stocks/images/getty-images-LaU3HadwEeE-unsplash-640.webp 640w, https://cloudcdn.pro/stocks/images/getty-images-LaU3HadwEeE-unsplash-1200.webp 1200w, https://cloudcdn.pro/stocks/images/getty-images-LaU3HadwEeE-unsplash-1920.webp 1920w" sizes="(max-width: 40rem) 100vw, 80rem" width="1200" height="675" alt="High-throughput content engineering and static site compilation dashboard" loading="lazy" decoding="async">
</picture>
<div class="consultation-card">
<p class="lilac-label">Content Pipeline Automation</p>
<h2 id="workflows-heading">Unified Metadata for Static Sites &amp; Content Engines</h2>
<p>Replace brittle regular expressions and archived YAML 1.1 parsers with a single deterministic crate. Ingest Markdown with YAML, TOML, or JSON headers and emit typed Rust structures or escaped HTML5 meta tags in microseconds.</p>
<a class="primary" href="/use-cases/index.html">View Production Blueprints <span aria-hidden="true">↗</span></a>
</div>
</div>
</section>

<section class="visage-features" id="features" aria-labelledby="features-heading">
<div class="wrap">
<header class="section-heading">
<p class="lilac-label">Engine Architecture</p>
<h2 id="features-heading">Engineered for predictable latency and untrusted input safety.</h2>
<p>Every module in <code>frontmatter-gen</code> separates zero-copy borrowing from heap allocation so callers pay only for the work they request.</p>
</header>
<div class="three-cells">
<article>
<span>01</span>
<h3>Zero-Copy Fence Splitting</h3>
<p><code>extractor::extract_raw_frontmatter</code> locates YAML (<code>---</code>), TOML (<code>+++</code>), or JSON (<code>{ ... }</code>) boundaries in a single forward scan and returns borrowed <code>(&amp;str, &amp;str)</code> slices with zero heap allocation.</p>
</article>
<article>
<span>02</span>
<h3>YAML 1.2, TOML 1.1 &amp; JSON</h3>
<p>Powered by pure-Rust <code>noyalib</code> (YAML 1.2 with explicit <code>Value::Tagged</code> preservation and no Norway boolean coercion), <code>toml</code> 1.1, and <code>serde_json</code>, unified behind a single recursive <code>Frontmatter</code> model.</p>
</article>
<article>
<span>03</span>
<h3>HTML Meta &amp; Template Engine</h3>
<p><code>meta::generate_metatags</code> transforms frontmatter maps into entity-escaped HTML <code>&lt;meta&gt;</code>, Open Graph (<code>og:*</code>), and Twitter Card tags, while the optional <code>ssg</code> feature drives static site builds.</p>
</article>
</div>
</div>
</section>

<section class="visage-process" id="process" aria-labelledby="process-heading">
<div class="wrap">
<p class="lilac-label">The Processing Pipeline</p>
<h2 id="process-heading">One pass from raw Markdown document to verified output.</h2>
<div class="process-grid">
<article>
<b>1</b>
<h3>Slice</h3>
<p>Strip optional UTF-8 BOM (<code>\u{FEFF}</code>) and split the leading frontmatter block from the Markdown body without copying either half.</p>
<small>extract_raw_frontmatter(&amp;str)</small>
</article>
<article>
<b>2</b>
<h3>Detect</h3>
<p>Inspect fence delimiters or leading structural tokens to classify the header as <code>Format::Yaml</code>, <code>Format::Toml</code>, or <code>Format::Json</code>.</p>
<small>detect_format(&amp;str)</small>
</article>
<article>
<b>3</b>
<h3>Parse &amp; Guard</h3>
<p>Deserialize into <code>Frontmatter</code> while enforcing optional <code>ParseOptions</code> limits on nesting depth, total keys, and required fields.</p>
<small>parse_with_options(&amp;str, Format, &amp;ParseOptions)</small>
</article>
<article>
<b>4</b>
<h3>Emit</h3>
<p>Serialize back to any format via <code>parser::to_string</code>, emit escaped HTML <code>&lt;meta&gt;</code> tags, or render static pages via <code>fmg</code>.</p>
<small>generate_metatags(&amp;Frontmatter)</small>
</article>
</div>
</div>
</section>

<section class="analysis-stage" id="architecture-preview" aria-labelledby="arch-heading">
<div class="wrap image-shell">
<picture>
<source media="(max-width: 40rem)" srcset="https://cloudcdn.pro/stocks/images/vadim-sherbakov-xS_RzdD5CFE-320.webp 320w, https://cloudcdn.pro/stocks/images/vadim-sherbakov-xS_RzdD5CFE-640.webp 640w, https://cloudcdn.pro/stocks/images/vadim-sherbakov-xS_RzdD5CFE-1200.webp 1200w" sizes="100vw">
<img src="https://cloudcdn.pro/stocks/images/vadim-sherbakov-xS_RzdD5CFE-1200.webp" srcset="https://cloudcdn.pro/stocks/images/vadim-sherbakov-xS_RzdD5CFE-640.webp 640w, https://cloudcdn.pro/stocks/images/vadim-sherbakov-xS_RzdD5CFE-1200.webp 1200w, https://cloudcdn.pro/stocks/images/vadim-sherbakov-xS_RzdD5CFE-1920.webp 1920w" sizes="(max-width: 40rem) 100vw, 80rem" width="1200" height="675" alt="Architectural view of London at night representing deterministic Rust parsing infrastructure" loading="lazy" decoding="async">
</picture>
<div class="consultation-card">
<p class="lilac-label">High-Assurance Pipeline</p>
<h2 id="arch-heading">Deterministic Execution at Scale</h2>
<p>Designed for static site compilers, documentation servers, and CI linters requiring sub-microsecond slice extraction, bounded recursion depth, and strict YAML 1.2 fidelity.</p>
<a class="primary" href="/architecture/index.html">View Architecture Blueprint <span aria-hidden="true">↗</span></a>
</div>
</div>
</section>

<section class="terminal-stage" aria-labelledby="quickstart-heading">
<div class="wrap terminal-grid">
<div>
<p class="lilac-label">Developer Quickstart</p>
<h2 id="quickstart-heading">Add the Rust Crate or Install the CLI in Seconds</h2>
<p>Embed <code>frontmatter_gen::extract</code> directly in your Rust library, or install the standalone <code>fmg</code> binary to extract frontmatter and build static sites from your terminal.</p>
<div class="actions">
<a class="primary" href="/getting-started/index.html">Full Documentation →</a>
<a href="/api/index.html">API &amp; CLI Reference</a>
</div>
</div>
<div class="terminal-box">
<div class="terminal-bar">
<span class="terminal-dot dot-red"></span>
<span class="terminal-dot dot-yellow"></span>
<span class="terminal-dot dot-green"></span>
<span class="terminal-title">rust &amp; bash — frontmatter-gen v0.0.15</span>
</div>
<div class="terminal-body">
<div class="t-line"><span class="t-comment">&#35; 1. Add library crate or install CLI binary</span></div>
<div class="t-line"><span class="t-prompt">$</span>cargo add frontmatter-gen</div>
<div class="t-line"><span class="t-prompt">$</span>cargo install frontmatter-gen --features cli</div>
<div class="t-line">&nbsp;</div>
<div class="t-line"><span class="t-comment">&#35; 2. Extract and parse YAML 1.2, TOML, or JSON in Rust</span></div>
<div class="t-line"><span class="t-key">let</span> (fm, body) = frontmatter_gen::extract(markdown)?;</div>
<div class="t-line"><span class="t-key">let</span> meta_html = frontmatter_gen::meta::generate_metatags(&amp;fm)?;</div>
<div class="t-line">&nbsp;</div>
<div class="t-line"><span class="t-comment">&#35; 3. Extract frontmatter to JSON from the terminal</span></div>
<div class="t-line"><span class="t-prompt">$</span>fmg extract content/post.md --format json --output meta.json</div>
</div>
</div>
</div>
</section>

<section class="privacy-panel" aria-labelledby="security-heading">
<div class="wrap privacy-grid">
<p class="lilac-label">Formal &amp; Empirical Assurance</p>
<div>
<h2 id="security-heading">Zero unsafe code. Proven under Miri Tree Borrows.</h2>
<p>Every crate boundary enforces <code>#![forbid(unsafe_code)]</code>. Continuous verification runs Miri with <code>-Zmiri-strict-provenance -Zmiri-tree-borrows</code> across both default and minimal feature sets, backed by 4 structure-aware <code>cargo-fuzz</code> harnesses and <code>cargo-vet</code> supply-chain audits.</p>
</div>
<a href="/security/index.html">Read Security &amp; Verification Architecture <span aria-hidden="true">↓</span></a>
</div>
</section>

<section class="visage-faq" id="faq" aria-labelledby="faq-heading">
<div class="wrap faq-layout">
<header>
<p class="lilac-label">Clear Answers</p>
<h2 id="faq-heading">Frequently Asked Questions</h2>
</header>
<div>
<details>
<summary>Why does frontmatter-gen use noyalib instead of serde_yaml?</summary>
<p><code>serde_yaml</code> was archived upstream in March 2024 and implements YAML 1.1, where unquoted scalars like <code>no</code> or <code>off</code> coerce to booleans. <code>frontmatter-gen</code> uses <code>noyalib</code>, an actively maintained, pure-Rust YAML 1.2 parser with zero unsafe code and explicit tag support.</p>
</details>
<details>
<summary>Does extract_raw_frontmatter allocate on the heap?</summary>
<p>No. <code>extractor::extract_raw_frontmatter</code> returns <code>Result&lt;(&amp;str, &amp;str), ParseError&gt;</code> borrowed directly from your input <code>&amp;str</code>. You only allocate when you parse the raw slice into a <code>Frontmatter</code> map.</p>
</details>
<details>
<summary>How do I protect my server against deeply nested frontmatter payloads?</summary>
<p>Use <code>parser::parse_with_options</code> with a <code>ParseOptions</code> struct setting <code>max_depth</code> (for example, <code>Some(16)</code>) and <code>max_keys</code> (for example, <code>Some(128)</code>). Payloads exceeding either threshold return <code>ParseError::InvalidFrontmatter</code> immediately.</p>
</details>
<details>
<summary>Are the CLI and SSG engine mandatory dependencies?</summary>
<p>No. The default build includes only the core extractor, YAML/TOML/JSON parsers, and HTML meta tag generator. The <code>cli</code> feature (<code>fmg</code> binary) and <code>ssg</code> feature (static site engine) are strictly opt-in.</p>
</details>
</div>
</div>
</section>

<section class="visage-closing" aria-labelledby="visage-close">
<div class="wrap">
<div>
<p class="lilac-label">Developer Quickstart</p>
<h2 id="visage-close">Document metadata is foundational.<br><em>Your frontmatter parser should be deterministic.</em></h2>
</div>
<div>
<p>Get started in seconds with the Rust library crate or the standalone <code>fmg</code> CLI across Linux, macOS, and Windows.</p>
<a class="primary" href="/getting-started/index.html">Install Frontmatter Gen</a>
</div>
</div>
</section>
