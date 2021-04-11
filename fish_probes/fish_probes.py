#!/usr/bin/env python
import sys
try:
    from fish_probes import load_input, predict_probes, log
except Exception as e:
    sys.stderr.write("Error 1: Unable to load the python packages. Message:\n")
    sys.stderr.write(str(e)+"\n")
    sys.exit(1)

import time

def main():
    t0 = time.time()

    # load the input files
    sequences,taxonomy,sel_clade,\
      probe_len,verbose,outfile = load_input.load_and_check_input()

    # find probes
    predict_probes.predict_probes(sequences,\
                                  taxonomy,\
                                  sel_clade,\
                                  probe_len,\
                                  verbose,\
                                  outfile)

    sys.exit(0)

if __name__ == '__main__':
    main()
