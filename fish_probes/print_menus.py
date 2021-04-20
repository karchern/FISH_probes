import sys


# ------------------------------------------------------------------------------
# main menu
# ------------------------------------------------------------------------------
def main_message(name=None):
    str_msg = '''
\00
Program: fish_probes - a tool to design FISH probes for 16S sequences
Usage: fish_probes <command> [options]

Command:
   design       Identify suitable probes for a given clade
   test_probe   Test properties of a probe

Type ish_probes <command> to print the help for a specific command
        '''
    return str_msg


# ------------------------------------------------------------------------------
# design menu
# ------------------------------------------------------------------------------
def design():
    sys.stderr.write("\n")
    sys.stderr.write("Usage: fish_probes design -s <seq> -t <tax> -c CLADE [options]\n\n")
    sys.stderr.write("Options:\n")
    sys.stderr.write("   -s  FILE    fasta file with the 16S sequences\n")
    sys.stderr.write("   -t  FILE    file with the taxonomy for the 16S sequences provided in -s\n")
    sys.stderr.write("   -c  STR     clade for which we need to find the probe\n")
    sys.stderr.write("   -k  INT     length of the probe [20]\n")
    sys.stderr.write("   -o          output file name [stdout]\n")
    sys.stderr.write("   -p  FLOAT   minimum fraction of sequences that should contain the selected probe [0.9]\n")
    sys.stderr.write("   -v  INT     verbose level: 1=error, 2=warning, 3=message, 4+=debugging [3]\n\n")

# ------------------------------------------------------------------------------
# test_probe menu
# ------------------------------------------------------------------------------
def test_probe():
    sys.stderr.write("\n")
    sys.stderr.write("Usage: fish_probes test_probe -i SEQUENCE [options]\n\n")
    sys.stderr.write("Options:\n")
    sys.stderr.write("   -i  STR   probe to test\n")
    sys.stderr.write("   -v  INT   verbose level: 1=error, 2=warning, 3=message, 4+=debugging [3]\n\n")
