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
    ) -> plt:
        for info in kmer_info:
            taxon = info[0]
            probe = info[1]
            start_pos = info[2]
            print(f"Probe: {probe}, start_pos: {start_pos} on sequence itself")
            if start_pos is None:
                print("Probe not found in alignment, setting start_pos to 0.....")
                info[2] = 0
                info.extend([None, None, probe, len(probe), None])
                continue
            sequence = info[3]
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

        self.plot_object = self.entropy_plot(
            msa = msa,
            probe_positions = kmer_info,
        )


    def entropy_plot(
        self,
        msa: MSA.MSA,
        probe_positions: list,
    ) -> plt:
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.plot(msa.entropy_rolling_window)
        min_entropy, max_entropy = (min(msa.entropy_rolling_window), max(msa.entropy_rolling_window))
        offset_v = 0.1
        offset_increment = 0.1
        
        # Define a colormap from green to red using min_entropy and max_entropy as borders
        cmap = plt.cm.get_cmap('RdYlGn')
        norm = plt.Normalize(min_entropy, max_entropy)

        for probe_info in probe_positions:
            try:
                col = sum(msa.entropy_rolling_window[probe_info[4]:(probe_info[4]+probe_info[7])])/len(msa.entropy_rolling_window[probe_info[4]:(probe_info[4]+probe_info[7])])
            except:
                col = 'gray'
            if probe_info[4] is None:
                ax.plot([0, 0+probe_info[7]], [max_entropy * (1 + offset_v), max_entropy * (1 + offset_v)], color = 'gray', linewidth = 3, alpha = 0.3) # also add alpha
                ax.text(0, max_entropy * (1 + ((offset_v-offset_increment) + offset_increment * 0.5)), probe_info[6], va='bottom', ha='right', size = 8, color = 'black', alpha = 0.3)
                ax.text(len(msa.entropy_rolling_window)*1.025, max_entropy * (1 + ((offset_v-offset_increment) + offset_increment * 0.5)), probe_info[0], va='bottom', ha='left', size = 8, color = 'black', alpha = 0.3)
                ax.plot([0+probe_info[7] + 20, len(msa.entropy_rolling_window) * 1.125] , [max_entropy * (1 + offset_v), max_entropy * (1 + offset_v)], color = 'black', linewidth = 1, linestyle = "--", alpha = 0.3)
                offset_v += offset_increment
            else:
                ax.plot([probe_info[4], probe_info[4]+probe_info[7]], [max_entropy * (1 + offset_v), max_entropy * (1 + offset_v)], color = cmap(norm(col)), linewidth = 3)
                ax.text(probe_info[4]*0.98, max_entropy * (1 + ((offset_v-offset_increment) + offset_increment * 0.5)), probe_info[6], va='bottom', ha='right', size = 8, color = 'black')
                ax.text(len(msa.entropy_rolling_window)*1.025, max_entropy * (1 + ((offset_v-offset_increment) + offset_increment * 0.5)), probe_info[0], va='bottom', ha='left', size = 8, color = 'black')
                ax.plot([probe_info[4]+probe_info[7] + 20, len(msa.entropy_rolling_window) * 1.125] , [max_entropy * (1 + offset_v), max_entropy * (1 + offset_v)], color = 'black', linewidth = 1, linestyle = "--")
                offset_v += offset_increment                

            
        ax.set_ylabel("Entropy")
        ax.set_xlabel("Position along 16S rRNA gene")
        ax.set_ylim(min_entropy, max_entropy * 5)
        ax.set_xlim(-650, len(msa.entropy_rolling_window))
        #plt.subplots_adjust(left=0.1, right=0.6, bottom=0.1, top=0.6)
        plt.subplots_adjust(left=0.2, right=0.85, bottom=0.025, top=0.975)
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
    