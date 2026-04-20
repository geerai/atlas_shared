# Panel Dossier: SQ-016

## Question

What evidence shows that dynamic or daylight-aligned lighting in workplaces improves sleep quality, alertness, or mood in non-clinical populations?

## Topic / Subtopic

Lighting / Circadian alignment

## Status

`llm_panel_drafted`

## Panel Composition

| # | Name | Role | Affiliation | Expertise |
|---|------|------|-------------|-----------|
| 1 | **Mariana Figueiro** | Domain Lead | Mount Sinai / Icahn School of Medicine | Light and circadian entrainment, melatonin suppression, workplace lighting interventions |
| 2 | **Mirjam Münch** | Chronobiology Expert | Charité Berlin | Non-visual light effects, melanopic stimulus, daytime light exposure and alertness |
| 3 | Jan Wout Kruithof | Lighting Engineering Expert | Eindhoven University of Technology | Dynamic lighting control systems, tunable LED, WELL Building Standard lighting |
| 4 | Christian Cajochen | Sleep Physiology Expert | University of Basel | Evening light exposure, melatonin, sleep architecture, circadian phase assessment |
| 5 | Yvonne de Kort | Environmental Psychology Expert | Eindhoven University of Technology | Subjective lighting effects, vitality, perceived alertness, non-image-forming light effects |

## In-Criteria (Central Cases)

1. The study tests dynamic lighting interventions (time-varying CCT, illuminance, or spectral composition across the workday) and measures sleep quality, alertness, or mood in non-clinical workplace populations (office workers, teachers, nurses on regular shifts).
2. The study exposes participants to daylight-mimicking spectral distributions during the day and measures circadian-related outcomes (melatonin onset timing, sleep latency, actigraphy, alertness ratings, mood).
3. The study compares melanopically enriched daytime lighting against standard fluorescent or static LED lighting in workplace settings with objective circadian or performance outcomes.
4. Meta-analyses or systematic reviews of dynamic/circadian-aligned workplace lighting studies in non-clinical populations.

## Out-Criteria (Clear Rejections)

1. Papers about clinical light therapy for Seasonal Affective Disorder (SAD), shift-work sleep disorder, or circadian rhythm disorders. SQ-016 specifies non-clinical populations.
2. Papers about daylighting through windows measuring only energy savings or glare without psychological or physiological outcomes.
3. Papers about lighting ergonomics (visual comfort, task illuminance) without circadian, mood, or alertness outcomes.
4. Papers about screen light and blue light from devices (phones, computers) without workplace lighting intervention context.

## Hard Cases (Borderline Decisions)

1. **Nurse shift-work lighting studies**: Nurses are workplace populations but shift work is a clinical circadian challenge. *Tend toward: include if the study tests a lighting intervention to support normal circadian function during regular shifts (not treatment for diagnosed shift-work disorder).*

2. **School classroom lighting studies**: Dynamic lighting for student alertness and performance. Students are not "workplace" populations in the traditional sense. *Tend toward: include — the lighting intervention and circadian mechanism are identical; only the setting differs.*

3. **Simulated daylight (tunable LED) studies in windowless offices**: These test artificial circadian lighting, blurring the line between "daylight-aligned" (matching solar spectrum) and "dynamic" (any time-varying lighting). *Tend toward: include — this is a primary application of the technology.*

4. **Evening light restriction studies**: Research on reducing blue-enriched light in the evening rather than increasing it during the day. *Tend toward: edge case — the mechanism is circadian, but the intervention is at home, not in the workplace.*

5. **Studies measuring only subjective alertness without objective circadian markers**: Self-report alertness is vulnerable to expectation effects. *Tend toward: include, but flag that subjective-only evidence is weaker.*

## False Friends

- **"Dynamic lighting"** in photography — variable studio lighting setups
- **"Daylight savings"** — clock change policy, not circadian lighting
- **"Light therapy"** for depression — clinical treatment, not workplace design
- **"Mood lighting"** — decorative ambiance, not circadian
- **"Smart lighting"** for energy management — IoT automation without circadian intent

## Evidence Markers

- Melanopic equivalent daylight illuminance (melanopic EDI), melanopic lux
- Correlated colour temperature (CCT) in Kelvin, specified by time of day
- Dim Light Melatonin Onset (DLMO) as circadian phase marker
- Actigraphy, sleep diary, Pittsburgh Sleep Quality Index (PSQI)
- Karolinska Sleepiness Scale (KSS), Psychomotor Vigilance Task (PVT)
- References to Figueiro et al. (2017, 2019), Viola et al. (2008), de Kort & Smolders (2010), Münch et al. (2012)
- well-v2, WELL Building Standard credits for circadian lighting

## Article Type Guidance

| Type | Verdict | Rationale |
|------|---------|-----------|
| `empirical_research` | **Accept** | Workplace lighting intervention studies |
| `meta_analysis` | **Accept** | Pooled evidence |
| `systematic_review` | **Accept** | Evidence mapping |
| `narrative_review` | **Marginal** | Circadian lighting reviews |
| `theoretical` | **Marginal** | Circadian model predictions |
| `methods` | **Marginal** | Melanopic stimulus measurement protocols |

## Escalation Triggers

The following cases MUST be escalated to a subscribed LLM adjudicator rather than resolved by keyword heuristics:

1. **Studies comparing melanopic EDI standards against traditional illuminance standards** for the same outcomes. The adjudicator must assess whether the study's lighting specification is detailed enough to determine which standard was actually met, and flag the result for its direct building-code implications.

2. **Studies finding ceiling effects or null results for dynamic lighting in well-daylit offices.** If occupants already receive sufficient daylight, additional tunable lighting may not help. The adjudicator must determine whether the null result reflects a genuine ceiling effect (informative) or inadequate intervention dose/duration (uninformative).

3. **Studies measuring cognitive performance (not just alertness/mood/sleep) under circadian lighting.** These bridge SQ-016 with SQ-017. The adjudicator must classify the paper under whichever question best matches the primary research question, and cross-reference the other.

## Unresolved Ambiguities

- "Non-clinical" is ambiguous — does it exclude populations with subclinical circadian disruption (poor sleep hygiene, excessive evening screen use)?
- Whether the benefit comes from increased daytime melanopic light, reduced evening blue light, or the dynamic change across the day is rarely disentangled.

## LLM Drafting Note

This constitution was drafted with LLM panel reasoning. SQ-016 is the most rapidly evolving topic in the bank due to the recent adoption of melanopic standards (CIE S 026:2018) and the WELL Building Standard. The main challenge is that circadian lighting research originated in clinical populations and is being extrapolated to workplaces with much smaller expected effect sizes.
