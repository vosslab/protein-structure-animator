# Dependency verification

## Installed TypeScript toolchain

The manifest, lockfile and installed packages now agree on the latest compiler and the latest
compatibility package, using open-ended npm aliases:

| Dependency key | Requirement | Installed role |
| --- | --- | --- |
| `@typescript/native` | `npm:typescript@>=7.0.2` | TypeScript 7.0.2, `tsc` |
| `typescript` | `npm:@typescript/typescript6@>=6.0.2` | Compatibility package 6.0.2, `tsc6` and compiler API 6.0.3 |
| `typescript-eslint` | `>=8.72.2` | ESLint integration 8.72.2 |

Registry `latest` queries confirmed TypeScript 7.0.2, compatibility package 6.0.2 and
typescript-eslint 8.72.2 on 2026-11-11. Node was v26.13.0 and npm was 11.20.0. These are tested
observations, not exact dependency constraints.

Normal installation with only `typescript >=7.0.2` failed with `ERESOLVE`: typescript-eslint's
upstream peer range is `>=4.8.4 <6.1.0`. An isolated install bypassing that peer check demonstrated
an actual runtime failure: importing typescript-eslint throws because it does not support TS 7.0.
The selected side-by-side aliases follow Microsoft's documented
[TypeScript 7 transition guidance](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/#running-side-by-side-with-typescript-6.0).
They preserve the latest native compiler and the existing ESLint configuration without adapters
or dependency upper bounds.

Installation used `npm install --ignore-scripts --cache /Users/vosslab/.cache/npm --no-audit`.
The existing ordinary TypeScript package required an explicit alias install to replace it; the
open-ended floor was retained. `npm rebuild @typescript/native --ignore-scripts` restored the
native `tsc` link after the compatibility package's transitive compiler temporarily replaced it.
Lifecycle scripts did not run. No renderer dependency was changed.

## Verification results

- `npm ls --depth=0` passes. Manifest requirements match the root lockfile requirements, and
  installed compiler package names and versions match their lockfile entries.
- `npx tsc --version` reports 7.0.2; `npx tsc6 --version` reports 6.0.3. Importing
  typescript-eslint succeeds using compiler API 6.0.3.
- A clean isolated `npm ci --ignore-scripts --cache /Users/vosslab/.cache/npm --no-audit`, using
  the final repository manifest and lockfile, installs successfully. Its `tsc` reports 7.0.2,
  `tsc6` reports 6.0.3, peer inspection passes, and typescript-eslint imports without relinking.
- `./check_codebase.sh` passes its root TypeScript check with TypeScript 7.0.2, then exits 2 with
  TS18003 at `tsconfig.lint.json`. That configuration includes `tests/**/*.ts` and `tools/**/*.ts`,
  and this repository currently has no TypeScript files in those trees. No placeholder
  application or test source was added. This is not a full gate pass.
- The existing ESLint command passes independently:
  `npx eslint --max-warnings 0 '**/*.{ts,tsx,mts,cts,js,mjs,cjs}'`.
- The existing Prettier check passes independently, with all three configured ignore paths.
- No `tests/test_*.mjs` Node tests exist, so the shell gate's Node test lane has no inputs.
- `npm audit --cache /Users/vosslab/.cache/npm --ignore-scripts --json` still reports 10 moderate
  minimatch-related advisories through ESLint/typescript-eslint. These predate this compiler
  change and are separate from Mol*. No forced audit fix or downgrade was applied.

Command logs and the audit JSON are under the ignored `output/dependency_verification/` directory.
The isolated installation directories were temporary verification, not application source.

## Refresh caveat

The vendored `devel/sync_typescript_package_pins.py` queries dependency keys and rewrites their
requirements uniformly as `>=latest`; it does not preserve npm aliases. Applying it would replace
the `typescript` compatibility alias with the incompatible direct TypeScript requirement. Review
and restore the documented aliases after any use of that helper. The helper and canonical
TypeScript/ESLint configuration were preserved.

## Minimatch resolution on 2026-11-12

The earlier ten moderate findings above are historical. Removing the unused direct minimatch
dependency and applying the open-ended root override `minimatch >=11.0.8` now gives a zero-finding
npm audit. ESLint 10.14.0, typescript-eslint 8.72.2 and both TypeScript aliases remain current and
unchanged. A fresh scripts-disabled `npm ci`, both compilers, actual ESLint traversal and
ignore/negation matching, and typescript-eslint project-service matching pass. Canonical ESLint
and Prettier pass; the shell gate still stops at its existing TS18003 empty lint inputs after
passing the root typecheck. See [minimatch_remediation.md](../audits/minimatch_remediation.md)
for exact commands, major-version compatibility rationale and evidence limits. Linter replacement
was investigated separately; no migration was performed.
