import sys
from fish_probes import UTIL_log

# ------------------------------------------------------------------------------
# main menu
# ------------------------------------------------------------------------------
def main_message(tool_version):
    str_msg = '''
\00
'''
    # HEADER -------------------------------------------------------------------
    str_msg = str_msg+UTIL_log.colour("Program: ", "cyan")
    str_msg = str_msg+"fish_probes - a tool to design FISH probes for 16S sequences\n"

    str_msg = str_msg+UTIL_log.colour("Version: ", "cyan")
    str_msg = str_msg+str(tool_version)+"\n"

    str_msg = str_msg+UTIL_log.colour("Usage: ", "cyan")
    str_msg = str_msg+"fish_probes <command> [options]\n\n"

    str_msg = str_msg+UTIL_log.colour("Command:\n", "cyan")

    # COMMANDS -----------------------------------------------------------------
    str_msg = str_msg+UTIL_log.colour("   design       ", "green_bold")
    str_msg = str_msg+"Identify suitable probes for a given clade\n"

    str_msg = str_msg+UTIL_log.colour("   check_probe  ", "green_bold")
    str_msg = str_msg+"Check physical properties of a probe\n"

    str_msg = str_msg+UTIL_log.colour("   test         ", "green_bold")
    str_msg = str_msg+"Test the tool\n"

    # CONCLUDING ---------------------------------------------------------------
    str_msg = str_msg+"\nType fish_probes <command> to print the help for a specific command"

    return str_msg


# ------------------------------------------------------------------------------
# design menu
# ------------------------------------------------------------------------------
def design():
    # HEADER -------------------------------------------------------------------
    sys.stderr.write("\n")
    sys.stderr.write(UTIL_log.colour("Usage: ", "cyan"))
    sys.stderr.write("fish_probes design ")
    sys.stderr.write(UTIL_log.colour("-s ", "blue"))
    sys.stderr.write("<seq> ")
    sys.stderr.write(UTIL_log.colour("-t ", "blue"))
    sys.stderr.write("<tax> ")
    sys.stderr.write(UTIL_log.colour("-c ", "blue"))
    sys.stderr.write("<clade>")

    sys.stderr.write(" [option]\n\n")

    # PARAMETERS ---------------------------------------------------------------
    sys.stderr.write(UTIL_log.colour("   -s  ","blue"))
    sys.stderr.write("FILE    ")
    sys.stderr.write("fasta file with the 16S sequences")
    sys.stderr.write(UTIL_log.colour("\n", "magenta"))

    sys.stderr.write(UTIL_log.colour("   -t  ","blue"))
    sys.stderr.write("FILE    ")
    sys.stderr.write("file with the taxonomy for the 16S sequences provided in -s")
    sys.stderr.write(UTIL_log.colour("\n", "magenta"))

    sys.stderr.write(UTIL_log.colour("   -c  ","blue"))
    sys.stderr.write("STR     ")
    sys.stderr.write("clade for which we need to find the probe (if more than one, separate with spaces)")
    sys.stderr.write(UTIL_log.colour("\n", "magenta"))

    sys.stderr.write(UTIL_log.colour("   -k  ","blue"))
    sys.stderr.write("INT     ")
    sys.stderr.write("length of the probe")
    sys.stderr.write(UTIL_log.colour(" [20]\n", "magenta"))

    sys.stderr.write(UTIL_log.colour("   -o  ","blue"))
    sys.stderr.write("FILE    ")
    sys.stderr.write("output file name")
    sys.stderr.write(UTIL_log.colour(" [stdout]\n", "magenta"))

    sys.stderr.write(UTIL_log.colour("   -p  ","blue"))
    sys.stderr.write("FLOAT   ")
    sys.stderr.write("minimum fraction of sequences that should contain the selected probe")
    sys.stderr.write(UTIL_log.colour(" [0.9]\n", "magenta"))

    sys.stderr.write(UTIL_log.colour("   -v  ","blue"))
    sys.stderr.write("INT     ")
    sys.stderr.write("verbose level: 1=error, 2=warning, 3=message, 4+=debugging")
    sys.stderr.write(UTIL_log.colour(" [3]\n", "magenta"))


# ------------------------------------------------------------------------------
# test_probe menu
# ------------------------------------------------------------------------------
def test_probe():
    # HEADER -------------------------------------------------------------------
    sys.stderr.write("\n")
    sys.stderr.write(UTIL_log.colour("Usage: ", "cyan"))
    sys.stderr.write("fish_probes test_probe ")
    sys.stderr.write(UTIL_log.colour("-i ", "blue"))
    sys.stderr.write("<probe_seq> ")

    sys.stderr.write(" [option]\n\n")

    # PARAMETERS ---------------------------------------------------------------
    sys.stderr.write(UTIL_log.colour("   -i  ","blue"))
    sys.stderr.write("STR     ")
    sys.stderr.write("probe to test")
    sys.stderr.write(UTIL_log.colour("\n", "magenta"))

    sys.stderr.write(UTIL_log.colour("   -sp ","blue"))
    sys.stderr.write("        ")
    sys.stderr.write("Evaluate also the two half of the probes alone")
    sys.stderr.write(UTIL_log.colour("\n", "magenta"))

    sys.stderr.write(UTIL_log.colour("   -v  ","blue"))
    sys.stderr.write("INT     ")
    sys.stderr.write("verbose level: 1=error, 2=warning, 3=message, 4+=debugging")
    sys.stderr.write(UTIL_log.colour(" [3]\n", "magenta"))
