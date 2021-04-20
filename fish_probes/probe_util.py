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
