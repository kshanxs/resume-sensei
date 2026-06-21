# Resume Sensei — Usage Guide

> You don't need to memorize any commands. Just talk naturally. This guide shows you what's possible and exactly what the conversation looks like at every stage.

---

## Quick Start

```
"Initialize the resume workspace"
```

That's it. The AI takes it from there — copying directories, setting up templates, and configuring files.

---

## Core Workflows in Action

### 1. Workspace Setup & Onboarding

When starting, the AI initializes your central folder structures and configuration logs.

**You:** `"Initialize the resume workspace"`

**AI:**
> I've initialized the **Resume Sensei Workspace** in your active directory:
> *   📁 [**`Master/`**](file:///Users/shubh/Developer/resume%20sensei/resume-sensei/assets/resume-hub/Master) - Directory for your full history.
> *   📁 [**`Tailored/`**](file:///Users/shubh/Developer/resume%20sensei/resume-sensei/assets/resume-hub/Tailored) - Directory for tailored resumes.
> *   📁 [**`Applications/`**](file:///Users/shubh/Developer/resume%20sensei/resume-sensei/assets/resume-hub/Applications) - Application tracker spreadsheet.
> *   📁 [**`Templates/`**](file:///Users/shubh/Developer/resume%20sensei/resume-sensei/assets/resume-hub/Templates) - Modern and Classic LaTeX layouts.
>
> Paste your current work history in [**`Master/Master_Resume.md`**](file:///Users/shubh/Developer/resume%20sensei/resume-sensei/assets/resume-hub/Master/Master_Resume.md) to get started, or upload a resume file and ask me to parse it!

---

### 2. Ingesting & Parsing Resumes

If you have an existing resume, the AI uses a dependency-free custom parser script to extract details without environment errors.

**You:** `"Parse my old resume: ./MyOldResume.docx"`

**AI:**
> 🔍 **Ingesting MyOldResume.docx...**
> I've successfully extracted your work history and formatted it into clean markdown.
> Writing parsed content to [**`Master/Master_Resume.md`**](file:///Users/shubh/Developer/resume%20sensei/resume-sensei/assets/resume-hub/Master/Master_Resume.md).
>
> **Extracted Sections:**
> - **Contact Info** (Sanitized/Generic placeholder rules checked)
> - **Summary**: 8+ years of experience in Software Engineering
> - **Experience**: Google (Senior SWE), Stripe (SWE)
> - **Skills**: Python, Go, Kubernetes, React
>
> Shall we begin optimizing this history for your target applications?

---

### 3. ATS Screening & Matching

Provide a job description to audit your keywords and identify gaps.

**You:** `"Check ATS match against this Google Senior SWE job: [paste requirements]"`

**AI:**
> 📊 **ATS Keyword Matching Report**
>
> **Match Score:** **65%**
>
> | Category | Found Keywords | Missing Keywords | Impact |
> | :--- | :--- | :--- | :--- |
> | **Hard Skills** | Python, Kubernetes, Go | **System Design, Distributed Systems, gRPC** | High |
> | **Soft Skills** | Mentorship, Leadership | **Cross-Functional Collaboration** | Medium |
> | **Domain Terms** | REST API, Scalability | **SLA, Capacity Planning** | Low |
>
> **Action Plan:**
> 1. Weave **System Design** and **Distributed Systems** into your Senior SWE section at Google.
> 2. Highlight a cross-functional project to address **Cross-Functional Collaboration**.
>
> Would you like me to suggest XYZ-improved bullet rewrites incorporating these keywords?

---

### 4. Improving Bullets (Google's X-Y-Z Formula)

The AI prompts you for missing metrics to build quantitative achievement statements.

**You:** `"Improve the bullet: 'Helped reduce backend latency'"**

**AI:**
> Let's rewrite this bullet using Google's X-Y-Z formula: *Accomplished [X], as measured by [Y], by doing [Z]*.
>
> To do this, I need a few details:
> 1. By what percentage or millisecond count was backend latency reduced? (e.g., *40%*, *150ms*)
> 2. What action did you take to achieve this? (e.g., *restructured queries*, *implemented caching*)
> 3. What scale or tech stack was involved? (e.g., *Go microservices*, *Redis*)
>
> Let me know any details you have, or approximate numbers!

**You:** *"It was about 35% using caching on Go microservices."*

**AI:**
> Here is the polished improvement:
>
> *   **Original**: Helped reduce backend latency.
> *   **XYZ-Formula Polish**: *Optimized response times by 35% [Y] across core Go microservices [Z] by designing and integrating a distributed Redis caching layer [X].*
>
> Shall I update this in your Master resume?

---

### 5. Compiling Tailored LaTeX Resumes

The AI formats your resume using compilation-safe LaTeX syntax, escaping special tokens automatically so the output compiles on first run.

**You:** `"Export this tailored resume to Modern LaTeX style"`

**AI:**
> 📝 **Generating compile-safe Modern LaTeX...**
> Sanitized special characters:
> - `&` $\rightarrow$ `\&`
> - `%` $\rightarrow$ `\%`
> - `_` $\rightarrow$ `\_`
>
> File written to: [**`Tailored/Google/Shukla_Resume_Google_2026-06.tex`**](file:///Users/shubh/Developer/resume%20sensei/resume-sensei/assets/resume-hub/Tailored)
>
> **Application Tracker Logged:**
> | Date | Company | Role | File Name | Status |
> | :--- | :--- | :--- | :--- | :--- |
> | 2026-06-20 | Google | Senior SWE | Shukla_Resume_Google_2026-06.tex | Staged |
>
> You can compile this file directly using the local compiler helper script (`python3 scripts/compile_resume.py <path_to_tex>`) or copy-paste it into Overleaf!

---

## Reference Tips

*   **central Master Resume**: Always keep your master markdown complete. The AI will do the heavy lifting of pruning and restructuring for each application.
*   **Compile-Safe Conversions**: The AI checks templates for standard TeX packages like `hyperref`, `geometry`, and `fontawesome5`. Do not add custom third-party sty packages unless they are standard on basic LaTeX distributions.
