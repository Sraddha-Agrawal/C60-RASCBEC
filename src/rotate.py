"""
Title: POSCAR Rotation Script
Author: Rui Zhang
Date: 11/06/2024
License: MIT License

Description:
This script reads a VASP POSCAR file, applies rotations along the x, y, and z axes to the lattice vectors 
and atomic positions, and saves the rotated structures to new POSCAR files (ex.POSCAR.vasp, ey.POSCAR.vasp, ez.POSCAR.vasp).

Dependencies:
- numpy

Usage:
- Place this script in the same directory as your POSCAR file.
- Run the script using the command: python rotate.py
- The script will output three new files with rotated lattice and atomic positions for each axis.

Output:
- ex.POSCAR.vasp : POSCAR rotated along the x-axis
- ey.POSCAR.vasp : POSCAR rotated along the y-axis
- ez.POSCAR.vasp : POSCAR rotated along the z-axis
"""


import numpy as np

# Define rotation matrices for rotations along x, y, and z directions
rotation_x = np.array([[1/np.sqrt(2), -1/np.sqrt(2), 0], [1/np.sqrt(2), 1/np.sqrt(2), 0], [0, 0, 1]])
rotation_y = np.array([[1, 0, 0], [0, 1/np.sqrt(2), -1/np.sqrt(2)], [0, 1/np.sqrt(2), 1/np.sqrt(2)]])
rotation_z = np.array([[1/np.sqrt(2), 0, 1/np.sqrt(2)], [0, 1, 0], [-1/np.sqrt(2), 0, 1/np.sqrt(2)]])

# Function to read lattice vectors and atomic positions from POSCAR file
def read_poscar(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Read lattice vectors (lines 2-4)
    lattice_vectors = np.array([list(map(float, lines[i].split())) for i in range(2, 5)])

    # Determine number of atoms from atom counts on line 6
    atom_counts = list(map(int, lines[6].split()))
    total_atoms = sum(atom_counts)

    # Read atomic positions (line 9 onward, depending on total_atoms count)
    atomic_positions = np.array([list(map(float, lines[8 + i].split()[:3])) for i in range(total_atoms)])

    return lines, lattice_vectors, atomic_positions

# Function to write rotated lattice vectors and atomic positions to new POSCAR file
def write_poscar(filename, lines, lattice_vectors, atomic_positions):
    with open(filename, 'w') as f:
        f.writelines(lines[:2])  # Copy header lines
        # Write rotated lattice vectors
        for vec in lattice_vectors:
            f.write(f"{' '.join(map(str, vec))}\n")
        f.writelines(lines[5:8])  # Copy atom type, count, and "Direct" line
        # Write rotated atomic positions
        for pos in atomic_positions:
            f.write(f"{' '.join(map(str, pos))}\n")

# Main function to perform rotations and save new POSCAR files
def main():
    # Load original POSCAR data
    lines, lattice_vectors, atomic_positions = read_poscar('POSCAR')

    # Apply x-direction rotation
    lattice_rotated_x = rotation_x @ lattice_vectors
    #atomic_rotated_x = atomic_positions @ rotation_x.T
    write_poscar('ex.POSCAR.vasp', lines, lattice_rotated_x, atomic_positions)

    # Apply y-direction rotation
    lattice_rotated_y = rotation_y @ lattice_vectors
    #atomic_rotated_y = atomic_positions @ rotation_y.T
    write_poscar('ey.POSCAR.vasp', lines, lattice_rotated_y, atomic_positions)

    # Apply z-direction rotation
    lattice_rotated_z = rotation_z @ lattice_vectors
    #atomic_rotated_z = atomic_positions @ rotation_z.T
    write_poscar('ez.POSCAR.vasp', lines, lattice_rotated_z, atomic_positions)

    print("Rotation complete. New POSCAR files saved as ex.POSCAR.vasp, ey.POSCAR.vasp, and ez.POSCAR.vasp.")

# Execute the main function
if __name__ == "__main__":
    main()

