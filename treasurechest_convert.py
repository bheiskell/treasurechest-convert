"""
Converts TreasureChest chests.yml file into the new multi-file format.
"""
from yaml import load, dump
from os import mkdir
from os.path import isdir, isfile
from sys import argv

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

if len(argv) != 3:
    raise ValueError("Usage: %s plugins/TreasureChest/chests.yml "\
          "plugins/TreasureChest/treasure\n"\
          "Remember to backup your treasure directory!"\
          % argv[0])

chests_file = argv[1]
destination = argv[2]

assert isfile(chests_file)
assert isdir(destination)

chests_stream = file(chests_file, 'r')
chests_object = load(chests_stream, Loader=Loader)

for key, chest in chests_object['chests']['chests'].iteritems():

    new_chest = {
        'location': {
            '==': 'com.mtihc.minecraft.treasurechest.v8.core.TreasureChest',
            'container': {
                '==': 'com.mtihc.minecraft.treasurechest.v8.core.BlockInventory',
                'world': chest['location']['world'],
                'coords': {
                    '==': 'Vector',
                    'x': chest['location']['vec']['x'],
                    'y': chest['location']['vec']['y'],
                    'z': chest['location']['vec']['z'],
                },
                'type': 'CHEST',
                'size': chest['inventory']['size'],
                'contents': {},
            },
            'messages': {
               'UNLIMITED': chest['messages']['FOUND_UNLIMITED'],
               'FOUND': chest['messages']['FOUND'],
               'FOUND_ALREADY': chest['messages']['FOUND_ALREADY'],
            },
            'ranks': [],
            'random': chest['randomness'],
            'forget-time': chest['forgetTime'],
            'ignore-protection': chest['ignoreProtection'],
            'rewards': {},
            'unlimited': chest['isUnlimited'],
        },
    }

    for item_key, item in chest['inventory']['items'].iteritems():

        new_chest['location']['container']['contents'][item_key] = {
            '==': 'com.mtihc.minecraft.treasurechest.v8.core.ItemStackWrapper',
            'stack': item,
        }

    world_directory = '%s/%s' % (destination, chest['location']['world'])
    if not isdir(world_directory):
        mkdir(world_directory)

    chest_file = '%s/%s_%s_%s.yml' % (world_directory,
        int(chest['location']['vec']['x']),
        int(chest['location']['vec']['y']),
        int(chest['location']['vec']['z']))

    chest_stream = file(chest_file, 'w')
    dump(new_chest, chest_stream, Dumper=Dumper, default_flow_style=False)

    #print dump(chests, Dumper=Dumper, default_flow_style=False)
    #print dump(new_chest, Dumper=Dumper, default_flow_style=False)
