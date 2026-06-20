# ATS Optimization Guidelines

Use this guide when the user wants to check ATS compatibility, run a keyword match analysis against a job description, or resolve screening issues.

---

## 1. ATS Ingestion Rules
Ensure the resume is structured so automated parsers can extract clean text.

*   **File Format**: Standardize on `.docx` or text-based `.pdf` (never scanned images or `.pages`).
*   **Naming Conventions**: Save files as `FirstName_LastName_Resume.pdf` or `FirstName_LastName_Resume.docx`. Avoid generic names like `resume.pdf` or version indicators like `resume_v2_final.pdf`.
*   **Layout Safety**:
    *   Avoid using text boxes, columns, tables (except simple borders), images, charts, icons, or visual proficiency bars.
    *   Do not place critical information (like contact details) in the document's header or footer sections; ATS parsers frequently skip them. Place them in the main document body.
    *   Use a single-column layout.
    *   Use standard bullet characters (`•`, `-`, `*`).

---

## 2. Standard Section Headers
Always use industry-standard headers. Non-standard headers (e.g., "Where I've Been") fail ATS categorizations.

*   **Summary**: `PROFESSIONAL SUMMARY` or `SUMMARY`
*   **Experience**: `PROFESSIONAL EXPERIENCE` or `WORK EXPERIENCE`
*   **Skills**: `SKILLS` or `TECHNICAL SKILLS`
*   **Education**: `EDUCATION`
*   **Certifications**: `CERTIFICATIONS` or `CERTIFICATIONS & LICENSES`
*   **Projects**: `PROJECTS` or `KEY PROJECTS`

---

## 3. Keyword Matching Process

Follow this structured process when comparing a resume to a job description:

### Step 1: Extract Job Description Keywords
Categorize requirements into three buckets:
1.  **Hard Skills (Technical)**: Programming languages, platforms, frameworks, methodologies, and tools.
2.  **Soft Skills**: Stakeholder management, communication, leadership, and collaboration.
3.  **Industry Domain Terms**: E-commerce, B2B SaaS, HIPAA compliance, KPI definitions, etc.

### Step 2: Perform Exact & Synonymous Audit
Check the resume for exact occurrences of the keywords. If the resume uses synonyms (e.g., "risk mitigation" instead of "risk management" required by the JD), flag it and recommend swapping for the exact phrase to optimize parsing matches.

### Step 3: Calculate the Match Score
Use the following formula to estimate match readiness:

$$\text{Match Score} = \left( \frac{\text{Keywords Matched}}{\text{Total Crucial JD Keywords}} \right) \times 100$$

*   **Under 70%**: Critical gap. Suggest major revisions.
*   **70% -- 80%**: Moderate match. Recommend adding key missing skills.
*   **80%+**: Strong match. Ready for submission.

---

## 4. ATS Scoring & Audit Output Template
When performing an ATS audit, format your response using this structure:

```markdown
# ATS COMPATIBILITY & KEYWORD REPORT

## Overall Score: [X]/100
*Target: 80%+ recommended for submission.*

### File Setup Audit
*   **Format Check**: [DOCX/PDF] - [PASS/FAIL]
*   **Text Extraction Status**: [Success/Failed (Scanned Image)] - [PASS/FAIL]
*   **File Naming**: [Name of file] - [PASS/FAIL]

### Formatting & Layout Flags
*   [PASS/FAIL/WARN] [No tables/columns detected]
*   [PASS/FAIL/WARN] [Contact info placement check]
*   [PASS/FAIL/WARN] [Font size & bullet consistency check]

### Keyword Match Analysis
**Critical Keywords (Must Have):**
*   [PASS] [Keyword A] -- Found [X] times
*   [FAIL] [Keyword B] -- MISSING (mentioned [Y] times in JD)

**Important Keywords:**
*   [PASS] [Keyword C] -- Found [X] times
*   [WARN] [Keyword D] -- Synonym mismatch (using "[term]" instead of exact JD term "[JD term]")

### Match Score: [X]%

### Recommended Action Items
1.  **Add Missing Keywords**:
    *   Suggest inserting "[Keyword B]" in the [Section] (e.g., "In summary section, change '...' to '...'").
2.  **Align Phrasing**:
    *   Change "[term]" to "[JD term]" in experience bullet for exact parsing match.
3.  **Fix Layout Flags**:
    *   [E.g., Move contact info from page header to main body].

**Estimated New Match Score after edits: [Y]%**
```
