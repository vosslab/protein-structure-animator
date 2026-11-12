# Minimatch audit remediation

## Outcome and ledger

Investigated on 2026-11-12 with Node v26.13.0 and npm 11.20.0. Scope is the npm warning
GHSA-g3hv-75wg-m249, not a broader dependency audit or linter migration.

| Step | Status | Evidence or next action |
| --- | --- | --- |
| Investigation | Complete | Current audit, registry, installed callers and API inspection below |
| D1: forward remediation | Accepted by manager | Remove unused direct minimatch; override transitive copies with `>=11.0.8` |
| Implementation | Complete | Unused direct dependency removed; root `>=11.0.8` override and forward lock refresh |
| Compatibility verification | Complete with known gate limit | Zero audit findings; clean install and actual consumer checks pass; TS18003 remains |
| Lint alternatives investigation | Complete, read-only | [lint_toolchain_review.md](lint_toolchain_review.md); bounded parity trial recommended, no migration |
| D1 specification review | PASS with unrelated freshness note | Fresh reviewer confirms D1 and records a current Prettier update outside scope |
| D2: latest Prettier followup | Accepted by manager; implemented | Refresh 3.10.0 to 3.10.1 after the latest-release snapshot drifts |
| Final specification review | PASS | Fresh review confirms final D1 plus D2 state; see below |
| Quality review | PASS | `/root/minimatch_quality` checks actual callers, engines, lock scope and evidence accuracy; see below |
| Integration review | PASS | `/root/minimatch_integration` reviewed final composition and evidence boundaries below |

The investigation was read-only outside this report. The later D1 implementation and its evidence
are recorded below; existing unrelated README, guidance, changelog and npm edits are preserved.

## Finding and reachability

`npm audit --json --cache /Users/vosslab/.cache/npm` exits 1: 10 moderate package findings,
zero high/critical findings, and 359 dependencies counted by npm. All ten package findings derive
from one advisory, rather than ten independent vulnerabilities. Three minimatch 10.2.6 copies
remain under ESLint, config-array and typescript-estree. Root minimatch is already 11.0.8.

The [GitHub advisory](https://github.com/advisories/GHSA-g3hv-75wg-m249) identifies
CVE-2026-118764, CWE-405, moderate severity and CVSS v4 6.9. It affects `>=7.0.0 <11.0.1`;
11.0.1 is the first patched release. Attacker-controlled globs can amplify CPU/memory use during
preprocessing when `optimizationLevel >= 2`. npm's audit JSON currently gives no CVSS vector
and score 0; the reviewed advisory provides the severity score above.

The installed callers use the following API and options:

| Consumer | Actual use | Advisory path |
| --- | --- | --- |
| ESLint 10.14.0 | `new Minimatch(pattern, {dot:true})`, `.match(path, true)` for directory traversal, `.match(path)` and `.pattern` | No level 2 option |
| config-array 0.23.5 | `Minimatch` constructor and `.match`; `{dot:true}`, plus `flipNegate:true` for ignore negation | No level 2 option |
| typescript-estree 8.72.2 | Named `minimatch(path, pattern, {dot:true})` in project-service `allowDefaultProject` matching | No level 2 option; repo uses `project`, not `projectService` |

Source inspection: `node_modules/eslint/lib/eslint/eslint-helpers.js` lines 33, 210, 290, 352;
`node_modules/@eslint/config-array/dist/cjs/index.cjs` lines 244, 412-429, 728; and
`node_modules/@typescript-eslint/typescript-estree/dist/useProgramFromProjectService.js` line 244.
The installed v10 implementation defaults `optimizationLevel` to 1 (lines 341-342).
No inspected consumer enables this advisory's prerequisite. This is source-based reachability
evidence, not a proof for every third-party path. All affected copies are development tooling:
`npm audit --omit=dev --json --cache /Users/vosslab/.cache/npm` exits 0 with zero findings.
Repository source has no direct minimatch imports or calls. The protein renderer uses Mol*;
the warning does not establish an exploitable animation or browser-runtime path.

## Current upstream releases

Live queries use `https://registry.npmjs.org/`, confirmed by `npm config get registry`.
`npm view <package>@latest version dependencies.minimatch --json --cache /Users/vosslab/.cache/npm`
returns:

| Package | Latest release | Requested minimatch |
| --- | --- | --- |
| [minimatch](https://registry.npmjs.org/minimatch/latest) | 11.0.8 | Not applicable |
| [eslint](https://registry.npmjs.org/eslint/latest) | 10.14.0 | `^10.2.6` |
| [@eslint/config-array](https://registry.npmjs.org/@eslint%2fconfig-array/latest) | 0.23.5 | `^10.2.4` |
| [@typescript-eslint/typescript-estree](https://registry.npmjs.org/@typescript-eslint%2ftypescript-estree/latest) | 8.72.2 | `^10.2.2` |
| [typescript-eslint](https://registry.npmjs.org/typescript-eslint/latest) | 8.72.2 | Through typescript-estree |
| [@eslint/js](https://registry.npmjs.org/@eslint%2fjs/latest) | 10.0.1 | Through ESLint |

`npm view minimatch@10 version --json` ends at 10.2.6: there is no published patched v10.
The manager additionally ran `npm outdated --json --cache /Users/vosslab/.cache/npm`: exit 0,
`{}`. Current direct versions are already latest; no unrelated refresh is needed.

Audit suggests ESLint/@eslint/js 9.39.5 and typescript-eslint 8.36.0 as fixes. Those are backward
moves and conflict with the user's latest-release policy. `npm audit fix --force` was not run.

## Decision and compatibility

D1 removes the unused direct `dependencies.minimatch` entry and adds this root setting:

```json
"overrides": {
  "minimatch": ">=11.0.8"
}
```

This is a current minimum, with no upper bound or exact pin. It replaces all three vulnerable
transitive copies while retaining current ESLint/typescript-eslint and both TypeScript aliases:
`@typescript/native: npm:typescript@>=7.0.2` and
`typescript: npm:@typescript/typescript6@>=6.0.2`.
The direct dependency addition alone cannot satisfy parents' v10 ranges. Removing its unused
runtime entry is smaller than retaining it solely as an override reference.
[npm overrides documentation](https://docs.npmjs.com/cli/v11/configuring-npm/package-json/#overrides)
supports root overrides with ranges; a retained direct dependency would require an identical
override spec or a `$minimatch` reference to avoid `EOVERRIDE`.

This crosses a major version outside the parents' declared ranges. Local v10/v11 API comparison
finds removed exports `makeRe` and `AST`, and removed prototype methods `debug`,
`levelTwoFileOptimize`, `partsMatch`, `matchOne`, `makeRe` and `slashSplit`. The three inspected
consumers use none of these. v11 replaces regex components in `.set` with `Matcher` components;
the inspected consumers do not read `.set`. Its named `minimatch`, `Minimatch`, `.match` (including
the partial flag), `.pattern`, dot matching and negation support remain present.
The [v11 README](https://github.com/isaacs/minimatch/blob/v11.0.8/README.md) documents the matcher
rewrite, both module formats, and these public APIs. Matching semantics still need consumer
checks; API names alone do not establish compatibility. v11 drops Node 18 (`20 || >=22`, versus
v10 `18 || 20 || >=22`); the observed Node 26 satisfies its engine.

Reassess this override when latest parents accept patched minimatch directly. A later refresh
may select another major under the user's open-ended policy and needs the same caller checks.

## Baseline and verification handoff

Before investigation, `git diff --numstat` reports package.json 2 additions/1 deletion and the
lockfile 241 additions/188 deletions. The manifest change adds direct minimatch `>=11.0.1`;
the lock has 360 package entries versus HEAD's 356. It moves root minimatch 10.2.6 to 11.0.8,
adds its matcher dependency and three nested v10 copies, and rearranges typescript-eslint
hoisting. Do not discard these existing changes wholesale.

Current SHA-256 snapshots before implementation:

```text
package.json       2610dd3b580d51101c53bcdde4f6c9fd4b4bf10cd6da168e4086fee6ce167d7f
package-lock.json  539430431d0b26c0b562368afb8c8c4e8768827895b10825823e9175a3cebbcc
```

The implementation reaches package.json, package-lock.json, this ledger, a dated resolution
pointer in [dependency_verification.md](../reports/dependency_verification.md),
[DESIGN_DECISIONS.md](../../DESIGN_DECISIONS.md) and [CHANGELOG.md](../../CHANGELOG.md).
No application callers, fixtures, exports or permanent third-party-internal tests need changes.

After D1, run normal npm resolution with the writable cache and inspect the lock diff. Verify
`npm ls minimatch --all`, zero audit findings, current parent versions and unchanged aliases.
Use a separate temporary directory with the final manifest/lock for
`npm ci --ignore-scripts --cache /Users/vosslab/.cache/npm --no-audit`; scripts-disabled clean
installation must be described accurately. Verify both compiler binaries and typescript-eslint
import there. Do not run the alias-rewriting dependency refresh helper.

Run the existing canonical ESLint and Prettier commands and `./check_codebase.sh`. Its known
TS18003 failure from empty `tsconfig.lint.json` inputs must remain separately reported; dummy
TypeScript files are unnecessary. Meaningful temporary consumer smoke checks should:

- Exercise actual ESLint `lintFiles` with a glob over real JS/MJS files, proving traversal and
  configuration matching still include the expected files; test ignore and negated-ignore
  behavior through ESLint/config-array. Prefer the real existing configuration where applicable.
- Invoke the actual typescript-eslint parser in a disposable project-service configuration with
  `allowDefaultProject` for a small temporary JS file, proving its named minimatch call works.
- Resolve minimatch from each parent to confirm all use the patched package; direct calls to
  root minimatch alone do not prove parent compatibility.

Those checks were pending at investigation handoff. The completed implementation checks follow.

## D1 implementation verification

Completed on 2026-11-12 with Node v26.13.0 and npm 11.20.0. The manifest removes unused
`dependencies.minimatch` and adds only `overrides.minimatch: >=11.0.8`. Relative to the saved
pre-implementation lock, the three nested 10.2.6 entries disappear, the existing root 11.0.8 and
its matcher/brace dependencies become development-only, and no remaining package version moves
backward or forward. ESLint 10.14.0, typescript-eslint 8.72.2 and both compiler alias package entries are
unchanged. Existing changes relative to HEAD are retained.

The commands below ran from the repository root unless marked isolated. Logs are retained in the
ignored `output/minimatch_verification/` directory.

| Command or check | Result |
| --- | --- |
| `npm install --cache /Users/vosslab/.cache/npm --no-audit` | Exit 0; removed unused root packages but initially retained stale nested v10 copies |
| `npm update minimatch --cache /Users/vosslab/.cache/npm --no-audit` | Exit 0; replaced the stale copies with deduplicated 11.0.8; lifecycle scripts were not disabled |
| `npm ls minimatch --all --cache /Users/vosslab/.cache/npm` | Exit 0; ESLint, config-array and typescript-estree all resolve 11.0.8 |
| `npm ls --depth=0 --cache /Users/vosslab/.cache/npm` | Exit 0; current direct packages and both aliases valid |
| `npm outdated --json --cache /Users/vosslab/.cache/npm` | Exit 0; `{}` |
| `npm audit --json --cache /Users/vosslab/.cache/npm` | Exit 0; zero vulnerabilities, 356 dependencies counted |
| Isolated `npm ci --prefix "$minimatch_ci_dir" --ignore-scripts --cache /Users/vosslab/.cache/npm --no-audit` | Exit 0; final manifest/lock copied into a fresh temporary directory; clean peer tree and all minimatch copies 11.0.8 |
| `npx tsc --version`, `npx tsc6 --version`; isolated equivalents through `node_modules/.bin/` | Exit 0; 7.0.2 and 6.0.3 in both installations |
| Root and isolated typescript-eslint import, compatibility API assertion | Pass; compiler API 6.0.3 |
| `node output/minimatch_verification/_temp_consumers.mjs` | Exit 0; disposable actual-consumer assertions described below |
| `npx eslint --max-warnings 0 '**/*.{ts,tsx,mts,cts,js,mjs,cjs}'` | Exit 0; canonical configuration |
| `npx prettier --check --ignore-path .gitignore --ignore-path .prettierignore --ignore-path .prettierignore.local '**/*.{ts,tsx,mts,cts,js,mjs,cjs}'` | Exit 0 |
| `npm run check` | Exit 2; root TypeScript check passes, then unchanged TS18003 from empty `tsconfig.lint.json` inputs |
| `source source_me.sh && python3 -m pytest tests/test_markdown_links.py -q -k 'minimatch_remediation or lint_toolchain_review or dependency_verification or DESIGN_DECISIONS or CHANGELOG'` | 5 passed, 54 deselected |
| Repository-bootstrapped Python ASCII assertions on the five related documentation files | Pass |
| `git diff --check` | Pass |

The disposable consumer check resolves minimatch from all three actual parent modules, asserting
11.0.8 rather than testing the root import alone. `ESLint.lintFiles` with the canonical glob and
configuration includes exactly the six existing TS/JS/MJS files and reports no findings. A small
temporary-directory ESLint configuration ignores `*.js`, restores `!keep.js`, and applies
`no-unused-vars` to exactly `keep.js` and `include.mjs`. The real typescript-eslint parser with
`projectService.allowDefaultProject: ['*.js']` produces a typed Program for a temporary JS file,
exercising typescript-estree's named minimatch call. Initial scratch checks corrected a missing
`playwright.config.ts` expectation and removed an unavailable wrapper cleanup method; neither
required a product change. Scratch source and isolated installation are removed after checking;
the small result logs remain. No permanent third-party-internal tests were added.

The isolated installation disables lifecycle scripts; it does not demonstrate lifecycle-script
execution. The normal update used `ignore-scripts=false`, but no lifecycle execution was needed
for these package changes. No exploit stress payload, renderer, playback, Impress, full Python
suite or live Dependabot alert-state check was run. Dependabot closure requires GitHub to rescan
the eventual committed lockfile. The major-version override remains a compatibility exception
to parent ranges and should be reassessed when current parents accept patched minimatch directly.

## Specification review

**Verdict: PASS.** Reviewer: `/root/minimatch_specification` (`gpt-6-luna`), fresh
requirements review. D1 removes the unused direct dependency, applies the requested open-ended
`>=11.0.8` override at the current minimatch release, and preserves the current ESLint,
typescript-eslint and TypeScript alias setup. The saved lock hash matches the reviewed file.
Current registry checks still report minimatch 11.0.8, ESLint 10.14.0, typescript-eslint 8.72.2,
TypeScript 7.0.2 and `@typescript/typescript6` 6.0.2. A live audit reports zero vulnerabilities,
and `npm ls minimatch --all` shows all three parents resolving to 11.0.8. The read-only lint
alternatives report makes no migration or parity claim.

Fresh `npm outdated --json` now reports Prettier 3.10.0 behind 3.10.1, so the earlier recorded
`{}` observation has drifted. Prettier is outside D1; this does not block its specification, but
the global no-outdated-dependencies claim should not be repeated without refresh. This review did
not rerun the clean install or consumer checks; it relies on the dated implementation receipt for
those, and retains its documented scripts-disabled, TS18003 and Dependabot limitations.

D1 SHA-256 snapshots at specification review (historical):

```text
package.json       e353f63cea53f4d8dff8154c67e161bab3c47ef18cc63065df12adb85c1fef50
package-lock.json  8b7f2fe392d8fec5c3112671d16ce0d9ed36c4a2666530e34f35aba683eb9a9b
```

## D2 latest Prettier followup

Owner: `/root/latest_prettier_refresh` (`gpt-6.1-sol`, medium). The manager accepts this small
followup under the user's instruction, "I want the latest versions." Refresh only Prettier and
its open-ended floor; retain both compiler aliases, current lint packages and the minimatch
override. No source, formatter configuration, linter migration or alias-refresh helper changes.

On 2026-11-12, `npm view prettier@latest version engines --json --cache /Users/vosslab/.cache/npm`
reports 3.10.1 and Node `>=14`; observed Node v26.13.0 satisfies it. Change the manifest floor to
`>=3.10.1`, then run `npm update prettier --cache /Users/vosslab/.cache/npm --no-audit`: exit 0,
one package changed. JSON deep comparison against the saved D1 manifest/lock confirms that only
the Prettier floor and `node_modules/prettier` entry differ. Every other package entry is equal.

Final-state checks use the same canonical commands recorded above, with results retained under
`output/minimatch_verification/d2_*`:

| Command or check | Result |
| --- | --- |
| `npm ls --depth=0 --cache /Users/vosslab/.cache/npm` | Exit 0; Prettier 3.10.1, both aliases and current lint packages valid |
| `npm outdated --json --cache /Users/vosslab/.cache/npm` | Exit 0; `{}` at this new registry snapshot |
| `npm audit --json --cache /Users/vosslab/.cache/npm` | Exit 0; zero vulnerabilities, 356 dependencies counted |
| Canonical Prettier check with all three ignore paths and TS/JS glob above | Exit 0; all matched files formatted; no write command used |
| Canonical ESLint command above | Exit 0; zero warnings |
| Fresh isolated `npm ci --prefix "$prettier_ci_dir" --ignore-scripts --cache /Users/vosslab/.cache/npm --no-audit` | Exit 0; 312 packages installed from final manifest/lock |
| Isolated `npm ls --depth=0` and Prettier, `tsc`, `tsc6` binaries | Exit 0; Prettier 3.10.1, compiler versions 7.0.2 and 6.0.3; aliases valid |
| `source source_me.sh && python3 -m pytest tests/test_markdown_links.py -q -k 'minimatch_remediation or CHANGELOG'` | 2 passed, 57 deselected |
| Changed-document ASCII checks; `git diff --check` | Pass |

The isolated install and saved comparison inputs are removed after verification. D1 consumer
smoke checks are not repeated because all non-Prettier lock entries remain equal. The full shell
gate, renderer, playback, browsers, Impress and full Python suite are not rerun for this patch;
the known TS18003 limit and scripts-disabled clean-install scope remain. The earlier D1 clean
install and specification verdict describe their historical hashes, not this final state. At this
D2 handoff, final specification, quality and integration reviews were pending; their receipts follow.

Final D2 SHA-256 snapshots for fresh review:

```text
package.json       3667354cd7eed59dac5b1828468611d2d91c20d4e66349c787407eedd2a3e655
package-lock.json  d1358ee86b7d5c7fd6eba6fca2afc63fb48bcea42e9d066b6e7eabddb33222ba
```

## Final specification review

**Verdict: PASS.** Reviewer: `/root/latest_specification` (`gpt-6-luna`), fresh final-state
specification review, 2026-11-12. The final manifest and lockfile match the recorded D2 SHA-256
snapshots. The manifest removes the unused direct minimatch dependency, keeps the open-ended
`>=11.0.8` override, retains ESLint 10.14.0 and typescript-eslint 8.72.2, preserves both TypeScript
aliases, and sets Prettier to the now-current `>=3.10.1` floor. The lock root agrees with the
manifest; its resolved versions are minimatch 11.0.8, Prettier 3.10.1, TypeScript 7.0.2 and the
TypeScript 6 alias 6.0.2. No exact root dependency pin or upper bound was found.

This reviewer independently ran `npm audit --json --cache /Users/vosslab/.cache/npm` (exit 0,
zero findings, 356 dependencies) and `npm outdated --json --cache /Users/vosslab/.cache/npm`
(exit 0, `{}`). These are dated observations, not guarantees about future registry state. The D2
receipt supplies the scripts-disabled clean-install, compiler-alias, formatter and linter checks;
the D1 receipt supplies the minimatch consumer checks, which need not be repeated because D2
changed only Prettier's floor and package entry. The known `TS18003` empty-input gate limitation,
scripts-disabled install scope and Dependabot rescan dependency remain as recorded above.

The separate lint-toolchain report is a recommendation only: no alternative package was installed,
parity was not measured, and this task did not authorize or perform an ESLint migration. This is a
specification verdict only; quality and integration reviews were still pending at this handoff.

Reviewer: `/root/latest_specification`; task: fresh final-state specification review after D2;
model: `gpt-6-luna`. Reviewed manifest and lock hashes:

```text
package.json       3667354cd7eed59dac5b1828468611d2d91c20d4e66349c787407eedd2a3e655
package-lock.json  d1358ee86b7d5c7fd6eba6fca2afc63fb48bcea42e9d066b6e7eabddb33222ba
```

## Quality review

**Verdict: PASS.** Reviewer: `/root/minimatch_quality` (`gpt-6.1-sol`, medium), fresh
quality review after final specification PASS, 2026-11-12. What this change does: it replaces
vulnerable development-tool matching through one root override and refreshes Prettier. It keeps
the existing toolchain. No actionable correctness, compatibility or simplicity finding remains.

Independent inspection confirms that the override in `package.json` reaches all three installed
parents, whose actual calls in `eslint/lib/eslint/eslint-helpers.js`,
`@eslint/config-array/dist/cjs/index.cjs` and
`@typescript-eslint/typescript-estree/dist/useProgramFromProjectService.js` use retained v11
APIs. The Node 26 runtime satisfies minimatch and the stricter existing ESLint engine; the
override introduces no additional effective Node requirement for this toolchain. The compiler
alias package names remain distinct from their reported compiler API versions: the TS6 package
is 6.0.2 and its compiler reports 6.0.3. The receipt accurately preserves that distinction.

Independent checks use `node --input-type=module` with Node's `assert`, `fs`, `crypto`,
`createRequire` and `child_process` APIs. They hash both final files, compare lock package versions
against `git show HEAD:package-lock.json`, resolve minimatch from each parent, exercise dot and
partial matching, and read installed package engines. Both hashes match D2; only minimatch
10.2.6 to 11.0.8 and Prettier 3.10.0 to 3.10.1 change versions relative to HEAD. A separate
`node --input-type=module` check calls `new ESLint().lintFiles` with
`['**/*.{ts,tsx,mts,cts,js,mjs,cjs}']` and asserts its paths equal
`git ls-files '*.js' '*.mjs' '*.cjs' '*.ts' '*.tsx' '*.mts' '*.cts'`: exactly six tracked files,
zero errors and warnings. These checks pass against the final hashes recorded above.

Reviewed saved `consumers.log`, `d2_lock_comparison.log`, `d2_ci_compilers.log`, `d2_ci_tree.log`
and `check.log` under `output/minimatch_verification/`, plus the relevant decision, changelog,
historical dependency receipt and separate alternatives report. Reliance on implementation
evidence is limited to ignore negation, typed project-service matching, clean installation and
the D1-to-D2 deep comparison; final specification supplies the current audit/outdated snapshot.
The change follows **Keep it simple (KISS)**: no application logic, new dependency, permanent
third-party test or speculative linter migration is needed.

Report validation: `source source_me.sh && python3 -m pytest tests/test_markdown_links.py -q
-k minimatch_remediation` passes (1 passed, 58 deselected); `git diff --check` passes.

Not rerun: clean installation, registry queries, full shell gate, renderer, playback, full suite
or live Dependabot state. The known TS18003 gate failure and scripts-disabled installation scope
remain explicit. The major-version override is a documented compatibility exception; later major
refreshes need renewed consumer checks. Integration review was pending at this handoff.

## Integration review

**Verdict: PASS.** Reviewer: `/root/minimatch_integration` (`gpt-6-luna`), fresh composition
review, 2026-11-12. The final manifest and lockfile match the recorded D2 hashes, and the staged
decision, dependency-verification addendum, changelog, and separate lint-alternatives report agree
on the requested scope and final state. The root override, open dependency floors, current ESLint
and typescript-eslint releases, and both TypeScript aliases are represented consistently. The
alternative-linter report remains a recommendation only; no migration or parity claim is made.

The recorded evidence supports the claims at their stated scope: fresh final-state specification
and quality reviews pass; D2 logs show a scripts-disabled clean install, both compiler binaries,
canonical ESLint and Prettier checks, and zero audit findings. The known TS18003 empty-input limit
and scripts-disabled install boundary remain disclosed. No registry/install rerun, full shell gate,
Dependabot rescan, renderer, playback, or full test suite was performed for this integration
review. The alternatives recommendation is a future decision, not an unresolved requirement.

Reviewer: `/root/minimatch_integration`; task: final integration review and ledger closeout;
model: `gpt-6-luna`. Composition was checked against the recorded D1/D2 implementation and final
specification/quality receipts; no package or source files were changed.

