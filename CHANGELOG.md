# Changelog

All notable changes to the `resume-sensei` skill will be documented in this file.

## v1.5.0 — 2026-07-01
- **Typst Migration**: Transitioned the templates and compilation engine entirely from LaTeX to Typst.
- **Mulish Font Support**: Packaged the Mulish Google Font family in the workspace Templates directory for portable offline compilation.
- **Typst Compiler Script**: Updated `scripts/compile_resume.py` to compile Typst source files locally and pass relative font directory paths.
- **PEP 723 Script Metadata**: Added PEP 723 inline script metadata to Python helper scripts to enable clean, isolated execution via `uv run`.
- **Anonymized Profile Template**: Replaced template placeholders with Shubhanshu Shukla's anonymized resume data.
- **Documentation Overhaul**: Updated `README.md`, `docs/FEATURES.md`, and `docs/USAGE.md` to match the Typst engine.

## v1.2.0 — 2026-06-21
- **LaTeX Compiler Tool**: Added `scripts/compile_resume.py` to check for local compilers (`pdflatex`, `xelatex`, `lualatex`), compile `.tex` files, or print copy-paste Overleaf instructions.
- **Modernized ATS Rules**: Revised `references/ats_optimization.md` to support semantic keyword parsing and warn against exact-keyword stuffing.
- **Secure PDF Ingestion Rules**: Added safety warnings in `SKILL.md` to flag multi-column PDF layouts where text extraction might scramble reading order.
- **Directory Layout Standardization**: Aligned directory blueprints in `tailoring_and_versioning.md` and `SKILL.md` to match the workspace templates folder.
- **Documentation Updates**: Documented compiler tool and usage in `README.md`, `docs/FEATURES.md`, and `docs/USAGE.md`.

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
