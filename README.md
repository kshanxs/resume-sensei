<div align="center">

<br>

# ✦ resume-sensei ✦

### *The Complete AI Resume & ATS Studio*

*ATS Optimization · Google X-Y-Z achievements · Dual LaTeX engines · Centralized Workspace*

<br>

[![Version](https://img.shields.io/badge/version-1.2.0-8957e5?style=for-the-badge&labelColor=161b22)](./docs/FEATURES.md)
[![Install](https://img.shields.io/badge/⚡_Install-npx_skills_add-0d1117?style=for-the-badge&labelColor=161b22)](https://github.com/kshanxs/resume-sensei)
[![License](https://img.shields.io/badge/License-MIT-2ea043?style=for-the-badge&labelColor=161b22)](./LICENSE)
[![Docs](https://img.shields.io/badge/Docs-USAGE.md-f78166?style=for-the-badge&labelColor=161b22)](./docs/USAGE.md)

<br>

*Most resume tools give you raw templates. This gives you a career copilot — parsing old histories,*
*quantifying bullets with Google formulas, scoring job description gaps, and rendering compile-safe LaTeX.*

</div>

---

## 🚀 Installation

```bash
npx skills add https://github.com/kshanxs/resume-sensei --skill resume-sensei
```

### Update to latest version

```bash
npx skills update resume-sensei
```

---

## 💬 Quick Start

```
"Initialize the resume workspace"
"Parse my old resume: ./MyOldResume.docx"
"Check ATS match against this job description: [paste job text]"
```

The AI guides you through importing history, improving metrics, and generating print-ready PDFs.

**→ [Full usage guide with examples](./docs/USAGE.md)**

---

## ✨ Highlights

| | |
|---|---|
| 📦 **Centralized Workspace** | Organizes your `Master/` history, `Tailored/` resume versions, and application trackers |
| 🔌 **Zero-Dependency Parser** | Standard-library Python script parses DOCX/text resume structures with zero package failures |
| 📊 **ATS Keyword Audit** | Compares skills against a job description, scores compatibility, and lists precise missing keywords |
| 📈 **Google X-Y-Z Formula** | Rewrites weak accomplishments into highly quantifiable result-driven statements |
| 🎨 **Dual LaTeX Styles** | Supports both a clean,Centered Modern layout and a bold, colored-block Classic style |
| 🛡️ **Compilation Safeguards** | Sanitizes TeX special tokens (`&`, `%`, `_`, `$`) to guarantee crash-free compiles |
| 🛠️ **Compiler Helper** | Standalone Python script compiles LaTeX locally or prints copy-paste Overleaf instructions |
| 📁 **Automatic .gitignore** | Automatically excludes private resumes, trackers, and document versions from public Git history |

**→ [See all features and architectures](./docs/FEATURES.md)**

---

## ⚡ Command Reference

| Say this | What happens |
|---|---|
| `"Initialize the resume workspace"` | Copies the standard workspace folders and Templates to the active directory |
| `"Parse [resume.docx]"` | Extracts text content from DOCX and normalizes to Markdown |
| `"Check ATS match against [job description]"` | Analyzes resume keywords, calculates match score, and reports gaps |
| `"Improve this bullet using X-Y-Z"` | Rewrites experience bullets with quantified metrics and active verbs |
| `"Tailor my resume for [Role] at [Company]"` | Aligns experiences to job priorities and saves version details |
| `"Export this tailored resume to Modern LaTeX"` | Generates compile-safe LaTeX code matching the Modern template |
| `"Export this tailored resume to Classic LaTeX"` | Generates compile-safe LaTeX code matching the Classic template |
| `"Compile resume [path_to_tex]"` | Compiles LaTeX code to a PDF or outputs online compiling directions |

**→ [Full command reference](./docs/FEATURES.md#command-reference)**

---

## 📁 Project Structure

```
resume-sensei-repo/
├── README.md                    ← Main info (GitHub landing page)
├── LICENSE                      ← Project license terms
├── CHANGELOG.md                 ← Version release history
├── sample_resume.md             ← Example markdown resume using XYZ bullets
├── sample_resume_modern.tex     ← Pre-filled Modern LaTeX template
├── sample_resume_classic.tex    ← Pre-filled Classic LaTeX template
├── docs/                        ← Detailed guides
│   ├── FEATURES.md
│   └── USAGE.md
└── resume-sensei/               ← Installed Skill Package
    ├── SKILL.md                 ← Entrypoint and routing tables
    ├── references/              ← Rules files loaded on-demand
    └── assets/                  ← Template files copied on initialization
```

---

## 📝 Changelog

See [CHANGELOG.md](./CHANGELOG.md) for details on all versions and releases.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

Copyright © 2026 [Shubhanshu Shukla](https://github.com/kshanxs). All rights reserved.

---

<p align="center">
  <sub>MIT License &nbsp;•&nbsp; Permission to Modify & Distribute &nbsp;•&nbsp; No Warranty or Liability</sub><br>
  <sub>Built with passion for candidates who care about their career.</sub>
</p>
