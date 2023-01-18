# ANZT Amplifier Randomiser

###### Thrown together in one night, with very very limited experience in windows applications and tkinter. The code works and makes sense, but by god are the design and naming conventions a mess. I'll refactor this at some point :)

Created for [ANZT 10 Summer](https://osu.ppy.sh/community/forums/topics/1699251) (an osu! Standard tournament), the ANZT Amplifier Randomiser is a desktop application that, with a list of player avatars, and a set of pre-created cards, will randomly assign 3 cards to each player, and output the data to a csv file.

## Setup

This was really not designed for use other than by myself, however it shouldn't be too difficult to set up. Ensure the Python modules customtkinter and PIL are installed, then run main.py. 

## Usage

The main GUI has three buttons; Next, Prev, and Roll.

All self explanatory, next and prev navigate between viable players, and roll will select 3 cards for the current player. Data is automatically updated and saved, so you can reroll a player multiple times and exit the application at any time. *Relaunching the application without doing anything with the saved data will overwrite it.*

## Change input

Inside of the *data* directory are two folders, *amplifiers* and *players*. 

*Amplifiers* is a list of card images, of which the names are irrelevant. The current sizing is designed for 836x1077 cards.

*Players* is a list of player avatars, all of which arenamed after the respective player. The current sizing is designed for 256x256 avatars.

Inside of *data* are two images, *stream_bg.png* and *Box.png*. The background is self explanatory, and the box is used to replace a card when cycling through players to create a blank screen. It doesn't look the best visually as tkinter doesn't support transparency, so solid colours were neccessary.

## Changing resolution

Don't.
