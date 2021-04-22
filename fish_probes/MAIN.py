#!/usr/bin/env python
import sys
try:
    from fish_probes import load_input, predict_probes, log, arg_parser, probe_util
except Exception as e:
    sys.stderr.write("Error 1: Unable to load the python packages. Message:\n")
    sys.stderr.write(str(e)+"\n")
    sys.exit(1)

def main():
    # load sys.argv
    args = arg_parser.input_parser()

    log.print_message("Call: ")
    log.print_message(" ".join(sys.argv)+"\n")

    # find probes --------------------------------------------------------------
    if args.command == "design":
        sequences,taxonomy = load_input.load_and_check_input(args)
        predict_probes.predict_probes(sequences,taxonomy,args)

    # test a given probe -------------------------------------------------------
    if args.command == "test_probe":
        print(probe_util.create_to_print(args.input,header = True))

    sys.exit(0)

if __name__ == '__main__':
    main()
