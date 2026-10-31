---
name: "Frontmatter Gen"
short_name: "frontmatter-gen"
title: "Frequently Asked Questions: Frontmatter Gen Technical FAQ"
description: "Answers to 16 common questions about frontmatter-gen: YAML 1.2 vs YAML 1.1, zero-copy extraction, ParseOptions DoS limits, HTML meta tags, Miri, and licensing."
keywords: "frontmatter-gen faq, yaml 1.2 rust faq, noyalib vs serde_yaml, rust frontmatter parser questions"
author: "Sebastien Rousseau"
date: "2026-10-31"
language: "en-GB"
layout: "faqs"
permalink: "https://frontmatter-gen.com/faqs/"
logo: "https://cloudcdn.pro/clients/frontmatter-gen/v1/logos/frontmatter-gen.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Frontmatter Gen: Zero-Copy Frontmatter Extraction and Parsing in Rust"
eyebrow: "Technical Knowledge Base"
headline: "Frequently Asked Questions"
lead: "Direct engineering answers covering format semantics, zero-copy lifetimes, security budgets, CLI usage, and licensing."
category: "Documentation"
changefreq: "weekly"
date_published: "2026-01-15T00:00:00Z"
date_modified: "2026-10-31T00:00:00Z"
priority: "0.9"
slug: "faqs"
url: "/faqs/"
apple_touch_icon_sizes: "192x192"
schema_type: "FAQPage"
theme_color: "#22242f"
---

<div class="faq-container">
<div class="faq-search-box">
<span class="faq-search-icon" aria-hidden="true"></span>
<input type="search" class="faq-search-input" id="faqSearchInput" placeholder="Filter questions by keyword (e.g. YAML 1.2, zero-copy, ParseOptions, Miri, CLI)..." aria-label="Search frequently asked questions" />
</div>

<div class="faq-filter-pills" role="tablist" aria-label="FAQ Categories">
<button class="faq-pill active" data-filter="all" type="button">All Questions <span class="pill-count">16</span></button>
<button class="faq-pill" data-filter="architecture" type="button">Architecture &amp; Formats <span class="pill-count">4</span></button>
<button class="faq-pill" data-filter="security" type="button">Security &amp; Verification <span class="pill-count">4</span></button>
<button class="faq-pill" data-filter="integration" type="button">API &amp; CLI Integration <span class="pill-count">4</span></button>
<button class="faq-pill" data-filter="compliance" type="button">Toolchain &amp; Licensing <span class="pill-count">4</span></button>
</div>

<div class="faq-action-bar">
<span class="faq-count-label" id="faqCountLabel">Showing 16 of 16 questions</span>
<button type="button" class="faq-toggle-all-btn" id="faqToggleAllBtn" aria-expanded="false">
<span class="btn-text">Expand all</span>
<span class="chevron" aria-hidden="true"></span>
</button>
</div>

<div class="faq-list" id="faqList">
<details class="faq-card" data-category="architecture">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">Formats</span>
<span class="faq-question">Which frontmatter formats does frontmatter-gen support out of the box?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p><code>frontmatter-gen</code> supports three formats out of the box with no feature flags required: <strong>YAML 1.2</strong> (bounded by <code>---</code> fences, parsed via <code>noyalib</code>), <strong>TOML 1.1</strong> (bounded by <code>+++</code> fences, parsed via <code>toml</code>), and <strong>JSON</strong> (a balanced leading <code>{ ... }</code> object or fenced JSON block, parsed via <code>serde_json</code>).</p>
</div>
</details>

<details class="faq-card" data-category="architecture">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">YAML 1.2</span>
<span class="faq-question">Why did frontmatter-gen switch from serde_yml / serde_yaml to noyalib?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p><code>serde_yaml</code> was archived upstream in March 2024 and implements YAML 1.1, which suffers from the Norway problem (unquoted <code>NO</code>, <code>no</code>, <code>on</code>, and <code>off</code> coerce to booleans). <code>noyalib</code> is an actively maintained, pure-Rust YAML 1.2 parser with zero <code>unsafe</code> code that keeps unquoted <code>no</code> and <code>off</code> as strings and preserves explicit YAML tags via <code>Value::Tagged</code> (ADR-0003).</p>
</div>
</details>

<details class="faq-card" data-category="architecture">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">Zero-Copy</span>
<span class="faq-question">Is extract_raw_frontmatter truly zero-copy?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>Yes. <code>extractor::extract_raw_frontmatter(content: &amp;str) -&gt; Result&lt;(&amp;str, &amp;str), ParseError&gt;</code> performs a single forward scan and returns two sub-slices borrowed directly from <code>content</code>. Neither the raw frontmatter slice nor the Markdown body slice is copied to the heap.</p>
</div>
</details>

<details class="faq-card" data-category="architecture">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">Encoding</span>
<span class="faq-question">How are UTF-8 byte-order marks (BOM) and CRLF line endings handled?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>If an input document starts with a UTF-8 BOM (<code>\u{FEFF}</code>), <code>extract_raw_frontmatter</code> strips the 3-byte prefix before checking for opening delimiters. Both Unix (<code>\n</code>) and Windows (<code>\r\n</code>) line endings are supported across YAML, TOML, and JSON extraction.</p>
</div>
</details>

<details class="faq-card" data-category="security">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">DoS Budgets</span>
<span class="faq-question">How do I protect against deeply nested or oversized frontmatter payloads?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>Pass a <code>ParseOptions</code> struct to <code>parser::parse_with_options</code> with <code>max_depth</code> (for example, <code>Some(8)</code>) and <code>max_keys</code> (for example, <code>Some(64)</code>). If the parsed frontmatter exceeds either limit, <code>parse_with_options</code> returns <code>Err(ParseError::InvalidFrontmatter)</code> immediately.</p>
</div>
</details>

<details class="faq-card" data-category="security">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">Memory Safety</span>
<span class="faq-question">Does frontmatter-gen contain any unsafe Rust blocks?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>No. Both the library crate (<code>src/lib.rs</code>) and binary crate (<code>src/main.rs</code>) declare <code>#![forbid(unsafe_code)]</code>. Any attempt to introduce an <code>unsafe</code> block fails compilation immediately.</p>
</div>
</details>

<details class="faq-card" data-category="security">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">Miri &amp; Fuzzing</span>
<span class="faq-question">How is memory safety verified beyond the Rust borrow checker?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>Every pull request runs the unit test suite under <strong>Miri</strong> with <code>-Zmiri-strict-provenance -Zmiri-tree-borrows -Zmiri-symbolic-alignment-check</code> across both <code>--no-default-features</code> and default feature sets, alongside 4 structure-aware <code>cargo-fuzz</code> targets and <code>proptest</code> property suites.</p>
</div>
</details>

<details class="faq-card" data-category="security">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">XSS Prevention</span>
<span class="faq-question">Does generate_metatags escape HTML special characters against XSS?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>Yes. <code>meta::generate_metatags</code> escapes <code>&amp;</code>, <code>&lt;</code>, <code>&gt;</code>, <code>&quot;</code>, and <code>&#39;</code> in all attribute values so untrusted frontmatter strings cannot break out of <code>content=&quot;...&quot;</code> attributes or inject script tags.</p>
</div>
</details>

<details class="faq-card" data-category="integration">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">Rust Crate</span>
<span class="faq-question">How do I integrate frontmatter-gen into an existing Rust application?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>Add the dependency to your <code>Cargo.toml</code>:</p>
<pre><code>[dependencies]&#10;frontmatter-gen = &quot;0.0.15&quot;</code></pre>
<p>Then extract and parse any Markdown document in one call:</p>
<pre><code>use frontmatter_gen::{extract, Value};&#10;fn main() -&gt; Result&lt;(), Box&lt;dyn std::error::Error&gt;&gt; {&#10;    let (fm, body) = extract(&quot;---\ntitle: Hello\n---\n# Body&quot;)?;&#10;    assert_eq!(fm.get(&quot;title&quot;), Some(&amp;Value::String(&quot;Hello&quot;.into())));&#10;    assert_eq!(body.trim(), &quot;# Body&quot;);&#10;    Ok(())&#10;}</code></pre>
</div>
</details>

<details class="faq-card" data-category="integration">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">Format Conversion</span>
<span class="faq-question">Can I convert frontmatter from one format to another (e.g. YAML to TOML or JSON)?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>Yes. Because YAML, TOML, and JSON all deserialize into the same <code>Frontmatter</code> type, you can parse a YAML header and call <code>frontmatter_gen::parser::to_string(&amp;fm, Format::Toml)</code> or <code>to_string(&amp;fm, Format::Json)</code> to serialize it into another format.</p>
</div>
</details>

<details class="faq-card" data-category="integration">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">YAML Tags</span>
<span class="faq-question">How does frontmatter-gen handle explicit YAML 1.2 tags like !custom?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>Explicit YAML tags are preserved as <code>Value::Tagged(String, Box&lt;Value&gt;)</code> where the first element is the tag name without the leading <code>!</code> and the second element is the inner <code>Value</code>. You can inspect them via <code>val.as_tagged()</code>.</p>
</div>
</details>

<details class="faq-card" data-category="integration">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">CLI &amp; SSG</span>
<span class="faq-question">What is the difference between the default library, the cli feature, and the ssg feature?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>The default library provides <code>extract</code>, <code>extractor</code>, <code>parser</code>, <code>meta</code>, and <code>error</code> with minimal dependencies. Enabling <code>--features cli</code> builds the <code>fmg</code> binary with <code>clap</code> and <code>tokio</code>. Enabling <code>--features ssg</code> adds the static site builder module powered by <code>tera</code> and <code>comrak</code>.</p>
</div>
</details>

<details class="faq-card" data-category="compliance">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">MSRV</span>
<span class="faq-question">What is the Minimum Supported Rust Version (MSRV)?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p><code>frontmatter-gen</code> targets <strong>Rust 1.85.0</strong> and <strong>Rust Edition 2024</strong>. The MSRV is verified in CI on every pull request.</p>
</div>
</details>

<details class="faq-card" data-category="compliance">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">Stability</span>
<span class="faq-question">What constitutes a breaking change in frontmatter-gen?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>In addition to Rust type and signature changes, any change to the observable output of <code>extract_metadata</code> or <code>generate_metatags</code> for existing inputs is treated as a breaking change under our stability policy.</p>
</div>
</details>

<details class="faq-card" data-category="compliance">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">Licensing</span>
<span class="faq-question">Under what license is frontmatter-gen distributed?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p><code>frontmatter-gen</code> is dual-licensed under the <strong>Apache License, Version 2.0</strong> and the <strong>MIT License</strong> (<code>Apache-2.0 OR MIT</code>) at the recipient's option, and is 100% REUSE 3.3 compliant.</p>
</div>
</details>

<details class="faq-card" data-category="compliance">
<summary class="faq-summary">
<span class="faq-question-wrap">
<span class="faq-category-badge">Support</span>
<span class="faq-question">Where can I report bugs, request features, or ask integration questions?</span>
</span>
<span class="faq-icon" aria-hidden="true"></span>
</summary>
<div class="faq-answer">
<p>Open an issue or discussion on <a href="https://github.com/sebastienrousseau/frontmatter-gen">GitHub</a>, or reach out via our <a href="/contact/index.html">Contact Page</a>. For security vulnerabilities, follow our <a href="/security/index.html">Security Policy</a>.</p>
</div>
</details>
</div>

<div class="faq-no-results" id="faqNoResults" role="status" aria-live="polite">
<div class="faq-no-results-icon" aria-hidden="true"></div>
<h2>No matching questions found</h2>
<p>Try searching for broader terms such as &ldquo;YAML 1.2&rdquo;, &ldquo;TOML&rdquo;, &ldquo;Miri&rdquo;, or &ldquo;CLI&rdquo;.</p>
<button type="button" class="faq-reset-btn" id="faqResetBtn">Reset search &amp; filters</button>
</div>

<div class="faq-help-card">
<div class="faq-help-icon" aria-hidden="true"></div>
<div class="faq-help-content">
<h2>Have a question not listed here?</h2>
<p>Explore the getting started guide and API reference, open an issue on GitHub, or contact us directly for architecture and integration support.</p>
<div class="faq-help-actions">
<a href="/getting-started/index.html" class="primary">Getting Started Guide</a>
<a href="https://github.com/sebastienrousseau/frontmatter-gen/issues" class="secondary" target="_blank" rel="noopener">GitHub Issues</a>
<a href="/contact/index.html" class="secondary">Contact Support</a>
</div>
</div>
</div>
</div>
