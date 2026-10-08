# Work — `/work/`

Final copy. Use the text exactly as written. Lines in *[brackets]* are notes for the build, not copy.

## Head

- **Title:** Work | Raj Balaji-Wright
- **Description:** Hybrid physics and machine learning simulation, and reduced models that make multi-scale systems cheap to simulate.

## Page opening

Heading: Work

Lede: I build models and solvers for nonlinear, multi-scale systems. The work below is grouped by method: hybrid physics and machine learning first, then reduced models that make multi-scale problems cheap enough to solve.

## 01 / Hybrid physics and machine learning

Meta line above both cards: Ark Biotech, Cambridge, MA. Modeler from 2025, Senior Modeler from 2026.

*[Two cards. Neither links to a case study. No note about what the page leaves out.]*

### Card one *[the same generic schematic as homepage card one]*

**Solvers for hybrid physics and machine learning models**

I joined Ark Biotech in April 2025 to work on bioprocess simulation. My first project was a hybrid simulation framework that combines machine learning with physics-based models. The combination gives accurate predictions where data is sparse and the dynamics are highly nonlinear.

I then led a refactor of the production engine's numerical core. It improved robustness and cut run times from hours to minutes.

I'm now building a fully auto-differentiable simulation engine to improve speed, robustness and extensibility, alongside self-directed research that blends physics-based methods with machine learning.

### Card two *[new generic schematic: a simulation running beside a live experiment, exchanging measured data and updated predictions]*

**Simulation that guides experiments**

Once the engine was fast and robust, it could do more than single runs: optimization, sensitivity analysis and model-based design of experiments.

As Senior Modeler, I helped design and launch the first version of a real-time bioprocess digital twin. Simulations run alongside live experiments, compare against measured data and retrain continuously, so a process can be adjusted while it runs.

## 02 / Reduced models for multi-scale systems

*[Four work cards: figure, title, one sentence and the reference. Each links to its case study.]*

1. **Simulating a whole cell without resolving every pore.** Full-cell simulations of capacitive deionization over many charge cycles, with nanometer pores handled analytically. — Desalination 587, 117924 (2024) → `/work/capacitive-deionization/`
2. **A 1D model for a chaotic 3D flow.** An eddy diffusivity measured from experiment turns chaotic electroconvection into a steady 1D problem. — Phys. Rev. Fluids 9, 023701 (2024) → `/work/electrodialysis/`
3. **A 3D model of a two-phase catalyst, cheap enough to explore designs.** A reduced model of CO2 electroreduction catalysts in which gas and liquid pathways are intermixed. — Papers in preparation → `/work/co2-electro-reduction/`
4. **One solver for any stack of electrochemical layers.** A general 1D simulation platform in which each layer of a cell is described in an input file. — Paper in preparation → `/work/multi-layered-cell-simulation/`
