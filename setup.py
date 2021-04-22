from setuptools import setup, find_packages

# import version from init
version_init = [line.strip().split(" ")[-1] for line in open("fish_probes/__init__.py") if line.startswith("__version__")][0]

# setup
setup(
    name='fish_probes',
    version=version_init,
    author='Alessio Milanese',
    author_email='milanese.alessio@gmail.com',
    # we add the test files
    package_data={
        "fish_probes.test": ["seq.fa", "tax"]
    },
    # entry point
    entry_points={
        'console_scripts': [
            'fish_probes = fish_probes.MAIN:main',
        ]
    }
)
