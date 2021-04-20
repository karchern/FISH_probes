# find the gc content of a probe
def gc_content(sequence):
    n_gc = 0
    for c in sequence:
        if c == "C" or c == "c" or c == "G" or c == "g":
            n_gc = n_gc + 1
    return (n_gc / float(len(sequence)) ) * 100

# find sequence entropy
def sequence_entropy(sequence):
    return 0

# find melting temperature
def melting_temperature(sequence):
    return 0

# add variables for printing
def create_to_print(sequence, header = False):
    if header:
        this_str = "GC_content\tsequence_entropy\tmelting_temperature\n"
    else:
        this_str = ""
    this_str = this_str+str(gc_content(sequence))+"\t"
    this_str = this_str+str(sequence_entropy(sequence))+"\t"
    this_str = this_str+str(melting_temperature(sequence))
    return this_str
