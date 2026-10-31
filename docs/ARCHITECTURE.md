# Architecture

`frontmatter-gen.github.io` is the static documentation site for
[frontmatter-gen](https://github.com/sebastienrousseau/frontmatter-gen) (`https://frontmatter-gen.com/`).

## Build pipeline

1. `_posts/*.md` holds page content and YAML frontmatter.
2. `_layouts/*.html` holds Tera templates (`base.html`, `header.html`, `footer.html`, `index.html`, `page.html`, `faqs.html`, `contact.html`, `404.html`, `offline.html`).
3. `ssg` (`0.0.69`) compiles Markdown and templates into `public/` and `scripts/post-build.py` synchronizes the verified output to `docs/`.
4. `ssg audit`, `audit/contrast.py`, and `scripts/regression-test.py` verify WCAG 2.2 Level AAA accessibility, Subresource Integrity (SRI), Content Security Policy (CSP), and structural completeness.
