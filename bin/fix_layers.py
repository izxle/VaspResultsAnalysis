#!/usr/bin/env python

from ase.io import read
from ase.geometry import get_layers
from ase.constraints import FixAtoms

from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('filename')
parser.add_argument('-f', '--fix', type=int)
parser.add_argument('-l', '--layers', type=int)
args = parser.parse_args()

atoms = read(args.filename)
tags, positions = get_layers(atoms, (0,0,1), 0.3)
atoms.set_tags(tags)

if args.fix:
    fix = args.fix
else:
    fix = len(positions) / 2

mask = [a.tag < fix for a in atoms]
constraint = FixAtoms(mask=mask)
atoms.set_constraint(constraint)
