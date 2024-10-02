#!/usr/bin/env python
import sys
import json
try:

    # import UTIL
    from fish_probes import UTIL_log, UTIL_arg_parser, UTIL_probe, C_test, MSA, Plots
    #import UTIL_log, UTIL_arg_parser, UTIL_probe, C_test
    # import commands files
    from fish_probes import C_load_input, C_predict_probes
    #import C_load_input, C_predict_probes
    # import version
    from . import __version__ as tool_version
    #tool_version = "NA"
except Exception as e:
    sys.stderr.write("Error 1: Unable to load the python packages. Message:\n")
    sys.stderr.write(str(e)+"\n")
    sys.exit(1)

def main():
    # load sys.argv
    
    args = UTIL_arg_parser.input_parser(tool_version)
    reference_msa = MSA.MSA.from_reference_alignment()
    if args.verbose > 2:
        UTIL_log.print_message("Call: ")
        UTIL_log.print_message(" ".join(sys.argv)+"\n")

    
    # find probes --------------------------------------------------------------
    if args.command == "design":
        sequences,taxonomy = C_load_input.load_and_check_input(args)
        C_predict_probes.predict_probes(sequences,taxonomy,args)

    # test a given probe -------------------------------------------------------
    if args.command == "check_probe":
        print(UTIL_probe.create_to_print(args.input,header = True,split = args.split_probe))
    
    if args.command == "evaluate_probe_sens_spec":
        sequences,taxonomy = C_load_input.load_and_check_input(args)
        C_predict_probes.evaluate_probe_sens_spec(sequences,taxonomy,args)

    if args.command == "get_entropy_plot":
        sequences = C_load_input.load_and_check_input(args, only_seqs = True)
        kmer_map = json.load(open(args.taxon_probe_map))
        kmer_info = C_predict_probes.get_kmer_info(sequences, kmer_map)
        Plots.EntropyPlot(
            msa = reference_msa, 
            kmer_info = kmer_info,
            )

    # test the tool ------------------------------------------------------------
    if args.command == "test":
        C_test.test()

    sys.exit(0)

if __name__ == '__main__':
    main()
