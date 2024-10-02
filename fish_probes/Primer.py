from collections import namedtuple

Primer = namedtuple('Primer', ['forward_primer', 'reverse_primer', 'forward_sequence', 'reverse_sequence', 'specificity', 'annealing_temp', 'reference'])

PRIMERS = {
    "V1_V2": Primer(
        forward_primer="27F",
        reverse_primer="338R",
        forward_sequence="AGAGTTTGATYMTGGCTCAG",
        reverse_sequence="GCTGCCTCCCGTAGGAGT",
        specificity="Universal",
        annealing_temp=57,
        reference="Salter et al. (115)"
    ),
    "V1_V3": Primer(
        forward_primer="27F",
        reverse_primer="534R",
        forward_sequence="AGAGTTTGATYMTGGCTCAG",
        reverse_sequence="ATTACCGCGGCTGCTGG",
        specificity="Universal",
        annealing_temp=57,
        reference="Walker et al. (84)"
    ),
    "V3_V4": Primer(
        forward_primer="341F",
        reverse_primer="785R",
        forward_sequence="CCTACGGGNGGCWGCAG",
        reverse_sequence="GACTACHVGGGTATCTAATCC",
        specificity="Universal",
        annealing_temp=55,
        reference="Klindworth et al. (70)"
    ),
    "V4": Primer(
        forward_primer="515F",
        reverse_primer="806R",
        forward_sequence="GTGCCAGCMGCCGCGGTAA",
        reverse_sequence="GGACTACHVGGGTWTCTAAT",
        specificity="Universal",
        annealing_temp=53,
        reference="Caporaso et al. (116)"
    ),
    "V4_V5": Primer(
        forward_primer="515F",
        reverse_primer="944R",
        forward_sequence="GTGCCAGCMGCCGCGGTAA",
        reverse_sequence="GAATTAAACCACATGCTC",
        specificity="Bacterial",
        annealing_temp=53,
        reference="Fuks et al. (117)"
    ),
    "V6_V8": Primer(
        forward_primer="939F",
        reverse_primer="1378R",
        forward_sequence="GAATTGACGGGGGCCCGCACAAG",
        reverse_sequence="CGGTGTGTACAAGGCCCGGGAAACG",
        specificity="Bacterial",
        annealing_temp=58,
        reference="Lebuhn et al. (118)"
    ),
    "V7_V9": Primer(
        forward_primer="1115F",
        reverse_primer="1492R",
        forward_sequence="CAACGAGCGCAACCCT",
        reverse_sequence="TACGGYTACCTTGTTACGACTT",
        specificity="Bacterial",
        annealing_temp=51,
        reference="Turner et al. (119)"
    )
}

