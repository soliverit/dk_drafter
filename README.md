# dk_drafter
Excel/Python lib for drawing Dungeon Keeper maps without a map editor

## What is it?
An object model and Excel spreadsheet template. The spreadsheet is used to design Dungeons. The object model creates a Tile map that can be used to modify the model and convert to an image.

## What does it do?
It provides a way for drawing dungeons in Excel or in Python and building a simple object model in Python.

Example:

<img src="https://i.imgur.com/QuGPFdy.png" width="300">

Can be modified using the library then converted to an image.

Example: 

<img src="https://imgur.com/jAnV5hf.png" width="300">

## Getting started (developed with Python 3.1. Any 3 should be fine).
- Install pandas (DataFrame library that parses the spreadsheet)
- Install pillow (Image drawing library)

```python

# Create a blank Map with 32*32 tiles
map	= Map(32, 32)
##
# Parse spreadsheet
#
# Read the contents of a spreadsheet based on "./base.xlsx", ideally from "./drafts/". Spreadsheets
# contain cells with one or two character labels for Tile types and possibly a Player ID.
#
# Single character labels denote surfaces, two character activity spaces excluding circulation (change that, man)
#
# For example: "La 2" or "la2" both mean Lair owned by Player 2. "La" and "la" are Player 1 by default.
#
# Tile lables (taken from ./lib/tile.py)
# KEYED_PROPERTIES	={						
# "c":{"label": "CLAIMED"},
# "d":{"label": "DIRT"},
# "r": {"label": "REINFORCED"},
# "w": {"label": "WATER"},
# "l": {"label": "LAVA"},
# "i": {"label": "IMPENETRABLE"},
# "ba": {"label": "BARRACKS"},
# "br": {"label": "BRIDGE"},
# "gr": {"label": "GRAVEYARD"},
# "gu": {"label": "GUARD_POST"},
# "ha": {"label": "HATCHERY"},
# "la": {"label": "LAIR"},
# "li": {"label": "LIBRARY"},
# "pr": {"label": "PRISON"},
# "sc": {"label": "SCAVENGER_ROOM"},
# "te": {"label": "TEMPLE"},
# "to": {"label": "TORTURE_CHAMBER"},
# "tr": {"label": "TRAINING_ROOM"},
# "te": {"label": "TREASURE_ROOM"},
# "wo": {"label": "WORKSHOP"}
# }
#
# Notes:
#	- Spreadsheet and Map sizes are independent. If the Map is smaller than the spreadsheet. Only the 
#	  Map dimensions are parsed.
##
map.parseExcel("./drafts/example.xlsx")
# Draw Map to conosole: Just random single character assigned to Tile types for dirty viewing pleasure
map.drawToConsole()
##
# Draw an image using Pillow
##
# Number of pixel per Tile
map.drawSize	= 50
map.drawImage()	# Include path="./some_path.jpg" to write to file
```

