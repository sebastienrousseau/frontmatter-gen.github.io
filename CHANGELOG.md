# Changelog

All notable changes to this website are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.0.2] - 2026-10-31
### Changed
- Bumped the `python-test` dependency group in `requirements/` (`hypothesis` 6.170.13 and `pytest` 9.2.0).
### Fixed
- Removed redundant `aria-label` on `<ul class="hero-assurances">` in `_posts/index.md` to satisfy `html-validate@10` (`aria-label-misuse`) in CI and unblock GitHub Pages deployment.
- Ordered `python3 scripts/post-build.py` before `ssg audit` in `.github/workflows/release.yml` so `/.well-known/security.txt` is present during release link auditing, and preserved `docs/_csp/` assets in `.github/workflows/ci.yml`.

## [0.0.1] - 2026-10-31

### Added

- Launched `frontmatter-gen.com` (`frontmatter-gen.github.io`) compiled with
  native Rust Static Site Generator (`ssg` 0.0.69) and the Skeletonic CSS
  `kairo` brand-matched terracotta, parchment cream, and slate-navy theme.
- Documented `frontmatter-gen` v0.0.15 across 20 pages: zero-copy extraction
  (`extract_raw_frontmatter`), YAML 1.2 (`noyalib`), TOML 1.1, and JSON parsing,
  configurable DoS budgets (`ParseOptions`), HTML `<meta>` tag synthesis
  (`generate_metatags`), `fmg` CLI, Miri Tree Borrows verification, and
  structure-aware `Arbitrary` fuzzing.
- Enforced WCAG 2.2 Level AAA accessibility across 41 audited color token pairs
  (`>= 7.51:1` light mode, `>= 7.53:1` dark mode), full keyboard navigation, and
  3-state theme persistence (`Light`, `Dark`, `System`).
- Added Subresource Integrity (`sha384-` SRI), strict Content Security Policy
  (CSP) headers, RFC 9116 `/.well-known/security.txt`, CycloneDX SBOM
  generation, and `llms.txt` / `llms-full.txt` bundles.
- Dual-licensed under Apache-2.0 OR MIT.

[Unreleased]: https://github.com/sebastienrousseau/frontmatter-gen.github.io/compare/v0.0.1...HEAD
[0.0.1]: https://github.com/sebastienrousseau/frontmatter-gen.github.io/releases/tag/v0.0.1
