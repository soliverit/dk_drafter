class Tile():
	# Tile types. Some dirty, convenient constants
	LABELED_PROPERTIES	= 	{
		"CLAIMED":{"label": "c", "colour": (0, 0, 153), "drawLabel": "A"},
		"DIRT":{"label": "d", "colour":(0, 0, 0), "drawLabel": " "},
		"REINFORCED": {"label": "r", "colour":(255, 255, 255), "drawLabel": "B"},
		"WATER": {"label": "w", "colour":(0, 176, 240), "drawLabel": "C"},
		"LAVA": {"label": "l", "colour":(204, 176, 0), "drawLabel": "D"},
		"IMPENETRABLE": {"label": "d", "colour":(102 , 51, 0), "drawLabel": "E"},
		"BARRACKS": {"label": "ba", "colour":(160, 43, 147), "drawLabel": "F"},
		"BRIDGE": {"label": "br", "colour":(126, 53, 14), "drawLabel": "G"},
		"GRAVEYARD": {"label": "gr", "colour":(15, 158, 213), "drawLabel": "H"},
		"GUARD_POST": {"label": "gu", "colour":(116,116, 116), "drawLabel": "I"},
		"HATCHERY": {"label": "ha", "colour":(233, 113, 50), "drawLabel": "J"},
		"LAIR": {"label": "la", "colour":(21, 96, 130), "drawLabel": "K"},
		"LIBRARY": {"label": "li", "colour":(112, 48, 160), "drawLabel": "L"},
		"PRISON": {"label": "pr", "colour":(241, 169, 131), "drawLabel": "M"},
		"SCAVENGER_ROOM": {"label": "sc", "colour":(173, 173, 173), "drawLabel": "N"},
		"TEMPLE": {"label": "te", "colour":(255 , 255, 0), "drawLabel": "O"},
		"TORTURE_CHAMBER": {"label": "to", "colour":(192 , 0, 0), "drawLabel": "P"},
		"TRAINING_ROOM": {"label": "tr", "colour":(60, 125, 34), "drawLabel": "Q"},
		"TREASURE_ROOM": {"label": "te", "colour":(255, 153, 0), "drawLabel": "R"},
		"WORKSHOP": {"label": "wo", "colour":(255 , 192, 0), "drawLabel": "S"}
	}
	KEYED_PROPERTIES	={						
		"c":{"label": "CLAIMED", "colour":(0 , 0, 0)},
		"d":{"label": "DIRT", "colour":(0 , 0, 0)},
		"r": {"label": "REINFORCED", "colour":(0 , 0, 0)},
		"w": {"label": "WATER", "colour":(0 , 0, 0)},
		"l": {"label": "LAVA", "colour":(0 , 0, 0)},
		"i": {"label": "IMPENETRABLE", "colour":(0 , 0, 0)},
		"ba": {"label": "BARRACKS", "colour":(0 , 0, 0)},
		"br": {"label": "BRIDGE", "colour":(0 , 0, 0)},
		"gr": {"label": "GRAVEYARD", "colour":(0 , 0, 0)},
		"gu": {"label": "GUARD_POST", "colour":(0 , 0, 0)},
		"ha": {"label": "HATCHERY", "colour":(0 , 0, 0)},
		"la": {"label": "LAIR", "colour":(0 , 0, 0)},
		"li": {"label": "LIBRARY", "colour":(0 , 0, 0)},
		"pr": {"label": "PRISON", "colour":(0 , 0, 0)},
		"sc": {"label": "SCAVENGER_ROOM", "colour":(0 , 0, 0)},
		"te": {"label": "TEMPLE", "colour":(0 , 0, 0)},
		"to": {"label": "TORTURE_CHAMBER", "colour":(0 , 0, 0)},
		"tr": {"label": "TRAINING_ROOM", "colour":(0 , 0, 0)},
		"te": {"label": "TREASURE_ROOM", "colour":(0 , 0, 0)},
		"wo": {"label": "WORKSHOP", "colour":(0 , 0, 0)}
	}
	CLAIMED			= "CLAIMED"
	DIRT			= "DIRT"
	REINFORCED		= "REINFORCED"
	WATER			= "WATER"
	LAVA			= "LAVA"
	IMPENETRABLE	= "IMPENETRABLE"
	BARRACKS		= "BARRACKS"
	GRAVEYARD		= "GRAVEYARD"
	GUARD_POST		= "GUARD_POST"
	HATCHERY		= "HATCHERY"
	LAIR			= "LAIR"
	LIBRARY			= "LIBRARY"
	PRISON			= "PRISON"
	SCAVENGER_ROOM	= "SCAVENGER_ROOM"
	TEMPLE			= "TEMPLE"
	TORTURE_CHAMBER	= "TORTURE_CHAMBER"
	TRAINING_ROOM	= "TRAINING_ROOM"
	TREASURE_ROOM	= "TREASURE_ROOM"
	WORKSHOP		= "WORKSHOP"
	def __init__(self, alias, playerID):
		self.alias		= alias		# LABELED_PROPERTIES keyword. E.g. self.DIRT
		self.playerID	= playerID	# ID of Player. Kind of redundant but might be useful
	# Colour tuple for Pillow (image drawer)	
	@property
	def colour(self):
		return self.__class__.LABELED_PROPERTIES[self.alias]["colour"]
	# Excel cell label
	@property
	def label(self):
		return self.__class__.LABELED_PROPERTIES[self.alias]["label"]
	# Single character assigned to each label for drawing to console.
	@property
	def drawLabel(self):
		return self.__class__.LABELED_PROPERTIES[self.alias]["drawLabel"]