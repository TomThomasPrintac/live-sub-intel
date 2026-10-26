# Demo video — concrete screen-led narration

26 October 2026 revision. Route: **0 → 5 → 10 → cut to 25 → cut to 65 → cut to 85**. English narration: **184 words**, target 1:50–1:55 and strictly under two minutes. [Standalone voiceover](VIDEO_NARRATION_EN.txt) · [Hebrew capture instructions](RECORDING_ROUTE_HE.md) · [All audited checkpoints](RECORDING_CHECKPOINT_REVIEW.md).

| Video time | Screen action | English narration |
|---|---|---|
| 0:00–0:10 | Minute 0, Arsenal, Balanced / Seek a win. Show the lineup and bench. | “Live Sub Intel helps you make the next move: who comes on, who comes off, and where everyone plays.” |
| 0:10–0:25 | Advance from 0 to 5 to 10; show the clock, event feed and statistics. Fast playback is optional for this opening; return to Instant for the remaining scenes. | “We’re following Arsenal in a generated match, using historical player profiles and physical estimates. As time advances, events arrive and the statistics update with the game.” |
| 0:25–0:42 | Cut to 25, Balanced / Win. Open plan inspection and Position changes. Point to Ramsey and Flamini on the current/proposed pitches. | “At twenty-five minutes, it recommends swapping Ramsey and Flamini’s midfield positions. Ramsey moves left; Flamini moves right. The proposed lineup highlights both moves.” |
| 0:42–1:04 | Stay at 25. Explain as Broadcaster in English, switch explanation language to Español and explain again, then select Analyst and explain. Point to one statistic actually present in the returned text. | “The broadcaster gets a short explanation of that move. Switch to Spanish, and the same plan is explained in Spanish. Choose Analyst, and the explanation adds relevant match statistics and trade-offs.” |
| 1:04–1:23 | Cut to 65, More attacking / Seek a win; return explanation output to English. Show Campbell → Oxlade-Chamberlain, the proposed pitch and Compare players & scoring. | “Now Arsenal are leading. The system recommends fresh legs on the wing: Oxlade-Chamberlain for Campbell. Open the comparison to see their profiles and what the change adds to the team.” |
| 1:23–1:40 | Cut to 85, Attack / Win. Show Arsenal behind, select Coach, then change Result objective to Avoid defeat and show the recalculated recommendation. | “At eighty-five minutes, Arsenal are behind. Seeking a win calls for a midfield adjustment. Switch to avoiding defeat, and the system recommends holding the current setup.” |
| 1:40–1:55 | Wide app view, then end card with project name, live site, repository and source attribution. Optional on-screen flow: match events → decision engine → Foundry explanation. | “Azure App Service hosts the match room. Microsoft Foundry selects the relevant facts and translates the explanation, so a coach and a Spanish-speaking broadcaster can follow the same decision.” |

## Off-mic production notes

- Record the real Azure app, with the interface in English. Prepare the exact plan/audience/language requests once before recording. Confirm the source label; do not present a template fallback as a successful model request. This is a production check, not spoken narration.
- Keep JSON, methodology and sensitivity panels closed. Open only Position changes at 25 and Compare players & scoring at 65 when the narration points to them.
- Spanish is the **explanation language**; leave the interface in English. Press Explain after each audience/language change. Check that the output really is Spanish before recording it.
- Keep cuts visible as edits. The 25-minute move swaps the two midfield positions in the same 4-2-3-1. It is not a new formation. Inspection does not execute a substitute or change future events; no line about that is required in the voiceover, but the film must not imply otherwise.
- At 65 the recommendation is mainly freshness-led. Do not claim the booking is an independently scored sending-off-risk penalty. Do not include the Mertesacker/Gabriel alternative in this film.
- At 85, Win yields a tactical adjustment and Draw yields Wait on the audited baseline. Show the actual result; this demonstrates policy sensitivity, not proven coaching accuracy. If you need to save time, omit the Coach explanation request and show only the objective change.
- Keep the final export strictly below two minutes. Target 1:50–1:55; measure your actual voice recording. Shorten transition pauses or omit the opening 10-minute checkpoint if needed. Do not speed the narration until it becomes hard to follow.
- Put the official StatsBomb logo and a short source line on the end card: `Historical research: StatsBomb Open Data. Physical references: SkillCorner Open Data.` Link DATA_SOURCES.md in the public video description. Use original or appropriately licensed audio/assets; background music is optional.
- Add corrected English captions. Check Ramsey, Flamini, Campbell, Oxlade-Chamberlain, Foundry and Spanish names/output. Captions follow the voiceover; they need not transcribe the whole UI explanation.
- Warm up/check the actual deployed build before recording. Do not merge/deploy during capture. This script edit does not modify the app, player data, ratings or decision rules.
