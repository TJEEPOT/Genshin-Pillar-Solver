# What It Does #
This project solves the cyclical pillar puzzles in [Genshin Impact](https://genshin.mihoyo.com/) using AI (IDDFS
 Algorithm), written in Python. The script takes user input in the form of a binary array representing the state of
  the pillars in the puzzle being on or off and outputs instructions on which pillars to activate to quickly complete
   the puzzle. This project is based on my earlier work with AI as detailed in the 
    [8-Tile-Solution project](https://github.com/TJEEPOT/8-Tile-Solution) (which may still be private). 

# What I Learned #
Since the core was already written, I only had to work out how to solve the puzzle and add ways for the user to tell
 the program what the input is, and how to tell the user what to do. The basic version of just showing the path to
  the end state was easy enough, though.

# Usage Notes #
This script is written in Python 3, therefore I recommend installing the latest version of Python to run it. Open a
 terminal / command line / Powershell prompt in the folder the script is in and type ```python solver``` to run.
  Follow the prompts to correctly input your pillars: 
1. Start from the pillar in front of you in-game 
2. Type it's status as either a 0 if it's off, or 1 if it's on
3. Move clockwise (to the next pillar to the left) and do the same until you're at the pillar before the one you
 started at. i.e. for the 5-pillar puzzle in Domain of the Wayward Path: ![Pillar puzzle in Domain of the Wayward Path
 ](https://i.imgur.com/poOhufs.png), starting from the pillar to the right of the player character, we get the code
  `11010`.
4. The program will give you back a list of states from where you started from to the goal (11111 for a 5-pillar
 puzzle).
 
This program can work from any initial state, so don't worry if you've already tried to solve the puzzle in your game,
 just follow the steps above to input the puzzle from your current state and it will tell you where to move next.