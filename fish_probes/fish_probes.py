#!/usr/bin/env python
import sys
try:
    from fish_probes import load_input, predict_probes
except ImportError:
    sys.exit("CRITICAL ERROR: Unable to find the util python package.")

import time

def main():
    t0 = time.time()

    # load the input files
    sequences,taxonomy,sel_clade,\
      min_len,verbose,outfile = load_input.load_and_check_input()
    # find probes
    predict_probes.predict_probes(sequences,\
                                  taxonomy,\
                                  sel_clade,\
                                  min_len,\
                                  verbose,\
                                  outfile)

    sys.stderr.write('Elapsed time: {} s\n'.format( (time.time()-t0) ) )

if __name__ == '__main__':
    main()
