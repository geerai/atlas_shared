# Panel Dossier: SQ-001

## Question

What empirical evidence supports the claim that natural environments restore directed attention better than urban environments?

## Topic / Subtopic

Attention Restoration Theory / Core evidence

## Status

`llm_panel_drafted`

## Panel Composition

| # | Name | Role | Affiliation | Expertise |
|---|------|------|-------------|-----------|
| 1 | **Ming Kuo** | Domain Lead | University of Illinois Urbana-Champaign | ART empirical testing, nature-health mechanisms, dose-response in nature exposure |
| 2 | **Marc Berman** | Domain Expert | University of Chicago | Computational neuroscience of environmental perception, neural mechanisms of attention restoration |
| 3 | Rita Berto | Environmental Psychologist | University of Verona | Nature exposure and cognitive functioning, restorative environments |
| 4 | Marcus Hedblom | Methodologist | Swedish University of Agricultural Sciences | Multi-sensory environmental assessment, field experimental design |
| 5 | Danielle Shanahan | Information / Scope Expert | University of Queensland | Systematic review of nature-health evidence, population-level green space research |

## In-Criteria (Central Cases)

A paper is clearly relevant to SQ-001 if:

1. The study exposes human participants to natural versus urban or built environments, and measures a cognitive outcome that can be interpreted as directed attention or its close cognate (executive function, sustained attention, working memory under attentional load).
2. The study uses a controlled or quasi-experimental design where the environmental condition (natural vs. non-natural) is the independent variable or a primary predictor, not merely a covariate or demographic descriptor.
3. The study reports quantitative outcomes — effect sizes, significance tests, or descriptive statistics sufficient to evaluate whether nature exposure produced a measurable change in attentional performance.
4. Meta-analyses or systematic reviews that pool multiple studies of nature exposure and attention-related outcomes, even if individual studies within the pool vary in design quality.

## Out-Criteria (Clear Rejections)

A paper is clearly irrelevant to SQ-001 if:

1. The paper is about clinical ADHD treatment using nature as a therapeutic modality — this is a different research question (nature as medicine vs. nature as general restorative). Papers framed around "green prescriptions" or "nature-based therapy for ADHD" belong to a clinical intervention question, not this one.
2. The paper studies nature exposure but measures only stress biomarkers (cortisol, heart rate, blood pressure) or self-reported mood/affect with no attention or cognitive measure of any kind — these belong to SQ-004 (Stress Recovery Theory) instead.
3. The paper is a landscape preference or aesthetic judgment study where participants rate how much they like nature photographs — this is about environmental preference, not attentional performance.
4. The word "nature" appears in the title or abstract but refers to "the nature of X" (a common false friend) rather than to natural environments.
5. The paper is a textbook chapter, opinion piece, or editorial with no original data or systematic evidence synthesis.

## Hard Cases (Borderline Decisions)

1. **Nature + stress + no attention task**: A paper that exposes participants to nature, measures physiological stress recovery (cortisol, HRV) but also includes a brief cognitive measure that could be interpreted as attention-related (e.g., reaction time, digit span mentioned in passing). The question is whether the cognitive measure is substantive enough to count. *Tend toward: include if the attention measure is reported with effect sizes; exclude if it is mentioned only as a secondary outcome with no quantitative result.*

2. **Restoration language without attention measurement**: Papers that invoke "restorative environments" or "cognitive restoration" in the Kaplan framework but actually measure general well-being, relaxation, or positive affect rather than directed attention specifically. The ART literature uses "restoration" to mean attention recovery, but many authors use it loosely. *Tend toward: edge_case / escalate to LLM adjudicator.*

3. **Indirect attention measures**: Studies using reaction time tasks, Stroop-like interference tasks, or vigilance decrement tasks that are not standard ART attention measures (like the backward digit span or Attention Network Test) but plausibly tap directed attention. *Tend toward: include as direct evidence if the task has documented attention-loading; include as indirect if unclear.*

4. **Virtual nature studies**: Papers testing whether viewing nature images, videos, or VR nature scenes restores attention. These are topically relevant but test a different mechanism (digital vs. real nature). *Tend toward: include as direct evidence — the question asks about natural environments but the evidence base includes simulated nature, and this boundary is itself informative.*

5. **Review or theoretical papers**: A narrative review of ART that synthesizes existing evidence but adds no new data. *Tend toward: include as contextual relevance, not direct evidence.*

## False Friends

These terms or phrases appear to signal relevance but frequently lead to off-topic papers:

- **"nature of attention"** — refers to the character or structure of attention, not to natural environments
- **"natural attention"** — sometimes means spontaneous or involuntary attention in psycholinguistics, not nature-induced attention
- **"restorative justice"** — uses "restorative" in a legal/social context
- **"attention deficit"** / **"ADHD"** — clinical condition management, not general restoration
- **"environmental attention"** — sometimes refers to environmental monitoring or surveillance, not person-environment interaction

## Evidence Markers

A paper that actually tests ART will typically contain several of these in its methods section:

- Named attention tasks: backward digit span, Attention Network Test (ANT), Necker cube reversal, Stroop, SART, Trail Making Test
- "Pre-test / post-test" or "before/after walk" design
- Participant counts (N = ...) and random assignment language
- References to Kaplan (1989, 1995) or Berman et al. (2008, 2012)
- Phrases: "directed attention fatigue," "involuntary attention," "soft fascination," "cognitive restoration"

## Article Type Guidance

| Type | Verdict | Rationale |
|------|---------|-----------|
| `empirical_research` | **Accept** | Primary evidence source |
| `meta_analysis` | **Accept** | Pooled evidence directly addresses the question |
| `systematic_review` | **Accept** | Structured evidence synthesis |
| `narrative_review` | **Marginal** | Contextually useful but not direct evidence |
| `theoretical` | **Marginal** | May define constructs but adds no data |
| `case_study` | **Marginal** | Weak evidence unless methodologically strong |
| `qualitative_research` | **Marginal** | May illuminate mechanisms but not test the claim |
| `methods` | **Marginal** | Relevant only if validating attention measurement in nature contexts |
| `book_review` | **Reject** | No original evidence |
| `editorial` | **Reject** | No original evidence |
| `computational_simulation` | **Reject** | Not empirical human evidence |

## Escalation Triggers

The following cases MUST be escalated to a subscribed LLM adjudicator rather than resolved by keyword heuristics:

1. **Papers measuring "restoration" without specifying the outcome domain.** The word "restoration" in the nature-health literature is genuinely ambiguous between attention restoration (ART), stress recovery (SRT), and general well-being. A keyword filter cannot resolve this — it requires reading the methods section to determine which dependent variable was actually measured.

2. **Papers that study attention in outdoor settings but are not testing ART.** For example, a study measuring how noise affects concentration in an outdoor workspace uses nature and attention but is really about acoustic distraction, not the restorative quality of nature.

3. **Papers from adjacent fields (e.g., neuroarchitecture, biophilic design) that invoke ART as a theoretical framing but measure a different outcome.** A biophilic office study that cites Kaplan but measures productivity or absenteeism may or may not be relevant depending on whether "productivity" is operationalized through an attention measure.

## Unresolved Ambiguities

- Should studies of **indoor plants** (no outdoor nature exposure) count as "natural environments"? The biophilic design literature assumes yes, but classic ART testing typically involves outdoor walks. This boundary should be reviewed by a human panel.
- Should **exercise confound** studies be included? Some nature-walk studies confound nature exposure with physical exercise. Studies that attempt to control for this (e.g., treadmill vs. outdoor walk) are more informative, but should studies that don't control for exercise be excluded or just flagged?

## LLM Drafting Note

This constitution was drafted with LLM panel reasoning. The 5-member panel composition above reflects domain expertise (Kuo, Berman, Berto for ART), methodology (Hedblom), and information scope (Shanahan). The constitution should be promoted to `panel_reviewed` only after human expert feedback confirms the boundary decisions, especially around the restoration-ambiguity and indoor-plant questions.
