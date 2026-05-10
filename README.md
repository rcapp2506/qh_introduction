# qh_introduction

Generator scripts for the figures of the **Introduction chapter** (Cap. 1)
of Roberto Cappuccio's PhD thesis,
*New Perspectives on Quantum Technologies: Progress on Quantum Sensing
and Quantum Computation* (Università di Siena, Ciclo XXXVII).

This repository sits alongside the three thesis-content code repositories
([`qh_hardware`](https://github.com/rcapp2506/qh_hardware),
[`qh_algorithms`](https://github.com/rcapp2506/qh_algorithms),
[`qh_sensing`](https://github.com/rcapp2506/qh_sensing))
and hosts only those figures that belong to the Introduction and have no
content-chapter counterpart.

The corresponding LaTeX source is in
[`PhDThesis`](https://github.com/rcapp2506/PhDThesis), under
`chapters/introduction_revised.tex`. Generated PNGs are committed to
`PhDThesis/chapters/in_figures/` so that the manuscript builds without a
dependency on this repository.

## Contents

| Script | Output | LaTeX label |
|---|---|---|
| `two_quantum_revolutions_diagram.py` | `two_quantum_revolutions_improved_2.png` | `fig:revolutions` |

## Reproducing the figures

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python two_quantum_revolutions_diagram.py
```

Each script writes its output PNG into the current working directory.
To refresh the asset in the thesis source, copy it into
`PhDThesis/chapters/in_figures/`.

## Tested with

- Python 3.14
- matplotlib 3.x
- numpy 2.x
- Pillow (only required to verify output dimensions)

## Sources adapted

The Two Quantum Revolutions diagram adapts the framing of:

- J. P. Dowling and G. J. Milburn, *Phil. Trans. R. Soc. A* **361**, 1655 (2003).
- I. H. Deutsch, *PRX Quantum* **1**, 020101 (2020).

The figure caption in the thesis credits both papers verbatim.

## License

The code in this repository is released under the MIT License (see
`LICENSE`). Figures derived from third-party works are reproduced under
fair-use scholarly attribution and must not be redistributed outside the
context of the thesis without independent permission from the original
publishers.
