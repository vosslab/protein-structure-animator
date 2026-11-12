# Lint toolchain review

Reviewed 2026-11-12. This is an investigation, not an approved migration. The human wants latest
versions and is considering dropping ESLint; no replacement is installed by this review.

## Recommendation

Replacing ESLint with Oxlint is reasonable for this repository, after a small comparison proves
that useful JavaScript checks survive. Keep Prettier and the latest TypeScript compiler. Avoid
retaining two linters or adding a typed backend solely to preserve unused template scaffolding.
This follows **Keep it simple (KISS)** and **Ground requirements in actual needs** in
[REPO_STYLE.md](../../REPO_STYLE.md).

ESLint is useful here, but mainly for ordinary JavaScript errors. Its TypeScript 6 compatibility
installation buys little for the current authored code. This does not establish that removing it
now is safe: Oxlint's undeclared-variable rule needs particular scrutiny.

## Actual repository scope

`git ls-files` finds six JavaScript/TypeScript files, 583 lines total:

| Files | Role |
| --- | --- |
| `examples/render_molstar.mjs` | 302-line Node/Playwright renderer with browser callbacks |
| `tools/html_to_pdf.mjs` | 99-line Node/Playwright PDF utility |
| `tests/playwright/repo_root.mjs` | 10-line Git-root helper |
| `playwright.config.ts` | 22-line Playwright configuration; the only tracked TypeScript file |
| `eslint.config.js`, `eslint.config.local.js` | 150 lines of lint configuration |

There is no tracked application TypeScript. The Mol* renderer is JavaScript and disables typed
rules. Its effective ESLint configuration enables undeclared variables, unreachable code,
constant conditions and unused variables, including intentional underscore-prefixed exclusions.
These can catch real mistakes in renderer callbacks and CLI helpers. The local configuration
allows `window` and `molstar` only in the renderer. Typed floating/misused-promise rules are off
for JavaScript and on for the Playwright configuration. Explicit return types apply only to
TypeScript. Consequently, broad advertised typed-rule parity matters less than JavaScript
variable and scope checks for this repository today.

The shell gate runs both compiler projects before ESLint and Prettier. Its second project
currently has no TypeScript inputs; the earlier verified TS18003 failure is recorded in
[dependency_verification.md](../reports/dependency_verification.md). A linter migration alone
does not repair that separate gate limitation.

## Current upstream evidence

Live `npm view <package> version` observations on 2026-11-12:

| Package | Latest version |
| --- | --- |
| `eslint` | 10.14.0 |
| `typescript-eslint` | 8.72.2 |
| `typescript` | 7.0.2 |
| `@typescript/typescript6` | 6.0.2 |
| `oxlint` | 1.93.0 |
| `oxlint-tsgolint` | 7.0.2006 |
| `@biomejs/biome` | 2.6.7 |

These are observations, not pins. Any later installation keeps open-ended `>=` minimums and
refreshes its lockfile forward.

| Choice | Relevant evidence and limitation |
| --- | --- |
| Latest ESLint/typescript-eslint | Official [dependency support](https://typescript-eslint.io/users/dependency-versions/) includes ESLint 10 but TypeScript `>=4.8.4 <6.1.0`. The current dual compiler aliases solve that boundary while keeping TypeScript 7 available. |
| Oxlint | Official [migration guidance](https://oxc.rs/docs/guide/usage/linter/migrate-from-eslint.html) covers rules, overrides, globals and ignores. [Undeclared variables](https://oxc.rs/docs/guide/usage/linter/rules/eslint/no-undef.html) are supported but marked Nursery. This is a concrete reason to compare findings and explicitly enable the rule rather than accept defaults. |
| Oxlint with typed backend | Official [type-aware documentation](https://oxc.rs/docs/guide/usage/linter/type-aware.html) reports 59 of 61 typescript-eslint typed rules, requires `oxlint-tsgolint`, and uses the TypeScript 7 backend. It supports floating promises without the TS6 compiler API. This is future capacity, not a demonstrated need for the present renderer. |
| Biome | A viable combined formatter/linter, but replacing Prettier adds scope here. Its [floating-promise rule](https://biomejs.dev/linter/rules/no-floating-promises/javascript/) is experimental and uses its own inference engine. Prefer Oxlint for a focused lint replacement; do not infer identical diagnostics from similar rule names. |

All linked official documentation was accessed 2026-11-12. No performance or dependency-security
advantage was measured; neither is needed to justify simplifying this small toolchain.

## Smallest migration to evaluate

If replacement is requested, change only the manifest/lockfile, lint configuration and lint
invocation, their setup/documentation references, and the obsolete TS6 compatibility dependency
after checking its remaining consumers. Preserve browser globals, underscore exclusions, ignored
generated/scratch paths and zero-warning behavior. Keep the existing compiler and Prettier gates.
Treat the empty compiler project separately; do not add dummy TypeScript to satisfy it.

Prefer one compact Oxlint configuration over mechanically reproducing all template comments and
unused typed overrides. Several current files are vendored and may be overwritten by template
propagation, so record or resolve that maintenance source during an actual migration.

Acceptance should compare current ESLint and candidate Oxlint on all tracked JS/TS files, inspect
every diagnostic difference, and demonstrate detection of an undeclared callback variable and an
unused variable in temporary copies of real JavaScript. Confirm `window`/`molstar` remain allowed
in the renderer while misspelled globals fail; intentional `_` exclusions must still pass. Only
require a typed promise check if typed linting is deliberately retained. A green run on already
clean files alone does not establish parity. Then verify clean install, compiler, formatting and
audit results with the chosen latest dependencies.

## Evidence and limits

Inventory commands:

```sh
git ls-files '*.js' '*.mjs' '*.cjs' '*.ts' '*.tsx' '*.mts' '*.cts'
wc -l eslint.config.js eslint.config.local.js examples/render_molstar.mjs \
  playwright.config.ts tests/playwright/repo_root.mjs tools/html_to_pdf.mjs
npm view oxlint version
npm view oxlint-tsgolint version
npm view @biomejs/biome version
npm view eslint version
npm view typescript-eslint version
npm view typescript version
npm view @typescript/typescript6 version
```

Read the listed sources/configuration, both compiler projects, `check_codebase.sh`, setup helper,
and dependency-verification receipt. Used the installed ESLint `calculateConfigForFile` API for
`examples/render_molstar.mjs` and `playwright.config.ts` to verify effective rule states. Inventory
and rule-state results are direct observations; the migration recommendation is judgment based
on them and the linked upstream capabilities.

No alternative installed, migration run, lint parity measured, renderer launched, or broad suite
rerun. Alternative dependency trees and audit results remain unverified.
