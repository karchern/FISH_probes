#!/usr/bin/env python
import sys
try:
    # import UTIL
    from fish_probes import UTIL_log, UTIL_arg_parser, UTIL_probe, TEST
    # import commands files
    from fish_probes import C_load_input, C_predict_probes
    # import version
    from . import __version__ as tool_version
except Exception as e:
    sys.stderr.write("Error 1: Unable to load the python packages. Message:\n")
    sys.stderr.write(str(e)+"\n")
    sys.exit(1)

def main():
    # load sys.argv
    args = UTIL_arg_parser.input_parser(tool_version)

    if args.verbose > 2:
        UTIL_log.print_message("Call: ")
        UTIL_log.print_message(" ".join(sys.argv)+"\n")

    # find probes --------------------------------------------------------------
    if args.command == "design":
        sequences,taxonomy = C_load_input.load_and_check_input(args)
        C_predict_probes.predict_probes(sequences,taxonomy,args)

    # test a given probe -------------------------------------------------------
    if args.command == "check_probe":
        print(UTIL_probe.create_to_print(args.input,header = True))

    # test the tool ------------------------------------------------------------
    if args.command == "test":
        TEST.test()

    sys.exit(0)

if __name__ == '__main__':
    main()
