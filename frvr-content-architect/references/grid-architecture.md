# Grid architecture: seasons, series, rows and threads

## 1. The hierarchy

```
VISION · MISSION (fixed)                The FRVR Temple: Christ at the centre, a man formed forever
└─ YEAR (one lap of the Temple)         all four faces, about one season each
   └─ SEASON (6–12 weeks)               one face or one root family, with a season name and look
      └─ SERIES (3–9 posts)             one theme, Root to Fruit complete, ends in one next step
         └─ POST (carousel, reel, card) one act or layer, linked back and forward
            └─ SLIDE / BEAT             one idea
```

Every post must be able to answer four questions: **Which series am I in? Which act and layer do I carry? What did I build on? What do I set up?**

## 2. The year: a lap of the Temple

A suggested order. It follows the gospel logic, so adjust it to the calendar and to Aziel's own season.

| Season | Face | Why here | Root family it works on |
|---|---|---|---|
| 1 | **SPIRIT · Received** | Identity first. Everything after this is built *from* it | Worth |
| 2 | **SOUL · Renewed** | The mind, the lies, focus, calling, money | Control, Significance |
| 3 | **SOMA · Stewarded** | The body as a temple, now on the right foundation | Comfort |
| 4 | **SOCIAL · Belonging** | Brothers, family, fruit for others. Formation is never solo | Belonging |

Seasonal moments (Lent, Easter, Advent, New Year, Father's Day) slot in as bridge series. They always point back to the season's face. Easter Scripture is the only use of crimson (design system rule).

Inside each season, the series climb the four acts: **Design → Distortion → Deliverance → Discipleship**. A season usually opens with a "how you were made" series and closes with a protocol or challenge series plus its lead magnet.

## 3. Series templates

**Default 6-post series**

| # | Act / layer | Typical format | Account |
|---|---|---|---|
| 1 | Design: how it's meant to work | Teaching carousel (C1/C7), evidence-led | Well |
| 2 | Distortion: Fruit + Pattern, the mirror | Diagnosis (C3), or a POV reel | Well / AZ |
| 3 | Distortion: Lie + Root | Split (C4) or Argument (C2) | Well |
| 4 | Deliverance: Truth, the turn | Verse card set (C14), Gospel Object (C12), talking head | AZ / Well |
| 5 | Discipleship: Frame + Framework + Protocol | Maxxing / Blueprint / 101 | Well |
| 6 | Discipleship: Fruit, lived | Documented journey (C16) or Story (C5) → next step | AZ |

**Short 3-post series (one grid row):** Mirror (Fruit → Root) · Turn (Truth + Frame) · Tool (Protocol + Fruit).

**Long 9-post series (three rows):** Row 1 = Design + Distortion. Row 2 = the root and the turn. Row 3 = formation and fruit.

Every series has a name, a series mark, numbering on every cover ("03 / 06"), one signature look across all its posts, and one next step at the end. Most series end in Scripture, a local church, a brother or prayer. Only some end in a resource (Temple Audit, a Blueprint, Temple 101), and a resource is always a gift that serves the man, never the funnel.

## 4. The profile grid

**How the grid behaves.** Check current specs with `platform-specs-and-validation` before relying on them.
- Newest posts appear top-left. Every new post pushes everything along by one tile, so **rows only stay aligned if you add grid posts in threes.** A single extra post shifts every row.
- Pinned posts sit at the top and break the flow below them. Treat the pinned row as fixed.
- The profile grid crops thumbnails taller than square (3:4 since early 2025), and 4:5 posts lose a little at the top and bottom. Keep every cover's hook inside the central safe area.
- Reels show on the grid by default. Either count them in the row or take them off the profile grid where the platform allows.

**Design rules**
- **Every tile stands alone.** Puzzle grids (one image split across tiles) break the moment the count is off by one. Use colour, look and series marks to make rows cohere, not cut images.
- **One row = one week = one mini Root to Fruit.** With three grid posts a week, each row is a triptych: Mirror · Turn · Tool. Visitors scanning the grid see the whole method on every line.
- **Reading order.** In a row, the post published last sits on the left. If a row must read left to right as 1-2-3, publish part 3 first. Most of the time, publish in story order for feed followers, and design each row so it reads in either direction.
- **Rhythm of grounds.** Alternate midnight (night) and light (day) grounds, or keep one ground per series, so the season reads as bands of colour. Every row keeps one gold accent, per the design system.
- **Faces at a glance.** Use the face glyph or series mark in the same corner on every cover, so a visitor can see the Temple being built.

## 5. The front door: pinned posts and the first 12

A new visitor decides in seconds. The pinned row is the front door. Keep it to three, and refresh it each season:

1. **The Why** (manifesto): who FRVR is for, the problem in his words, and "a son starts from Someone".
2. **The Temple**: the framework in one carousel. Four faces, Christ at the centre, where to start.
3. **Start Here**: the current lead magnet (Temple Audit), with a comment keyword.

**Current plan:** Season 0 "Whole" (`assets/season-0-whole.csv`, from `integration-thesis.md` §7) replaces the generic table below. Its pinned row is Not Balance. Integration. · The Cross of Integration · Start Here: the Alignment Audit (with the Integration pairs). Its four rows are One Centre (SPIRIT), Undivided Heart (SOUL), Rhythm (SOMA) and Lion and Lamb (SOCIAL). The table below stays as the generic pattern.

**Genesis 12: a proposed launch sequence** (or a relaunch) for a fresh grid. Four rows, each a Mirror · Turn · Tool triptych, each row one face:

| Row | Face | Mirror | Turn | Tool |
|---|---|---|---|---|
| 1 | SPIRIT | "You're tired of trying to become someone." | A son starts from Someone (Eph 2:8–10) | Five minutes with the Word: the floor |
| 2 | SOUL | "Your mind never stops." | Renewed, not self-made (Rom 12:2) | One phone-free first hour |
| 3 | SOMA | "You treat your body like a project." | A temple, bought at a price (1 Cor 6:19–20) | Morning light and walk protocol |
| 4 | SOCIAL | "You have followers, not brothers." | Two are better than one (Eccl 4:9–12) | One weekly brother: the invite script |

Once these 12 are published, the grid shows the full Temple and the whole method. Seasons can then go deep on one face at a time. All verse references are to be fetched in the BSB and read in context.

## 6. Weekly rhythm

| Day | Grid | Job | Account lean |
|---|---|---|---|
| Mon | ✔ | **Mirror**: Distortion (Fruit → Root) | Well |
| Tue | stories | poll or question box on Monday's mirror (this feeds the heart map) | both |
| Wed | ✔ | **Turn**: Deliverance (Truth + Frame) | AZ |
| Thu | stories / reel off-grid | behind the scenes, Aziel living it | AZ |
| Fri | ✔ | **Tool**: Discipleship (Framework + Protocol + Fruit) | Well |
| Sat | stories | the protocol in practice; replies to comments | both |
| Sun | rest or one verse story | Sabbath: no selling | — |

Adjust the cadence to Aziel's capacity. If the week is short, keep the triptych and drop the stories. The row matters more than the volume.

## 7. Threads: how pieces visibly connect

- **Series marks and numbering** on every cover and in the caption's first line.
- **Callbacks:** slide 2 or the caption opens with "Last week we found the root…" and names the previous post.
- **Forward hooks:** the last slide before the CTA plants the next question: "But why does the lie feel true? Friday."
- **Shared vocabulary:** the same names everywhere (floor, Unbroken, the Temple, the faces). One word, one meaning.
- **Story Highlights as the library:** one Highlight per series, plus "Start Here" and "The Temple".
- **Pinned comment** on each post linking to the previous and next part.
- **Cross-account bridges:** Well teaches the framework; AZ shows Aziel living it the same week and points across.
- **The next step completes the series.** Where a resource fits, it is the series' Fruit in a form people can keep, and its first page names the root the series uncovered and points to Christ.

## 8. Idea Bank (no stray posts)

Ideas that don't fit the current season go to the Idea Bank in the Thread Map, as rows with `status = idea` and a proposed season and series. When a season is planned, pull from the bank first. An idea that never finds a series is probably a caption, a story or a slide, not a post.
