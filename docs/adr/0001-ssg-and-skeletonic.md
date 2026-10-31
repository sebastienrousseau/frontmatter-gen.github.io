# ADR 0001: Use Rust SSG and Skeletonic Kairo Brand Theme

- **Status**: Accepted
- **Date**: 2026-10-31

## Context

`frontmatter-gen.com` requires deterministic, fast static site generation with
WCAG 2.2 Level AAA accessibility, zero third-party telemetry, and cryptographic
Subresource Integrity (SRI).

## Decision

Compile the site with the Rust `ssg` binary (`0.0.69`) and style it with the
Skeletonic CSS (`kairo` warm terracotta & slate theme from `ssg-themes.github.io`)
matched to the `frontmatter-gen` logo colors (`#fa6238`, `#f8ebce`, `#22242f`)
using WCAG 2.2 AAA color tokens (`>= 7.0:1` contrast across Light and Dark modes).

## Consequences

All HTML, CSS, RSS, sitemap, and SBOM artifacts are generated reproducibly in
under two seconds without a Node.js runtime dependency at build time.
