import sys
import shutil
import tempfile
import os
from fish_probes import UTIL_log

################################################################################
# function to save lines into a file or print to stdout
################################################################################
#   - lines is a list with strings to print
#   - outfile is either a path to a file or if it is None, it will be printed in
#     in stdout
def save_file(lines,outfile):
    # set temp file
    try:
        if outfile is None:
            temp_file = sys.stdout
        else:
            temp_file = tempfile.NamedTemporaryFile(delete=False, mode="w")
            os.chmod(temp_file.name, 0o644)
    except Exception as e:
        UTIL_log.print_error("couldn't create the file. Message:",exit = False)
        UTIL_log.print_error(str(e))

    # write lines --------------------------------------------------------------
    for l in lines:
        temp_file.write(l)

    # close and move to final destination --------------------------------------
    if not outfile is None:
        try:
            temp_file.flush()
            os.fsync(temp_file.fileno())
            temp_file.close()
            shutil.move(temp_file.name,outfile)
        except Exception as e:
            UTIL_log.print_error("couldn't save the file:",exit = False)
            UTIL_log.print_error(str(e))
