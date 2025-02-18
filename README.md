# Quantum Espresso Utils

Here I will be adding tools for Quantum Espresso calculations.

The first one is the pwo2cif-xyz.py, this one will read a Quantum Espresso output and convert it to xyz and cif files.<br>
Three files are writen:
- trajectory.xyz: A xyz trajectory with the coordinates for all the relaxation process.
- initial.xyz: The initial coordinates for the calculation.
- relaxed.xyz: The coordinates for the relaxation process.
- relaxed.cif: A cif file with the relaxed coordinates.
Usage of the code:
- python pwo2cif-xyz.py espresso.pwo (or any name you gave to your espresso output file)
