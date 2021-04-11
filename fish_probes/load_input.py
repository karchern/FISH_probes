import sys
import argparse
from fish_probes import log

# ------------------------------------------------------------------------------
# Function to parse the input
# ------------------------------------------------------------------------------
def input_parser():
    parser = argparse.ArgumentParser()

    # File with the sequences in fasta format
    parser.add_argument('sequences', action="store", default=None,
                        help='File containing the sequences')

    # File with the taxonomy, the taxonomy is separated by ";", and there is a
    # "\t" between name and tax (Example: "gene1\tclade1;clade2;clade3\n")
    parser.add_argument('taxonomy', action="store", default=None,
                        help='File containing the taxonomy')

    # Clade for which we have to find the primers
    parser.add_argument('sel_clade', action="store", default=None,
                        help='Clade selected to design the primers')

    # Verbose level
    parser.add_argument('-v', action='store', type=int, default=3,
                        dest='verbose', help='Verbose level: 1=error,'\
                        ' 2=warning, 3=message, 4+=debugging [3]')

    # Length of the probes that we identify
    parser.add_argument('-k', action='store', type=int, default=20,
                        dest='probe_len', help='Probe length [20]')

    # Output file
    parser.add_argument('-o', action='store', default=None,
                        dest='outfile', help='Output file [stdout]')

    args = parser.parse_args()

    # check args verbose
    if args.verbose < 1:
        log.print_error("Verbose (-v) needs to be higher than 0",2)

    return args


# ------------------------------------------------------------------------------
# Function to load the fasta file with the sequences
# ------------------------------------------------------------------------------
def load_sequences(sequences_file):
    try:
        o = open(sequences_file,"r")
    except:
        log.print_error("Cannot load the fasta file with the sequences",3)

    # save result to a dict
    result = dict()
    # load file assuming is a fasta file
    first_line = o.readline()
    if not(first_line.startswith(">")):
        log.print_error("Not a fasta file",4)
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

    log.print_message("Found "+str(len(result))+" sequences.\n")
    return result

# ------------------------------------------------------------------------------
# Function to load the taxonomy
# ------------------------------------------------------------------------------
def load_taxonomy(taxonomy_file):
    try:
        o = open(taxonomy_file,"r")
    except:
        log.print_error("Cannot load the taxonomy file",5)

    # save result to a dict
    result = dict()
    # load file
    for line in o:
        vals = line.rstrip().split("\t")
        result[vals[0]] = vals[1]

    o.close()

    log.print_message("Found taxonomy information for "+str(len(result))+" sequences.\n")
    return result

# ------------------------------------------------------------------------------
# Function to check that the input is correct
# ------------------------------------------------------------------------------
def check_input(sequences,taxonomy,args):
    # check length of the probe
    if args.probe_len < 1:
        log.print_error("Probe length (-m) cannot be lower than 0",6)

    # check that the clade is in the taxonomy
    found_clade = False
    for seq in taxonomy:
        if args.sel_clade in taxonomy[seq].split(";"):
            found_clade = True
    if not found_clade:
        log.print_error("Selected clade is not present in the taxonomy",7)

    # check that we have a taxonomy annotation for each sequence
    # NOTE: it can be that there are more taxonomy entries than sequences, but
    # not the contrary
    for seq in sequences:
        if not seq in taxonomy:
            log.print_error("Sequence '"+seq+"' does not have a taxonomy",8)

    # Remove entries from the taxonomy, if there are no corresponding sequences
    to_remove = list()
    for seq in taxonomy:
        if not seq in sequences:
            to_remove.append(seq)
    for r in to_remove:
        del taxonomy[r]
    if len(to_remove) > 0:
        log.print_message("Removed "+str(len(to_remove))+" taxonomy line(s) because no sequence was present.\n")

# ------------------------------------------------------------------------------
# Main function
# ------------------------------------------------------------------------------
# The purpouse of this function is to:
#  - print the available commands
#  - parse the arguments
#  - load the input from the files and check that it is correct
#  - return the created objects
def load_and_check_input():
    # load sys.argv
    args = input_parser()

    # load data from files
    log.print_log("Load sequences")
    sequences = load_sequences(args.sequences)
    log.print_log("Load taxonomy")
    taxonomy = load_taxonomy(args.taxonomy)

    # check that the input is correct
    log.print_log("Check input files")
    check_input(sequences,taxonomy,args)

    return sequences,taxonomy,args.sel_clade,args.probe_len,args.verbose,\
             args.outfile
