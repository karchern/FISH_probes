import sys
import argparse
from fish_probes import UTIL_log, UTIL_print_menus

# ------------------------------------------------------------------------------
# Function to parse the input
# ------------------------------------------------------------------------------
def input_parser(tool_version):
    parser = argparse.ArgumentParser(usage=UTIL_print_menus.main_message(tool_version), formatter_class=CapitalisedHelpFormatter,add_help=False)

    # COMMAND
    parser.add_argument('command', action="store", default=None,
                        help='command',choices=['design','check_probe','test'])

    # File with the sequences in fasta format
    parser.add_argument('-s', dest = 'sequences', action="store", default=None,
                        help='File containing the sequences')

    # File with the taxonomy, the taxonomy is separated by ";", and there is a
    # "\t" between name and tax (Example: "gene1\tclade1;clade2;clade3\n")
    parser.add_argument('-t', dest = 'taxonomy', action="store", default=None,
                        help='File containing the taxonomy')

    # Clade for which we have to find the primers
    parser.add_argument('-c', dest = 'sel_clade', action="store", default=None,
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

    # General input file
    parser.add_argument('-i', action='store', default=None,
                        dest='input', help='General input')

    # Min fraction of sequences from the selected clade
    parser.add_argument('-p', action='store', default=0.9, type = float,
                        dest='perc_seq', help='Minimum fraction of sequences that should contain the selected probe [0.9]')

    # version
    parser.add_argument('--version', action='version', version='%(prog)s {0} on python {1}'.format(tool_version, sys.version.split()[0]))

    args = parser.parse_args()

    ############################################################################
    # CHECK ARGUMENTS
    # check args verbose
    if args.verbose < 1:
        UTIL_log.print_error("Verbose (-v) needs to be higher than 0")
    # check args perc seq
    if args.perc_seq < 0 or args.perc_seq > 1:
        UTIL_log.print_error("Threshold (-p) should be between 0 and 1")
    # check length of the probe
    if args.probe_len < 1:
        UTIL_log.print_error("Probe length (-k) cannot be lower than 0")


    ############################################################################
    # CHECK ARGUMENTS FOR COMMAND DESIGN
    if args.command == "design":
        # there are three mandatory input
        if args.sequences is None:
            UTIL_print_menus.design()
            UTIL_log.print_error("Missing -s.")
        if args.taxonomy is None:
            UTIL_print_menus.design()
            UTIL_log.print_error("Missing -t.")
        if args.sel_clade is None:
            UTIL_print_menus.design()
            UTIL_log.print_error("Missing -c.")

    ############################################################################
    # CHECK ARGUMENTS FOR COMMAND TEST_PROBE
    if args.command == "check_probe":
        # there is only one mandatory input
        if args.input is None:
            UTIL_print_menus.test_probe()
            UTIL_log.print_error("Missing -i.")

    return args


# class to print the main menu -------------------------------------------------
class CapitalisedHelpFormatter(argparse.HelpFormatter):
    def add_usage(self, usage, actions, groups, prefix=None):
        if prefix is None:
            prefix = ''
        return super(CapitalisedHelpFormatter, self).add_usage(usage, actions, groups, prefix)
