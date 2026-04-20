# Panel Dossier: SQ-013

## Question

Do virtual or simulated nature views (screens, VR, projected scenes) produce restorative effects comparable to real windows onto nature?

## Topic / Subtopic

Views of Nature / Virtual nature

## Status

`llm_panel_drafted`

## Panel Composition

| # | Name | Role | Affiliation | Expertise |
|---|------|------|-------------|-----------|
| 1 | **Mathew White** | Domain Lead | University of Vienna / University of Exeter | BlueHealth project, virtual nature and wellbeing, nature dose-response |
| 2 | **Peter Aspinall** | Environmental Perception Expert | Edinburgh Napier University | Mobile EEG in urban environments, VR nature exposure, psychophysiology |
| 3 | Andrea Stevenson Won | VR Experience Expert | Cornell University | VR immersion and wellbeing, virtual embodiment, presence measurement |
| 4 | Chanuki Seresinhe | Computational Scenicness Expert | University of Warwick | Scenic beauty prediction, nature content quantification, visual analysis |
| 5 | Donna Coffin | Clinical Integration Expert | Mayo Clinic | Nature imagery in clinical settings, patient experience, screen-based interventions |

## In-Criteria (Central Cases)

1. The study compares restorative outcomes (stress, attention, mood, preference, physiological) between virtual/simulated nature (video, photographs, VR, projected images, digital screens) and real nature exposure or real window views.
2. The study compares virtual nature to a non-nature control (blank screen, urban video, no screen) to establish whether simulated nature provides any restorative benefit at all.
3. The study tests dose-response relationships with virtual nature — duration, resolution, screen size, immersion level, or content fidelity — and their effect on restorative outcomes.
4. Meta-analyses or systematic reviews comparing effect sizes of virtual vs. real nature exposure across multiple studies.

## Out-Criteria (Clear Rejections)

1. Papers about VR technology development, rendering algorithms, or display hardware without psychological outcomes.
2. Papers about VR for exposure therapy (phobias, PTSD) using natural scenes as clinical tools, not as restorative environments.
3. Papers about real nature exposure only with no simulated/virtual condition. These belong to SQ-001 or SQ-004.
4. Papers about virtual environments for purposes unrelated to nature (virtual classrooms, VR gaming, telework).

## Hard Cases (Borderline Decisions)

1. **Nature photographs in laboratory settings**: Nearly all ART/SRT laboratory studies use photographs or videos of nature as stimuli. These are technically "simulated nature" but are not usually framed as a virtual-vs-real comparison. *Tend toward: include only if the study explicitly addresses the question of whether the photograph/video achieves effects comparable to real exposure. If photos are merely the stimulus delivery method, the paper belongs to SQ-001.*

2. **Augmented reality nature overlays**: AR systems that overlay nature imagery onto built environment views through smart glasses or screens. *Tend toward: include — this is a genuinely novel form of simulated nature with design implications.*

3. **Window-substitute screens**: Commercially available "virtual windows" (e.g., Atmoph, Sky Factory) displaying nature video in windowless rooms. Applied studies testing these products. *Tend toward: include — directly addresses SQ-013's practical question.*

4. **Sound-augmented virtual nature**: VR nature environments with spatial audio (birdsong, water sounds). Studies may find stronger effects from the multimodal combination than from vision alone. *Tend toward: include — the multimodal question is practically important, but flag that the visual component is not isolated.*

5. **360-degree nature video without head tracking**: Panoramic nature videos viewed on flat screens or in non-tracked headsets. These provide more immersion than photos but less than full VR. *Tend toward: include — immersion fidelity is itself a research variable.*

## False Friends

- **"Virtual environment"** in computational ecology — simulated ecosystems, not human perception
- **"Simulated nature"** in evolutionary biology — agent-based natural selection models
- **"Nature view"** as philosophical term — naturalistic worldview
- **"Screen time"** in pediatric health — sedentary behavior, not therapeutic nature content

## Evidence Markers

- VR headset model specification (Oculus, HTC Vive, etc.)
- Screen size, resolution, viewing distance
- Immersion measures: presence questionnaires (IPQ, SUS, PQ)
- Nature content description (forest, ocean, garden, landscape)
- Direct comparison: real vs. virtual (same scene or equivalent)
- Classic questionnaires: PRS, ROS, SVS, POMS, STAI
- References to Valtchanov & Ellard (2015), White et al. (2018), Browning et al. (2020)

## Article Type Guidance

| Type | Verdict | Rationale |
|------|---------|-----------|
| `empirical_research` | **Accept** | Experimental comparisons of virtual vs. real nature |
| `meta_analysis` | **Accept** | Pooled effect sizes across delivery modalities |
| `systematic_review` | **Accept** | Evidence mapping |
| `methods` | **Marginal** | VR nature stimulus development and validation |
| `narrative_review` | **Marginal** | Technology-in-healthcare reviews |
| `case_study` | **Marginal** | Single-site installation evaluations |

## Escalation Triggers

The following cases MUST be escalated to a subscribed LLM adjudicator rather than resolved by keyword heuristics:

1. **Studies using nature photographs in lab settings without VR or screen-substitute framing.** Most ART and SRT laboratory studies use projected nature images — these are technically "simulated nature" but are rarely framed that way. The adjudicator must determine whether the study is testing the simulation medium (relevant to SQ-013) or using photographs merely as a convenient proxy for nature exposure (relevant to SQ-001/SQ-004 instead).

2. **Papers identifying specific fidelity thresholds** — e.g., "below 4K resolution, no restorative benefit; above 4K, effects are comparable to real nature." The adjudicator must flag these for their practical design value and ensure the threshold claim is supported by dose-response data, not a single comparison.

3. **Augmented reality nature overlays on real indoor environments.** AR blends real and virtual in a way that challenges the binary real-vs-simulated framing. The adjudicator must classify these as a distinct modality and assess whether the study contributes to the "comparable to real?" question or introduces a third category. These critiques are relevant to the broader question of whether simulated nature is an adequate substitute.

## Unresolved Ambiguities

- Is the comparison between simulated and real nature about *fidelity* (does the simulation look real enough?) or about *presence* (does the person feel they are in nature?)?
- Virtual nature studies confound the modality (screen/headset) with the content (nature). The real-vs-virtual comparison never holds the delivery method constant.
- Longitudinal effects are almost entirely unstudied — does virtual nature exposure habituate faster than real nature exposure?

## LLM Drafting Note

This constitution was drafted with LLM panel reasoning. SQ-013 is rapidly growing due to the COVID-era surge of VR-in-healthcare research. The main challenge is the enormous variety of "virtual nature" implementations — from a small tablet showing a photograph to a full-immersion VR forest with spatial audio. The constitution avoids assuming that all virtual modalities are equivalent.
