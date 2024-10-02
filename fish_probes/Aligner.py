from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from dataclasses import dataclass

@dataclass
class PairwiseAligner:
    seq1: str
    seq2: str

    @property
    def seq1(self):
        return self._seq1

    @seq1.setter
    def seq1(self, value):
        if not isinstance(value, str):
            raise ValueError("seq1 must be a string") from None
        self._seq1 = value.upper()

    @property
    def seq2(self):
        return self._seq2

    @seq2.setter
    def seq2(self, value):
        if not isinstance(value, str):
            raise ValueError("seq2 must be a string") from None
        
        self._seq2 = value.upper()

    def __repr__(self):
        return f"PairwiseAligner object with sequences {self.seq1} and {self.seq2}"

    def align_locally_and_return_alignments(self):
        alignments = pairwise2.align.localmd(self.seq1, self.seq2, 2,-5,-6,-3,-100,0,one_alignment_only=True )
        assert len(alignments) == 1
        formatted_alignment = format_alignment(*alignments[0])
        print(formatted_alignment)
        return((formatted_alignment, alignments[0]))


