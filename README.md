16S FISH probes
========

This tool identify FISH probes from 16S sequences.
Given a clade, it identifies sequences (of a given length) that belong to that and only that clade.

Pre-requisites
--------------

The mOTU profiler requires:
* Python 3 (or higher)


Installation
--------------

First clone the repo:
```
git clone https://github.com/AlessioMilanese/FISH_probes.git
```

Setup:
```
cd FISH_probes
python setup.py bdist_wheel
pip install --no-deps --force-reinstall dist/*.whl
```

You will need a fasta file with 16S sequences and relative taxonomy.

Simple examples
--------------
