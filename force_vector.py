'''
http://pymolwiki.org/index.php/cgo_arrow

(c) 2013 Thomas Holder, Schrodinger Inc.

License: BSD-2-Clause
'''

import numpy as np
import os
from glob import glob
from pymol import cmd, cgo, CmdException
from pmf_energy_plot import *

def cgo_arrow(atom1='pk1', atom2='pk2', radius=0.5, gap=0.0, hlength=-1, hradius=-1,
              color='blue red', name=''):
    '''
DESCRIPTION

    Create a CGO arrow between two picked atoms.

ARGUMENTS

    atom1 = string: single atom selection or list of 3 floats {default: pk1}

    atom2 = string: single atom selection or list of 3 floats {default: pk2}

    radius = float: arrow radius {default: 0.5}

    gap = float: gap between arrow tips and the two atoms {default: 0.0}

    hlength = float: length of head

    hradius = float: radius of head

    color = string: one or two color names {default: blue red}

    name = string: name of CGO object
    '''
    from chempy import cpv

    radius, gap = float(radius), float(gap)
    hlength, hradius = float(hlength), float(hradius)

    try:
        color1, color2 = color.split()
    except:
        color1 = color2 = color
    color1 = list(cmd.get_color_tuple(color1))
    color2 = list(cmd.get_color_tuple(color2))

    def get_coord(v):
        if not isinstance(v, str):
            return v
        if v.startswith('['):
            return cmd.safe_list_eval(v)
        return cmd.get_atom_coords(v)

    xyz1 = get_coord(atom1)
    print(xyz1)
    xyz2 = get_coord(atom2)
    print(xyz2)
    normal = cpv.normalize(cpv.sub(xyz1, xyz2))

    if hlength < 0:
        hlength = radius * 3.0
    if hradius < 0:
        hradius = hlength * 0.6

    if gap:
        diff = cpv.scale(normal, gap)
        xyz1 = cpv.sub(xyz1, diff)
        xyz2 = cpv.add(xyz2, diff)

    xyz3 = cpv.add(cpv.scale(normal, hlength), xyz2)

    obj = [cgo.CYLINDER] + xyz1 + xyz3 + [radius] + color1 + color2 + \
          [cgo.CONE] + xyz3 + xyz2 + [hradius, 0.0] + color2 + color2 + \
          [1.0, 0.0]

    if not name:
        name = cmd.get_unused_name('arrow')

    cmd.load_cgo(obj, name)

def force_vector(tunnel_pdb, md_folder, k):
    pos_files = sorted(glob(md_folder + "/*_water.xvg"), key=os.path.getmtime)
    tunnel_points = read_tunnel_pdb(tunnel_pdb)
    force_vectors = get_force_vs_site(tunnel_points, pos_files, float(k))
    num_of_pts = tunnel_points.shape[0]
    for i in range(num_of_pts):
        tp = tunnel_points[i]
        fv = force_vectors[i] * 0.05
        end_point = (tp + fv) 
        cgo_arrow(tp.tolist(), end_point.tolist(), radius=0.1, name="force%d"%i)


cmd.extend('cgo_arrow', cgo_arrow)
cmd.extend('force_vector', force_vector)
