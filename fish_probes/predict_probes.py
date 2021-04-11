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
def DnaCheck(sequence):
    return all(base.upper() in ('A', 'C', 'T', 'G', 'U') for base in sequence)

def find_kmers(string,k):
    f = {}
    for x in range(len(string)+1-k):
        kmer = string[x:x+k]
        # we select only if they contain nucleotide sequences
        if DnaCheck(kmer):
            f[kmer] = f.get(kmer, 0) + 1
    return f

def find_conserved_regions(list_strings,k):
    all_strings_kmers = dict()
    for s in list_strings:
        all_strings_kmers[s] = find_kmers(s,k)
    # find all possible k-mers
    all_kmers = set()
    for s in all_strings_kmers:
        for kmer in all_strings_kmers[s]:
            all_kmers.add(kmer)
    # now we count how many times it appear
    count_mers = dict()
    for kmer in list(all_kmers):
        count_mers[kmer] = 0
    # now we add the counts
    for s in all_strings_kmers:
        for kmer in all_strings_kmers[s]:
            count_mers[kmer] = count_mers[kmer] + 1
    # return
    return count_mers

# ------------------------------------------------------------------------------
# Starting from the conserved regions, check if they are unique
# ------------------------------------------------------------------------------
def check_uniqueness(all_conserved_position, seq_other, probe_len):
    print("ok")


# ------------------------------------------------------------------------------
# Main function
# ------------------------------------------------------------------------------
# Input:
#  - sequences, dictionary of seq_id -> nucleotide sequence
#  - taxonomy, dictionary of seq_id -> "clade1;clade2;clade3"
#  - sel_clade, clade for which we have to design the probe
#  - probe_len, length for the selected probe (positive integer)
#  - verbose,
#  - outfile, where to save the output. If None, then stdout
def predict_probes(sequences,taxonomy,sel_clade,probe_len,verbose,outfile):
    # Zero, find sequences that belong to the selected clade
    seq_sel_clade, seq_other = split_sequences(taxonomy,sel_clade,sequences)

    # First, identify possible conserved regions
    all_sel_kmers = find_conserved_regions(list(seq_sel_clade.values()),\
                                                probe_len)

    # Second, check if identified regions are unique, compared to the other
    # clades
    check_uniqueness(all_sel_kmers,seq_other,probe_len)
