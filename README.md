Set of scripts to identify FISH probes in 16S sequences.
The probes are unique for the selected clade.

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
