# Case studies — `/work/<slug>/`

Each of the four pages keeps its existing sections, body text and figures from the current site (`/research/<slug>/` on rajbalajiwright.com), and gains a new title and a three-part lead: the problem, the modeling move, the result. Below the lead, port the body as it stands, apart from the edits listed.

Lines in *[brackets]* are notes for the build, not copy.

## On all four pages

- Drop the date ranges such as "Aug 2022 – Ongoing".
- Give every figure alt text and a one-line caption.
- Place each published figure on the `plate` backing (see `design/brand.md`, Figures).
- Equations render with self-hosted KaTeX, loaded only on pages that have equations.
- Head title: `<page title> | Raj Balaji-Wright`. Description: the first lead paragraph, shortened if needed.

---

## Capacitive deionization — `/work/capacitive-deionization/`

**Simulating a whole cell without resolving every pore**

Capacitive deionization cells lose performance as the anode slowly corrodes. Predicting that takes a full-cell simulation over many charge cycles, but the pores that store the ions are about a nanometer wide and the cell is about a centimeter across.

The pores respond much faster than the cell does. They can be treated as being in local equilibrium and solved on paper, which leaves only the cell-scale transport for the computer.

The reduced model spans seven orders of magnitude in length and runs whole cells over many cycles. It showed shock-like pH fronts moving through the electrodes, shaping where and when the anode corrodes.

Desalination 587, 117924 (2024). With J. Wu, A. N. Shocron, A. G. Dana and M. Suss at Technion, and A. Mani. *[link the citation to its DOI]*

Edits to the ported body:
- Change "MatLab" to "MATLAB".
- Where the page gives the cell's size as a thickness of O(1 mm), say the electrode is about 1 mm thick and the cell about 1 cm along the flow.

---

## Electrodialysis — `/work/electrodialysis/`

**A 1D model for a chaotic 3D flow**

Near an ion-selective membrane at high voltage, the electrolyte flow turns chaotic. That mixing sets how much current a cell can carry, and resolving it directly takes an unsteady 3D simulation.

Most uses need only the averaged concentration and potential. Averaging the equations leaves one unknown term, which we closed with an eddy diffusivity measured from 3D velocity fields recorded by collaborators at RWTH Aachen.

With that one measured profile, a steady 1D solve gives the mean fields directly. Its predicted current-voltage curve agrees with experiment.

[Phys. Rev. Fluids 9, 023701 (2024)](https://doi.org/10.1103/PhysRevFluids.9.023701). With F. Stockmeier, R. Dunkel and M. Wessling at RWTH Aachen, and A. Mani.

Edits to the ported body:
- Point the publication link at the DOI above, not the "accepted" address the current page uses.
- Correct the year of reference [1], Mani and Wang (Annual Review of Fluid Mechanics, vol. 52), from 2024 to 2020.

---

## CO2 electroreduction — `/work/co2-electro-reduction/`

**A 3D model of a two-phase catalyst, cheap enough to explore designs**

Copper catalysts turn CO2 into simple hydrocarbons, and mixing in water-repelling PTFE regions gives the gas a faster route to the reaction sites. The design space is large, and a simulation that resolves every pore in 3D is too expensive to search it.

Scaling arguments show which processes dominate. Keeping those and dropping the rest gives a medium-fidelity continuum model, and reshaping the geometry lets it run on a simple structured mesh, with the copper and PTFE regions coupled iteratively.

The model covers the catalyst microenvironment and the full device in 3D, at a cost that allows parameter sweeps. Validation against experiments for CO2 and CO reduction is in two papers in preparation.

With K. R. Disselkoen and M. Kanan in Stanford Chemistry, M. A. Khanwale, and A. Mani.

Code: [the MATLAB source, on GitHub](https://github.com/arunrajbalaji/3DCatalystModeling_public)

Edits to the ported body:
- Replace the sentence promising submission "in early to mid 2025" with "Validation results will be added here when the papers are published."

---

## Multi-layered cells — `/work/multi-layered-cell-simulation/`

**One solver for any stack of electrochemical layers**

Many electrochemical cells are stacks of layers: membranes, electrodes and the electrolyte between them. Each new arrangement usually means writing a new simulation.

This solver takes a cell as a list of layers in an input file, each with its own geometry, transport properties and chemistry. The mesh refines exponentially toward each interface and the time step adapts, so thin reaction zones and long runs to steady state are both affordable.

A researcher can set up a new cell without writing code. Its first use is a study of proton shuttling in forward-biased bipolar membranes, with a paper in preparation.

With J. Toh and Y. Surendranath in MIT Chemistry, and A. Mani.

Code: [the MATLAB source, on GitHub](https://github.com/arunrajbalaji/multiLayerSimulation_public)

Edits to the ported body:
- Replace the sentence promising submission "in mid to late 2025" with "Results will be added here when the paper is published."
