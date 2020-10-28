import sys

# ------------------------------------------------------------------------------
# Find sequences from the selected clade
# ------------------------------------------------------------------------------
def split_sequences(taxonomy,sel_clade):
    result = dict()
    for seq in taxonomy:
        if sel_clade in taxonomy[seq].split(";"):
            result[seq] = True
        else:
            result[seq] = False
    return result

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
    is_sel_clade = split_sequences(taxonomy,sel_clade)

    print(is_sel_clade)

    # First, identify possible conserved regions

    # Second, check if identified regions are unique, compared to the other
    # clades
