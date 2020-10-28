import sys
import argparse

def input_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('sequences', action="store", default=None, help='File containing the sequences')
    parser.add_argument('taxonomy', action="store", default=None, help='File containing the taxonomy')
    parser.add_argument('sel_clade', action="store", default=None, help='Clade selected to design the primers')
    parser.add_argument('-v', action='store', type=int, default=3, dest='verbose', help='Verbose level: 1=error, 2=warning, 3=message, 4+=debugging [3]')
    parser.add_argument('-m', action='store', type=int, default=20, dest='min_len', help='Minimum probe length [20]')
    args = parser.parse_args()
    return args

# ------------------------------------------------------------------------------
# Main function
# ------------------------------------------------------------------------------
# The purpouse of this function is to:
#  - print the available commands
#  - load the input from sys.argv
#  - check that the input is correct
#  - return the objects created
def load_and_check_input():
    # load sys.argv
    args = input_parser()
    sys.stderr.write("check \n")
    return 1,2,3,4
