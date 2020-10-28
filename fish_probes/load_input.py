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

    sys.stderr.write("check \n")
    return 1,2,3,4
