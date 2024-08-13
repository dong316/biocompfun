"""=================================================================================================
Given a DNA Sequence, what are all the open reading frames (ORF) longer than L
lengths in nucleotides
lengths in residues
amino acid sequence


Michael Gribskov     20 January 2023
================================================================================================="""

# codon data
codon2aa = {"AAA": "K", "AAC": "N", "AAG": "K", "AAT": "N",
            "ACA": "T", "ACC": "T", "ACG": "T", "ACT": "T",
            "AGA": "R", "AGC": "S", "AGG": "R", "AGT": "S",
            "ATA": "I", "ATC": "I", "ATG": "M", "ATT": "I",

            "CAA": "Q", "CAC": "H", "CAG": "Q", "CAT": "H",
            "CCA": "P", "CCC": "P", "CCG": "P", "CCT": "P",
            "CGA": "R", "CGC": "R", "CGG": "R", "CGT": "R",
            "CTA": "L", "CTC": "L", "CTG": "L", "CTT": "L",

            "GAA": "E", "GAC": "D", "GAG": "E", "GAT": "D",
            "GCA": "A", "GCC": "A", "GCG": "A", "GCT": "A",
            "GGA": "G", "GGC": "G", "GGG": "G", "GGT": "G",
            "GTA": "V", "GTC": "V", "GTG": "V", "GTT": "V",

            "TAA": "*", "TAC": "Y", "TAG": "*", "TAT": "T",
            "TCA": "S", "TCC": "S", "TCG": "S", "TCT": "S",
            "TGA": "*", "TGC": "C", "TGG": "W", "TGT": "C",
            "TTA": "L", "TTC": "F", "TTG": "L", "TTT": "F"}

# --------------------------------------------------------------------------------------------------
# main program
# --------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # open a file for reading
    try:
        infile = open('scaffolds_short.fa', 'r')
    except:
        print('error opening file')

    # read and store each sequence
    sequence = {}
    for line in infile:
        # print(line)

        if line.startswith('>'):
            # this is a documentation line

            # start a new sequence
            id = line.rstrip().replace('>', '')
            sequence[id] = ''
        else:
            # this is a sequence line
            sequence[id] += line.rstrip()

    infile.close()

    # for each sequence translate each reading frame and store
    i = 0
    rf = {}
    for seq in sequence:
        this_seq = sequence[seq]
        i += 1
        print(f'{i:4d}\t{len(this_seq):4d}\t{seq}')
        for f in range(3):
            # loop over reading frames
            frame = ''
            for pos in range(f, len(this_seq)-2, 3):
                frame += codon2aa[this_seq[pos:pos + 3]]

            # construct a name and store
            name = seq + f' rf{f}'
            rf[name] = frame

    # for each stored reading frame, break into ORFs and calculate lengths
    all_orf = {}
    for f in rf:
        frame = rf[f]
        orf = frame.split('*')
        i = 0
        for o in orf:
            i += 1
            all_orf[f+f' orf{i}'] = o

    # final result
    for orf in all_orf:
        if len(all_orf[orf]) > 50:
            print(f'{orf}\t{len(all_orf[orf])}\t{all_orf[orf]}')


    exit(0)
