import pygame
import pygame.freetype

name = "ZapWizard"

WIDTH = 720
HEIGHT = 720
FULLSCREEN = False

#Colors
black = (0,0,0)
bright = (0,230,0)
light = (0,150,0)
mid = (0,120,0)
dim = (0,60,0)
dark = (0,30,0)

#Header, Footer heights
header_height = 50
footer_height = 50

#Top Menu Position
top_menu_x = 0
top_menu_y = 51

#Sub Menu Position
sub_menu_x = 73
sub_menu_y = 93

#Menu Position
menu_x = 33
menu_y = 189

#Default music selection
station = 0 # No station = 0 
volume = 0.5 # Set default volume

# OUTPUT_WIDTH = 320
# OUTPUT_HEIGHT = 240

#MAP_FOCUS = (-5.9347681, 54.5889076)
#MAP_FOCUS = (-102.3016145, 21.8841274) #Old Default?
#MAP_FOCUS = (-118.5723894,34.3917171)#CodeNinjasValencia
#MAP_FOCUS = (32.7157, 117.1611)
#MAP_FOCUS = (-92.1943197, 38.5653437)
MAP_FOCUS = (-98.0878917, 30.1914818) # Zap's Hometown

WORLD_MAP_FOCUS = 0.07 #Needed to handle the 50k node limit from OSM

LOAD_CACHED_MAP = True

EVENTS = {
    'SONG_END': pygame.USEREVENT + 1
}

MODULES = {
    0: "STAT",
    1: "INV",
    2: "DATA",
    3: "MAP",
    4: "RADIO",
    5: "BOOT"
}

#MODULE_TEXT = ["RADIO","MAP","DATA","INV","STAT"]
MODULE_TEXT = ["STAT","INV","DATA","MAP","RADIO"]

ACTIONS = {
    pygame.K_F1: "module_stats",
    pygame.K_F2: "module_items",
    pygame.K_F3: "module_data",
    pygame.K_F4: "module_map",
    pygame.K_F5: "module_radio",
    pygame.K_F6: "module_boot",
    pygame.K_1:	"knob_1",
    pygame.K_2: "knob_2",
    pygame.K_3: "knob_3",
    pygame.K_4: "knob_4",
    pygame.K_5: "knob_5",
    pygame.K_UP: "dial_up",
    pygame.K_DOWN: "dial_down",
    pygame.K_PLUS: "zoom_in",
    pygame.K_MINUS: "zoom_out",
    pygame.K_KP_PLUS: "zoom_in",
    pygame.K_KP_MINUS: "zoom_out",
}

# Using GPIO.BCM as mode
#GPIO 23 pin16 reboot
#GPIO 25 pin 22 blank screen do not use
GPIO_ACTIONS = {
#    19: "module_stats", #GPIO 4
#    26: "module_items", #GPIO 14
#    16: "module_data", #GPIO 15
#	18:	"knob_1", #GPIO 18 Do Not enable messes with the screen. 
#	18: "knob_2", #GPIO 18 Turns screen off do not use
#	7: "knob_3", #GPIO 7
#	22: "knob_1", #GPIO 22
#	22: "dial_down", #GPIO 22
#	25: "dial_up", #GPIO 25
#    20: "knob_2", #GPIO 24
#	25: "knob_3" #GPIO 23
}


MAP_ICONS = {
    "camp": 		pygame.image.load('images/map_icons/camp.png'),
    "factory": 		pygame.image.load('images/map_icons/factory.png'),
    "metro": 		pygame.image.load('images/map_icons/metro.png'),
    "misc": 		pygame.image.load('images/map_icons/misc.png'),
    "monument": 	pygame.image.load('images/map_icons/monument.png'),
    "vault": 		pygame.image.load('images/map_icons/vault.png'),
    "settlement": 	pygame.image.load('images/map_icons/settlement.png'),
    "ruin": 		pygame.image.load('images/map_icons/ruin.png'),
    "cave": 		pygame.image.load('images/map_icons/cave.png'),
    "landmark": 	pygame.image.load('images/map_icons/landmark.png'),
    "city": 		pygame.image.load('images/map_icons/city.png'),
    "office": 		pygame.image.load('images/map_icons/office.png'),
    "sewer": 		pygame.image.load('images/map_icons/sewer.png'),
}

AMENITIES = {
    'pub': 				MAP_ICONS['vault'],
    'nightclub': 		MAP_ICONS['vault'],
    'bar': 				MAP_ICONS['vault'],
    'fast_food': 		MAP_ICONS['settlement'],
	'cafe': 			MAP_ICONS['settlement'],
#	'drinking_water': 	MAP_ICONS['sewer'],
    'restaurant': 		MAP_ICONS['settlement'],
    'cinema': 			MAP_ICONS['office'],
    'pharmacy': 		MAP_ICONS['office'],
    'school': 			MAP_ICONS['office'],
    'bank': 			MAP_ICONS['monument'],
    'townhall': 		MAP_ICONS['monument'],
#	'bicycle_parking': 	MAP_ICONS['misc'],
#	'place_of_worship': MAP_ICONS['misc'],
	'theatre': 			MAP_ICONS['office'],
#	'bus_station': 		MAP_ICONS['misc'],
#	'parking': 			MAP_ICONS['misc'],
#	'fountain': 		MAP_ICONS['misc'],
#	'marketplace': 		MAP_ICONS['misc'],
#	'atm': 				MAP_ICONS['misc'],
    'misc':             MAP_ICONS['misc']
}

INVENTORY_OLD = [
"Ranger Sequoia",
"Anti-Materiel Rifle ",
"Deathclaw Gauntlet",
"Flamer",
"NCR dogtag",
".45-70 Gov't(20)",
".44 Magnum(20)",
"Pulse Grenade (2)"
]

WEAPONS = [
    "10mm Pistol",
    "Combat Knife",
    "Fragmentation Grenade (2)",
    "Laser Pistol",
    "Plasma Mine (3)"
]

ARMOR = [
    "Eyeglasses",
    "Vault 111 Jumpsuit",
    "Wedding Ring"
]

AID = [
    "Purified Water (3)",
    "Rad Away (2)",
    "Stim Pack (2)"
]

MISC = [
    "Pencil",
    "Pre-War Money (250)",
    "Super Glue",
    "Toy Mini-Nuke"
]

AMMO = [
    "10mm Rounds (15)",
    "Fusion Cells (28)"
]

QUESTS = [
    "Cosplacon",
    "Cosplay Royale",
    "Drink n Draw",
    "Queens of Cosplay"
]

SKILLS = [
    "Action Boy",
    "Animal Friend",
    "Awareness",
    "Gunslinger"
    "Hacker",
    "Mysterious Stranger",
    "Rifleman",
    "Science"   
]

PERKS = [
    "Action Boy",
    "Animal Friend",
    "Awareness",
    "Gunslinger"
    "Hacker",
    "Mysterious Stranger",
    "Rifleman",
    "Science"   
]

pygame.font.init()
RobotoB = {}
RobotoR = {}
for x in range(10, 34):
    RobotoB[x] = pygame.font.Font('fonts/RobotoCondensed-Bold.ttf', x)    
    RobotoR[x] = pygame.font.Font('fonts/RobotoCondensed-Regular.ttf', x)    

pygame.freetype.init()
FreeRobotoB = {}
FreeRobotoR = {}
FreeTechMono = {}
for x in range(10, 34):
    FreeRobotoB[x] = pygame.freetype.Font('fonts/RobotoCondensed-Bold.ttf', x)    
    FreeRobotoR[x] = pygame.freetype.Font('fonts/RobotoCondensed-Regular.ttf', x)    
    FreeTechMono[x] = pygame.freetype.Font('fonts/TechMono.ttf', x)