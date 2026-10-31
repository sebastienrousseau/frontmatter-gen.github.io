---
name: "Frontmatter Gen"
short_name: "frontmatter-gen"
title: "Contributing Guide: Quality Gates & Verification"
description: "Contribution guidelines for frontmatter-gen and frontmatter-gen.com: +0.0.1 versioning, signed commits, 100% test coverage, Miri, and REUSE 3.3 compliance."
keywords: "frontmatter-gen contributing, rust open source contribution, miri tests, reuse lint"
author: "Sebastien Rousseau"
date: "2026-10-31"
language: "en-GB"
layout: "page"
permalink: "https://frontmatter-gen.com/contributing/"
logo: "https://cloudcdn.pro/clients/frontmatter-gen/v1/logos/frontmatter-gen.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Frontmatter Gen: Zero-Copy Frontmatter Extraction and Parsing in Rust"
eyebrow: "Community & Code"
headline: "Contributing to Frontmatter Gen"
lead: "Guidelines for bug reports, pull requests, local quality gates, and DCO sign-offs."
category: "Legal"
changefreq: "monthly"
date_published: "2026-01-15T00:00:00Z"
date_modified: "2026-10-31T00:00:00Z"
priority: "0.5"
slug: "contributing"
url: "/contributing/"
apple_touch_icon_sizes: "192x192"
schema_type: "WebPage"
theme_color: "#22242f"
---

Contributions to both the [frontmatter-gen Rust crate](https://github.com/sebastienrousseau/frontmatter-gen) and the [frontmatter-gen.github.io documentation portal](https://github.com/sebastienrousseau/frontmatter-gen.github.io) are welcome under our dual `Apache-2.0 OR MIT` license.

<div class="step-item">
<div class="step-header">
<span class="step-badge">01</span>
<h2 class="step-title">Rust Crate Quality Gates (`frontmatter-gen`)</h2>
</div>
<p>Every pull request to the Rust crate must pass the full local verification battery before review:</p>

<div class="terminal-box my-3">
<div class="terminal-bar">
<span class="terminal-dot dot-red"></span>
<span class="terminal-dot dot-yellow"></span>
<span class="terminal-dot dot-green"></span>
<span class="terminal-title">bash — crate verification battery</span>
</div>
<div class="terminal-body">
<div class="t-line"><span class="t-prompt">$</span>cargo fmt --all -- --check</div>
<div class="t-line"><span class="t-prompt">$</span>cargo clippy --all-targets --all-features -- -D warnings</div>
<div class="t-line"><span class="t-prompt">$</span>cargo test --all-features</div>
<div class="t-line"><span class="t-prompt">$</span>MIRIFLAGS=<span class="t-val">&quot;-Zmiri-strict-provenance -Zmiri-tree-borrows -Zmiri-symbolic-alignment-check&quot;</span> cargo +nightly miri test --lib --locked</div>
<div class="t-line"><span class="t-prompt">$</span>reuse lint</div>
</div>
</div>
</div>

<div class="step-item">
<div class="step-header">
<span class="step-badge">02</span>
<h2 class="step-title">Documentation Portal Quality Gates (`frontmatter-gen.github.io`)</h2>
</div>
<p>Build the static site and run the 15-gate <code>ssg audit</code>, WCAG 2.2 AAA contrast verification, and regression test suite:</p>

<div class="terminal-box my-3">
<div class="terminal-bar">
<span class="terminal-dot dot-red"></span>
<span class="terminal-dot dot-yellow"></span>
<span class="terminal-dot dot-green"></span>
<span class="terminal-title">bash — website verification battery</span>
</div>
<div class="terminal-body">
<div class="t-line"><span class="t-prompt">$</span>make build</div>
<div class="t-line"><span class="t-prompt">$</span>make verify</div>
</div>
</div>
</div>

<div class="step-item">
<div class="step-header">
<span class="step-badge">03</span>
<h2 class="step-title">Versioning, Commits &amp; DCO Sign-Off</h2>
</div>
<p>All repositories follow strict versioning and commit standards:</p>

<div class="table-responsive my-3">
<table class="visage-table">
<thead>
<tr>
<th>Standard</th>
<th>Requirement</th>
<th>Verification</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Semantic Versioning</strong></td>
<td>Releases increment strictly by <code>+0.0.1</code> on <code>feat/vX.Y.Z</code> branches.</td>
<td>Verified by <code>verify-release-versions.sh</code></td>
</tr>
<tr>
<td><strong>Conventional Commits</strong></td>
<td>Imperative subject line (max 50 chars) with SSH/GPG signature (<code>-S</code>).</td>
<td>Enforced by commitlint &amp; branch protection</td>
</tr>
<tr>
<td><strong>DCO &amp; SPDX</strong></td>
<td><code>Signed-off-by</code> trailer (<code>-s</code>) and SPDX license headers on all files.</td>
<td>Verified by <code>reuse lint</code> &amp; DCO check</td>
</tr>
</tbody>
</table>
</div>
</div>
