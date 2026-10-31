# Migration Guide

This guide covers migrating existing Rust frontmatter pipelines to **frontmatter-gen** (`v0.0.15`) from `serde_yaml`-based crates (`gray_matter`, `yaml-front-matter`, `pulldown-cmark-frontmatter`) and earlier `0.0.x` releases.

---

## 1. Migrating from `serde_yaml`-Based Frontmatter Crates

`serde_yaml` was archived upstream in March 2024 and parses YAML 1.1 (where unquoted `no`, `off`, and `on` coerce to booleans). `frontmatter-gen` uses `noyalib` (pure-Rust YAML 1.2) and supports YAML 1.2, TOML 1.1, and JSON in a single dependency.

| Capability | Legacy `serde_yaml` Crates | `frontmatter-gen` (`v0.0.15`) |
| :--- | :--- | :--- |
| **YAML Specification** | YAML 1.1 (`serde_yaml`, archived) | YAML 1.2 (`noyalib`, active) |
| **Supported Formats** | Typically YAML-only or requires feature flags | YAML 1.2 + TOML 1.1 + JSON enabled by default |
| **Body Extraction** | Allocates owned `String` copies | Zero-copy `(&str, &str)` via `extract_raw_frontmatter` |
| **Safety & Verification** | Unbounded recursion on untrusted input | `#![forbid(unsafe_code)]`, `ParseOptions` budgets, Miri Tree Borrows |

### Replacement Pattern (Rust)

```rust
// Extract and parse YAML, TOML, or JSON frontmatter in one call:
use frontmatter_gen::{extract, Value};

let content = "---\ntitle: Hello Rust\ndraft: false\n---\n# Body\n";
let (frontmatter, body) = extract(content)?;
assert_eq!(
    frontmatter.get("title"),
    Some(&Value::String("Hello Rust".to_string()))
);
assert_eq!(body.trim(), "# Body");
```

---

## 2. Migrating Within `frontmatter-gen` (`0.0.12` to `0.0.15`)

- **YAML 1.2 Engine (`0.0.13+`)**: `serde_yml` was replaced by `noyalib` (`=0.0.58`). Unquoted `yes`/`no`/`on`/`off` are now plain strings per YAML 1.2 (`true`/`false` remain booleans). Explicit YAML tags (`!custom value`) are preserved as `Value::Tagged(tag, inner)`.
- **Path Validation (`0.0.13+`)**: `fmg` CLI commands now reject `..` traversal components and symlinked input files via `validate_path_safety` before opening files.
- **Verification Gate (`0.0.15`)**: Added Miri verification under Tree Borrows (`-Zmiri-strict-provenance -Zmiri-tree-borrows`), structure-aware `Arbitrary` fuzzing (`fuzz_structured`), and 100% unit test coverage.
