# load the protein
# cmd.load("movie/Mode0/Mode0.pdb")

import sys

# take input from the command line
# open the file of new values (just 1 column of numbers, one for each alpha carbon)
color_file = open(sys.argv[1], 'r')

# create the global, stored array
stored.chain_H = []

# read the new B factors from file
for line in color_file.readlines(): stored.chain_H.append( float(line) )

# close the input file
color_file.close()

# update the B Factors with new properties
alter chain_H_mode0 and n. CA, b=stored.chain_H.pop(0)

# color the protein based on the new B Factors of the alpha carbons
spectrum b, white red, chain_H_mode0
# saving the new pdb with probabilities
# cmd.save("Mode0_colored.pdb", "Mode0")
