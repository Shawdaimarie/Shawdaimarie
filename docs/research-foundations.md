# Research foundations and engineering relevance

Reviewed November 6, 2026. This map separates published research from portfolio implementation evidence. It does not claim institutional affiliation, course completion, a degree, postdoctoral training, or equivalent research achievement. University rankings vary by subject, publisher, and year; no universal “top four” is asserted.

## AI and software engineering

| Source | What the research addresses | Engineering connection and limit |
|---|---|---|
| [MIT ABxLab](https://abxlab.media.mit.edu/) | Controlled changes to ordering, prices, ratings, and persuasive cues can affect agent choices. | Motivates controlled perturbations and explicit behavioral measurements. The portfolio does not reproduce ABxLab experiments or demonstrate universal agent reliability. |
| [Caltech-led LeanDojo](https://arxiv.org/abs/2306.15626) | Connects language-model theorem proving to Lean's executable proof environment. | Highlights the importance of machine-checkable feedback. Python unit tests in these repositories are not formal proofs or an implementation of LeanDojo. |
| [Stanford CRFM: HELM](https://crfm.stanford.edu/2022/11/17/helm.html) | Evaluates language models across scenarios and multiple dimensions, with transparent reporting. | Supports reporting evaluation scope and missing measurements. A small synthetic regression corpus is not a general model-capability benchmark. |
| [CMU-led WebArena](https://webarena.dev/og/) | Evaluates agents carrying out tasks in interactive website environments using outcome-state checks. | Connects task success to observable results. The portfolio's offline fixtures do not establish WebArena performance or live-agent success. |

These are methodological connections, not claims that the cited research originated the existing implementations.

## Neuroscience and physics

### MIT: neural dynamics and sequence modeling

[MIT EECS: Novel AI model inspired by neural dynamics from the brain](https://www.eecs.mit.edu/novel-ai-model-inspired-by-neural-dynamics-from-the-brain) describes **linear oscillatory state-space models (LinOSS)**. The model draws on forced harmonic oscillators and neural oscillations to model long sequences.

This is a specific connection between dynamical systems, physics, and neuroscience-inspired machine learning. It is not evidence that all neural networks reproduce biological cognition. No LinOSS implementation or result is claimed in this portfolio.

### Caltech: physics-informed neural operators

[Li et al., Physics-Informed Neural Operator for Learning Partial Differential Equations](https://authors.library.caltech.edu/records/06m4r-8jf10), published in 2024, combines training data and partial differential equation constraints to learn solution operators for families of PDEs.

This illustrates how physical knowledge can enter a learning objective and how model behavior can be assessed against mathematical constraints. It does not establish that ordinary software tests enforce physical laws, or that the portfolio implements a scientific simulator. No PINO reproduction is claimed here.

## Evidence standard for future work

A future implementation should identify its research question, exact source, dataset, baseline, environment, acceptance criteria, and known limits. Report independently held-out tests separately from development fixtures. Separate numerical accuracy, computational cost, and task success. Publish a reproduction claim only after running and documenting the relevant experiment.

Current implementation evidence remains in [Sentinel](https://github.com/Shawdaimarie/sentinel#reviewer-path), [EDS Assurance](https://github.com/Shawdaimarie/eds-assurance), and [Agent Trace Fixtures](https://github.com/Shawdaimarie/agent-trace-fixtures). University research provides context, not validation of those projects or of individual proficiency.
