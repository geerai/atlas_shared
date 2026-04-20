# Panel Dossier: SQ-011

## Question

Is the stress-reducing effect of fractal patterns explained by fractal self-similarity per se, or by spatial frequency and luminance contrast?

## Topic / Subtopic

Fractal Patterns / Mechanism dispute

## Status

`llm_panel_drafted`

## Panel Composition

| # | Name | Role | Affiliation | Expertise |
|---|------|------|-------------|-----------|
| 1 | **Branka Spehar** | Domain Lead | University of New South Wales | 1/f noise, fractal and non-fractal visual complexity, aesthetic preference; has published both with and against Taylor's fractal fluency account |
| 2 | **Richard Taylor** | Domain Expert (Advocate) | University of Oregon | Fractal fluency theory originator, fractal dimension measurement, stress reduction through fractals |
| 3 | Christoph Redies | Counter-Position Expert | University of Jena | Edge-orientation entropy (EOE) as alternative predictor of aesthetic preference, statistical image properties |
| 4 | Daniel Graham | Spatial Frequency Expert | Hobart and William Smith Colleges | Natural scene statistics, spatial frequency and contrast distributions, efficient coding hypothesis |
| 5 | Anjan Chatterjee | Neuroaesthetics Methodologist | University of Pennsylvania | Neural correlates of visual preference, neuroaesthetics methods, disentangling perceptual confounds |

## In-Criteria (Central Cases)

1. The study directly tests whether fractal self-similarity (scale-invariant repeating structure) is the operative feature driving stress reduction or aesthetic preference, as against spatial frequency distribution (1/f slope), luminance contrast, or edge-orientation statistics.
2. The study uses stimuli that decouple fractal dimension from spatial frequency — e.g., stimuli matched on 1/f slope but differing in self-similarity, or stimuli matched on fractal dimension but varying in contrast.
3. The study provides a formal comparison between fractal dimension and an alternative image statistic (1/f exponent, EOE, Fourier slope, RMS contrast) as predictors of the same response variable.
4. The study uses neuroimaging (fMRI, EEG) to identify which image property (fractal structure vs. spectral content) is the better predictor of neural responses associated with aesthetic preference or stress modulation.

## Out-Criteria (Clear Rejections)

1. Papers measuring only fractal dimension and preference without testing any competing predictor. These belong to SQ-010.
2. Papers about spatial frequency and contrast sensitivity in basic vision science with no connection to aesthetic preference, stress, or environmental perception.
3. Papers about fractals in mathematics, physics, or computer science with no perceptual or psychological component.
4. Papers about image compression or signal processing using fractal techniques as engineering tools.

## Hard Cases (Borderline Decisions)

1. **1/f noise studies without explicit fractal framing**: Research showing that images with 1/f amplitude spectra are preferred, without computing fractal dimension. 1/f spectra are closely related to mid-range fractal dimension, but the relationship is not exact. *Tend toward: include if the paper discusses the perceptual or aesthetic consequence of 1/f spectra, because this is the spatial-frequency side of the mechanism debate.*

2. **EOE (edge-orientation entropy) studies**: Redies and colleagues propose that edge-orientation entropy, not fractal dimension, predicts aesthetic preference. These papers may not mention "fractal" at all. *Tend toward: include — they are the primary alternative account and directly address the mechanism question.*

3. **Natural scene statistics studies**: Papers analyzing the statistical regularities of natural images (Field 1987, Simoncelli & Olshausen) without connection to aesthetics or stress. *Tend toward: edge case — include only if the paper connects scene statistics to perceptual processing ease or affective response.*

4. **Fractal architecture or design studies**: Papers applying fractal design principles to buildings but not testing the mechanism (is it the fractality or the complexity or the familiarity?). *Tend toward: edge case if mechanism is discussed; reject if fractal label is used without mechanistic analysis.*

5. **Phase-scrambled vs. intact image studies**: Studies comparing responses to images with preserved amplitude spectra but randomized phase (destroying structure while maintaining spatial frequency). These cleanly separate spectral from structural contributions. *Tend toward: definitely include — this is the key experimental paradigm for the mechanism question.*

## False Friends

- **"Fractal analysis"** in materials science — surface roughness measurement, not psychophysiology
- **"Self-similar"** in network science — scale-free graphs, not visual patterns
- **"Spatial frequency"** in audio processing — spectral analysis of sounds, not images
- **"Contrast sensitivity"** in clinical ophthalmology — visual acuity testing, not aesthetic preference
- **"Luminance"** in lighting engineering — illumination design, not image statistics

## Evidence Markers

- Phase-scrambled / phase-randomized stimuli
- 1/f slope, spectral exponent, beta exponent
- Edge-orientation entropy (EOE), edge-orientation histogram
- Fractal dimension (D, D_f) vs. spectral slope comparison
- Computational image analysis: Fourier transform, box-counting
- References to Spehar, Redies, Graham, Taylor, Field
- Regression or mediation analyses comparing predictors

## Article Type Guidance

| Type | Verdict | Rationale |
|------|---------|-----------|
| `empirical_research` | **Accept** | Experimental tests comparing fractal vs. non-fractal predictors |
| `meta_analysis` | **Accept** | Pooled evidence on competing predictors |
| `systematic_review` | **Accept** | Evidence mapping of the mechanism debate |
| `theoretical` | **Marginal** | Computational models of visual processing and fractals |
| `methods` | **Marginal** | Stimulus generation and fractal measurement validation |
| `narrative_review` | **Marginal** | Overviews of the fractal aesthetics debate |

## Escalation Triggers

The following cases MUST be escalated to a subscribed LLM adjudicator rather than resolved by keyword heuristics:

1. **Papers using deep neural network (DNN) features to predict aesthetic preference.** Modern computational aesthetics may subsume both fractal dimension and spatial frequency within learned feature hierarchies. The adjudicator must accept if the paper explicitly compares DNN features against fractal/spectral predictors; reject if the DNN analysis does not reference the fractal-vs-spectral debate.

2. **Papers measuring physiological responses (EEG alpha, skin conductance) to fractal stimuli without presenting a mechanism comparison.** The data may be informative, but without a formal fractal-vs-spectral comparison, the paper does not directly address SQ-011. The adjudicator must classify as edge case and flag for human review.

3. **Papers from the natural scene statistics tradition** that establish baseline spectral regularities (1/f amplitude spectra) in outdoor environments without testing preference or stress. The adjudicator must determine whether the paper provides sufficient methodological foundation for the mechanism question to warrant inclusion as contextual evidence.

## Unresolved Ambiguities

- Fractal dimension and 1/f slope are mathematically related but not identical. A study can vary one while holding the other approximately constant, but perfect decoupling is impossible for natural images. This measurement reality limits how cleanly the mechanism question can be resolved.
- It is possible that fractal self-similarity AND spatial frequency slope both contribute independently — the question assumes they are competing explanations, but they may be synergistic.

## LLM Drafting Note

This constitution was drafted with LLM panel reasoning. SQ-011 is the mechanism companion to SQ-010's empirical finding. The key challenge is that many studies in this space compute fractal dimension without testing alternatives, or compute spectral slopes without testing fractals. The constitution deliberately includes the EOE tradition (Redies) and the natural scene statistics tradition (Graham, Field) as primary comparison accounts, even though these researchers may not use "fractal" in their abstracts.
