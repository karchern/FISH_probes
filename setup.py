from setuptools import setup

setup(
    name='fish_probes',
    version='0.0.0',
    author='Alessio Milanese',
    author_email='milanese.alessio@gmail.com',
    entry_points={
        'console_scripts': [
            'fish_probes = util.fish_probes:main',
        ]
    }
)
