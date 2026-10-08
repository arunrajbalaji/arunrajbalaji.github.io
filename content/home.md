# Homepage — `/`

Final copy. Use the text exactly as written. Lines in *[brackets]* are notes for the build, not copy.

## Head

- **Title:** Raj Balaji-Wright | Simulation, numerical methods and scientific ML
- **Description:** Computational scientist building production simulation software for nonlinear, multi-scale systems with physics-based modeling and machine learning.

## 1. Hero

Name: Raj Balaji-Wright

Headline: From equations on paper to production code.

Subhead: I build simulation software for nonlinear, multi-scale systems, combining physics-based modeling, numerical methods and machine learning.

## 2. Now

I'm a Senior Modeler at Ark Biotech in Cambridge, MA, working on bioprocess simulation. I helped design and launch the first version of a real-time bioprocess digital twin: simulations that run alongside live experiments, compare against measured data, and retrain as they go. I'm now building a new simulation engine, alongside self-directed research that blends physics-based methods with machine learning.

Before Ark, I completed a Ph.D. in Mechanical Engineering at Stanford in 2024, developing models and solvers for electrochemical systems.

## 3. Selected work

*[Three work cards. Card one links to `/work/`; cards two and three link to their case studies.]*

### Card one *[generic schematic: a physics model and a machine-learning model coupled in one simulation that produces predictions; nothing company-specific]*

**Hybrid physics + machine learning simulation.** A hybrid simulation framework that combines machine learning with physics-based models, for predictions where data is sparse and the dynamics are highly nonlinear. I also led a refactor of the production engine's numerical core that improved robustness and cut run times from hours to minutes, opening it to optimization and sensitivity analysis. Now in progress: a fully auto-differentiable simulation engine.

Meta: Ark Biotech, 2025 to present.

### Card two *[full-cell figure; links to `/work/capacitive-deionization/`]*

**Simulating a whole cell without resolving every pore.** A model that treats nanometer-scale pores analytically, so the full centimeter-scale cell can be simulated over many charge cycles. It showed shock-like pH fronts moving through the electrodes and shaping where and when the anode corrodes.

Meta: Published in Desalination, 2024. *[link: https://doi.org/ — take the DOI from the Publications page for Desalination 587, 117924]*

### Card three *[current-voltage figure; links to `/work/electrodialysis/`]*

**A 1D model for a chaotic 3D flow.** Chaotic electroconvection near membranes normally demands unsteady 3D simulation. With velocity fields measured by collaborators at RWTH Aachen, we computed an eddy diffusivity that turns the problem into a steady 1D solve. Predicted current-voltage curves match experiment.

Meta: Published in Physical Review Fluids, 2024. *[link: https://doi.org/10.1103/PhysRevFluids.9.023701]*

## 4. How I work

Most of my projects follow one loop. I start from the physics and write the model down on paper. Before writing code, I look for structure that makes the problem cheaper: separated time scales, thin layers, small parameters. Then I design a numerical method for what remains, build software that other people can run, and test it against data.

*[Callout:]* At Stanford and at Ark, that loop has delivered 10 to 100-fold gains in simulation cost and robustness.

## 5. Proof row

Ph.D., Stanford, Kruger Graduate Fellow · B.S.E., Princeton · Stanford Centennial Teaching Assistant Award · 3 peer-reviewed papers and 12 presentations

## 6. Footer links

contact@rajbalajiwright.com · CV · LinkedIn · GitHub · Google Scholar
