<div align="center">

# resume-sensei — Features & Reference

**v1.2.0** · *Complete feature list, command reference, and skill architecture*

</div>

---

## Full Feature List

<table>
<tr>
<td width="50%">

### Ingestion & Parsing
| | |
|---|---|
| **DOCX Parsing** | Dependency-free custom parser reads text from word files using Python standard libraries |
| **PDF extraction** | Integrated PDF reading for parsing existing resumes |
| **Markdown Normalization** | Automatically formats parsed resume details into a clean markdown structure |
| **Experience Extraction** | Extracts dates, locations, bullet lists, and summary details |

</td>
<td width="50%">

### ATS Screening
| | |
|---|---|
| **Keyword Auditing** | Automatically identifies hard skills, soft skills, and domain terms in a job description |
| **Match Scoring** | Calculates a keyword match score between the job description and your resume |
| **ATS Gap Checklist** | Lists exactly which high-impact keywords are missing from your resume |
| **Placement Blueprint** | Suggests precise sections and contexts to weave in missing keywords |

</td>
</tr>
<tr>
<td width="50%">

### Bullet Optimization
| | |
|---|---|
| **Google X-Y-Z Formula** | Rewrites weak bullets as: *Accomplished [X], as measured by [Y], by doing [Z]* |
| **STAR Formula** | Aligns professional bullets with Situation, Task, Action, and Result framing |
| **Action Verb Database** | Replaces passive verbs (e.g., *managed*, *worked*) with active, high-impact verbs |
| **Quantification Prompts** | Agent actively prompts you for missing metrics, stats, and business impacts |

</td>
<td width="50%">

### LaTeX Generation
| | |
|---|---|
| **Modern Style** | Elegant layout with centered name rule, light blue accents, and clean metadata headers |
| **Classic Style** | Academic layout with a solid color-block header band, orange accents, and filled section bars |
| **Special Token Escaping** | Automatically sanitizes ampersands (`&`), percentages (`%`), underscores (`_`), and dollar signs (`$`) |
| **Compile Safety** | Sanitizes TeX input and provides a standalone Python compilation script (`compile_resume.py`) with Overleaf guidelines |

</td>
</tr>
<tr>
<td width="50%">

### Workspace & Versions
| | |
|---|---|
| **Workspace Init** | Installs standard Workspace directories (`Master/`, `Tailored/`, `Applications/`) |
| **Central Source** | Single `Master/Master_Resume.md` tracks all professional history |
| **Version Control** | Automatically creates and organizes tailored versions for specific roles |
| **Application Tracker** | Central tracker logging sent resumes, roles, companies, and date updates |

</td>
<td width="50%">

### Context Efficiency
| | |
|---|---|
| **Lazy Loading** | Modular reference guides are loaded only on demand to prevent prompt token bloat |
| **Clean Orchestration** | Core instructions (`SKILL.md`) routes agent behaviors using small sub-rules |

</td>
</tr>
</table>

---

## Command Reference

| Say this | What happens |
|---|---|
| `"Initialize the resume workspace"` | Copies the standard workspace folders and Templates to active directory |
| `"Parse [resume.docx]"` | Extracts text content from DOCX and normalizes to Markdown |
| `"Check ATS match against [job description]"` | Analyzes resume keywords, calculates match score, and reports gaps |
| `"Improve this bullet using X-Y-Z"` | Rewrites experience bullets with quantified metrics and active verbs |
| `"Tailor my resume for [Role] at [Company]"` | Aligns experiences to job priorities and saves version details |
| `"Generate [classic/modern] LaTeX resume"` | Generates compile-safe LaTeX code based on templates |
| `"Compile resume [path_to_tex]"` | Calls `scripts/compile_resume.py` to compile LaTeX locally or display Overleaf guides |
| `"Update application tracker"` | Appends a row to the centralized job application spreadsheet log |

---

## Skill Architecture

```
resume-sensei-repo/           # Workspace Root
├── docs/
│   ├── USAGE.md              # Interactive guides and dialog examples
│   └── FEATURES.md           # Feature specs and command directory (This file)
├── CHANGELOG.md              # Version and update history
├── LICENSE                   # MIT license file
├── README.md                 # Project landing page
├── resume-sensei/            # Core Skill Package
│   ├── SKILL.md              # Main entrypoint & lazy loading routing rules
│   ├── references/           # Specialized rule files (loaded on demand)
│   │   ├── ats_optimization.md
│   │   ├── bullet_writing.md
│   │   ├── formatting_and_sections.md
│   │   └── tailoring_and_versioning.md
│   ├── scripts/
│   │   ├── compile_resume.py # LaTeX compile & verification helper script
│   │   └── parse_resume.py   # Dependency-free docx parser script
│   └── assets/
│       └── resume-hub/       # Template workspace skeleton
│           ├── Master/
│           ├── Applications/
│           └── Templates/
```
