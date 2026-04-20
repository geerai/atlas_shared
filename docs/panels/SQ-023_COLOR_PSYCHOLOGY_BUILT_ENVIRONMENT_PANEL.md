# Panel Dossier: SQ-023

## Question

What experimental evidence supports specific colour recommendations (e.g. blue for focus, green for calm) in educational or healthcare interior design?

## Topic / Subtopic

Color Psychology / Built environment

## Status

`llm_panel_drafted`

## Panel Composition

| # | Name | Role | Affiliation | Expertise |
|---|------|------|-------------|-----------|
| 1 | **Andrew Elliot** | Domain Lead | University of Rochester | Color-in-context theory, red-avoidance effect, color and cognitive performance |
| 2 | **Ravi Mehta** | Color and Creativity Expert | University of Illinois | Red vs. blue effects on creativity and attention, color and motivated cognition |
| 3 | Nilüfer Saglar Onay | Architectural Color Expert | Bilkent University | Color in interior design, color and spatial perception, cultural color meaning |
| 4 | Anya Hurlbert | Color Vision Expert | Newcastle University | Color preference biology, sex differences in color preference, spectral processing |
| 5 | Ruth Tofle | Evidence-Based Color Expert | University of Missouri | Systematic review of color and healthcare environments, color research methodology critique |

## In-Criteria (Central Cases)

1. The study tests the effect of interior wall colour, ceiling colour, or ambient coloured lighting on cognitive performance (attention, focus, creativity), emotional state (calm, anxiety, mood), or physiological arousal in educational or healthcare interior settings.
2. The study controls for confounds: luminance, saturation, and brightness are held constant or varied systematically alongside hue, so the hue effect can be isolated.
3. The study tests specific colour recommendations — e.g., "blue enhances focus," "green promotes calm," "red increases arousal" — with objective outcome measures.
4. Systematic reviews or meta-analyses evaluating the strength of evidence behind specific colour-function claims in built environments.

## Out-Criteria (Clear Rejections)

1. Papers about colour preference without functional outcomes (which colour do you like best? without measuring performance or mood).
2. Papers about colour on screens, product packaging, or branding — colour-in-marketing without built environment context.
3. Papers about lighting colour temperature (warm/cool white). These are SQ-017 territory — CCT is not hue.
4. Papers about colour vision deficiency, chromatic adaptation, or colour science without psychological function in built environments.

## Hard Cases (Borderline Decisions)

1. **Laboratory studies using coloured backgrounds on screens**: The classic Mehta & Zhu (2009) red-vs-blue study used computer screen backgrounds, not room colours. *Tend toward: include — this is foundational evidence for the "blue = focus, red = avoidance" claim, even though the setting is not an architectural interior.*

2. **Studies confounding hue with brightness/saturation**: Many "colour" studies compare bright blue to dim red, confounding hue with other attributes. *Tend toward: include with warning — flag the confound, because this is the primary methodological weakness of the colour-function literature.*

3. **Cultural colour meaning studies**: Red means luck in Chinese culture vs. danger in Western culture. *Tend toward: include if the study measures a functional outcome (performance, mood), not just semantic association.*

4. **Studies finding null effects of colour on cognition**: These are important because the popular claim that colour significantly affects behaviour may be overstated. *Tend toward: definitely include — null findings are epistemically essential for this topic.*

5. **Coloured lighting vs. coloured surfaces**: LED systems that bathe rooms in coloured light produce different experiences from painted walls. *Tend toward: include both, but distinguish the mechanism — coloured lighting changes the entire visual field while painted surfaces interact with illumination.*

## False Friends

- **"Green building"** — sustainable certification, not the colour green
- **"Blue light"** — short-wavelength light and circadian effects (SQ-016), not blue room colour
- **"Red flag"** — warning signal metaphor
- **"Color-coded"** — data visualization or categorization system
- **"Warm colors"** in lighting — CCT (SQ-017), not warm hues

## Evidence Markers

- Munsell notation or explicit hue/saturation/brightness specification
- Controlled illumination: specified lux, CRI, and spectral power distribution
- Cognitive tasks under colour conditions: Stroop, RAT (Remote Associates), anagram, attention tasks
- Physiological measures: skin conductance, heart rate, EEG under colour conditions
- References to Elliot & Maier (2012, 2014), Mehta & Zhu (2009), Kwallek et al. (2007), Tofle et al. (2004)
- Sample sizes and effect sizes — this literature has notable replication concerns

## Article Type Guidance

| Type | Verdict | Rationale |
|------|---------|-----------|
| `empirical_research` | **Accept** | Experimental colour-function studies |
| `meta_analysis` | **Accept** | Pooled colour effect evidence |
| `systematic_review` | **Accept** | Evidence mapping (especially Tofle et al.) |
| `narrative_review` | **Marginal** | Colour psychology overviews |
| `theoretical` | **Marginal** | Colour-in-context theory |

## Escalation Triggers

The following cases MUST be escalated to a subscribed LLM adjudicator rather than resolved by keyword heuristics:

1. **Replication failures of Mehta & Zhu (2009)** or Elliot red-avoidance effects. The adjudicator must determine whether the replication attempt used comparable methodology (same tasks, similar sample sizes, same colour specifications) and report the comparison of effect sizes between the original and replication.

2. **Studies showing that colour effects are entirely explained by brightness or saturation** rather than hue. The adjudicator must assess whether the study's design adequately disentangles hue from luminance and saturation, and determine whether this refutes hue-based colour recommendations or merely identifies a confound.

3. **Studies in non-Western populations** where colour associations differ substantially from Western samples. The adjudicator must determine whether the study measures functional outcomes (performance, mood) or merely semantic associations (colour-meaning surveys), and cross-reference SQ-029 (cultural variation) if the cultural dimension is the primary finding.

## Unresolved Ambiguities

- The entire field has a replication problem. Effect sizes from foundational studies may be inflated, and many popular colour recommendations rest on weak evidence.
- Whether colour effects on cognition are direct (colour → arousal → performance) or mediated by colour semantics (colour → meaning → motivation → performance) is unresolved.
- The practical effect size of room colour in real interiors — even if statistically significant — may be too small to matter compared to lighting, layout, or acoustic design.

## LLM Drafting Note

This constitution was drafted with LLM panel reasoning. SQ-023 is the question most likely to reveal a gap between popular belief and scientific evidence. The popular narrative ("paint classrooms blue for focus") far outruns the empirical base. Including Tofle (author of a devastating systematic review of colour-in-healthcare claims) and Elliot (who has both supported and identified limits of colour effects) provides essential critical balance. The constitution deliberately prioritizes null findings and replication evidence.
