import importlib_resources
from dataclasses import dataclass
from Bio import SeqIO
from typing import List
from collections import Counter
from math import log2
from functools import cached_property

@dataclass
class MSA:
    sequences: List[SeqIO.SeqRecord]
    aligned: bool = False

    def __repr__(self):
        return "MSA object with {} sequences".format(len(self._sequences))

    @property
    def sequences(self):
        return self._sequences

    @sequences.setter
    def sequences(self, value):
        if not isinstance(value, list):
            raise ValueError("Sequences must be list") from None
        if not all([isinstance(x, SeqIO.SeqRecord) for x in value]):
            raise ValueError("Sequences must be list of SeqIO.SeqRecord objects") from None
        if not len(set(map(len, value))) == 1:
            raise ValueError("All sequences in an alignment must have the same length - are you sure you supplied a multiple sequence alignment?") from None
        self._sequences = value

    @classmethod
    def from_reference_alignment(cls):
        path = importlib_resources.files("fish_probes.reference_sequences").joinpath("reference_alignment.faa")
        data = list(SeqIO.parse(path, "fasta"))
        return(MSA(data))

    #@property
    @cached_property
    def entropy(self):
        print("Calculating entropy - but only because you asked :)")
        return MSA.calculate_entropy(self)

    def calculate_entropy(self):
        entropies = []
        alignment_length = len(self.sequences[0])
        for i in range(alignment_length):
            column = [seq.seq[i] for seq in self.sequences]
            column_counter = Counter(column)
            column_length = len(column)
            entropy = 0
            for count in column_counter.values():
                frequency = count / column_length
                entropy -= frequency * log2(frequency)
            entropies.append(entropy)
        return entropies



if __name__ == "__main__":
    msa = MSA.from_reference_alignment()
    entropy = msa.entropy