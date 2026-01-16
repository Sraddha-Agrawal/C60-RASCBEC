# C60-RASCBEC

Raman activity calculation using finite-field Born effective charge (BEC) derivatives
from VASP and phonon eigenvectors from Phonopy.

This repository contains a minimal post-processing workflow demonstrated for C60.
The implementation follows the same core methodology as the original RASCBEC code,
reorganized into a simple notebook-based structure.

---

## Acknowledgement

The methodology and original implementation ideas for Raman activity calculations
based on BEC derivatives are due to the authors of the RASCBEC code. This repository
is a modified, system-specific adaptation of that approach using Phonopy eigenvectors.

---

## Repository Structure

```
C60-RASCBEC/
├── notebooks/
│   ├── 01_compute_raman_activity.ipynb
├── src/
│   └── copy_bec_runs.py
├── data/
│   ├── bec_runs/              # finite-field BEC runs (OUTCAR only)
│   ├── phonopy/               # phonopy inputs and outputs
│   │   ├── POSCAR             # reference structure used for phonopy
│   │   ├── freqs_phonopy.dat
│   │   └── eigvecs_phonopy.dat
│   └── processed/             # generated Raman activity tables
└── plots/
```

---

## Required Data

### 1) Reference structure (Phonopy)

The file

```
data/phonopy/POSCAR
```

defines the **reference structure** used for the phonopy calculation.
This structure sets the atom ordering and degrees of freedom for the
phonon eigenvectors.

All finite-field BEC calculations must be consistent with this structure
(same atom ordering and cell, up to numerical precision).

---

### 2) Phonopy outputs

Place the following files in `data/phonopy/`:

- `freqs_phonopy.dat`  
  phonon frequencies

- `eigvecs_phonopy.dat`  
  phonon eigenvectors corresponding to the reference POSCAR

---

### 3) Finite-field BEC calculations (OUTCAR only)

Raman activity calculations use **Born effective charge tensors** extracted
directly from VASP `OUTCAR` files. Since `OUTCAR` already contains the full
structural information, separate `INCAR` and per-run `POSCAR` files are not required.

Each finite-field calculation is therefore represented by a single `OUTCAR`.

```
data/bec_runs/
  E0.05/
    1/OUTCAR   m1/OUTCAR
    x/OUTCAR   mx/OUTCAR
    y/OUTCAR   my/OUTCAR
    z/OUTCAR   mz/OUTCAR
  E0.1/
    (same layout)
```

Label meaning:

| Label | Description |
|------:|-------------|
| x / mx | +E / −E along x |
| y / my | +E / −E along y |
| z / mz | +E / −E along z |
| 1 / m1 | reference pair (along x,y,z) |

---

## Notebooks

### 01_compute_raman_activity.ipynb

- Parses BEC tensors from OUTCAR files
- Computes central finite-difference derivatives
- Projects derivatives onto phonon eigenvectors
- Evaluates Raman activity for E0.05 and E0.1

Outputs are written to `data/processed/`.

---

Figures are written to `plots/`.

---

## Generating rotated POSCAR files for x/mx; y/my; z/mz pairs using rotate.py (rotate.py is in src folder)

---

## Notes

- This repository is intended for analysis and post-processing.
- All finite-field calculations must be structurally consistent with the
  reference phonopy POSCAR.
