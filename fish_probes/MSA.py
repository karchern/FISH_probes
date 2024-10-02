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
        print("Loading reference alignment, might mean entropy plot is not optimal.")
        #path = importlib_resources.files("fish_probes.reference_sequences").joinpath("reference_alignment.faa")
        path = importlib_resources.files("fish_probes.reference_sequences").joinpath("reference_alignment_2.faa")
        data = list(SeqIO.parse(path, "fasta"))
        return(MSA(data, aligned=True))

    @classmethod
    def from_alignment(cls, path: str):
        #path = importlib_resources.files("fish_probes.reference_sequences").joinpath("reference_alignment.faa")
        data = list(SeqIO.parse(path, "fasta"))
        return(MSA(data, aligned=True))

    #@property
    @cached_property
    def entropy_rolling_window(self):
        return MSA.calculate_entropy_rolling_window(self)

    @cached_property
    def consensus(self):
        return MSA.calculate_consensus(self)

    def calculate_entropy_rolling_window(self, window_size = 25) -> List[float]:
        if not self.aligned:
            raise ValueError("Cannot calculate entropy from unaligned sequences") from None        
        entropies = []
        alignment_length = len(self.sequences[0])
        for i in range(alignment_length):
            start = max(0, i - window_size // 2)
            end = min(alignment_length, start + window_size)
            window = [seq.seq[start:end] for seq in self.sequences]
            window_counter = Counter(window)
            window_length = len(window)
            entropy = 0
            for count in window_counter.values():
                frequency = count / window_length
                entropy -= frequency * log2(frequency)
            entropies.append(entropy)
        return entropies
    
    def calculate_consensus(self) -> List[str]:
        if not self.aligned:
            raise ValueError("Cannot calculate consensus sequence from unaligned sequences") from None
        consensus = []
        alignment_length = len(self.sequences[0])
        for i in range(alignment_length):
            column = [seq.seq[i] for seq in self.sequences]
            column_counter = Counter(column)
            consensus.append(column_counter.most_common(1)[0][0])
        return consensus



if __name__ == "__main__":
    msa = MSA.from_reference_alignment()
    entropy = msa.entropy_rolling_window