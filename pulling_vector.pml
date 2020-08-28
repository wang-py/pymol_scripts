# make two new pseudoatoms, just for
# making a distance measure between them
# Specify your own position vectors in pos=[x, y, z]

# get positions of ALA63 methyl and PHE28 HZ
pseudoatom ALA63_methyl, pos=[21.35666666666667, 20.76, 26.03666666666667]
select PHE28, /Q1H2_10A_1500ps_1///PHE`28/HZ

# get positions of ALA242 methyl and PRO59 HB2
pseudoatom ALA242_methyl, pos=[28.28, 23.273333333333333, 24.49]
select PRO59, /Q1H2_10A_1500ps_1///PRO`246/HB2

# draw short axis
distance short_axis, ALA63_methyl, 'PHE28'

# draw long axis
distance long_axis, ALA242_methyl, 'PRO59'

# draw pulling vector, starting at C18
pseudoatom C18, pos=[23.05, 26.05, 22.30]
pseudoatom virtual_path, pos=[24.6285822, 21.0064066, 33.6578178]
distance pulling_vector, C18, virtual_path

# clean up the representation to make this look
# more like a solid line
set dash_gap, 0.5
set dash_radius, 0.1
set dash_round_ends, 0
# white lines for axes
set dash_color, 0xffffff, short_axis long_axis
# yellow line for pulling
set dash_color, 0xffff00, pulling_vector
hide labels, short_axis long_axis pulling_vector
