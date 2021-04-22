import sys
import os
import pkg_resources
from fish_probes import UTIL_log
import subprocess
import shlex

TEST_DATA_PATH = pkg_resources.resource_filename("fish_probes", "test")

def test():
    UTIL_log.print_log("Prepare test")
    UTIL_log.print_message("Run test on /fish_probes/test/.")

    # prepare command ----------------------------------------------------------
    to_run = "fish_probes design -c Firmicutes -k 7 -v1"
    to_run = to_run + " -s " + os.path.join(TEST_DATA_PATH, "seq.fa")
    to_run = to_run + " -t " + os.path.join(TEST_DATA_PATH, "tax")

    UTIL_log.print_message("Command:")
    UTIL_log.print_message(to_run+"\n")

    # we run the command -------------------------------------------------------
    UTIL_log.print_log("Run test")
    try:
        from subprocess import DEVNULL
    except ImportError:
        DEVNULL = open(os.devnull, 'wb')

    popenCMD = shlex.split(to_run)
    cmd = subprocess.Popen(popenCMD,stdout=subprocess.PIPE,stderr=DEVNULL)

    # save the result
    result = list()
    for line in cmd.stdout:
        result.append(line.decode('ascii'))

    # check exit status
    cmd.stdout.close()
    return_code = cmd.wait()
    if return_code:
        UTIL_log.print_error("Tool failed")
    else:
        UTIL_log.print_message("Command completed correctly.\n")


    # we check the result ------------------------------------------------------
    UTIL_log.print_log("Check result")

    # check that there is a header
    if not result[0].startswith("probe"):
        UTIL_log.print_error("Header incorrect:", exit = False)
        UTIL_log.print_error(result[0])


    # check that the probe with the highest priority is correct
    if not result[1].startswith("CTCGATT"):
        UTIL_log.print_error("Predicted probe not correct", exit = False)
        UTIL_log.print_error(result[1])

    UTIL_log.print_message("Result is correct.\n")
