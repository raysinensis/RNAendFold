import RNA ##install viennaRNA python binding first

##for each gene, grab 3' most 100nt for folding
genename="RN7SL1"
geneseq="GCCGGGCGCGGTGGCGCGTGCCTGTAGTCCCAGCTACTCGGGAGGCTGAGGCTGGAGGATCGCTTGAGTCCAGGAGTTCTGGGCTGTAGTGCGCTATGCCGATCGGGTGTCCGCACTAAGTTCGGCATCAATATGGTGACCTCCCGGGAGCGGGGGACCACCAGGTTGCCTAAGGAGGGGTGAACCGGCCCAGGTCGGAAACGGAGCAGGTCAAAACTCCCGTGCTGATCAGTAGTGGGATCGCGCCTGTGAATAGCCACTGCACTCCAGCCTGGGCAACATAGCGAGACCCCGTCTCT"
threeseq=geneseq[-100:]
folded=RNA.fold(threeseq)
foldtrack=folded[0]
foldenergy=folded[1]

##output to txt
foldout = "/home/rf/Desktop/fold.txt"
outfile = open(foldout, 'a')
outfile.write(genename+"\t"+foldtrack+"\t"+str(foldenergy)+"\n")
outfile.close()
