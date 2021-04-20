import sys
from fish_probes import log

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

    log.print_message("Sequences belonging to the selected clade: "+str(len(seq_sel_clade))+".")
    log.print_message("Sequences belonging to other clades: "+str(len(seq_other))+".\n")
    return seq_sel_clade, seq_other

# ------------------------------------------------------------------------------
# Find conserved regions in the sequences from the selected clade
# ------------------------------------------------------------------------------
def DnaCheck(sequence):
    return all(base.upper() in ('A', 'C', 'T', 'G', 'U') for base in sequence)

def find_kmers(string,k):
    res = {}
    res_N = {}
    for x in range(len(string)+1-k):
        kmer = string[x:x+k]
        # we select only if they contain nucleotide sequences
        if DnaCheck(kmer):
            res[kmer] = res.get(kmer, 0) + 1
        else:
            res_N[kmer] = res_N.get(kmer, 0) + 1
    return res, res_N

def find_conserved_regions(seq_sel_clade,k,perc_seq_with_kmer):
    all_strings_kmers = dict()
    for s in seq_sel_clade:
        allK,allK_N = find_kmers(seq_sel_clade[s],k)
        all_strings_kmers[s] = allK
    # find all possible k-mers
    all_kmers = set()
    for s in all_strings_kmers:
        for kmer in all_strings_kmers[s]:
            all_kmers.add(kmer)
    log.print_message("Identifed "+str(len(all_kmers))+" unique "+str(k)+"-mers.")
    # now we count how many times it appear
    count_mers = dict()
    for kmer in list(all_kmers):
        count_mers[kmer] = 0
    # now we add the counts per k-mer
    for s in all_strings_kmers:
        for kmer in all_strings_kmers[s]:
            count_mers[kmer] = count_mers[kmer] + 1
    # we check which k-mers covers all sequences
    n_seq = len(seq_sel_clade)
    kmers_recall = dict() # this will be filled in by "check_uniqueness"
    kmers_precision = dict()
    list_identical = list()
    for kmer in count_mers:
        if count_mers[kmer] == n_seq:
            list_identical.append(kmer) # used only to print
        if count_mers[kmer] > n_seq*perc_seq_with_kmer:
            kmers_recall[kmer] = count_mers[kmer]
            kmers_precision[kmer] = 0

    log.print_message("  (Identifed "+str(len(list_identical))+" "+str(k)+"-mers present in all sequences)")
    log.print_message(str(len(kmers_precision))+" "+str(k)+"-mers will go to the next step.")
    log.print_message("(only k-mers present in at least "+str(perc_seq_with_kmer*100)+"% of the sequences will be used).\n")

    if len(kmers_precision) == 0:
        log.print_warning("No k-mers passed the filter. Please decrease the threshold in -p")
    # return
    return kmers_recall,kmers_precision



# ------------------------------------------------------------------------------
# Starting from the conserved regions, check if they are unique
# ------------------------------------------------------------------------------
def check_uniqueness(kmers_precision, seq_other, probe_len):
    # we check if the kmers are covered by other sequences
    other_sel_clades = dict()
    for s in seq_other:
        this_kmers,this_kmers_N = find_kmers(seq_other[s],probe_len)
        for kmer in this_kmers:
            if kmer in kmers_precision:
                kmers_precision[kmer] = kmers_precision[kmer] + 1
                if not kmer in other_sel_clades:
                    other_sel_clades[kmer] = list()
                other_sel_clades[kmer].append(s)
        # we need to evaluate the ones with an N or others
        for kmer in this_kmers_N:
            dummy = "TODO"
    return other_sel_clades


# ------------------------------------------------------------------------------
# Order to show the probes
# ------------------------------------------------------------------------------
def priotitize_probes(kmers_recall,kmers_precision,other_sel_clades,taxonomy,n_seq_clade):
    # find the order
    probe_order = list()
    missing = list()
    # best one: cover all sequences, and not in the other clade
    for p in list(kmers_recall.keys()):
        if kmers_recall[p]/n_seq_clade == 1:
            if kmers_precision[p] == 0:
                probe_order.append(p)
            else:
                missing.append(p)
        else:
            missing.append(p)
    probe_order.extend(missing)

    # prepare lines to print
    to_print = list()
    for kmer in probe_order:
        this_str = kmer+"\t"+str(kmers_recall[kmer]/n_seq_clade)+"\t"
        this_str = this_str+str(kmers_recall[kmer])+"\t"
        this_str = this_str+str(kmers_precision[kmer])+"\t"
        if kmer in other_sel_clades:
            this_str = this_str+",".join(other_sel_clades[kmer])
        to_print.append(this_str+"\n")
    return to_print


# ------------------------------------------------------------------------------
# Save/Print result
# ------------------------------------------------------------------------------
def save_result(sel_probes, outfile):
    sys.stdout.write("probe\tperc_covered_sequences\tn_covered_sequences\tn_covered_others\tothers\n")
    for p in sel_probes:
        sys.stdout.write(p)

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
def predict_probes(sequences,taxonomy,args):
    # Zero, find sequences that belong to the selected clade
    log.print_log("Identify sequences from the selected clade")
    seq_sel_clade, seq_other = split_sequences(taxonomy,args.sel_clade,sequences)

    # First, identify possible conserved regions
    log.print_log("Identify k-mers for the query clade")
    kmers_recall,kmers_precision = find_conserved_regions(seq_sel_clade,args.probe_len,args.perc_seq)

    # Second, check if identified regions are unique, compared to the other
    # clades (~ evaluating precision)
    log.print_log("Check if the identified k-mers are present in the other clades")
    other_sel_clades = check_uniqueness(kmers_precision,seq_other,args.probe_len)

    # Third, prioritize selected probes
    log.print_log("Prioritize selected probes")
    sel_probes = priotitize_probes(kmers_recall,kmers_precision,other_sel_clades,taxonomy,len(seq_sel_clade))

    # print/save to outfile
    log.print_log("Save the result")
    save_result(sel_probes, args.outfile)
