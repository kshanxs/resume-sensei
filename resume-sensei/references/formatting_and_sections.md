# Formatting & Section Building Guidelines

Use this guide when the user needs to organize their resume sections, establish proper visual hierarchy, set margins, select fonts, or write section-specific content.

---

## 1. Visual Hierarchy & Formatting Defaults
A professional resume must be immediately scannable by a human recruiter in under 6 seconds, while remaining perfectly parsed by ATS software.

*   **Page Budget**:
    *   **Entry-Level (0-5 years)**: Strict 1 page.
    *   **Mid-Level (5-15 years)**: 1-2 pages.
    *   **Senior/Executive (15+ years)**: 2 pages (max 3 pages for highly senior CVs).
*   **Margins**: Keep margins between `0.5"` (minimum for content-dense resumes) and `1.0"` (maximum).
*   **Typography**:
    *   **ATS-Safe Fonts**: Arial, Calibri, Helvetica (Sans-serif) or Times New Roman, Georgia, Garamond (Serif).
    *   **Sizing Hierarchy**:
        *   *Name/Title*: 16-20pt (Bold)
        *   *Section Headers*: 12-14pt (Bold, uppercase)
        *   *Body text & bullets*: 10-12pt (Regular)
        *   *Minimum font size*: 10pt (any smaller is unreadable)
*   **Spacing**: Line spacing should be `1.0` to `1.15`. Ensure clear paragraph spacing (`6-12pt` after paragraphs) and section spacing (`12-16pt` between sections).

---

## 2. Section Ordering Guidelines by Role Type
Arrange sections to highlight the candidate's strongest qualifications first.

*   **Standard / General**:
    1. Contact Info
    2. Professional Summary (Optional)
    3. Skills
    4. Work Experience
    5. Education
    6. Additional (Certifications, Volunteer, Projects)
*   **Technical / Engineering**:
    1. Contact Info
    2. Skills (Prioritized to showcase languages/tools immediately)
    3. Work Experience
    4. Projects (To show hands-on technical application)
    5. Education & Certifications
*   **Recent Graduates**:
    1. Contact Info
    2. Education (Showcase school, degree, high GPAs, coursework first)
    3. Skills
    4. Work Experience / Internships
    5. Projects / Extra-curriculars
*   **Career Changers**:
    1. Contact Info
    2. Summary (Crucial here to explain the narrative transition)
    3. Transferable Skills
    4. Experience (Reframed to emphasize overlapping duties)
    5. Education & Retraining Projects

---

## 3. Section Content Blueprints

### A. Professional Summary (Formula)
Do not use generic objectives ("Seeking a challenging role"). Always use the following formula:

$$\text{[Title/Identity]} + \text{[Years of Experience]} + \text{[Core Competency Keywords]} + \text{[Unique Value Proposition]}$$

*   *Generic*: "Results-oriented professional with 5 years experience looking to grow."
*   *Premium*: "Product Manager with 6 years experience driving B2B SaaS platforms. Track record of growing products from concept to \$10M+ ARR through data-driven roadmaps and cross-functional leadership. Expert in developer tools and API platforms."

### B. Skills Section Layouts
*   **Categorized List (Recommended for Tech)**: Organize skills into logical categories to prevent a dense wall of text.
    ```
    TECHNICAL SKILLS
    Languages: Python, SQL, JavaScript, TypeScript
    Frameworks: React, Node.js, Express, Flask, Django
    Tools & Cloud: AWS (S3, EC2), Docker, Git, Tableau
    ```
*   **Simple List (Recommended for Space Constraints)**: A flat comma-separated list.
    ```
    SKILLS: Python, SQL, React, Node.js, AWS, Git, Agile, JIRA
    ```

### C. Experience Formatting Layout
Maintain strict consistency in text layout:

```
COMPANY NAME | City, State
Job Title | Start Month Year -- End Month Year
*   Achievement bullet with metric and result
*   Achievement bullet with metric and result
```

### D. Education Detail Guidelines
*   **Entry-Level**: List GPA if `3.5+`. Include honors, relevant coursework, and major academic projects.
*   **Mid-Career & Senior**: List degree, major, university, and location. Omit graduation date if concerned about age discrimination. Omit GPA and coursework.

---

## 4. Typst Style Configurations

When compile-formatting a resume, the workspace provides a clean, modular layout system defined in `Templates/template.typ` and `Templates/resume.typ`.

### Visual Parameters & Theme Customization
*   **Theme Color**: Change the theme accent color by modifying `theme: rgb("#0F83C0")` (or any other hex value) in the `project.with()` setup in your `.typ` file. This controls the background header bands, name font color, and link highlight colors.
*   **Font Selection**: Set using `#set text(font: "Mulish")` at the top of the file. The workspace packages the Google Mulish font family by default, but standard system fonts (like Arial or Calibri) can also be specified if they are installed locally.
*   **Margins**: Configured via the `margin` parameters inside `#set page(...)`. The default is set to `8mm` on all sides to maximize content area while remaining aesthetic.
*   **Contact Info Links**: Rendered dynamically using the `#contact(text: "Label", link: "URL")` helper. If a link is provided, it is automatically styled with the theme color and made clickable.
*   **Document Structure**:
    *   `section(title: "Section Name", content: (...))` renders a section with a full-width colored header band.
    *   `subSection(title: "Company/Inst", titleEnd: "Location", subTitle: "Role", subTitleEnd: "Date", content: [...])` defines specific entry details with left/right column alignment for easy reading.
