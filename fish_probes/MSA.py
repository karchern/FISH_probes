import importlib_resources
from dataclasses import dataclass
from Bio import SeqIO
from typing import List

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
            raise ValueError("All sequences must have the same length") from None
        self._sequences = value

    @classmethod
    def from_reference_alignment(cls):
        path = importlib_resources.files("fish_probes.reference_sequences").joinpath("reference_alignment.faa")
        data = list(SeqIO.parse(path, "fasta"))
        return(MSA(data))

if __name__ == "__main__":
    msa = MSA.from_reference_alignment()