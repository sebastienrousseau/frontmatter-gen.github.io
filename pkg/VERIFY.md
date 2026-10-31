# Artifact & Release Verification Guide

Every release of `frontmatter-gen.github.io` is cryptographically signed, accompanied by SHA-256 checksums, and ships with a CycloneDX Software Bill of Materials (`docs/sbom.cdx.json`).

---

## 1. Verify Git Tag Signatures (`KEYS.asc`)

Verify any release tag against the OpenSSH allowed-signers file [`KEYS.asc`](../KEYS.asc):

```sh
git -c gpg.ssh.allowedSignersFile=KEYS.asc tag -v v0.0.1
```

---

## 2. Verify Subresource Integrity (SRI) & Asset Checksums

Every compiled HTML page in `docs/` pins its stylesheet and script dependencies using `sha384-` Subresource Integrity hashes. To verify build artifacts manually:

```sh
shasum -a 256 docs/index.html docs/styles.*.css docs/main.*.js docs/sbom.cdx.json
```

Or run the automated portfolio quality gate, which recomputes SHA-384 digests across all assets and cross-checks every `<link>` and `<script>` tag:

```sh
make verify
```

---

## 3. Inspect CycloneDX SBOM

The static site generator emits a machine-readable CycloneDX SBOM at [`docs/sbom.cdx.json`](../docs/sbom.cdx.json) linked via `<link rel="sbom" type="application/vnd.cyclonedx+json" href="/sbom.cdx.json">` on every page.
