# Changelog

All notable changes to the `resume-sensei` skill will be documented in this file.

## v1.1.0 — 2026-06-20
- **Documentation Restructure:** Extracted extensive documentation to `docs/FEATURES.md` and `docs/USAGE.md` for better readability.
- **Repository Alignment:** Aligned landing page, badges, directory structures, and MIT license references with standard Claude-skills templates.
- **Improved Installation Badges:** Updated README with clean, colorful status badges.

## v1.0.0 — 2026-06-19
- **Modular Orchestration:** Consolidated 8 specialized resume sub-skills into a single entrypoint in `resume-sensei/SKILL.md`.
- **Dependency-Free Ingestion:** Integrated standard-library Python parser for `.docx` and text formats in `resume-sensei/scripts/parse_resume.py`.
- **ATS Keyword Matching:** Designed an ATS scoring algorithm and matrix checklist report in `references/ats_optimization.md`.
- **XYZ Achievement Formulation:** Codified guidelines for rewriting weak experiences using metrics in `references/bullet_writing.md`.
- **Dual LaTeX Layout Templates:** Created compile-safe templates for Modern (light blue accents) and Classic (orange color band accents) LaTeX styles in `assets/resume-hub/Templates/`.
- **Compilation Character Escaping:** Enforced automated rules to escape TeX symbols (`&`, `%`, `_`, `$`) to guarantee compile-safety.
