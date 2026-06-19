# Tailoring & Versioning Guidelines

Use this guide when the user wants to customize their resume for a specific job application, organize their tailored copies, or log applications in the tracking system.

---

## 1. The Tailoring Philosophy
*   **Highlighting vs. Fabricating**: Tailoring is the process of curating and emphasizing *real* experience. Never fabricate positions, skills, or metrics to pass a screener.
*   **The Resume as a Database**: Think of the Master Resume as a repository of all achievements. Tailoring is the process of querying that database and formatting the output to fit the target role.

---

## 2. Step-by-Step Tailoring Procedure

### Step 1: Analyze Job Priority Levels
Examine the target job description and extract requirements into three groups:
*   *Priority 1 (Deal-breakers)*: Core requirements mentioned first or repeated multiple times (e.g., "5+ years backend coding", "Expert in SQL").
*   *Priority 2 (Important)*: Skills highly desired but not primary (e.g., "Experience with Docker and AWS").
*   *Priority 3 (Bonus)*: Nice-to-have capabilities (e.g., "Familiarity with Tableau").

### Step 2: Customise the Professional Summary
Rewrite the top summary to speak directly to the job description keywords and the exact role title.
*   *Target Title*: If the JD is for a "Senior Infrastructure Engineer," use that title in the summary rather than "Senior Software Engineer" (if truthful to the experience).

### Step 3: Reorder and Select Skills
Place the most critical hard skills required by the job posting at the beginning of the skills categories. Add missing skills that the user possesses but forgot to highlight.

### Step 4: Emphasize and Swap Bullets
Within each job entry in the experience section:
*   **Move Relevant Bullets to the Top**: The first bullet point of any job role is read first. Put the achievement that aligns most with Priority 1 requirements at position 1.
*   **Vary Language**: Align terminology with the employer's phrasing (e.g., swap "agile delivery" for "Scrum methodology" if requested).
*   **De-emphasize Unrelated Work**: Trim bullet points that describe tasks irrelevant to the target role to save document space.

---

## 3. Directory Versioning System
Organize files in the following structure to prevent version confusion:

```
resume-hub/
├── Master/
│   └── LastName_Master_Resume.md (Exhaustive markdown document of all history)
├── Tailored/
│   ├── SWE/
│   │   └── LastName_Resume_SWE_Google_2026-06.pdf (Targeted PDF)
│   ├── PM/
│   │   └── LastName_Resume_PM_Meta_2026-06.pdf (Targeted PDF)
│   └── Templates/
│       └── resume.tex (Base LaTeX template)
└── Applications/
    └── tracker.md (Markdown table of sent applications)
```

### File Naming Convention
Consistently name final output files as:
`[LastName]_Resume_[Role]_[Company]_[YYYY-MM].pdf` (or `.tex` for sources)

Examples:
*   `Smith_Resume_BackendEng_Stripe_2026-06.pdf`
*   `Smith_Resume_DataAnalyst_HealthcareCo_2026-06.tex`

---

## 4. Job Search Update Workflow
Implement this clean loop for each job application:

1.  **Analyze**: Run the ATS keyword check on the Job Description vs. the `Master_Resume.md`.
2.  **Clone**: Copy `Master_Resume.md` (or the `resume.tex` base template) into a new file in the `Tailored/` subfolder.
3.  **Refine**: Rewrite summary, reorder skills, select and refine experience bullets, and insert keywords.
4.  **Export**: Generate the final LaTeX code or `.txt` output.
5.  **Log**: Append a new row to `Applications/tracker.md` with:
    *   Company name
    *   Role title
    *   Date applied
    *   Resume version file name
    *   Current status (`Applied`)
    *   Notes
