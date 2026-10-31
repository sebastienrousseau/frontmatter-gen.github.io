---
name: "Frontmatter Gen"
short_name: "frontmatter-gen"
title: "Security & Verification: Miri Tree Borrows, Fuzzing & Budgets"
description: "Security architecture of frontmatter-gen v0.0.15: #![forbid(unsafe_code)], Miri Tree Borrows verification, 4 cargo-fuzz targets, ParseOptions budgets, and cargo-vet."
keywords: "rust memory safety, miri tree borrows, cargo fuzz, ParseOptions DoS limits, cargo vet, forbid unsafe code, frontmatter security"
author: "Sebastien Rousseau"
date: "2026-10-31"
language: "en-GB"
layout: "page"
permalink: "https://frontmatter-gen.com/security/"
logo: "https://cloudcdn.pro/clients/frontmatter-gen/v1/logos/frontmatter-gen.svg"
banner: "https://cloudcdn.pro/stocks/images/block-chain-3055701-1200.webp"
banner_alt: "Frontmatter Gen: Formal Memory Safety Verification and Supply-Chain Integrity"
eyebrow: "Formal & Empirical Assurance"
headline: "Security Architecture & Trust Guarantees"
lead: "Defense-in-depth verification combining #![forbid(unsafe_code)], Miri Tree Borrows, structure-aware fuzzing, and configurable DoS budgets."
category: "Documentation"
changefreq: "weekly"
date_published: "2026-01-15T00:00:00Z"
date_modified: "2026-10-31T00:00:00Z"
priority: "0.9"
slug: "security"
url: "/security/"
apple_touch_icon_sizes: "192x192"
schema_type: "TechArticle"
theme_color: "#22242f"
---

Frontmatter parsers frequently sit at the trust boundary of content management systems, documentation portals, and static site pipelines where Markdown files arrive from external contributors or untrusted repositories. Frontmatter Gen enforces five layers of verification to ensure untrusted inputs cannot trigger memory unsafety, resource exhaustion, or HTML injection.

<div class="stat-grid my-4">
<div class="stat-card">
<div class="stat-figure">0 Unsafe</div>
<div class="stat-label">#![forbid(unsafe_code)]</div>
</div>
<div class="stat-card">
<div class="stat-figure">100%</div>
<div class="stat-label">Unit Test Coverage</div>
</div>
<div class="stat-card">
<div class="stat-figure">4 Targets</div>
<div class="stat-label">LibFuzzer Harnesses</div>
</div>
</div>

<div class="step-item">
<div class="step-header">
<span class="step-badge">01</span>
<h2 class="step-title">Memory Safety &amp; Miri Tree Borrows Verification</h2>
</div>
<p>Both <code>src/lib.rs</code> and <code>src/main.rs</code> declare <code>#![forbid(unsafe_code)]</code>, and the YAML 1.2 dependency <code>noyalib</code> is likewise 100% safe Rust. Every pull request runs the test suite under <strong>Miri</strong> with strict provenance and Tree Borrows aliasing checks:</p>

<div class="terminal-box my-3">
<div class="terminal-bar">
<span class="terminal-dot dot-red"></span>
<span class="terminal-dot dot-yellow"></span>
<span class="terminal-dot dot-green"></span>
<span class="terminal-title">bash — miri tree borrows verification</span>
</div>
<div class="terminal-body">
<div class="t-line"><span class="t-comment">&#35; Run Miri across minimal and default feature sets with Tree Borrows</span></div>
<div class="t-line"><span class="t-prompt">$</span>MIRIFLAGS=<span class="t-val">&quot;-Zmiri-strict-provenance -Zmiri-tree-borrows -Zmiri-symbolic-alignment-check&quot;</span> cargo +nightly miri test --lib --no-default-features --locked</div>
<div class="t-line"><span class="t-prompt">$</span>MIRIFLAGS=<span class="t-val">&quot;-Zmiri-strict-provenance -Zmiri-tree-borrows -Zmiri-symbolic-alignment-check&quot;</span> cargo +nightly miri test --lib --locked</div>
</div>
</div>
</div>

<div class="step-item">
<div class="step-header">
<span class="step-badge">02</span>
<h2 class="step-title">DoS Budget Guardrails &amp; Fuzzing Harnesses</h2>
</div>
<p>Untrusted YAML, TOML, or JSON headers can attempt denial-of-service via deeply nested structures or thousands of keys. <code>parser::parse_with_options</code> enforces deterministic budgets before returning a <code>Frontmatter</code> value, backed by four structure-aware <code>cargo-fuzz</code> targets:</p>

<div class="table-responsive my-3">
<table class="visage-table">
<thead>
<tr>
<th>Verification Control</th>
<th>Target / API</th>
<th>Security Guarantee</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Nesting Depth Budget</strong></td>
<td><code>ParseOptions::max_depth</code></td>
<td>Rejects YAML, TOML, or JSON trees nested deeper than <code>max_depth</code> levels.</td>
</tr>
<tr>
<td><strong>Key Count Budget</strong></td>
<td><code>ParseOptions::max_keys</code></td>
<td>Rejects frontmatter payloads containing more than <code>max_keys</code> total keys across all maps.</td>
</tr>
<tr>
<td><strong>HTML Entity Escaping</strong></td>
<td><code>meta::generate_metatags</code></td>
<td>Escapes <code>&amp;</code>, <code>&lt;</code>, <code>&gt;</code>, <code>&quot;</code>, and <code>&#39;</code> in all generated <code>&lt;meta&gt;</code> attributes.</td>
</tr>
<tr>
<td><strong>LibFuzzer Harnesses</strong></td>
<td><code>fuzz/fuzz_targets/*.rs</code></td>
<td>Continuous fuzzing across <code>extract_frontmatter</code>, <code>parse_yaml</code>, <code>parse_toml</code>, and <code>parse_json</code>.</td>
</tr>
<tr>
<td><strong>Supply-Chain Audits</strong></td>
<td><code>cargo-deny</code>, <code>cargo-vet</code>, <code>cargo-audit</code></td>
<td>Verifies license policies, RustSec advisories, and third-party crate audits on every CI run.</td>
</tr>
</tbody>
</table>
</div>
</div>

<div class="step-item">
<div class="step-header">
<span class="step-badge">03</span>
<h2 class="step-title">Vulnerability Disclosure Policy (RFC 9116)</h2>
</div>
<p>If you discover a security vulnerability in <code>frontmatter-gen</code>, please report it privately via <a href="https://github.com/sebastienrousseau/frontmatter-gen/security/advisories/new">GitHub Security Advisories</a> or email <a href="mailto:sebastien.rousseau@gmail.com">sebastien.rousseau@gmail.com</a>. See our machine-readable <a href="/.well-known/security.txt">/.well-known/security.txt</a> for RFC 9116 disclosure metadata.</p>

<div class="doc-visual-card">
<picture>
<source media="(max-width: 40rem)" srcset="https://cloudcdn.pro/stocks/images/block-chain-3055701-320.webp 320w, https://cloudcdn.pro/stocks/images/block-chain-3055701-640.webp 640w, https://cloudcdn.pro/stocks/images/block-chain-3055701-1200.webp 1200w" sizes="100vw">
<img src="https://cloudcdn.pro/stocks/images/block-chain-3055701-1200.webp" alt="Formal verification, Miri Tree Borrows, and supply-chain security for frontmatter-gen" width="1200" height="675" loading="lazy" />
</picture>
<div class="doc-visual-caption">Defense-in-depth assurance: #![forbid(unsafe_code)], Miri Tree Borrows, 100% unit test coverage, and REUSE 3.3 licensing compliance.</div>
</div>
</div>
