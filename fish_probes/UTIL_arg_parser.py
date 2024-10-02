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
                        help='command', choices=['design', 'check_probe', 'test', 'evaluate_probe_sens_spec', "get_entropy_plot"])

    # File with the sequences in fasta format
    parser.add_argument('-s', dest = 'sequences', action="store", default=None,
                        help='File containing the sequences')

    # File with the taxonomy, the taxonomy is separated by ";", and there is a
    # "\t" between name and tax (Example: "gene1\tclade1;clade2;clade3\n")
    parser.add_argument('-t', dest = 'taxonomy', action="store", default=None,
                        help='File containing the taxonomy')

    # Clade for which we have to find the primers
    parser.add_argument('-c', dest = 'sel_clade', action="store", default=None,
                        help='Clade selected to design the primers',nargs="+")
    
    # Specific probe to evaluate for evaluate_probe_sens_spec
    parser.add_argument('-pte', dest = 'probe_to_evaluate', action="store", default=None,
                        #help='Clade selected to design the primers',nargs="+")
                        help='probe to evaluate sensitivity and specificity for')    
                        
    # Specific probe to evaluate for evaluate_probe_sens_spec
    parser.add_argument('-pte_map', dest = 'taxon_probe_map', action="store", default=None,
                        #help='Clade selected to design the primers',nargs="+")
                        help='json file mapping taxa to their probe sequences')    

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

    # help
    parser.add_argument('-h','--help', action='store_true', default=False,
                        dest='help', help='Print help')

    # help
    parser.add_argument('-sp','--split', action='store_true', default=False,
                        dest='split_probe', help='Evaluate also a probe split in two')

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
        # print help
        if args.help:
            UTIL_print_menus.design()
            sys.exit(0)
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
        # print help
        if args.help:
            UTIL_print_menus.test_probe()
            sys.exit(0)
        # there is only one mandatory input
        if args.input is None:
            UTIL_print_menus.test_probe()
            UTIL_log.print_error("Missing -i.")

    if args.command == 'evaluate_probe_sens_spec':
        if args.help:
            sys.exit("TODO: Implement help text")
        # There are four mandatory inputs (three are shared with args.command == "design")
        if args.sequences is None:
            UTIL_print_menus.evaluate_probe_sens_spec()
            UTIL_log.print_error("Missing -s.")
        if args.taxonomy is None:
            UTIL_print_menus.evaluate_probe_sens_spec()
            UTIL_log.print_error("Missing -t.")
        if args.sel_clade is None:
            UTIL_print_menus.evaluate_probe_sens_spec()
            UTIL_log.print_error("Missing -c.")
        if args.probe_to_evaluate is None:
            UTIL_print_menus.evaluate_probe_sens_spec()
            UTIL_log.print_error("Missing -pte")

    if args.command == 'get_entropy_plot':
        if args.help:
            sys.exit("TODO: Implement help text")
        # There are four mandatory inputs (three are shared with args.command == "design")
        if args.sequences is None:
            UTIL_print_menus.get_entropy_plot()
            UTIL_log.print_error("Missing -s.")
        if args.taxon_probe_map is None:
            UTIL_print_menus.get_entropy_plot()
            UTIL_log.print_error("Missing -pte_map")

    return args


# class to print the main menu -------------------------------------------------
class CapitalisedHelpFormatter(argparse.HelpFormatter):
    def add_usage(self, usage, actions, groups, prefix=None):
        if prefix is None:
            prefix = ''
        return super(CapitalisedHelpFormatter, self).add_usage(usage, actions, groups, prefix)
