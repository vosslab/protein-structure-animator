# README quality review

## Result

**PASS for the reviewed scope; no actionable defects found.** The README and capture helper match
the approved README/screenshot contracts and the explicit animated WebP request. The current
specification receipt records PASS at 96/100; its four-point clean-install deduction remains
documented.

## Review

- README claims about the completed examples, their scientific limits, format playback, and GroEL
  quick start match the linked example records and verification reports. The README separates
  experimental endpoints, interpolated protein motion, and viewpoint rotation.
- The animated WebP and static comparison are legible at their native sizes. The animated image
  labels the fixed glucose pose and interpolated motion; its five-second, one-play behavior is
  supported by the capture receipt's metadata and Chromium evidence. The adjacent still and prose
  provide a motion-independent equivalent. The receipt also states that ordinary Markdown WebP
  continues to animate when reduced motion is requested.
- The capture helper checks its fixed source frames, dimensions, `cwebp`, and Pillow WebP support
  before writing. It passes command arguments without a shell, stores intermediates under `/tmp`,
  and updates only the README sentinel interior. Its fixed crop is called out in code and the
  capture receipt as requiring review if the camera changes.
- The managed block has one descriptive embed per line. Repository search found no stale live
  reference to the retired managed GIF. The original example GIF outputs remain available.
- The capture receipt records a repeat run with byte-identical README and assets, a disposable
  assert-based check for frame bounds, output metadata, motion, and sentinel failures, plus focused
  syntax, lint, typing/import/link, and README checks. There is no permanent test dedicated to the
  capture helper; the maintainer-only artifact workflow and recorded focused checks do not justify
  adding a broad test harness here.
- Minor style note: standard-library imports in `devel/capture_readme_visuals.py:10-15` do not
  follow the local length/alphabetical ordering rule. This has no behavioral impact and is not a
  release blocker.

## Review limits

I inspected the source, README, both final assets, and current receipts. I did not rerun rendering,
browser playback, a clean install, Impress playback, or the full test suite. Browser and repeat
capture statements rely on the current capture receipt; this review does not claim live GitHub
rendering or independent reproduction.
