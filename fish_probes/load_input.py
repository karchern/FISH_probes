import sys
import argparse

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

    # Minimum length of the probes that we identify
    parser.add_argument('-m', action='store', type=int, default=20,
                        dest='min_len', help='Minimum probe length [20]')

    args = parser.parse_args()
    return args


# ------------------------------------------------------------------------------
# Function to load the fasta file with the sequences
# ------------------------------------------------------------------------------
def load_sequences(sequences_file):
    try:
        o = open(sequences_file,"r")
    except:
        sys.stderr.write("Cannot load the fasta file with the sequences.\n")
        sys.exit(1)

    # save result to a dict
    result = dict()
    # load file assuming is a fasta file
    first_line = o.readline()
    if not(first_line.startswith(">")):
        sys.stderr.write("Error, not a fasta file.\n")
        sys.exit(1)
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
    return result

# ------------------------------------------------------------------------------
# Function to load the taxonomy
# ------------------------------------------------------------------------------
def load_taxonomy(taxonomy_file):
    try:
        o = open(taxonomy_file,"r")
    except:
        sys.stderr.write("Cannot load the taxonomy file.\n")
        sys.exit(1)

    # save result to a dict
    result = dict()
    # load file
    for line in o:
        vals = line.rstrip().split("\t")
        result[vals[0]] = vals[1]

    o.close()
    return result

# ------------------------------------------------------------------------------
# Function to check that the input is correct
# ------------------------------------------------------------------------------
def check_input(sequences,taxonomy,args):
    # check args verbose
    if args.verbose < 1:
        sys.stderr.write("Verbose (-v) needs to be lower than 0.\n")
        sys.exit(1)

    # check min length of the probe
    if args.min_len < 1:
        sys.stderr.write("Probe length (-m) cannot be lower than 0.\n")
        sys.exit(1)

    # check that the clade is in the taxonomy
    found_clade = False
    for seq in taxonomy:
        if args.sel_clade in taxonomy[seq].split(";"):
            found_clade = True
    if not found_clade:
        sys.stderr.write("Selected clade is not present in the taxonomy.\n")
        sys.exit(1)

    # check that we have a taxonomy annotation for each sequence
    # NOTE: it can be that there are more taxonomy entries than sequences, but
    # not the contrary
    for seq in sequences:
        if not seq in taxonomy:
            sys.stderr.write("Sequence '"+seq+"' does not have a taxonomy.\n")
            sys.exit(1)

    # Remove entries from the taxonomy, if there are no corresponding sequences
    to_remove = list()
    for seq in taxonomy:
        if not seq in sequences:
            to_remove.append(seq)
    for r in to_remove:
        del taxonomy[r]

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
    sequences = load_sequences(args.sequences)
    taxonomy = load_taxonomy(args.taxonomy)

    # check that the input is correct
    check_input(sequences,taxonomy,args)

    return sequences,taxonomy,args.sel_clade,args.min_len,args.verbose
