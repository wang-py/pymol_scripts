# load the protein
# cmd.load("movie/Mode0/Mode0.pdb")

# open the file of new values (just 1 column of numbers, one for each alpha carbon)
chain_H = open("chain_H/chain_H_BB_mode0_cubic_root.txt", 'r')
chain_A = open("chain_A/chain_A_BB_mode0_cubic_root.txt", 'r')
chain_H1 = open("chain_H/chain_H_BB_mode1_cubic_root.txt", 'r')
chain_A1 = open("chain_A/chain_A_BB_mode1_sqrt.txt", 'r')

# create the global, stored array
stored.chain_H = []
stored.chain_A = []
stored.chain_H1 = []
stored.chain_A1 = []

# read the new B factors from file
for line in chain_H.readlines(): stored.chain_H.append( float(line) )
for line in chain_A.readlines(): stored.chain_A.append( float(line) )
for line in chain_H1.readlines(): stored.chain_H1.append( float(line) )
for line in chain_A1.readlines(): stored.chain_A1.append( float(line) )

# close the input file
chain_H.close()
chain_A.close()
chain_H1.close()
chain_A1.close()

# clear out the old B Factors
alter chain_H_mode0, b=0.0
alter chain_A_mode0, b=0.0
alter chain_H_mode1, b=0.0
alter chain_A_mode1, b=0.0

# update the B Factors with new properties
alter chain_H_mode0 and n. CA, b=stored.chain_H.pop(0)
alter chain_A_mode0 and n. CA, b=stored.chain_A.pop(0)
alter chain_H_mode1 and n. CA, b=stored.chain_H1.pop(0)
alter chain_A_mode1 and n. CA, b=stored.chain_A1.pop(0)

# color the protein based on the new B Factors of the alpha carbons
spectrum b, white red, chain_H_mode0
spectrum b, yellow blue, chain_A_mode0
spectrum b, white red, chain_H_mode1
spectrum b, yellow blue, chain_A_mode1
# saving the new pdb with probabilities
# cmd.save("Mode0_colored.pdb", "Mode0")
