import sys
from fish_probes import log

# ------------------------------------------------------------------------------
# main menu
# ------------------------------------------------------------------------------
def main_message(name=None):
    str_msg = '''
\00
'''
    # HEADER -------------------------------------------------------------------
    str_msg = str_msg+log.colour("Program: ", "cyan")
    str_msg = str_msg+"fish_probes - a tool to design FISH probes for 16S sequences\n"

    str_msg = str_msg+log.colour("Usage: ", "cyan")
    str_msg = str_msg+"fish_probes <command> [options]\n\n"

    str_msg = str_msg+log.colour("Command:\n", "cyan")

    # COMMANDS -----------------------------------------------------------------
    str_msg = str_msg+log.colour("   design       ", "green_bold")
    str_msg = str_msg+"Identify suitable probes for a given clade\n"

    str_msg = str_msg+log.colour("   test_probe   ", "green_bold")
    str_msg = str_msg+"Test properties of a probe\n"

    # CONCLUDING ---------------------------------------------------------------
    str_msg = str_msg+"\nType fish_probes <command> to print the help for a specific command"

    return str_msg


# ------------------------------------------------------------------------------
# design menu
# ------------------------------------------------------------------------------
def design():
    # HEADER -------------------------------------------------------------------
    sys.stderr.write("\n")
    sys.stderr.write(log.colour("Usage: ", "cyan"))
    sys.stderr.write("fish_probes design ")
    sys.stderr.write(log.colour("-s ", "blue"))
    sys.stderr.write("<seq> ")
    sys.stderr.write(log.colour("-t ", "blue"))
    sys.stderr.write("<tax> ")
    sys.stderr.write(log.colour("-c ", "blue"))
    sys.stderr.write("<clade>")

    sys.stderr.write(" [option]\n\n")

    # PARAMETERS ---------------------------------------------------------------
    sys.stderr.write(log.colour("   -s  ","blue"))
    sys.stderr.write("FILE    ")
    sys.stderr.write("fasta file with the 16S sequences")
    sys.stderr.write(log.colour("\n", "magenta"))

    sys.stderr.write(log.colour("   -t  ","blue"))
    sys.stderr.write("FILE    ")
    sys.stderr.write("file with the taxonomy for the 16S sequences provided in -s")
    sys.stderr.write(log.colour("\n", "magenta"))

    sys.stderr.write(log.colour("   -c  ","blue"))
    sys.stderr.write("STR     ")
    sys.stderr.write("clade for which we need to find the probe")
    sys.stderr.write(log.colour("\n", "magenta"))

    sys.stderr.write(log.colour("   -k  ","blue"))
    sys.stderr.write("INT     ")
    sys.stderr.write("length of the probe")
    sys.stderr.write(log.colour(" [20]\n", "magenta"))

    sys.stderr.write(log.colour("   -o  ","blue"))
    sys.stderr.write("FILE    ")
    sys.stderr.write("output file name")
    sys.stderr.write(log.colour(" [stdout]\n", "magenta"))

    sys.stderr.write(log.colour("   -p  ","blue"))
    sys.stderr.write("FLOAT    ")
    sys.stderr.write("minimum fraction of sequences that should contain the selected probe")
    sys.stderr.write(log.colour(" [0.9]\n", "magenta"))

    sys.stderr.write(log.colour("   -v  ","blue"))
    sys.stderr.write("INT     ")
    sys.stderr.write("verbose level: 1=error, 2=warning, 3=message, 4+=debugging")
    sys.stderr.write(log.colour(" [3]\n", "magenta"))


# ------------------------------------------------------------------------------
# test_probe menu
# ------------------------------------------------------------------------------
def test_probe():
    # HEADER -------------------------------------------------------------------
    sys.stderr.write("\n")
    sys.stderr.write(log.colour("Usage: ", "cyan"))
    sys.stderr.write("fish_probes test_probe ")
    sys.stderr.write(log.colour("-i ", "blue"))
    sys.stderr.write("<probe_seq> ")

    sys.stderr.write(" [option]\n\n")

    # PARAMETERS ---------------------------------------------------------------
    sys.stderr.write(log.colour("   -i  ","blue"))
    sys.stderr.write("STR    ")
    sys.stderr.write("probe to test")
    sys.stderr.write(log.colour("\n", "magenta"))

    sys.stderr.write(log.colour("   -v  ","blue"))
    sys.stderr.write("INT     ")
    sys.stderr.write("verbose level: 1=error, 2=warning, 3=message, 4+=debugging")
    sys.stderr.write(log.colour(" [3]\n", "magenta"))
