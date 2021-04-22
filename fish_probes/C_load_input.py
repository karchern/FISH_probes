import sys
import argparse
from fish_probes import UTIL_log

VERBOSE = 1

# ------------------------------------------------------------------------------
# Function to load the fasta file with the sequences
# ------------------------------------------------------------------------------
def load_sequences(sequences_file):
    try:
        o = open(sequences_file,"r")
    except:
        UTIL_log.print_error("Cannot load the fasta file with the sequences")

    # save result to a dict
    result = dict()
    # load file assuming is a fasta file
    first_line = o.readline()
    if not(first_line.startswith(">")):
        UTIL_log.print_error("Not a fasta file",4)
    else:
        header = first_line.rstrip()[1:]
        temp_sequence = ""
    # go through each line
    for line in o:
        if line.startswith(">"):
            result[header] = temp_sequence
            header = line.rstrip()[1:]
            temp_sequence = ""
        else:
            temp_sequence = temp_sequence+line.rstrip()

    # we write the last line
    result[header] = temp_sequence

    o.close()

    if VERBOSE > 2:
        UTIL_log.print_message("Found "+str(len(result))+" sequences.\n")
    return result

# ------------------------------------------------------------------------------
# Function to load the taxonomy
# ------------------------------------------------------------------------------
def load_taxonomy(taxonomy_file):
    try:
        o = open(taxonomy_file,"r")
    except:
        UTIL_log.print_error("Cannot load the taxonomy file",5)

    # save result to a dict
    result = dict()
    # load file
    for line in o:
        vals = line.rstrip().split("\t")
        result[vals[0]] = vals[1]

    o.close()

    if VERBOSE > 2:
        UTIL_log.print_message("Found taxonomy information for "+str(len(result))+" sequences.\n")
    return result

# ------------------------------------------------------------------------------
# Function to check that the input is correct
# ------------------------------------------------------------------------------
def check_input(sequences,taxonomy,args):
    # check that the clade is in the taxonomy
    found_clade = False
    for seq in taxonomy:
        if args.sel_clade in taxonomy[seq].split(";"):
            found_clade = True
    if not found_clade:
        UTIL_log.print_error("Selected clade is not present in the taxonomy",7)

    # check that we have a taxonomy annotation for each sequence
    # NOTE: it can be that there are more taxonomy entries than sequences, but
    # not the contrary
    for seq in sequences:
        if not seq in taxonomy:
            UTIL_log.print_error("Sequence '"+seq+"' does not have a taxonomy",8)

    # Remove entries from the taxonomy, if there are no corresponding sequences
    to_remove = list()
    for seq in taxonomy:
        if not seq in sequences:
            to_remove.append(seq)
    for r in to_remove:
        del taxonomy[r]
    if len(to_remove) > 0:
        if VERBOSE > 2:
            UTIL_log.print_message("Removed "+str(len(to_remove))+" taxonomy line(s) because no sequence was present.\n")

# ------------------------------------------------------------------------------
# Main function
# ------------------------------------------------------------------------------
# The purpouse of this function is to:
#  - print the available commands
#  - parse the arguments
#  - load the input from the files and check that it is correct
#  - return the created objects
def load_and_check_input(args):
    # set verbose
    global VERBOSE
    VERBOSE = args.verbose

    # load data from files
    if VERBOSE > 2:
        UTIL_log.print_log("Load sequences")
    sequences = load_sequences(args.sequences)
    if VERBOSE > 2:
        UTIL_log.print_log("Load taxonomy")
    taxonomy = load_taxonomy(args.taxonomy)

    # check that the input is correct
    if VERBOSE > 2:
        UTIL_log.print_log("Check input files")
    check_input(sequences,taxonomy,args)

    return sequences,taxonomy
