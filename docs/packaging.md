# Packaging

Each tagged release `vX.Y.Z` produces three assets in `dist/`:

- `frontmatter-gen-site-vX.Y.Z.tar.gz` — deterministic PAX tarball (`mtime`
  pinned to commit timestamp, `uid/gid = 0`, `gzip -n`) containing the compiled
  `site/` tree and license files.
- `frontmatter-gen-site-vX.Y.Z.cdx.json` — CycloneDX 1.5 SBOM with a
  deterministic UUIDv5 `serialNumber`.
- `SHA256SUMS` — SHA-256 digests of the tarball and SBOM.
