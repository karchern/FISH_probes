import sys

# ------------------------------------------------------------------------------
# Find sequences from the selected clade
# ------------------------------------------------------------------------------
def split_sequences(taxonomy,sel_clade,sequences):
    seq_sel_clade = dict()
    seq_other = dict()
    for seq in taxonomy:
        if sel_clade in taxonomy[seq].split(";"):
            seq_sel_clade[seq] = sequences[seq]
        else:
            seq_other[seq] = sequences[seq]
    return seq_sel_clade, seq_other

# ------------------------------------------------------------------------------
# Find conserved regions in the sequences from the selected clade
# ------------------------------------------------------------------------------
def find_conserved_regions(sequences, min_len):
    # to return
    all_conserved_position = list()

    # we assume that we have a MSA and that the positions are aligned
    len_ali = len(sequences[list(sequences.keys())[1]])
    start_ali_tmp = -1
    # we go through each position and see if it is conserved
    for pos in range(len_ali):
        is_pos_conserved = True
        nucleotide_found = ""
        for seq in sequences:
            if nucleotide_found == "":
                nucleotide_found = sequences[seq][pos]
            else:
                if nucleotide_found != sequences[seq][pos]:
                    is_pos_conserved = False
        # if is_pos_conserved is True, then all sequences have the same
        # nucleotide in this position
        # a) set up the start
        if is_pos_conserved:
            if start_ali_tmp == -1:
                start_ali_tmp = pos
        # b) save (previous) region if it is not conserved anymore
        if not is_pos_conserved:
            if start_ali_tmp != -1:
                if pos - start_ali_tmp >= min_len:
                    all_conserved_position.append([start_ali_tmp,pos,
                                             sequences[seq][start_ali_tmp:pos]])
                start_ali_tmp = -1
        # c) case of the last position being conserved
        if is_pos_conserved and pos == len_ali-1:
            if start_ali_tmp != -1:
                if (pos+1) - start_ali_tmp >= min_len:
                    all_conserved_position.append([start_ali_tmp,(pos+1),
                                         sequences[seq][start_ali_tmp:(pos+1)]])

    return all_conserved_position

# ------------------------------------------------------------------------------
# Main function
# ------------------------------------------------------------------------------
# Input:
#  - sequences, dictionary of seq_id -> nucleotide sequence
#  - taxonomy, dictionary of seq_id -> "clade1;clade2;clade3"
#  - sel_clade, clade for which we have to design the probe
#  - min_len, minimul length for the selected probe (positive integer)
#  - verbose,
#  - outfile, where to save the output. If None, then stdout
def predict_probes(sequences,taxonomy,sel_clade,min_len,verbose,outfile):
    # Zero, find sequences that belong to the selected clade
    seq_sel_clade, seq_other = split_sequences(taxonomy,sel_clade,sequences)

    # First, identify possible conserved regions
    all_conserved_position = find_conserved_regions(seq_sel_clade,min_len)
    # Second, check if identified regions are unique, compared to the other
    # clades
