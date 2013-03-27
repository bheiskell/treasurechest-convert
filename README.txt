=======================
TreasureChest Converter
=======================

Converts the old chests.yml file format to the new multi-file format.

Typically I only upgrade plugins as needed. In TreasureChest's case I went several versions before upgrading to the new multi-file format. As a result, I couldn't use automagical embedded conversion command. This package performs that conversion manually.

This assumes you're in a *nix environment. For windows, just email me and I can perform the conversion for you.

    # create a working directory
    $ git clone ... ~/treasurechest
    $ cd ~/treasurechest

    # create a virtual environment and install this package
    $ virtualenv treasurechest_env
    $ . treasurechest_env/bin/activate
    $ easy_install .
    
    # get into position and run the conversion script
    $ cd path/to/usr/plugins/TreasureChest
    $ mkdir -p treasure
    $ treasurechest_convert.py chests.yml treasure

    # cleanup by removing the working directory
    $ rm -rf ~/treasurechest
    $ exit
