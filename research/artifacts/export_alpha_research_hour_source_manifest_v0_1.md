# Export Alpha Research Hour Source Manifest v0.1

**State:** REVIEW  
**Received:** 2026-07-23  
**Purpose:** Preserve the identity, role, and incorporation status of the files produced during the completed PI research hour.

## Source files

| Source artifact | SHA-256 | Laboratory role | Repository incorporation |
|---|---|---|---|
| `README.md` | `56f0fac1729941a34ce5b997bab1e20537ca099dce429c49e317769b92452c29` | Bundle index and evidence boundary | Represented by this manifest |
| `export_alpha_formal_framework_compendium_v0_1.md` | `e1adf29cf5affafd3c3e4e92f61ec931de9466fab701f1e50e940b65e48c7173` | Full formal derivation, tests, decisions, and adversarial review | Integrated into `export_alpha_framework_integration_v0_1.md`; full source pending lossless file transfer |
| `export_alpha_research_hour_close_v0_1.md` | `c0d1c3579542ac3ca461c1c2ec55ddb34e460d101ab67f971024f948674f58f5` | Hour close, formal result, next test, and restart pointer | Committed at its canonical path |
| `export_alpha_synthesis_map_v0_1.md` | `b75825d18d19bc7f6e96c9680d8df2b1fb43c285709c9e159c0af813e915c517` | Thesis–experiment–figure–code map and critic register | Integrated into `export_alpha_framework_integration_v0_1.md`; full source pending lossless file transfer |
| `french_exporters_notebook_atlas_v0_1.md` | `6f0dbce73e262a47e85c8b25956452c83a62c5f2f2450085301a47b549f60d91` | Notebook navigation guide | Existing canonical repository guide retained |

## Boundary

No original data was opened. No notebook was executed. No refactor or wider manuscript architecture was started during the hour.

The two long source documents were reviewed and incorporated scientifically through the integration artifact and laboratory state. Their exact hashes are retained here so a later local or connector transfer can verify byte-for-byte identity before promotion to canonical repository files.

## Promotion rule

The full synthesis map and formal framework compendium remain REVIEW. A later import should:

1. copy each file to its canonical path;
2. verify its SHA-256 against this manifest;
3. run `git diff --check`;
4. preserve the `[T]`, `[D]`, and `[C]` provenance distinctions;
5. avoid scientific edits during the transfer commit.
