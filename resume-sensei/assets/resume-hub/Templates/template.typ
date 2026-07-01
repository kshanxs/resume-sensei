#let contact(text: "", link: none) = {
  (text: text, link: link)
}

#let subSection(title: "", titleEnd: none, subTitle: none, subTitleEnd: none, content: []) = {
  (title: title, titleEnd: titleEnd, subTitle: subTitle, subTitleEnd: subTitleEnd, content: content)
}

#let section(title: "", content: subSection()) = {
  (title: title, content: content)
}

#let project(
  theme: rgb("#4273B0"),
  style: "classic", // Supports "classic" (solid colored banners) or "modern" (clean bottom underlines)
  name: "",
  email: none,
  title: none,
  contact: ((text: [], link: "")),
  skills: (
    languages: ()
  ),
  main: (
    (title: "", content: [])
  ),
  sidebar: (),
  body) = {

  let backgroundTitle(content) = {
    if style == "classic" {
      align(center, box(fill: theme, text(white, size: 1.15em, weight: "bold", upper(content)), width: 100%, inset: 0.3em))
    } else {
      v(0.3em)
      block(width: 100%, inset: (bottom: 0.2em), stroke: (bottom: 1.5pt + theme))[
        #text(theme, size: 1.15em, weight: "bold", upper(content))
      ]
      v(0.1em)
    }
  }

  let secondaryTitle(content) = {
    text(weight: "bold", size: 1.125em, upper(content))
  }

  let italicColorTitle(content) = {
    text(weight: "bold", style: "italic", size: 1.125em, theme, content)
  }


  let formattedName = block(upper(text(2.5em, weight: "bold", theme, name)))

  let contactLine = contact.map(c => {
    if c.link == none [
      #c.text
    ] else [
      #link(c.link, text(theme, c.text))
    ]
  }).join(" • ")

  align(center)[
    #formattedName
    #contactLine
  ]
  
  set par(justify: true)

  let formattedLanguageSkills = [
    #text(skills.languages.join(" • "))
  ]

  let createLeftRight(left: [], right: none) = {
    if (right == none) { 
      align(start, text(left))
    } else {
      grid(
        columns: (1fr, 1fr),
        align(start, text(left)),
        align(end, right),
      )
    } 
  }

//  let parseContentList(contentList) = {
//    if contentList.format == "bulletJoin" [
//      #text(contentList.content.join(" • "))
//    ] else if contentList.format == "bulletList" [
//      #contentList.content.map(c => list(c)).join()
//    ]
//  }

  let parseSubSections(subSections) = {
    subSections.map(s => {
      [
        #createLeftRight(
          left: secondaryTitle(s.title),
          right: if s.titleEnd != none { 
            italicColorTitle(s.titleEnd)
          }
        )
        #if s.subTitle != none or s.subTitleEnd != none [
          #text(
            top-edge: 0.2em,
            createLeftRight(
              left: italicColorTitle(s.subTitle),
              right: s.subTitleEnd
            ),
          )
        ]
        #s.content
      ]
    }).join()
  }

  let parseSection(section) = {
    section.map(m => {
      [
        #backgroundTitle(m.title)
        #parseSubSections(m.content)
      ]
    }).join()
  }

  let mainSection = parseSection(main)
  let sidebarSection = parseSection(sidebar)


  mainSection
}