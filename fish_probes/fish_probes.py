#!/usr/bin/env python
import sys
try:
    from fish_probes import load_input, predict_probes, log, arg_parser
except Exception as e:
    sys.stderr.write("Error 1: Unable to load the python packages. Message:\n")
    sys.stderr.write(str(e)+"\n")
    sys.exit(1)

def main():
    # load sys.argv
    args = arg_parser.input_parser()

    log.print_message("Call: ")
    log.print_message(" ".join(sys.argv)+"\n")

    # load the input files
    sequences,taxonomy,sel_clade,probe_len,verbose,outfile,\
      perc_seq_with_kmer = load_input.load_and_check_input(args)

    # find probes
    predict_probes.predict_probes(sequences,\
                                  taxonomy,\
                                  sel_clade,\
                                  probe_len,\
                                  verbose,\
                                  outfile,\
                                  perc_seq_with_kmer)

    sys.exit(0)

if __name__ == '__main__':
    main()
