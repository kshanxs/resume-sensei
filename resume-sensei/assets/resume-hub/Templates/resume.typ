#import "template.typ": *

#set page(
  margin: (
    left: 8mm,
    right: 8mm,
    top: 8mm,
    bottom: 8mm
  ),
)

// Set standard premium sans-serif typography
#set text(font: "Mulish")

#show: project.with(
  theme: rgb("#4A5568"), // Custom premium theme color (e.g., #4A5568 for Slate Grey, #0F83C0 for Blue)
  style: "classic",      // Theme style: "classic" (colored blocks) or "modern" (clean underlines)
  name: "Shubhanshu Shukla",
  contact: (
    contact(
      text: "email@example.com",
      link: "mailto:email@example.com"
    ),
    contact(
      text: "+91-99999-99999",
      link: none
    ),
    contact(
      text: "linkedin.com/in/username",
      link: "https://www.linkedin.com/in/shubhanshu-shukla"
    ),
    contact(
      text: "github.com/kshanxs",
      link: "https://github.com/kshanxs"
    )
  ),
  main: (
    section(
      title: "Objective",
      content: (
        subSection(
          content: [
            Aim to pursue an MS in computer science with a specialisation in artificial intelligence and cloud computing to strengthen technical foundation and deepen understanding of modern computing systems. Willing to explore advanced concepts in networking, intelligent systems, and scalable cloud architectures. Post-graduation, I aspire to work as a software engineer in innovative, fast-growing technology domains.
          ]
        ),
      )
    ),
    section(
      title: "Education",
      content: (
        subSection(
          title: "JMIETI / Kurukshetra University",
          titleEnd: "Yamunanagar, Haryana, India",
          subTitle: "B.Tech in Computer Science and Engineering",
          subTitleEnd: "(August 2019 – June 2023)",
          content: [
            CGPA: 7.3/10
          ],
        ),
      ),
    ),
    section(
      title: "Experience",
      content: (
        subSection(
          title: "Freelance Full-Stack Developer",
          titleEnd: "Yamunanagar, Haryana, India",
          subTitle: "Self-Employed / Multiple Clients",
          subTitleEnd: "(August 2023 – Present)",
          content: list(
            [Develop full-stack web solutions using Node.js, Python, TypeScript, Supabase, and MongoDB to ensure scalable, reliable application performance.],
            [Implement backend enhancements, optimise APIs, and collaborate with clients to deliver customised, production-ready features.],
            [Strengthen database designs, streamline deployment processes, and maintain end-to-end project quality across diverse client requirements.],
            [Consistently completed projects with strong client feedback for technical proficiency, problem-solving, and timely delivery.]
          ),
        ),
      ),
    ),
    // NOTE: For 2-page CVs/Resumes, you can uncomment the pagebreak below to force a page split:
    // #pagebreak()
    section(
      title: "Academic Projects",
      content: (
        subSection(
          title: "Soul NFT Marketplace",
          titleEnd: "JMIETI, Yamunanagar, India",
          subTitle: "Team Lead | Team Size: 3 Members",
          subTitleEnd: "(March 2023 – May 2023)",
          content: [
            Developed "Soul," a decentralised NFT marketplace that empowers users to securely create, buy, and sell digital assets. Leveraging blockchain technology ensures transparency and security, fostering a seamless and innovative environment for digital asset transactions and ownership management.
          ]
        ),
        subSection(
          title: "Image Steganography",
          titleEnd: "JMIETI, Yamunanagar, India",
          subTitle: "Solo | Role: Team Lead",
          subTitleEnd: "(February 2022 – May 2022)",
          content: [
            Implemented an image-steganography tool in Python that embeds and extracts hidden messages using cryptography and image-processing techniques, enabling secure and covert data concealment. Utilised robust file-handling and algorithmic logic to ensure reliable encoding/decoding while maintaining image integrity. The project successfully demonstrated a practical solution for privacy-focused data transmission.
          ]
        )
      ),
    ),
    section(
      title: "Technical Skills",
      content: (
        subSection(
          title: "Core Stack & Familiarity",
          content: [
            *Languages:* JavaScript (5 yrs), Python (3 yrs), TypeScript (2 yrs) \
            *Runtime Environments:* Node.js (2 yrs) \
            *Databases & BaaS:* MongoDB (2 yrs), Supabase (2 yrs) \
            *Version Control & Tools:* Git, GitHub (6 yrs)
          ]
        ),
      )
    ),
    section(
      title: "Certifications & Training",
      content: (
        subSection(
          title: "Professional Training Courses",
          content: list(
            [Data Science -- Infosys (2026)],
            [Smart India Hackathon -- Selected Participant (2022)],
            [Allsoft Solutions -- IBM Business Partner (2020)]
          )
        ),
      )
    ),
    section(
      title: "Achievements & Extracurriculars",
      content: (
        subSection(
          title: "Community & Competition Highlights",
          content: list(
            [Nominated as an *Ambitious AI User* at the iQOO Tech Event, recognising active engagement with emerging AI tools (2025).],
            [Joined the Nothing Community Event in Delhi and interacted with the CEO, gaining insights into modern tech ecosystems (2025).],
            [Selected and participated in the *Smart India Hackathon*, contributing to innovative problem-solving (2022).],
            [State-Level Chess Championship Runner-Up, demonstrating strong strategic and analytical skills (2017).],
            [Winner of the District-Level Chess Tournament, showcasing consistency and focus (2016).]
          )
        ),
      )
    ),
    section(
      title: "Languages Known",
      content: (
        subSection(
          title: "Proficiency Levels",
          content: [
            English (Proficient) #sym.dot.c Hindi (Native) #sym.dot.c German (Basic)
          ]
        ),
      )
    )
  ),
  sidebar: (),
)
