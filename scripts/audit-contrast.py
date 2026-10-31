#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT
"""
WCAG 2.2 Level AAA Contrast Verification Suite for Frontmatter Gen.
Mathematically proves >= 7.0:1 contrast ratio for all normal text pairs
and >= 4.5:1 for large text / UI borders across Light and Dark modes.
"""

import sys


def srgb_to_linear(c: int) -> float:
    v = c / 255.0
    return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4


def hex_to_luminance(hex_code: str) -> float:
    h = hex_code.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return 0.2126 * srgb_to_linear(r) + 0.7152 * srgb_to_linear(g) + 0.0722 * srgb_to_linear(b)


def contrast_ratio(fg: str, bg: str) -> float:
    l1 = hex_to_luminance(fg)
    l2 = hex_to_luminance(bg)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


PAIRS = [
    # Light Mode Pairs (Target >= 7.0:1 for AAA Normal Text)
    ("Light: Body Text (--ink on --bg)", "#161821", "#f8f5ef", 7.0),
    ("Light: Card Text (--ink on --surface)", "#161821", "#ffffff", 7.0),
    ("Light: Secondary Text (--ink-soft on --bg)", "#22242f", "#f8f5ef", 7.0),
    ("Light: Secondary on Surface (--ink-soft on --surface)", "#22242f", "#ffffff", 7.0),
    ("Light: Muted Text (--ink-muted on --bg)", "#3d404f", "#f8f5ef", 7.0),
    ("Light: Muted on Surface (--ink-muted on --surface)", "#3d404f", "#ffffff", 7.0),
    ("Light: Primary Link (--accent on --bg)", "#8f250c", "#f8f5ef", 7.0),
    ("Light: Primary Link on Card (--accent on --surface)", "#8f250c", "#ffffff", 7.0),
    ("Light: Primary Button Text (--accent-ink on --accent)", "#ffffff", "#8f250c", 7.0),
    ("Light: Highlight Text (--on-accent-soft on --accent-soft)", "#4a1404", "#f8ebce", 7.0),
    ("Light: Scene Text (--scene-ink on --scene)", "#ffffff", "#22242f", 7.0),

    # Dark Mode Pairs (Target >= 7.0:1 for AAA Normal Text)
    ("Dark: Body Text (--ink on --bg)", "#faf6ed", "#12131a", 7.0),
    ("Dark: Card Text (--ink on --surface)", "#faf6ed", "#1b1d28", 7.0),
    ("Dark: Secondary Text (--ink-soft on --bg)", "#f8ebce", "#12131a", 7.0),
    ("Dark: Secondary on Card (--ink-soft on --surface)", "#f8ebce", "#1b1d28", 7.0),
    ("Dark: Muted Text (--ink-muted on --bg)", "#cfc4ae", "#12131a", 7.0),
    ("Dark: Muted on Card (--ink-muted on --surface)", "#cfc4ae", "#1b1d28", 7.0),
    ("Dark: Primary Link (--accent on --bg)", "#ff9e80", "#12131a", 7.0),
    ("Dark: Primary Link on Card (--accent on --surface)", "#ff9e80", "#1b1d28", 7.0),
    ("Dark: Primary Button Text (--accent-ink on --accent)", "#1b0802", "#ff9e80", 7.0),
    ("Dark: Highlight Text (--on-accent-soft on --accent-soft)", "#fff2eb", "#4a1c0d", 7.0),
]


def main() -> int:
    print("WCAG 2.2 Level AAA Contrast Verification Suite")
    print("=" * 68)
    failed = 0
    for label, fg, bg, min_ratio in PAIRS:
        ratio = contrast_ratio(fg, bg)
        status = "PASS (AAA)" if ratio >= min_ratio else "FAIL"
        if ratio < min_ratio:
            failed += 1
        print(f"[{status:10s}] {ratio:5.2f}:1 (req >= {min_ratio:.1f}:1) | {fg} on {bg} | {label}")
    print("=" * 68)
    if failed > 0:
        print(f"ERROR: {failed} contrast pair(s) failed WCAG 2.2 AAA threshold.")
        return 1
    print(f"SUCCESS: All {len(PAIRS)} color pairs strictly exceed WCAG 2.2 Level AAA (>= 7.0:1).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
