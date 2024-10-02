import matplotlib.pyplot as plt
from fish_probes import MSA, Aligner
from typing import List
from dataclasses import dataclass

@dataclass
class ProbeMatch():
    start: int
    end: int
    sequence_id: str
    sequence_index: int
    hamming_distance: int

@dataclass
class ProbeMatchSet():
    probe_sequence: str
    probe_matches: List[ProbeMatch]

    @property
    def number_probe_matches(self): 
        return len(self.probe_matches)
    


class EntropyPlot():

    def __init__(
        self,
        msa: MSA.MSA,
        kmer_info: list[list],
        padding_for_alignment = 100
    ):
        for info in kmer_info:
            probe = info[0]
            start_pos = info[1]
            print(f"Probe: {probe}, start_pos: {start_pos} on sequence itself")
            if start_pos is None:
                print("Probe not found in alignment, setting start_pos to 0.....")
                info[1] = 0
                info.extend([0, 0, probe, len(probe), padding_for_alignment])
                continue
            sequence = info[2]
            #aligner = Aligner.PairwiseAligner(probe, "".join(msa.consensus))
            aligner = Aligner.PairwiseAligner(sequence[(start_pos - padding_for_alignment) : (start_pos + padding_for_alignment)], "".join(msa.consensus))
            (formatted_alignment, raw_alignment) = aligner.align_locally_and_return_alignments()
            #start_pos_of_alignment_in_extended_probe_sequence = int(formatted_alignment.split(" ")[2])
            start_pos_of_alignment_in_extended_probe_sequence = int(formatted_alignment.lstrip().split(" ")[0])
            len_of_alignment = raw_alignment.end - raw_alignment.start
            #print(f"Start pos of alignment in extended probe sequence (extended by {padding_for_alignment}): {start_pos_of_alignment_in_extended_probe_sequence}")
            start_pos_of_probe_on_ref_al = raw_alignment.start + ((padding_for_alignment - start_pos_of_alignment_in_extended_probe_sequence))
            #print(f"By extension, start pos of alignment OF PROBE on reference alignment): {start_pos_of_probe_on_ref_al}")
            #print(f"Length of alignment: {len_of_alignment}")
            info.extend([start_pos_of_probe_on_ref_al, start_pos_of_alignment_in_extended_probe_sequence, probe, len(probe), padding_for_alignment])

        plot_object = self.entropy_plot(
            msa = msa,
            probe_positions = kmer_info,
        )
        plt.show()

    def entropy_plot(
        self,
        msa: MSA.MSA,
        probe_positions: list,
    ) -> plt:
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.plot(msa.entropy_rolling_window)
        min_entropy, max_entropy = (min(msa.entropy_rolling_window), max(msa.entropy_rolling_window))
        offset_v = 0.1
        offset_increment = 0.1
        for probe_info in probe_positions:
            print(probe_info)
            # if offset_v >= 1:
            #     print(f"Too many probes to plot, stopping at {probe_info[5]}")
            #     break
            ax.plot([probe_info[3], probe_info[3]+probe_info[6]], [max_entropy * (1 + offset_v), max_entropy * (1 + offset_v)])
            ax.text(probe_info[3], max_entropy * (1 + ((offset_v-offset_increment) + offset_increment * 0.85)), probe_info[5], va='bottom', ha='right', size = 8)
            #ax.text(probe_info[3], max_entropy * (1 + ((offset_v-offset_increment) + offset_increment * 0.35)), probe_info[5], va='bottom', ha='right', size = 8)
            offset_v += offset_increment
            
        ax.set_ylabel("Entropy")
        ax.set_xlabel("Position along 16S rRNA gene")
        ax.set_ylim(min_entropy, max_entropy * 3)
        return(fig)

    @staticmethod
    def get_hamming(
        s1: str,
        s2: str
    ) -> float:
        if len(s1) != len(s2):
            raise ValueError("Sequences must be the same length") from None
        return sum([a != b for a, b in zip(s1, s2)])

    # @timer.timer
    # def get_probe_matches(
    #     self, 
    #     probe: str,
    #     msa: MSA.MSA,
    #     ) -> tuple[int]:
    #     probe_matches = []
    #     for i in range(len(msa.sequences[0])-len(probe)):
    #         for sequence_index, sequence in enumerate(msa.sequences):
    #             hd = self.get_hamming(probe, sequence.seq[i:i+len(probe)])
    #             if hd == 0:
    #                 probe_matches.append(ProbeMatch(i, i+len(probe) - 1, sequence.id, sequence_index, hd))                
    #                 return ProbeMatchSet(probe, probe_matches)            
    #             if hd < 2:
    #                 probe_matches.append(ProbeMatch(i, i+len(probe) - 1, sequence.id, sequence_index, hd))
    #     return ProbeMatchSet(probe, probe_matches)
    