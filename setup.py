from setuptools import setup, find_packages

# setup
setup(
    name='fish_probes',
    version='0.1.1',
    author='Alessio Milanese',
    author_email='milanese.alessio@gmail.com',
    packages=find_packages(exclude=["test"]),
    # we add the test files
    package_data={
        "fish_probes.test": ["seq.fa", "tax"],
        'fish_probes.reference_sequences' : ['reference_alignment.faa', 'reference_alignment_2.faa']
    },
    # entry point
    entry_points={
        'console_scripts': [
            'fish_probes = fish_probes.MAIN:main',
        ]
    },
    install_requires=[
        'json',
        'biopython',
        'matplotlib',
    ],
    include_package_data=True,
)
