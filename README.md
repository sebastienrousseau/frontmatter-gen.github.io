<!-- SPDX-License-Identifier: Apache-2.0 OR MIT -->

<p align="center">
  <img src="https://cloudcdn.pro/clients/frontmatter-gen/v1/logos/frontmatter-gen.svg" alt="Frontmatter Gen logo" width="128" />
</p>

<h1 align="center">Frontmatter Gen</h1>

<p align="center">
  Official static documentation portal for <code>frontmatter-gen</code>: zero-copy frontmatter extraction and multi-format parsing library and CLI for YAML 1.2, TOML, and JSON in Rust with HTML meta tag generation and zero unsafe code.
</p>

<p align="center">
  <a href="https://github.com/sebastienrousseau/frontmatter-gen.github.io/actions"><img src="https://img.shields.io/github/actions/workflow/status/sebastienrousseau/frontmatter-gen.github.io/ci.yml?style=for-the-badge&logo=github" alt="Build" height="28" /></a>
  <a href="https://github.com/sebastienrousseau/frontmatter-gen.github.io/releases"><img src="https://img.shields.io/github/v/release/sebastienrousseau/frontmatter-gen.github.io?style=for-the-badge&color=fc8d62&logo=git" alt="Release" height="28" /></a>
  <a href="https://frontmatter-gen.com"><img src="https://img.shields.io/badge/docs-frontmatter--gen.com-fa6238?style=for-the-badge&labelColor=22242f&logo=googlechrome" alt="Docs" height="28" /></a>
  <a href="https://scorecard.dev/viewer/?uri=github.com/sebastienrousseau/frontmatter-gen.github.io"><img src="https://img.shields.io/ossf-scorecard/github.com/sebastienrousseau/frontmatter-gen.github.io?style=for-the-badge&label=OpenSSF%20Scorecard&logo=openssf" alt="OpenSSF Scorecard" height="28" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0%20OR%20MIT-blue.svg?style=for-the-badge" alt="License: Apache-2.0 OR MIT" height="28" /></a>
  <a href="https://static-site-generator.com/"><img src="https://img.shields.io/badge/SSG-0.0.69-93450a.svg?style=for-the-badge&logo=rust" alt="Built with Rust SSG" height="28" /></a>
</p>

---

## Contents

**Getting started**

- [Install](#install) — build prerequisites and tooling
- [Requirements](#requirements) — toolchain floor, platforms
- [Quick Start](#quick-start) — compile and preview the static site

**The Frontmatter Gen ecosystem**

- [The Frontmatter Gen ecosystem](#the-frontmatter-gen-ecosystem) — core Rust crate, `fmg` CLI, `ssg` engine, and documentation portal

**Library reference**

- [Capabilities at a glance](#capabilities-at-a-glance) — static site architecture and web standards
- [Ecosystem comparison](#ecosystem-comparison) — design and accessibility comparison
- [Benchmarks](#benchmarks) — compilation speed and WCAG audit scores
- [Features](#features) — site capabilities and security features
- [Configuration](#configuration) — SSG manifest and layout configuration
- [Examples](#examples) — runnable development workflows

**Operational**

- [When not to use Frontmatter Gen](#when-not-to-use-frontmatter-gen) — limitations
- [Development](#development) — make targets, validation, and quality gates
- [Security](#security) — Subresource Integrity (SRI) and CSP enforcement
- [Documentation](#documentation) — all reference docs
- [Stability guarantees](#stability-guarantees) — versioning discipline and WCAG AAA compliance
- [License](#license)

---

## Install

### As a Static Site Generator project

Ensure `ssg` (Static Site Generator) and Python are installed:

```bash
# Install the Rust static site generator
cargo install ssg --locked --version 0.0.69

# Clone the documentation repository
git clone https://github.com/sebastienrousseau/frontmatter-gen.github.io.git
cd frontmatter-gen.github.io
```

Optional audit tooling includes `html-validate`, `pa11y-ci`, and `@lhci/cli` for CI conformance testing:

```bash
npm install -g html-validate pa11y-ci @lhci/cli
```

---

## Requirements

- **Rust Toolchain**: Rust 1.85+ (for compiling `ssg` static site generator and `frontmatter-gen`).
- **Node.js**: Node 24+ (for HTML validation and accessibility CI suites).
- **Python**: Python 3.12+ (for contrast ratios and regression testing).
- **Target Platforms**: Linux, macOS, Windows (cross-platform static deployment).

---

## Quick Start

```bash
# Build the complete site using Rust SSG and post-build optimization
make build

# Run WCAG 2.2 Level AAA and regression test suites
make audit

# Serve locally for preview
make serve
```

Navigate to `http://127.0.0.1:8000` to inspect the generated documentation portal.

---

## The Frontmatter Gen ecosystem

The `frontmatter-gen` suite provides end-to-end tooling for Markdown frontmatter extraction, multi-format parsing, SEO meta tag generation, and static documentation:

| Component | Purpose | Use case |
| :--- | :--- | :--- |
| [frontmatter-gen](https://github.com/sebastienrousseau/frontmatter-gen) | Core Rust library (`v0.0.15`) | Zero-copy extraction and YAML 1.2, TOML, and JSON frontmatter parsing |
| [fmg CLI](https://github.com/sebastienrousseau/frontmatter-gen) | Standalone command-line binary (`--features cli`) | Terminal frontmatter extraction (`fmg extract`) and static site builds (`fmg build`) |
| [frontmatter-gen.github.io](https://github.com/sebastienrousseau/frontmatter-gen.github.io) | Static documentation portal (`frontmatter-gen.com`) | Zero-telemetry documentation, API reference, and architectural guides |

---

## Capabilities at a glance

| Area | Capability | Status |
| :--- | :--- | :--- |
| Static Generation | Rust SSG v0.0.69 + Tera template compilation | Active |
| Theme Architecture | Skeletonic CSS v3.0.0 (`kairo` brand-matched terracotta & slate) | Active |
| Accessibility | 100% WCAG 2.2 Level AAA compliance (>= 7.51:1 worst text contrast) | Verified |
| Content Security | Strict Content-Security-Policy (CSP) with zero inline scripts | Enforced |
| Integrity | SHA-384 Subresource Integrity (SRI) on all scripts and styles | Active |
| Search Engine | Client-side zero-telemetry indexing via `search-index.json` | Active |
| Feeds & Syndication | Atom, RSS 2.0, JSON Feed, Sitemap, `llms.txt`, and CycloneDX SBOM | Automated |

---

## Ecosystem comparison

| Project | Zero Telemetry | WCAG 2.2 AAA | Subresource Integrity | Fast Native SSG |
| :--- | :---: | :---: | :---: | :---: |
| **Frontmatter Gen Web** | **Yes** | **Yes (7.51:1 worst)** | **Yes (SHA-384)** | **Yes (Rust SSG)** |
| Docusaurus | No (Default telemetry) | Partial (AA) | No | No (Node.js) |
| GitBook / Cloud Docs | No (Third-party hosted) | Partial (AA) | No | No (Proprietary SaaS) |

---

## Benchmarks

Audit and regression suites are executed continuously on every commit:

| Scenario | Result | Environment |
| :--- | ---: | :--- |
| Full Site Compilation (20 Pages) | < 2.0s | Rust `ssg` 0.0.69, 32 plugins |
| Worst Light Mode Text Contrast Ratio | 7.51:1 | WCAG 2.2 AAA (Threshold >= 7.0:1) |
| Worst Dark Mode Text Contrast Ratio | 7.53:1 | WCAG 2.2 AAA (Threshold >= 7.0:1) |
| Lighthouse Performance / A11y | 100 / 100 | Clean ECMAScript, zero heavy runtimes |

---

## Features

- **Rust Static Site Generator (SSG)**: Markdown content parsing and Tera template compilation with sub-second page generation.
- **Brand-Matched Kairo Theme**: Warm terracotta (`#fa6238` / `#8f250c` light, `#ff9e80` dark), parchment cream (`#f8ebce`), and deep slate-navy (`#22242f`) WCAG 2.2 AAA token system with 3-state theme persistence (`Light`, `Dark`, `System`).
- **Subresource Integrity (SRI)**: SHA-384 cryptographic digests enforced across all assets.
- **Zero Third-Party Tracking**: Completely self-hosted static assets on high-assurance edge CDN (`cloudcdn.pro`).
- **Offline PWA Readiness**: Service worker (`sw.js`), manifest generation, and offline fallback routes.
- **AI Integration Manifests**: Machine-readable `llms.txt`, `llms-full.txt`, and Agent API documentation.

---

## Configuration

Site configuration is governed by `config/ssg.json` and `ssg.toml`:

```json
{
  "title": "Frontmatter Gen",
  "description": "Zero-copy frontmatter extraction and multi-format parsing library and CLI for YAML 1.2, TOML, and JSON in Rust with HTML meta tag generation and zero unsafe code.",
  "cdn": "https://cloudcdn.pro"
}
```

Template layouts reside in `_layouts/` with Markdown articles under `_posts/`. Compiled web assets are mirrored to `docs/` for GitHub Pages distribution.

---

## Examples

### Local Compilation & Contrast Verification

```bash
# Compile Markdown content and layout templates into public/ and docs/
make build

# Run mathematical color contrast verification
make contrast

# Run Markdown frontmatter schema validator
make validate
```

---

## When not to use Frontmatter Gen

- **Dynamic Server-Side Applications**: This repository produces purely static, pre-rendered HTML/CSS/JS. It does not include a dynamic backend database or runtime server.
- **Full-Document YAML/TOML/JSON Serialization**: The `frontmatter-gen` library documented here focuses on document headers (`Frontmatter` key-value maps) rather than arbitrary top-level arrays or streaming gigabyte payloads.

---

## Development

```bash
# Run complete verification suite (lint + test + audit)
make verify

# Run HTML5 and WCAG structural validation
npx --yes html-validate@10 "docs/**/*.html"

# Run color contrast compliance check
python3 audit/contrast.py
```

All pull requests must pass HTML validation, contrast analysis, and structural self-hosting guardrails before merging.

---

## Security

Every deployment enforces strict cryptographic and architectural controls:

- **Strict Content Security Policy**: Eliminates unsafe script evaluation and restricts asset loading.
- **Air-Gapped Operation**: Zero outbound analytics, telemetry, or external tracking beacons.
- **Supply Chain Assurance**: CycloneDX SBOM generated on every build (`docs/sbom.cdx.json`).

Report vulnerabilities according to [`SECURITY.md`](SECURITY.md).

---

## Documentation

- [Getting Started Guide](https://frontmatter-gen.com/getting-started/index.html)
- [Supported Formats Matrix](https://frontmatter-gen.com/formats/index.html)
- [Pipeline Architecture](https://frontmatter-gen.com/architecture/index.html)
- [Performance Benchmarks](https://frontmatter-gen.com/benchmarks/index.html)
- [Miri & Fuzzing Security](https://frontmatter-gen.com/security/index.html)
- [Rust API & CLI Reference](https://frontmatter-gen.com/api/index.html)
- [Release Changelog](https://frontmatter-gen.com/changelog/index.html)
- [Contributing Guidelines](https://frontmatter-gen.com/contributing/index.html)
- [WCAG AAA Accessibility Statement](https://frontmatter-gen.com/accessibility/index.html)

---

## Stability guarantees

Versions follow strict Semantic Versioning (`0.0.1` -> `0.0.2` -> ...), advancing incrementally per repository conventions. The layout, visual contrast, and WCAG AAA compliance are regression-tested on every release.

---

## License

Dual-licensed under [Apache-2.0](LICENSE-APACHE) OR [MIT](LICENSE-MIT), at your option. See [LICENSE](LICENSE).
