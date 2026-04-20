# Panel Dossier: SQ-019

## Question

What epidemiological evidence links residential proximity to urban green spaces with better mental health outcomes?

## Topic / Subtopic

Urban Green Space / Mental health

## Status

`llm_panel_drafted`

## Panel Composition

| # | Name | Role | Affiliation | Expertise |
|---|------|------|-------------|-----------|
| 1 | **Mathew White** | Domain Lead | University of Vienna / University of Exeter | BlueHealth, green/blue space epidemiology, nature and wellbeing dose-response |
| 2 | **Marissa Astell-Burt** | Population Health Expert | University of Wollongong | Longitudinal green space-mental health studies, 45 and Up cohort, physical activity mediation |
| 3 | Payam Dadvand | Environmental Epidemiologist | ISGlobal Barcelona | Green space exposure measurement (NDVI), children's green space and neurodevelopment |
| 4 | Kathleen Wolf | Urban Forestry Expert | University of Washington | Urban tree canopy and health outcomes, green infrastructure economic valuation |
| 5 | Daniel Nutsford | GIS/Exposure Assessment Expert | University of Auckland | Spatial analysis of green space access, anxiety/mood disorder treatment rates and greenness |

## In-Criteria (Central Cases)

1. The study uses an epidemiological design (cross-sectional, cohort, or ecological) to test the association between residential green space proximity/quantity (NDVI, land use classification, park access distance) and mental health outcomes (depression, anxiety, psychological distress, wellbeing scores) at the population level.
2. The study controls for key confounders (SES, age, education, physical activity, social capital) to estimate an independent green space–mental health association.
3. Longitudinal or natural-experiment studies measuring mental health before and after green space changes (park creation, tree planting, urban greening programs).
4. Meta-analyses or systematic reviews pooling epidemiological green-space–mental-health evidence.

## Out-Criteria (Clear Rejections)

1. Papers about experimental nature exposure in small samples (lab studies, field experiments). These belong to SQ-001 or SQ-004.
2. Papers about green space and physical health only (cardiovascular, obesity, mortality) without mental health outcomes.
3. Papers about urban planning or green infrastructure focused on ecosystem services (stormwater, heat island, biodiversity) without health outcomes.
4. Papers about agricultural greenness or rural living that do not study urban populations.

## Hard Cases (Borderline Decisions)

1. **Physical activity as mediator studies**: Studies testing whether the green-space–mental-health link is explained by physical activity (people near parks exercise more). *Tend toward: include — mediation analysis directly addresses the mechanism question and is central to the evidence base.*

2. **Blue space (coastal, rivers, lakes) studies**: Water features in cities and mental health. *Tend toward: include if the study measures green and blue space simultaneously or if urban blue space is combined with green infrastructure. Pure blue-space studies are SQ-024 territory.*

3. **Air quality and noise mediation**: Studies proposing that green spaces improve mental health by filtering air pollution or buffering noise rather than through direct psychological restoration. *Tend toward: include — these are competing/complementary mechanisms within the same association.*

4. **Neighborhood-level studies with no individual mental health measurement**: Ecological studies using area-level prescribing rates for antidepressants as a mental health proxy. *Tend toward: include with caution — ecological fallacy concerns are real but these studies contribute population-level evidence.*

5. **Green space quality studies**: Studies distinguishing well-maintained parks from neglected vacant lots. Quality, not just quantity, may drive the association. *Tend toward: include — these refine the exposure measure.*

## False Friends

- **"Green space"** in computing — available memory/storage
- **"Mental health"** in workplace contexts — occupational wellness programs without green space
- **"Urban green"** — sustainable/environmental branding without health research
- **"Proximity"** in social psychology — interpersonal closeness
- **"Residential"** in electrical engineering — residential circuits

## Evidence Markers

- NDVI (Normalized Difference Vegetation Index) as exposure measure
- GIS-derived green space within specified buffer (300m, 500m, 1km)
- Mental health instruments: GHQ-12, K10, PHQ-9, WEMWBS, SF-36 MCS
- Population size: N > 500 typical for epidemiological studies
- Adjustment for confounders listed: income, education, urbanicity, age, sex
- References to White et al. (2013, 2019), Astell-Burt et al. (2013, 2019), Gascon et al. (2015)

## Article Type Guidance

| Type | Verdict | Rationale |
|------|---------|-----------|
| `empirical_research` | **Accept** | Population-level epidemiological studies |
| `meta_analysis` | **Accept** | Pooled epidemiological evidence |
| `systematic_review` | **Accept** | Evidence mapping |
| `narrative_review` | **Marginal** | Green space and health overviews |
| `ecological study` | **Accept** | Area-level analyses |

## Escalation Triggers

The following cases MUST be escalated to a subscribed LLM adjudicator rather than resolved by keyword heuristics:

1. **Mendelian randomization or natural experiment studies** providing stronger causal evidence than cross-sectional associations. The adjudicator must assess the validity of the instrument (for MR) or the exogeneity of the natural experiment, and flag these as epistemically powerful upgrades over standard observational evidence.

2. **Studies finding null associations after controlling for self-selection** — healthier, wealthier people may choose to live near green space. The adjudicator must determine whether the self-selection control is methodologically credible (e.g., propensity score matching, instrumental variable, longitudinal move-in design) and report whether the green-space coefficient changes substantially after adjustment.

3. **Studies in low- and middle-income countries** where green space access, SES patterns, and mental health profiles differ substantially from European/North American settings. The adjudicator must flag these for their generalizability value and note any differences in green-space measurement (NDVI calibration differs by climate zone).

## Unresolved Ambiguities

- Causation vs. selection: do green spaces improve mental health, or do mentally healthier people move to greener areas? Few studies have strong causal designs.
- Exposure measurement: NDVI captures greenness but not accessibility, safety, or quality. Satellite-derived greenness may misrepresent human-experienced green space.

## LLM Drafting Note

This constitution was drafted with LLM panel reasoning. SQ-019 has the largest expected evidence base of any question in the bank — hundreds of epidemiological studies exist. The main challenge is that most are cross-sectional and cannot establish causation. The constitution prioritizes longitudinal, natural-experiment, and mediation designs alongside the broader cross-sectional evidence.
