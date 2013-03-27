from distutils.core import setup

setup(
    name='TreasureChest Convert',
    version='1.0.0',
    author='Ben Heiskell',
    author_email='ben.heiskell@xdxa.org',
    scripts=['treasurechest_convert.py'],
    license='LICENSE.txt',
    description='Convert TreasureChest chests.yml to new multi-file format.',
    long_description=open('README.txt').read(),
    install_requires=[
        "pyyaml == 3.10",
    ],
)
