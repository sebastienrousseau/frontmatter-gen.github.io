---
name: "Frontmatter Gen"
short_name: "frontmatter-gen"
title: "Changelog & Release History: Frontmatter Gen"
description: "Release history and semantic changelog for frontmatter-gen through v0.0.15 and the frontmatter-gen.com documentation portal."
keywords: "frontmatter-gen changelog, frontmatter-gen v0.0.15, noyalib migration, release notes"
author: "Sebastien Rousseau"
date: "2026-10-31"
language: "en-GB"
layout: "page"
permalink: "https://frontmatter-gen.com/changelog/"
logo: "https://cloudcdn.pro/clients/frontmatter-gen/v1/logos/frontmatter-gen.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Frontmatter Gen: Zero-Copy Frontmatter Extraction and Parsing in Rust"
eyebrow: "Release History"
headline: "Changelog"
lead: "Every release increments strictly by +0.0.1 with signed tags, full test coverage, and zero unsafe code."
category: "Information"
changefreq: "weekly"
date_published: "2026-01-15T00:00:00Z"
date_modified: "2026-10-31T00:00:00Z"
priority: "0.8"
slug: "changelog"
url: "/changelog/"
apple_touch_icon_sizes: "192x192"
schema_type: "WebPage"
theme_color: "#22242f"
---

All notable changes to **Frontmatter Gen** (`frontmatter-gen`) are documented below following strict `+0.0.1` Semantic Versioning.

## [v0.0.15] - 2026-10-31
### Fixed
- Resolved a Miri symbolic alignment check failure (`_mm_load_si128` 16-byte alignment requirement on 8-byte aligned slice inside `memchr` 2.8.2) during `edge_case_tests::test_large_frontmatter` by upgrading `noyalib` to `0.0.60`.
### Added
- Reached **100.00% line, function, and region unit test coverage** across all 10 source files (`src/lib.rs`, `src/extractor.rs`, `src/parser.rs`, `src/meta.rs`, `src/error.rs`, `src/config.rs`, `src/engine.rs`, `src/fs.rs`, `src/markdown.rs`, `src/template.rs`).

## [v0.0.14] - 2026-04-19
### Changed
- Migrated YAML parsing and serialization from `serde_yml` (archived YAML 1.1) to pure-Rust **`noyalib`** (YAML 1.2) as recorded in ADR-0003.
- Preserved explicit YAML 1.2 tags via `Value::Tagged(String, Box<Value>)` and `Value::as_tagged()`.
- Added `ParseOptions` (`validate`, `max_depth`, `max_keys`) and `parser::parse_with_options` for configurable DoS budget enforcement.
- Added Miri verification with `-Zmiri-strict-provenance -Zmiri-tree-borrows -Zmiri-symbolic-alignment-check`, 4 `cargo-fuzz` targets, and `cargo-vet` supply-chain auditing.

## [v0.0.1 - v0.0.13] - 2023-2026
### Added
- Core zero-copy frontmatter extraction (`extractor::extract_raw_frontmatter`), automatic format detection (`detect_format`), multi-format parsing (YAML, TOML, JSON), HTML meta tag synthesis (`meta::generate_metatags`), optional `cli` (`fmg`) binary, and optional `ssg` static site builder.
- Full historical release notes are available in the [GitHub CHANGELOG.md](https://github.com/sebastienrousseau/frontmatter-gen/blob/main/CHANGELOG.md).
