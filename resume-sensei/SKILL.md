---
name: resume-sensei
description: |
  Comprehensive resume builder, ATS optimizer, and career version assistant. Use this skill whenever the user asks to:
  - Write, review, format, or optimize a resume, CV, or professional profile.
  - Tailor a resume to a specific job description or target role.
  - Check ATS compatibility, calculate keyword match scores, or find missing skills.
  - Quantify achievements, rewrite experience bullets, or apply Google's X-Y-Z formula.
  - Parse or extract text from an uploaded resume (e.g., PDF, DOCX, TXT formats).
  - Generate, edit, or output LaTeX code for a resume.
  - Initialize the resume hub workspace ("initialize resume workspace", "start resume setup").
  - Track job applications and manage different tailored resume versions.

  Use this skill even if the user does not explicitly name 'resume-sensei', as long as they provide a resume file, job description, or request updates to their work history.
---

# Resume Sensei

## Context Efficiency Rule (Lazy Loading)

**CRITICAL — Read this before loading reference files.**
This skill contains specialized guides to avoid context window bloat. Do NOT pre-load all references. Use **lazy loading** — only read a reference file using `view_file` when performing its specific workflow:

| Load this file... | When... |
| :--- | :--- |
| `references/ats_optimization.md` | Conducting ATS scoring, keyword matches, or auditing layout flags. |
| `references/bullet_writing.md` | Quantifying results, applying Google's X-Y-Z/STAR formulas, or drafting active verbs. |
| `references/formatting_and_sections.md` | Designing layout hierarchies, setting margins, or organizing page budgets. |
| `references/tailoring_and_versioning.md` | Customizing a resume to a target job description or setting up application trackers. |

Never load more than 1--2 reference files at a time.

---

## Core Workflows

### 1. Workspace Setup & Initialization
When the user requests to start a new resume project or "initialize the resume workspace," perform the following steps:
1.  Copy the entire `assets/resume-hub/` directory into the root of the user's active project directory.
2.  Maintain the folder structure:
    *   `/Master/Master_Resume.md` (The source of truth containing all experience history).
    *   `/Tailored/` (Folder where tailored versions for specific applications will reside).
    *   `/Applications/tracker.md` (The markdown file tracking sent resumes and statuses).
    *   `/Templates/resume_modern.tex` (Modern light-blue centered style LaTeX template).
    *   `/Templates/resume_classic.tex` (Classic orange background banner style LaTeX template).
3.  Instruct the user to paste their existing resume into `Master/Master_Resume.md`, or assist them in compiling their information manually.

### 2. Ingestion & Reading Uploaded Resumes
If the user uploads an existing resume file:
*   **PDF files**: Use the native `view_file` tool to read the text. Note that standard text extraction can scramble multi-column resume layouts by merging columns horizontally. Verify the extracted content in `Master_Resume.md` matches the source structure. If it is garbled, prompt the user to copy-paste the text directly or provide a `.docx` or `.md` copy.
*   **DOCX files**: Run the custom python script:
    `python3 scripts/parse_resume.py <path_to_docx>`
    to extract structured text without external dependencies.
*   **TXT/MD/TEX files**: Read them directly using `view_file`.
*   *Action*: Convert the extracted data into clean markdown format and save it in `Master/Master_Resume.md` to establish the source of truth.

### 3. ATS Screening & Optimization
When the user provides a job description (JD) and wants to check their resume's match:
1.  Read `references/ats_optimization.md`.
2.  Extract required hard skills, soft skills, and domain terms from the JD.
3.  Cross-reference with the user's resume and calculate the keyword match score.
4.  Generate the **ATS Compatibility & Keyword Report** using the template defined in the reference.

### 4. Improving Bullets & Quantification
When the user wants to polish their bullets or add metrics:
1.  Read `references/bullet_writing.md`.
2.  Identify weak bullet points (e.g., passive language, missing results).
3.  Prompt the user with targeted metric-discovery questions if metrics are missing.
4.  Rewrite the bullets using Google's X-Y-Z or STAR formulas.
5.  Output a structured comparison showing the "Original," "Improved," and "Key Changes" for each bullet.

### 5. Tailoring and Version Control
When the user is applying for a specific job:
1.  Read `references/tailoring_and_versioning.md`.
2.  Analyze the target company's priorities and align the resume summary, skill ordering, and experience bullet hierarchy.
3.  Write the tailored resume source to `Tailored/[Role]/[LastName]_Resume_[Company]_[YYYY-MM].tex` (or markdown).
4.  Update `Applications/tracker.md` by appending a new row with the target details, matching file name, and setting status to `Applied`.

### 6. LaTeX Code Generation Rules
When generating LaTeX resume source code:
1.  Use either `Templates/resume_modern.tex` or `Templates/resume_classic.tex` as the base structural blueprint, depending on whether the user requests a modern/clean or classic/color-block layout.
2.  **Strict Compilation Safety**: Always escape LaTeX special characters to prevent compiler crashes:
    *   Escape ampersands: `&` $\rightarrow$ `\&` (e.g., `Languages \& Databases`)
    *   Escape percentages: `%` $\rightarrow$ `\%` (e.g., `40\% reduction`)
    *   Escape underscores: `_` $\rightarrow$ `\_` (e.g., `Node\_js`, `user\_engagement`)
    *   Escape dollar signs: `$` $\rightarrow$ `\$` (e.g., `\$50K+ transactions`)
3.  Ensure the generated LaTeX code contains no syntax errors, utilizes only standard packages defined in the template, and aligns exactly with margins and item limits.
4.  **Local Verification & Compilation**: Run `python3 scripts/compile_resume.py <path_to_tex>` to verify that the generated LaTeX compiles cleanly to a PDF. If no local LaTeX compiler is detected, provide clear fallback instructions to the user to compile online via Overleaf.
