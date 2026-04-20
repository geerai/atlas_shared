# Panel Dossier: SQ-017

## Question

How does colour temperature (warm vs. cool white light) affect alertness, mood, or productivity in educational or office settings?

## Topic / Subtopic

Lighting / Colour temperature

## Status

`llm_panel_drafted`

## Panel Composition

| # | Name | Role | Affiliation | Expertise |
|---|------|------|-------------|-----------|
| 1 | **Yvonne de Kort** | Domain Lead | Eindhoven University of Technology | Subjective lighting appraisals, alertness under different CCT, human-centric lighting |
| 2 | **Karin Smolders** | Experimental Expert | Eindhoven University of Technology | CCT and cognitive performance, alertness, vitality, time-of-day interactions |
| 3 | Robert Stevens | Educational Lighting Expert | Salford University | Classroom lighting, student performance, lighting and learning environments |
| 4 | Soolyeon Cho | Building Science Expert | North Carolina State University | Office lighting, LED retrofit studies, CCT and task performance field studies |
| 5 | Shelley James | Lighting Practice Expert | Age of Light (UK) | Evidence translation for lighting design practice, human-centric lighting industry standards |

## In-Criteria (Central Cases)

1. The study manipulates correlated colour temperature (CCT) — warm white (≤ 3000K) vs. neutral (3500–4500K) vs. cool white (≥ 5000K) — and measures alertness, mood, or cognitive/task performance in office or educational settings.
2. The study uses controlled or quasi-experimental design with CCT as the independent variable and holds illuminance approximately constant (or statistically controls for illuminance differences).
3. The study measures both subjective (mood, alertness ratings) and objective (task performance, reaction time, EEG, pupillometry) outcomes under different CCT conditions.
4. Systematic reviews or meta-analyses pooling CCT-performance evidence across multiple studies.

## Out-Criteria (Clear Rejections)

1. Papers about colour temperature in display screens (monitors, tablets) without architectural lighting context.
2. Papers about lighting colour rendering index (CRI) or colour fidelity without CCT manipulation.
3. Papers measuring only visual comfort, glare, or lighting satisfaction without alertness, mood, or cognitive performance outcomes.
4. Papers about coloured (chromatic) lighting — red, blue, green ambient light — rather than white-light CCT variation. These belong to SQ-023.

## Hard Cases (Borderline Decisions)

1. **Studies confounding CCT with illuminance**: Many "cool light" conditions also provide higher illuminance. If CCT and illuminance covary, the CCT effect cannot be isolated. *Tend toward: include with warning — this confound is widespread and meta-analyses can potentially control for it.*

2. **Field studies without strict experimental control**: Real-office CCT retrofits where employee performance is measured before/after. Confounds are numerous but ecological validity is high. *Tend toward: include — field validity complements lab control.*

3. **Studies of full-spectrum daylight-simulating lighting**: These change spectral power distribution more broadly than just CCT. *Tend toward: edge case — if the study reports CCT as the primary manipulation it belongs here; if it focuses on melanopic content, it belongs to SQ-016.*

4. **Studies finding null effects of CCT on performance**: Important because the "blue = alert, warm = calm" popular narrative may not be well-supported. *Tend toward: definitely include — null findings are epistemically critical.*

5. **Time-of-day interaction studies**: Some research suggests CCT matters most in the afternoon (when circadian alertness drops). *Tend toward: include — these refine rather than contradict the core question.*

## False Friends

- **"Colour temperature"** in photography — camera white balance settings
- **"Warm light"** in physics — thermal radiation spectra
- **"Cool climate"** — thermal environment, not light colour
- **"White noise"** — acoustic, not visual
- **"Light therapy"** — clinical SAD treatment at specific lux/CCT, not workplace design

## Evidence Markers

- Correlated Colour Temperature (CCT) in Kelvin with specific values
- Illuminance held constant across conditions or statistically controlled
- Karolinska Sleepiness Scale (KSS), Visual Analogue Scale (VAS) for alertness
- Cognitive tasks: PVT, digit span, sustained attention, proofreading
- Classroom metrics: test scores, time-on-task, teacher observation
- References to Smolders & de Kort (2014), Viola et al. (2008), Barkmann et al. (2012)
- Kruithof curve reference (CCT × illuminance comfort zone)

## Article Type Guidance

| Type | Verdict | Rationale |
|------|---------|-----------|
| `empirical_research` | **Accept** | CCT manipulation studies |
| `meta_analysis` | **Accept** | Pooled CCT evidence |
| `systematic_review` | **Accept** | Evidence mapping |
| `narrative_review` | **Marginal** | Human-centric lighting overviews |
| `methods` | **Marginal** | CCT measurement and specification |

## Escalation Triggers

The following cases MUST be escalated to a subscribed LLM adjudicator rather than resolved by keyword heuristics:

1. **Studies explicitly testing the Kruithof hypothesis** — that preferred CCT depends on illuminance level. The adjudicator must determine whether the study provides empirical data on the interaction (not just a reference to the Kruithof curve as background) and whether the results predict that no single CCT is universally "best."

2. **Studies comparing CCT effects to illuminance effects**, testing which variable is the stronger predictor of alertness/performance. The adjudicator must assess whether CCT and illuminance were independently manipulated or confounded, and report the relative effect sizes for each.

3. **Cultural or climate variation in CCT preference**: Whether warm/cool light preferences vary by latitude, season, or cultural background. The adjudicator must determine whether the study provides cross-cultural comparison data (at least two populations) or merely notes its own cultural context as a limitation.

## Unresolved Ambiguities

- The CCT-alertness relationship may not be linear — some studies find an inverted-U, others find monotonic effects.
- "Productivity" is defined inconsistently across studies — self-reported productivity vs. objective task performance show different patterns.

## LLM Drafting Note

This constitution was drafted with LLM panel reasoning. SQ-017 is the most practically accessible lighting question — every office and classroom has a CCT setting. The main risk is over-confidence in the "cool = alert, warm = calm" narrative, which has weaker empirical support than commonly assumed. The constitution deliberately includes null-finding studies and time-of-day interactions.
