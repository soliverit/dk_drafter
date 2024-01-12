from os.path 	import exists
from pandas 	import read_excel
from math		import isnan
from lib.tile	import Tile
from PIL import Image, ImageDraw
##
# Map: A simple Dungeon Keeper map model
#
# Contains tile and play associations. 
##
class Map():
	MAP_IMAGE_PATH		= "C:/workspaces/dungeon_keeper/dungeon_drafter/images/map/gmap-32.png"
	MAP_WIDTH			= 320
	MAP_HEIGHT			= 200
	MAP_BASE_POINT_X	= 77
	MAP_BASE_POINT_Y	= 30
	MAP_BOX_SIZE		= 166
	def __init__(self, width, height):
		self.width			= width		# Dungeon width
		self.height			= height	# Dungeon height
		self.tiles		 	= False		# 2D tile map
		self.players		= []		# Player objects, labeled by number starting at 1.
		self.path			= False		# If parsed from a .xlsx, this is the path
		self.spreadsheet	= False		# Pandas table from the first spreadsheet in the path workbook
		self.drawSize		= 50		# No. pixels per tile on drawImage outputs
		self.rawImage		= False		# Draw image without map background
		self.prepareTiles()				# Create the 2D map with all dirt tiles
	##
	# Add a Player
	##
	def addPlayer(self, player):
		self.players.append(player)
	##
	# Draw the Map Tiles to an image, show it
	##
	def drawImage(self, path=False):
		# Canvas dimensions
		canvasWidth 	= self.width * self.drawSize if self.rawImage else self.__class__.MAP_WIDTH
		canvasHeight	= self.height * self.drawSize if self.rawImage else self.__class__.MAP_HEIGHT
		# Make the canvas
		if self.rawImage:
			im = Image.new('RGB', (canvasWidth, canvasHeight), Tile.LABELED_PROPERTIES[Tile.DIRT]["colour"])
		else:
			im	= Image.open(self.__class__.MAP_IMAGE_PATH)
		draw = ImageDraw.Draw(im)
		if not self.rawImage:
			draw.rectangle((self.__class__.MAP_BASE_POINT_X, self.__class__.MAP_BASE_POINT_Y, self.__class__.MAP_BASE_POINT_X + self.__class__.MAP_BOX_SIZE, self.__class__.MAP_BASE_POINT_Y + self.__class__.MAP_BOX_SIZE), fill=(0,0,0))
		# Every row of tiles
		for rowID in range(len(self.tiles)):
			row = self.tiles[rowID]
			# Every tile in the row
			for cellID in range(len(row)):
				tile = row[cellID]
				# If it's dirt, there's nothing to draw. Cavnas colour is dirt
				if tile.alias == Tile.DIRT:
					continue
				# Tile canvas dimensions
				if self.rawImage:
					startX	= cellID * self.drawSize + 1
					startY	= rowID * self.drawSize + 1 
					endX	= cellID * self.drawSize + self.drawSize + 1 
					endY	= rowID * self.drawSize + self.drawSize + 1 
				else:
					blockSize	= self.__class__.MAP_BOX_SIZE / self.width 
					startX	= cellID * blockSize + self.__class__.MAP_BASE_POINT_X + 1
					startY 	= rowID * blockSize + self.__class__.MAP_BASE_POINT_Y + 1
					endX	= cellID * blockSize + blockSize + self.__class__.MAP_BASE_POINT_X + 1
					endY 	= rowID * blockSize + blockSize + self.__class__.MAP_BASE_POINT_Y + 1
				# Pillow it
				draw.rectangle((startX, startY, endX, endY), fill=tile.colour)
		# Show it
		im.show()
		# Save it if a path is provided
		if path:
			im.save(path)
	##
	# Populate Tile map with DIRT tiles
	##
	def prepareTiles(self):
		self.tiles	= []
		# Do every row. Dimensions independent from any parsed spreadsheet or whatever DataFrame
		for rowID in range(self.height):
			row	= []
			# Do every tile. 
			for cellID in range(self.width):
				row.append(Tile(Tile.DIRT, False))
			self.tiles.append(row)
	##
	# Draw the map to the console
	#
	# Letters are just random single characters to keep the shape.
	##
	def drawToConsole(self):
		for rowID in range(self.height):
			row	= ""
			for cellID in range(self.width):
				row += self.tiles[rowID][cellID].drawLabel # Temp until colours added
			print(row)
	##
	# Parse spreadsheet
	##
	def parseExcel(self, path):
		# Can't parse what doesn't exist - Confucius  
		if not exists(path):
			raise "Map - Excel file not found " + path
		# Read the spreadsheet
		self.spreadsheet	= read_excel(path, header=None)
		# Every row in the spreadsheet
		for rowID, row in self.spreadsheet.iterrows():
			# Parse map dimensions are independent of the spreadsheet's (see Map constructor)
			if rowID >= self.height:
				break;
			# Draw every cell
			for cellID in range(len(row)):
				# Parse map dimensions are independent of the spreadsheet's (see Map constructor)
				if cellID >= self.width:
					break;
				# Blank cells are DIRT
				if not isinstance(row[cellID], str):
					continue
				# Labels need to be lower case for lookups
				label	= row[cellID].strip().lower()
				# Blank string and cells defined as DIRT are also DIRT
				if label == "" or label == Tile.LABELED_PROPERTIES[Tile.DIRT]["label"]:
					label = "d"
				# TODO: Players are identified by a number in the label. But, it's not implemented yet
				player	= False
				# All labels have two characters. E.g. "la" is lair, "to" is torture chamber
				if len(label) > 1:
					label	= label[0:2]
				# Update the tile
				self.tiles[rowID][cellID]	= Tile(Tile.KEYED_PROPERTIES[label]["label"], False)
				
		
		