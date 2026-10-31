#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
# SPDX-License-Identifier: Apache-2.0 OR MIT
"""WCAG 2.2 Level AAA color contrast audit for frontmatter-gen.com.

Computes relative luminance and contrast ratio per W3C WCAG 2.2 formulas
and asserts that every text pair meets >= 7.0:1 (AAA normal text) and
every UI/focus pair meets >= 3.0:1 (non-text contrast).
"""

import sys


def hex_to_rgb(hex_str: str) -> tuple[float, float, float]:
    h = hex_str.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return int(h[0:2], 16) / 255.0, int(h[2:4], 16) / 255.0, int(h[4:6], 16) / 255.0


def relative_luminance(rgb: tuple[float, float, float]) -> float:
    def channel(c: float) -> float:
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = (channel(x) for x in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(fg: str, bg: str) -> float:
    l1 = relative_luminance(hex_to_rgb(fg))
    l2 = relative_luminance(hex_to_rgb(bg))
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


LIGHT_PAIRS = [
    # (label, foreground, background, minimum_ratio)
    ("Light: --ink on --bg", "#161821", "#f8f5ef", 7.0),
    ("Light: --ink on --surface", "#161821", "#ffffff", 7.0),
    ("Light: --ink on --bg-soft", "#161821", "#f2ece1", 7.0),
    ("Light: --ink on --vi-soft (logo cream #f8ebce)", "#161821", "#f8ebce", 7.0),
    ("Light: --ink-soft (logo slate #22242f) on --bg", "#22242f", "#f8f5ef", 7.0),
    ("Light: --ink-soft (logo slate #22242f) on --surface", "#22242f", "#ffffff", 7.0),
    ("Light: --ink-soft (logo slate #22242f) on --bg-soft", "#22242f", "#f2ece1", 7.0),
    ("Light: --ink-muted on --surface", "#3d404f", "#ffffff", 7.0),
    ("Light: --ink-muted on --bg", "#3d404f", "#f8f5ef", 7.0),
    ("Light: --accent on --bg", "#8f250c", "#f8f5ef", 7.0),
    ("Light: --accent on --surface", "#8f250c", "#ffffff", 7.0),
    ("Light: --accent-hover on --bg", "#6e1b07", "#f8f5ef", 7.0),
    ("Light: --accent-hover on --surface", "#6e1b07", "#ffffff", 7.0),
    ("Light: --accent-ink on --accent", "#ffffff", "#8f250c", 7.0),
    ("Light: --accent-ink on --accent-hover", "#ffffff", "#6e1b07", 7.0),
    ("Light: --on-accent-soft on --accent-soft (#f8ebce)", "#4a1404", "#f8ebce", 7.0),
    ("Light: --scene-ink on --scene (logo slate #22242f)", "#ffffff", "#22242f", 7.0),
    ("Light: --scene-muted (#f8ebce) on --scene (#22242f)", "#f8ebce", "#22242f", 7.0),
    ("Light: --vi-button-ink on --vi-button (#22242f)", "#ffffff", "#22242f", 7.0),
    ("Light: --focus on --bg (UI/focus)", "#8f250c", "#f8f5ef", 3.0),
    ("Light: --line on --bg (UI border)", "#686b7a", "#f8f5ef", 3.0),
]

DARK_PAIRS = [
    ("Dark: --ink on --bg", "#faf6ed", "#12131a", 7.0),
    ("Dark: --ink on --surface", "#faf6ed", "#1b1d28", 7.0),
    ("Dark: --ink on --bg-soft", "#faf6ed", "#181a24", 7.0),
    ("Dark: --ink on --surface-soft (logo slate #22242f)", "#faf6ed", "#22242f", 7.0),
    ("Dark: --ink-soft (logo cream #f8ebce) on --bg", "#f8ebce", "#12131a", 7.0),
    ("Dark: --ink-soft (logo cream #f8ebce) on --surface", "#f8ebce", "#1b1d28", 7.0),
    ("Dark: --ink-soft (logo cream #f8ebce) on --bg-soft", "#f8ebce", "#181a24", 7.0),
    ("Dark: --ink-muted on --bg", "#cfc4ae", "#12131a", 7.0),
    ("Dark: --ink-muted on --surface", "#cfc4ae", "#1b1d28", 7.0),
    ("Dark: --accent on --bg", "#ff9e80", "#12131a", 7.0),
    ("Dark: --accent on --surface", "#ff9e80", "#1b1d28", 7.0),
    ("Dark: --accent on --surface-soft (#22242f)", "#ff9e80", "#22242f", 7.0),
    ("Dark: --accent-hover on --bg", "#ffbeab", "#12131a", 7.0),
    ("Dark: --accent-hover on --surface", "#ffbeab", "#1b1d28", 7.0),
    ("Dark: --accent-ink on --accent", "#1b0802", "#ff9e80", 7.0),
    ("Dark: --accent-ink on --accent-hover", "#1b0802", "#ffbeab", 7.0),
    ("Dark: --on-accent-soft on --accent-soft", "#fff2eb", "#4a1c0d", 7.0),
    ("Dark: --vi-button-ink on --vi-button (#f8ebce)", "#12131a", "#f8ebce", 7.0),
    ("Dark: --focus on --bg (UI/focus)", "#ffbeab", "#12131a", 3.0),
    ("Dark: --line on --bg (UI border)", "#8a8d9e", "#12131a", 3.0),
]


def main() -> int:
    failures = 0
    print("=" * 72)
    print("WCAG 2.2 Level AAA Color Contrast Audit — frontmatter-gen.com")
    print("=" * 72)

    for group_name, pairs in [("Light Mode", LIGHT_PAIRS), ("Dark Mode", DARK_PAIRS)]:
        print(f"\n[{group_name}]")
        for label, fg, bg, threshold in pairs:
            ratio = contrast_ratio(fg, bg)
            passed = ratio >= threshold
            status = "PASS (AAA)" if passed else "FAIL"
            print(f"  {status:10s} {ratio:6.2f}:1 (>= {threshold:.1f}:1) | {fg} on {bg} — {label}")
            if not passed:
                failures += 1

    print("\n" + "=" * 72)
    if failures:
        print(f"FAILED: {failures} color pair(s) did not meet WCAG 2.2 AAA thresholds.")
        return 1
    print(f"PASSED: All {len(LIGHT_PAIRS) + len(DARK_PAIRS)} color pairs meet WCAG 2.2 Level AAA.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
