# Resume Sensei 🎓💼

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#contributing)

A comprehensive, context-efficient AI coding agent skill that optimizes your professional history for Applicant Tracking Systems (ATS), tailors experiences using Google's X-Y-Z and STAR formulas, and generates compilation-safe, premium LaTeX source code.

> [!NOTE]
> This skill consolidates 8 distinct specialized resume sub-skills into a single orchestrator using a modular reference design. It lazy-loads specific guidelines only when required, minimizing prompt token bloat.

---

## 🌟 Key Features

*   **Modular Orchestration**: A single agent skill entrypoint that coordinates parsing, ATS keyword auditing, achievement quantification, layout styling, and version logs.
*   **Dependency-Free Parser**: Built-in Python tool to parse text from `.docx` packages and `.txt` files using only Python's standard library.
*   **ATS Screening Audit**: Extracts keywords (hard skills, soft skills, domain terms) from a job description, calculates a match score, and outputs a step-by-step keyword inclusion plan.
*   **X-Y-Z Achievement Quantification**: Rebuilds weak resume bullet points using active verbs and metrics based on Google's accomplishment formulas.
*   **Dual LaTeX Styles (Modern & Classic)**: Generates clean, compile-safe LaTeX code supporting both a Modern style (light blue accents, metadata headers, centered name rule) and a Classic style (full-width header band, orange accents, filled section bars, right-aligned dates). Automatically escapes LaTeX special tokens (`&`, `%`, `_`, `$`) to guarantee compile-on-first-try.
*   **Standardized Workspace ("Resume Hub")**: Initializes standard workspace folders to manage your master source-of-truth, tailored files, and job trackers.

---

## 📂 Repository Directory Layout

```
resume-sensei-repo/
├── resume-sensei/             # <-- The installable skill package folder
│   ├── SKILL.md               # Main orchestrator & lazy-loading routing table
│   ├── references/            # Domain-specific rules
│   │   ├── ats_optimization.md
│   │   ├── bullet_writing.md
│   │   ├── formatting_and_sections.md
│   │   └── tailoring_and_versioning.md
│   ├── scripts/
│   │   └── parse_resume.py    # Dependency-free DOCX and text parser
│   └── assets/
│       └── resume-hub/        # Initialized workspace skeleton
│           ├── Master/
│           │   └── Master_Resume.md
│           ├── Applications/
│           │   └── tracker.md
│           └── Templates/
│               ├── resume_modern.tex # Modern style LaTeX template
│               └── resume_classic.tex # Classic style LaTeX template
├── sample_resume.md           # Example markdown resume using XYZ bullets
├── sample_resume_modern.tex   # Pre-filled generic sample in Modern style
├── sample_resume_classic.tex  # Pre-filled generic sample in Classic style
├── README.md                  # This file
├── LICENSE                    # MIT license
└── .gitignore                 # Block personal credentials from Git commits
```

---

## 🚀 Installation & Setup

Add this skill directly to your AI agent environment (supporting Cline, Codex, Cursor, Trae, Trae Code, or Claude Code) using the `skills` CLI tool.

### 1. Project Scope Installation
```bash
npx skills add https://github.com/<your-username>/resume-sensei --skill resume-sensei
```

---

## 🛠️ Usage Workflows

Once installed, your AI agent will automatically trigger this skill when you talk about resume optimization, LaTeX conversion, or job tailoring.

### A. Initialize the Workspace
Ask your agent:
> "Initialize the resume-sensei workspace"

The agent will copy the template folder layout (`assets/resume-hub/`) to your active directory, giving you:
*   `/Master/Master_Resume.md` (To save your full history).
*   `/Applications/tracker.md` (To log your applications).

### B. Ingest and Parse Resume
Upload your current resume (e.g., `MyOldResume.docx` or `MyOldResume.pdf`) and tell the agent:
> "Extract the contents of MyOldResume.docx and save it to the Master resume file."

The agent will run `scripts/parse_resume.py` to extract text from DOCX, or use native PDF tools to read PDF data, formatting the output into your markdown master file.

### C. Check ATS Keyword Match
Provide a job description and request a screen check:
> "Analyze my master resume against this job description: [paste job requirements]"

The agent will audit keywords and output a detailed match score report showing missing keywords and placement edits.

### D. Tailor and Export to LaTeX
Generate your tailored LaTeX file for a specific role:
> "Tailor my resume for this Software Engineer role at Google and export the LaTeX source code."

The agent will adapt your summary and experience bullet hierarchies, format it using either the Classic or Modern LaTeX layout blueprint, escape special characters, write the final output, and append a log entry to your application tracker.

---

## 🔒 Security & Data Privacy

To prevent your personal details (email, phone, address, career history) from being leaked online:
*   This repository includes a strict `.gitignore` that blocks committing `*.pdf`, `*.docx`, `/Master/`, `/Tailored/`, and `tracker.md` logs.
*   Only your `resume-sensei/` skill configurations and generic sample resumes are tracked in Git.

---

## 📄 License
This project is licensed under the MIT License -- see the [LICENSE](LICENSE) file for details.
