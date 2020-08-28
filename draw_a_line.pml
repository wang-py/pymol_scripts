# make two new pseudoatoms, just for
# making a distance measure between them
# Specify your own position vectors in pos=[x, y, z]
pseudoatom aa, pos=[10.0, -14.0, 33.0]
pseudoatom bb, pos=[-15.3, 44.5, 8.3]

# create distance between the two atoms
distance d1, aa, bb

# clean up the representation to make this look
# more like a solid line
set dash_gap, 0
set dash_radius, 0.55
set dash_round_ends, 0
set dash_color, 0xffcc00, d1
hide labels, d1 
