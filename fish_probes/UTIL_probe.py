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
def create_to_print(sequence, header = False, split = False):
    if header:
        if split:
            # if split is true we print the info for the first and the second
            # half
            this_str = "GC_content\tsequence_entropy\tmelting_temperature\tPleft_GC_content\tPleft_sequence_entropy\tPleft_melting_temperature\tPright_GC_content\tPright_sequence_entropy\tPright_melting_temperature\n"
        else:
            this_str = "GC_content\tsequence_entropy\tmelting_temperature\n"
    else:
        this_str = ""
    # main part of the probe
    this_str = this_str+str(gc_content(sequence))+"\t"
    this_str = this_str+str(sequence_entropy(sequence))+"\t"
    this_str = this_str+str(melting_temperature(sequence))

    # if we print also the probe as split in two
    if split:
        half = round(len(sequence)/2)
        probe_left = sequence[0:half]
        probe_right = sequence[half:]
        # we add the measures
        this_str = this_str+"\t"
        this_str = this_str+str(gc_content(probe_left))+"\t"
        this_str = this_str+str(sequence_entropy(probe_left))+"\t"
        this_str = this_str+str(melting_temperature(probe_left))+"\t"
        # right
        this_str = this_str+str(gc_content(probe_right))+"\t"
        this_str = this_str+str(sequence_entropy(probe_right))+"\t"
        this_str = this_str+str(melting_temperature(probe_right))
    return this_str
