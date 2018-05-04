# Inkwell-Inc-Generic
 This repository is reserved for the generic code of our text adventure development library.

 This library allows you to easily build a functioning text adventure and contains a demo game that can be played straight away. Be aware that you need to be running Python 2.7.12 to run this game (such as through a virtual environment). To install the library, navigate to the directory containing ```setup.py``` from your console and run the file by typing:

    python setup.py install

 To make a temporary installation for your current session type:

    python setup.py develop

 The ```game.py, game_items.py, game_player.py, game_enemies.py and game_map.py``` files can be copied and run from anywhere on your computer but must be kept together. To play the demo game, simply navigate to the directory that contains these files, the same directory as ```setup.py``` by default, and run ```game.py```. To create your own game, you can simply copy these four files into a different directory and edit the latter four files appropriately. Similarly, you can then play your game by navigating to this directory and running the ```game.py``` file.

 When playing the game, you can type commands from the list that displays to perform an action. If the action requires additional input, you will be prompted to give it.
