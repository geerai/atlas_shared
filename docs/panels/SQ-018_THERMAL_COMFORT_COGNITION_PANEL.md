# Panel Dossier: SQ-018

## Question

What is the optimal temperature range for cognitive performance in office settings, and how much do deviations above or below this range impair output?

## Topic / Subtopic

Thermal Comfort / Cognitive performance

## Status

`llm_panel_drafted`

## Panel Composition

| # | Name | Role | Affiliation | Expertise |
|---|------|------|-------------|-----------|
| 1 | **Pawel Wargocki** | Domain Lead | Technical University of Denmark | Indoor environment quality, temperature-performance dose-response, productivity studies |
| 2 | **David Wyon** | Co-Lead Expert | DTU / independent | Pioneer in temperature-performance research, SBS studies, thermal environment and cognition |
| 3 | Stefano Schiavon | Building Science Expert | UC Berkeley | ASHRAE 55, CBE thermal comfort surveys, mixed-mode ventilation, occupant satisfaction |
| 4 | Wouter van Marken Lichtenbelt | Thermal Physiology Expert | Maastricht University | Thermoneutral zone, adaptive thermogenesis, mild cold/heat exposure and metabolism |
| 5 | Lily Heschong | Daylighting and Performance Expert | Heschong Mahone Group | Daylighting and productivity, multi-factor IEQ studies, field performance measurement |

## In-Criteria (Central Cases)

1. The study manipulates or measures indoor air temperature and assesses cognitive performance (attention, memory, mathematical reasoning, text processing, creative thinking) in office or office-like settings.
2. The study establishes or tests a dose-response curve — quantifying how much cognitive performance degrades per degree Celsius of deviation from the optimal range.
3. The study compares occupant performance across thermal conditions using the ASHRAE 55 comfort range (approximately 20–26°C) or challenges this range with evidence of narrower or shifted optima.
4. Meta-analyses or systematic reviews pooling temperature-performance evidence, especially those estimating productivity loss per degree.

## Out-Criteria (Clear Rejections)

1. Papers about thermal comfort perception (satisfaction, preference) without cognitive performance measurement. Comfort and performance are related but distinct.
2. Papers about extreme heat/cold exposure (outdoor work, military, athletic performance) beyond the indoor office range.
3. Papers about HVAC system design, energy optimization, or building simulation without occupant performance data.
4. Papers about temperature effects on physical labor output (manual work, factory settings) rather than cognitive performance.

## Hard Cases (Borderline Decisions)

1. **Self-reported productivity as the outcome**: Large surveys (CBE, Leesman) reporting "how much does temperature affect your productivity?" *Tend toward: include — these have large N and practical relevance, but flag that self-report may not track actual performance.*

2. **Multi-factor IEQ studies**: Studies where temperature varies alongside air quality, noise, or lighting. *Tend toward: include if temperature effects are reported separately or statistically controlled; edge case if effects are bundled.*

3. **Classroom temperature studies**: Student test performance at different temperatures. *Tend toward: include — the cognitive mechanism is the same; the setting is educational rather than office.*

4. **Studies of personal thermal control**: Desk fans, heated chairs, personal comfort systems. These change perceived comfort without changing air temperature. *Tend toward: include — they test whether it is temperature per se or thermal comfort (perceived control) that affects performance.*

5. **Seasonal studies**: Performance variation across seasons that correlates with indoor temperature changes. *Tend toward: edge case — seasonal variation confounds temperature with daylight, mood, and activity patterns.*

## False Friends

- **"Temperature" in cognitive science** — temperature as metaphor for network parameter (softmax temperature)
- **"Thermal comfort"** surveys measuring only satisfaction, not performance
- **"Heating"** in HVAC engineering — system performance, not occupant cognition
- **"Hot cognition"** — emotionally charged reasoning, not thermal environment
- **"Cool-down period"** — post-exercise recovery, not air conditioning

## Evidence Markers

- Specific temperatures: °C or °F values, temperature ranges
- ASHRAE Standard 55 or ISO 7730 reference
- PMV (Predicted Mean Vote), PPD (Predicted Percentage Dissatisfied)
- Cognitive task batteries: addition, text correction, reading comprehension, typing
- Productivity quantification: % performance change per °C, call center metrics
- References to Wargocki et al. (2006), Seppänen et al. (2006), Lan et al. (2011)

## Article Type Guidance

| Type | Verdict | Rationale |
|------|---------|-----------|
| `empirical_research` | **Accept** | Controlled temperature-performance studies |
| `meta_analysis` | **Accept** | Pooled dose-response evidence |
| `systematic_review` | **Accept** | Evidence mapping |
| `narrative_review` | **Marginal** | IEQ productivity reviews |
| `methods` | **Marginal** | Performance measurement protocols |

## Escalation Triggers

The following cases MUST be escalated to a subscribed LLM adjudicator rather than resolved by keyword heuristics:

1. **Studies finding that the performance optimum differs from the comfort preference** — people may prefer warmer conditions than those that maximize their performance. The adjudicator must determine whether the study measured both comfort and performance independently, and flag the discrepancy for its design policy implications.

2. **Studies testing the Yerkes-Dodson pattern** — mild thermal discomfort improving performance through increased arousal before further deviation causes decline. The adjudicator must assess whether the study design has enough temperature conditions to detect a non-monotonic curve, not just a two-condition comparison.

3. **Studies of temperature and creativity** (not just vigilance/accuracy tasks). The adjudicator must determine whether the creative task is valid (e.g., Guilford's Alternative Uses, Remote Associates Test) and whether the optimal range for divergent thinking differs from the range for convergent tasks reported in the existing dose-response literature.

## Unresolved Ambiguities

- The "optimal" temperature is likely task-dependent, population-dependent (clothing, acclimatization, metabolic rate), and may differ between males and females.
- Whether the effect is about absolute temperature or perceived comfort (thermal satisfaction) is rarely tested directly.

## LLM Drafting Note

This constitution was drafted with LLM panel reasoning. SQ-018 is distinctive because it produces directly actionable design recommendations — thermostat setpoints. The Seppänen/Wargocki dose-response curve (approximately 1-2% productivity loss per °C above 25°C) is widely cited but based on a limited evidence pool. The constitution must include challenges to this estimate alongside support.
