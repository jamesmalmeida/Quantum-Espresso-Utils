from ase.io import read, write
import sys

#USAGE: python pwo2cif-xyz.py espresso-output-file

#Get the filename provided by the user
espresso_output = sys.argv[1]
print('Reading espresso output', espresso_output)

all_coordinates = read(espresso_output, index=':')
initial_coordinates = all_coordinates[0]
relaxed_coordinates = all_coordinates[-1]

#Write trajectory
write('trajectory.xyz', all_coordinates)

#Write initial coordinates XYZ
write('initial.xyz', initial_coordinates, format='xyz')

#Write relaxed coordinates XYZ
write('relaxed.xyz', relaxed_coordinates, format='xyz')

#Write relaxed coordinates CIF
write('relaxed.cif', relaxed_coordinates)
