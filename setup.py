from setuptools import setup, find_packages

setup(
    name='fish_probes',
    version='0.0.0',
    author='Alessio Milanese',
    author_email='milanese.alessio@gmail.com',
    packages=find_packages(exclude=["test"]),
    entry_points={
        'console_scripts': [
            'fish_probes = fish_probes.MAIN:main',
        ]
    }
)
