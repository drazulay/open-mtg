import asyncio
import random

from enum import Enum

from events import EventType, EventEmitter, Event


class PlayerType(Enum):
    PLAYER = 0
    OPPONENT = 1


class Locations(Enum):
    STACK = 0
    HAND = 1
    TABLE = 1
    GRAVEYARD = 1


class CardType(Enum):
    ARTIFACT = 0
    CREATURE = 1
    ENCHANTMENT = 2
    INSTANT = 3
    LAND = 4
    PLANESWALKER = 5
    SORCERY = 6


class SpecialCardType(Enum):
    TOKEN = 0
    EMBLEM = 1
    CONSPIRACY = 2
    PHENOMENON = 3
    PLANE = 4
    VANGUARD = 5


class SuperType(Enum):
    BASIC = 0
    LEGENDARY = 1
    SNOW = 2
    WORLD = 3
    ONGOING = 4


class SubType(Enum):
    EQUIPMENT = 0
    CONTRAPTION = 1
    FORTIFICATION = 2
    VEHICLE = 3
    TREASURE = 4
    FOOD = 5
    CLUE = 6
    GOLD = 7


class CreatureType(Enum):
    ADVISOR = 0
    AETHERBORN = 1
    ALLY = 2
    ANGEL = 3
    ANT = 4
    ANTEATER = 5
    ANTELOPE = 6
    APE = 7
    ARCHER = 8
    ARCHON = 9
    ARMY = 10
    ARTIFICER = 11
    ASSASSIN = 12
    ASSEMBLY_WORKER = 13
    ATOG = 14
    AURA = 15
    AVATAR = 16
    AZRA = 17
    BADGER = 18
    BARBARIAN = 19
    BASILISK = 20
    BAT = 21
    BEAR = 22
    BEAST = 23
    BEEBLE = 24
    BEHEMOTH = 25
    BERZERKER = 26
    BIRD = 27
    BLINKMOTH = 28
    BOAR = 29
    BRINGER = 30
    BRUSHWAGG = 31
    CAMARID = 32
    CAMEL = 33
    CARIBOU = 34
    CARRIER = 35
    CAT = 36
    CENTAUR = 37
    CEPHALID = 38
    CHIMERA = 39
    CITIZEN = 40
    CLERIC = 41
    COCKATRICE = 42
    CONSTRUCT = 43
    COWARD = 44
    CRAB = 45
    CROCODILE = 46
    CYCLOPS = 47
    DAUTHI = 48
    DEMON = 49
    DESERTER = 50
    DEVIL = 51
    DINOSAUR = 52
    DJINN = 53
    DRAGON = 54
    DRAKE = 55
    DREADNOUGHT = 56
    DRONE = 57
    DRUID = 58
    DRYAD = 59
    DWARF = 60
    EFREET = 61
    EGG = 62
    ELDER = 63
    ELDRAZI = 64
    ELEMENTAL = 65
    ELEPHANT = 66
    ELF = 67
    ELK = 68
    EYE = 69
    FAERIE = 70
    FERRET = 71
    FISH = 72
    FLAGBEARER = 73
    FOX = 74
    FROG = 75
    FUNGUS = 76
    GARGOYLE = 77
    GERM = 78
    GIANT = 79
    GNOME = 80
    GOAT = 81
    GOBLIN = 82
    GOD = 83
    GOLEM = 84
    GORGON = 85
    GRAVEBORN = 86
    GREMLIN = 87
    GRIFFIN = 88
    HAG = 89
    HALF = 90
    HARPY = 91
    HELLION = 92
    HIPPO = 93
    HIPPOGRIFF = 94
    HOMARID = 95
    HOMUNCULUS = 96
    HORROR = 97
    HORSE = 98
    HOUND = 99
    HUMAN = 100
    HYDRA = 101
    HYENA = 102
    ILLUSION = 103
    IMP = 104
    INCARNATION = 105
    INSECT = 106
    JACKAL = 107
    JELLYFISH = 108
    JUGGERNAUT = 109
    KAVU = 110
    KIRIN = 111
    KITHKIN = 112
    KNIGHT = 113
    KOBOLD = 114
    KOR = 115
    KRAKEN = 116
    LAMIA = 117
    LAMMASU = 118
    LEECH = 119
    LEVIATHAN = 120
    LHURGOYF = 121
    LICID = 122
    LIZARD = 123
    MANTICORE = 124
    MASTICORE = 125
    MERCENARY = 126
    MERFOLK = 127
    METATHRAN = 128
    MINION = 129
    MINOTAUR = 130
    MOLE = 131
    MONGER = 132
    MONGOOSE = 133
    MONK = 134
    MONKEY = 135
    MOONFOLK = 136
    MUTANT = 137
    MYR = 138
    MYSTIC = 139
    NAAGA = 140
    NAGA = 141
    NAUTILUS = 142
    NEPHILIM = 143
    NIGHTMARE = 144
    NIGHTSTALKER = 145
    NINJA = 146
    NOGGLE = 147
    NOMAD = 148
    NYPH = 149
    OCTOPUS = 150
    OGRE = 151
    OOZE = 152
    ORACLE = 153
    ORC = 154
    ORGG = 155
    OTTER = 156
    OUPHE = 157
    OYSTER = 158
    PEGASUS = 159
    PENTAVITE = 160
    PEST = 161
    PHANTASM = 162
    PHOENIX = 163
    PILOT = 164
    PINCHER = 165
    PIRATE = 166
    PLANT = 167
    PRAETOR = 168
    PRISM = 169
    PROCESSOR = 170
    PYRROL = 171
    RABBIT = 172
    RAT = 173
    REBEL = 174
    REFLECTION = 175
    RHINO = 176
    RIGGER = 177
    ROGUE = 178
    SABLE = 179
    SALAMANDER = 180
    SAMURAI = 181
    SAND = 182
    SAPROLING = 183
    SATYR = 184
    SCARECROW = 185
    SCION = 186
    SCORPION = 187
    SCOUT = 188
    SERF = 189
    SERPENT = 190
    SERVO = 191
    SHADE = 192
    SHAMAN = 193
    SHAPESHIFTER = 194
    SHEEP = 195
    SIREN = 196
    SKELETON = 197
    SLITH = 198
    SLIVER = 199
    SLUG = 200
    SNAKE = 201
    SOLDIER = 202
    SOLTARI = 203
    SPAWN = 204
    SPECTER = 205
    SPELLSHAPER = 206
    SPHINX = 207
    SPIDER = 208
    SPIKE = 209
    SPIRIT = 210
    SPLINTER = 211
    SPONGE = 212
    SQUID = 213
    SQUIRREL = 214
    STARFISH = 215
    SURLAKAR = 216
    SURRAKAR = 217
    SURVIVOR = 218
    TETRAVITE = 219
    THALAKOS = 220
    THOPTER = 221
    THRULL = 222
    TREEFOLK = 223
    TRISKELAVITE = 224
    TROLL = 225
    TURTLE = 226
    UNICORN = 227
    VAMPIRE = 228
    VEDALKEN = 229
    VIASHINO = 230
    VOLVER = 231
    WALL = 232
    WARLOCK = 233
    WARRIOR = 234
    WEIRD = 235
    WHALE = 236
    WIZARD = 237
    WOLF = 238
    WOLVERINE = 239
    WOMBAT = 240
    WORM = 241
    WRAITH = 242
    WURM = 243
    YETI = 244
    ZOMBIE = 245
    ZUBERA = 246
    ZURG = 247
    THORN = 248
    THIRL = 249
    SHARK = 250
    SERVITOR = 251
    THEURGE = 252
    WEREWOLF = 253


class AbilityType(Enum):
    KEYWORD = 0
    TRIGGERED = 1
    ACTIVATED = 2
    STATIC = 3


class AbilitySpecificType(Enum):
    AFFLICT = 0
    AMASS = 1
    ANNIHILATOR = 2
    ASCEND = 3
    BANDING = 4
    BATTALION = 5
    BLOODTHIRST = 6
    BUSHIDO = 7
    BUYBACK = 8
    CASCADE = 9
    CHAMPION = 10
    CHANGELING = 11
    CIPHER = 12
    CLASH = 13
    CONSPIRE = 14
    CONVOKE = 15
    CREW = 16
    CUMULATIVE_UPKEEP = 17
    CYCLING = 18
    DASH = 19
    DEATHTOUCH = 20
    DEFENDER = 21
    DELVE = 22
    DETAIN = 23
    DETHRONE = 24
    DEVOID = 25
    DEVOUR = 26
    DOUBLE_STRIKE = 27
    DREDGE = 28
    ECHO = 29
    EMBALM = 30
    EMERGE = 31
    EMINENCE = 32
    ENCHANT = 33
    ENRAGE = 34
    ENTWINE = 45
    EPIC = 46
    EQUIP = 47
    ESCAPE = 48
    EVOKE = 49
    EVOLVE = 50
    EXALTED = 51
    EXPLOIT = 52
    EXPLORE = 53
    EXTORT = 54
    FABRICATE = 55
    FADING = 56
    FEAR = 57
    FEROCIOUS = 58
    FIGHT = 59
    STRIKE = 60
    FLANKING = 61
    FLASH = 62
    FLASHBACK = 63
    FLIP = 64
    FLYING = 65
    FORECAST = 66
    FORTIFY = 67
    FRENZY = 68
    FUSE = 69
    GRAFT = 70
    GRAVESTORM = 71
    HASTE = 72
    HAUNT = 73
    HELLBENT = 74
    HEROIC = 75
    HEXPROOF = 76
    HIDEAWAY = 77
    HORSEMANSHIP = 78
    IMPRINT = 79
    INDESTRUCTIBLE = 80
    INFECT = 81
    INGEST = 82
    INTIMIDATE = 83
    INVESTIGATE = 84
    FORCES = 85
    JUMP_START = 86
    KICKER = 87
    KINSHIP = 88
    LANDFALL = 89
    UP = 90
    LIFELINK = 91
    LIVING_WEAPON = 92
    MADNESS = 93
    MEGAMORPH = 94
    MELEE = 95
    MENACE = 96
    MENTOR = 97
    MIRACLE = 98
    MODULAR = 99
    MONSTROSITY = 100
    MORPH = 101
    MULTIKICKER = 102
    MUTATE = 103
    MYRIAD = 104
    NINJUTSU = 105
    OFFERING = 106
    OUTLAST = 107
    OVERLOAD = 108
    PARTNER = 109
    PERSIST = 110
    PHASING = 111
    POISONOUS = 112
    POPULATE = 113
    PROLIFERATE = 114
    PROVOKE = 115
    PROWESS = 116
    PROWL = 117
    RAID = 118
    RALLY = 119
    RAMPAGE = 120
    REACH = 121
    REBOUND = 122
    RECOVER = 123
    REINFORCE = 124
    RENOWN = 125
    REPLICATE = 126
    RETRACE = 127
    RIPPLE = 128
    RUSH = 129
    SACRIFICE = 130
    SCAVENGE = 131
    SHADOW = 132
    SHROUD = 133
    SKULK = 134
    SLIVERCYCLING = 135
    SOULBOND = 136
    SOULSHIFT = 137
    SPECTACLE = 138
    SPLICE = 139
    SPLIT = 139
    SECOND = 141
    STORM = 142
    SUNBURST = 143
    SUPPORT = 144
    SURGE = 145
    SUSPEND = 146
    TOTEM_ARMOR = 147
    TRAMPLE = 148
    TRANSFIGURE = 149
    TRANSFORM = 150
    TRANSMUTE = 151
    TRIBUTE = 152
    TYPECYCLING = 153
    UNDAUNTED = 154
    UNDYING = 155
    UNEARTH = 156
    UNLEASH = 157
    VANISHING = 158
    VIGILANCE = 169
    WITHER = 160
    JOIN = 161
    LEVEL = 162
    FIRST_STRIKE = 163


class LandType(Enum):
    PLAINS = 0
    ISLAND = 1
    SWAMP = 2
    MOUNTAIN = 3
    FOREST = 4


class LandSubType(Enum):
    DESERT = 0
    GATE = 1
    LAIR = 2
    LOCUS = 3
    MINE = 4
    POWER_PLANT = 5
    TOWER = 6
    URZA = 7
    WORKSHOP = 8
    WASTE = 9
    TOWN = 10
    PHYREXIA = 11


class LandSpecialType(Enum):
    DESERTED_TEMPLE = 1
    DESERTED_BEACH = 2
    DESERTED_FARM = 3
    DESERTED_GROUND = 4
    DESERTED_HARBOR = 5
    DESERTED_ISLAND = 6
    DESERTED_LIGHTHOUSE = 7
    DESERTED_RIDGE = 8
    DESERTED_RIVER = 9
    DESERTED_SANCTUARY = 10
    DESERTED_STATION = 11
    DESERTED_TOMB = 12
    DESERTED_WATCHTOWER = 13
    DESERTED_WELL = 14
    DESERTED_WILDERNESS = 16
    DESERTED_WOODS = 17
    DESERTED_CAVE = 18
    DESERTED_CEMETERY = 19
    DESERTED_CHURCH = 20
    DESERTED_CITY = 21
    DESERTED_CLIFF = 22
    DESERTED_CROSSROADS = 23
    DESERTED_DUNGEON = 24
    DESERTED_FOREST = 25
    DESERTED_FORT = 26
    DESERTED_GARDEN = 27
    DESERTED_GATE = 28
    DESERTED_GROVE = 29
    DESERTED_HALL = 30
    DESERTED_HAMLET = 31
    DESERTED_HILL = 33
    DESERTED_HOUSE = 34
    DESERTED_KEEP = 35
    DESERTED_LIBRARY = 36
    DESERTED_MANOR = 38
    DESERTED_MANSION = 39
    DESERTED_MARSH = 40
    DESERTED_MAZE = 41
    DESERTED_MILL = 42
    DESERTED_MINE = 43
    DESERTED_MONASTERY = 44
    DESERTED_MOUNTAIN = 45
    DESERTED_ORCHARD = 46
    DESERTED_PALACE = 47
    DESERTED_PARK = 48
    DESERTED_PASS = 49
    DESERTED_PEAK = 50
    DESERTED_PLAINS = 51
    DESERTED_PORT = 52
    DESERTED_QUARRY = 53
    DESERTED_ROAD = 56
    DESERTED_ROCK = 57
    DESERTED_RUINS = 58
    DESERTED_SEA = 60
    DESERTED_SHORE = 61
    DESERTED_SPRING = 62
    DESERTED_STONE = 64
    DESERTED_SWAMP = 65
    DESERTED_TOWER = 67
    DESERTED_TOWN = 68
    DESERTED_TRAIL = 69
    DESERTED_VALLEY = 70
    DESERTED_VILLAGE = 71
    DESERTED_WASTELAND = 72
    DESERTED_YARD = 75
    DESERTED_ZOO = 76
    DESERTED_ABBEY = 77
    DESERTED_ACADEMY = 78
    DESERTED_ALLEY = 79
    DESERTED_ALTAR = 80
    DESERTED_AMPHITHEATER = 81
    DESERTED_AQUEDUCT = 82
    DESERTED_ARCH = 83
    DESERTED_ARENA = 84
    DESERTED_ARMORY = 85
    DESERTED_ARTIFACT = 86
    DESERTED_ASH = 87
    DESERTED_ASHRAM = 88
    DESERTED_ASPHALT = 89


class Card:
    def __init__(self,
                 event_emitter: EventEmitter,
                 id: int,
                 power: int,
                 toughness: int,
                 name: str,
                 type: int,
                 image: str = None,
                 abilities: list = None):

        self.event_emitter = event_emitter

        self.id = id
        self.power = power
        self.toughness = toughness
        self.name = name
        self.type = type
        self.special_type = None
        self.super_type = None
        self.sub_type = None
        self.creature_type = None
        self.land_type = None
        self.location = Locations.STACK
        self.image = image
        self.abilities = abilities
        self.blockers = []

    def destroy(self):
        if self.location == Locations.HAND:
            self.event_emitter.emit(
                Event(EventType.E_CARD_FROM_HAND_TO_GRAVEYARD))
        elif self.location == Locations.TABLE:
            self.event_emitter.emit(
                Event(EventType.E_CARD_FROM_TABLE_TO_GRAVEYARD))

    def assign_blocker(self, card):
        self.blockers.append(card)

    def attack(self, card):
        self.event_emitter.emit(Event(EventType.E_MOD_CARD_HEALTH,
                                      [card, -self.power, 0]))

    def can_survive(self):
        return self.toughness > 0

    def afflict(self):
        pass

    def annihilator(self):
        pass

    def banding(self):
        pass

    def battalion(self):
        pass

    def become_creature(self):
        pass

    def gain_deathtouch(self):
        pass

    def prevent_attack(self):
        pass

    def detain(self):
        pass

    def increase_power_and_toughness(self):
        pass

    def devour(self):
        pass

    def double_strike(self):
        pass

    def enrage(self):
        pass

    def evolve(self):
        pass

    def exalted(self):
        pass

    def ferocious(self):
        pass

    def fading(self):
        pass

    def fight(self, target):
        pass

    def first_strike(self):
        pass

    def flanking(self):
        pass

    def flash(self):
        pass

    def flip(self):
        pass

    def flying(self):
        pass

    def frenzy(self):
        pass

    def graft(self, target):
        pass

    def haunt(self, target):
        pass

    def heroic(self, spell):
        pass

    def hexproof(self):
        pass

    def horsemanship(self):
        pass

    def imprint(self, card):
        pass

    def indestructible(self):
        pass

    def infect(self):
        pass

    def ingest(self, opponent):
        pass

    def intimidate(self):
        pass

    def kinship(self):
        pass

    def last_strike(self):
        pass

    def lifelink(self):
        pass

    def living_weapon(self):
        pass

    def megamorph(self):
        pass

    def mentor(self, target):
        pass

    def modular(self, target):
        pass

    def monstrosity(self):
        pass

    def mutate(self, target):
        pass

    def myriad(self):
        pass

    def outlast(self):
        pass

    def persist(self):
        pass

    def phasing(self):
        pass

    def poisonous(self):
        pass

    def provoke(self, target):
        pass

    def raid(self):
        pass

    def rally(self):
        pass

    def reach(self):
        pass

    def rampage(self):
        pass

    def renown(self):
        pass

    def rush(self):
        pass

    def soulbond(self, target):
        pass

    def sunburst(self):
        pass

    def tap(self):
        pass

    def totem_armor(self):
        pass

    def untap(self):
        pass

    def vanishing(self):
        pass

    def vigilance(self):
        pass

    def wither(self):
        pass

    def changeling(self):
        pass

    def level(self):
        pass

    def shadow(self):
        pass

    def shroud(self):
        pass

    def support(self, target):
        pass

    def skulk(self):
        pass

    def trample(self):
        pass

    def transform(self):
        pass

    def undying(self):
        pass

    def unleash(self):
        pass

    def fear(self):
        pass

    def make_colorless(self):
        pass

    def haste(self):
        pass

    def melee(self):
        pass

    def menace(self):
        pass


class Player:
    def __init__(self):
        self.lost_health_this_turn = None
        self.health = 20
        self.image = None
        self.stack = []
        self.graveyard = []
        self.combat = []
        self.hand = []
        self.table = []
        self.id = None

    def heal(self, health):
        self.health += health

    def attack(self, health):
        self.health -= health

    def amass(self):
        pass

    def has_ten_permanents(self):
        pass

    def ascend(self):
        pass

    def increase_unit_power(self):
        pass

    def return_spell_to_hand(self, spell):
        pass

    def cast_spell_for_free(self):
        pass

    def replace_unit(self, unit, replacement_unit):
        pass

    def pay_cumulative_upkeep(self, cost):
        pass

    def discard_and_draw(self, card):
        pass

    def cast_with_dash(self, creature):
        pass

    def exile_cards_for_spell(self, spell):
        pass

    def is_at_most_life(self):
        pass

    def embalm(self, creature):
        pass

    def emerge(self, creature, sacrifice):
        pass

    def dredge(self, card):
        pass

    def eminence(self, card):
        pass

    def enchant(self, card, target):
        pass

    def choose_all_modes(self, spell):
        pass

    def cast_with_evoke(self, creature):
        pass

    def equip(self, equipment, creature):
        pass

    def escape(self, card):
        pass

    def exploit(self, creature):
        pass

    def extort(self, spell):
        pass

    def fabricate(self, creature):
        pass

    def flashback(self, spell):
        pass

    def forecast(self, card):
        pass

    def fortify(self, fortification, land):
        pass

    def fuse(self, spell1, spell2):
        pass

    def gravestorm(self, spell):
        pass

    def hellbent(self):
        pass

    def hideaway(self, card):
        pass

    def investigate(self):
        pass

    def join_forces(self, spell):
        pass

    def jump_start(self, spell):
        pass

    def kicker(self, spell):
        pass

    def landfall(self):
        pass

    def madness(self, card):
        pass

    def miracle(self, spell):
        pass

    def morph(self, creature):
        pass

    def multikicker(self, spell):
        pass

    def ninjutsu(self, creature):
        pass

    def offering(self, creature):
        pass

    def overload(self, spell):
        pass

    def partner(self, spell):
        pass

    def populate(self, token):
        pass

    def proliferate(self, target):
        pass

    def prowess(self, spell):
        pass

    def prowl(self, spell):
        pass

    def rebound(self, spell):
        pass

    def recover(self, card):
        pass

    def reinforce(self, creature):
        pass

    def replicate(self, spell):
        pass

    def retrace(self, spell):
        pass

    def ripple(self, spell):
        pass

    def sacrifice(self, creature):
        pass

    def scavenge(self, creature):
        pass

    def scry(self):
        pass

    def search(self, card):
        pass

    def soulshift(self, card):
        pass

    def splice(self, spell1, spell2):
        pass

    def storm(self, spell):
        pass

    def sweep(self, spell):
        pass

    def threshold(self):
        pass

    def suspend(self, spell):
        pass

    def transfigure(self, creature):
        pass

    def transmute(self, card):
        pass

    def tutor(self, card):
        pass

    def unearth(self, creature):
        pass

    def wrath(self):
        pass

    def choose_x(self, spell):
        pass

    def yank(self, permanent):
        pass

    def zendikar(self):
        pass

    def zombie(self, creature):
        pass

    def zurgo(self, creature):
        pass

    def cipher(self, spell):
        pass

    def join(self, spell):
        pass

    def surge(self, spell):
        pass

    def slivercycling(self, card):
        pass

    def split(self, spell1, spell2):
        pass

    def spectacle(self, spell):
        pass

    def tribute(self, creature):
        pass

    def typecycling(self, card):
        pass

    def undaunted(self, spell):
        pass

    def explore(self):
        pass

    def clash(self):
        pass

    def conspire(self, spell):
        pass

    def convoke(self, spell):
        pass

    def prevent_casting(self, spell):
        pass

    def pay_echo(self, card):
        pass


class Unit:
    def __init__(self, id: int, player: Player, cards: list):
        self.id = id
        self.player = player
        self.cards = cards

    def increase_power_and_toughness(self, power: int, toughness: int):
        for card in self.cards:
            card.power += power
            card.toughness += toughness


class Ability:
    def __init__(self, id: AbilitySpecificType,
                 cost: list,
                 player: Player,
                 opponent: Player,
                 card: Card, phases: list,
                 target: Card = None,
                 permanent: Card = None,
                 sacrifice: Card = None,
                 in_combat: bool = False,
                 unit: Unit = None,
                 replacement_unit: Unit = None,
                 spell: Card = None,
                 spell1: Card = None,
                 spell2: Card = None):

        self.id = id
        self.player = player
        self.opponent = opponent
        self.card = card
        self.target = target
        self.permanent = permanent
        self.sacrifice = sacrifice
        self.cost = cost
        self.spell = spell
        self.spell1 = spell1
        self.spell2 = spell2
        self.unit = unit
        self.replacement_unit = replacement_unit
        self.phases = phases
        self.in_combat = in_combat

        if card.type == CardType.CREATURE:
            self.creature = card
        if card.type == CardType.ARTIFACT:
            self.artifact = card
        if card.type == CardType.ENCHANTMENT:
            self.enchantment = card
        if card.type == CardType.INSTANT:
            self.instant = card
        if card.type == CardType.LAND:
            self.land = card
        if card.type == CardType.PLANESWALKER:
            self.planeswalker = card

        if card.super_type == SuperType.BASIC:
            self.basic = card
        if card.super_type == SuperType.LEGENDARY:
            self.legendary = card
        if card.super_type == SuperType.SNOW:
            self.snow = card
        if card.super_type == SuperType.WORLD:
            self.world = card
        if card.super_type == SuperType.ONGOING:
            self.ongoing = card

        if card.special_type == CardType.SORCERY:
            self.sorcery = card
        if card.special_type == SpecialCardType.TOKEN:
            self.token = card
        if card.special_type == SpecialCardType.EMBLEM:
            self.emblem = card
        if card.special_type == SpecialCardType.CONSPIRACY:
            self.conspiracy = card
        if card.special_type == SpecialCardType.PHENOMENON:
            self.phenomenon = card
        if card.special_type == SpecialCardType.PLANE:
            self.plane = card
        if card.special_type == SpecialCardType.VANGUARD:
            self.vanguard = card

        if card.sub_type == SubType.EQUIPMENT:
            self.equipment = card
        if card.sub_type == SubType.CONTRAPTION:
            self.contraption = card
        if card.sub_type == SubType.FORTIFICATION:
            self.fortification = card
        if card.sub_type == SubType.VEHICLE:
            self.vehicle = card
        if card.sub_type == SubType.TREASURE:
            self.treasure = card
        if card.sub_type == SubType.FOOD:
            self.food = card
        if card.sub_type == SubType.CLUE:
            self.clue = card
        if card.sub_type == SubType.GOLD:
            self.gold = card

        if card.creature_type == CreatureType.ADVISOR:
            self.advisor = card
        if card.creature_type == CreatureType.AETHERBORN:
            self.aetherborn = card
        if card.creature_type == CreatureType.ALLY:
            self.ally = card
        if card.creature_type == CreatureType.ANGEL:
            self.angel = card
        if card.creature_type == CreatureType.ANT:
            self.ant = card
        if card.creature_type == CreatureType.ANTEATER:
            self.anteater = card
        if card.creature_type == CreatureType.ANTELOPE:
            self.antelope = card
        if card.creature_type == CreatureType.APE:
            self.ape = card
        if card.creature_type == CreatureType.ARCHER:
            self.archer = card
        if card.creature_type == CreatureType.ARCHON:
            self.archon = card
        if card.creature_type == CreatureType.ARMY:
            self.army = card
        if card.creature_type == CreatureType.ARTIFICER:
            self.artificer = card
        if card.creature_type == CreatureType.ASSASSIN:
            self.assassin = card
        if card.creature_type == CreatureType.ASSEMBLY_WORKER:
            self.assembly_worker = card
        if card.creature_type == CreatureType.ATOG:
            self.atog = card
        if card.creature_type == CreatureType.AURA:
            self.aura = card
        if card.creature_type == CreatureType.AVATAR:
            self.avatar = card
        if card.creature_type == CreatureType.AZRA:
            self.azra = card
        if card.creature_type == CreatureType.BADGER:
            self.badger = card
        if card.creature_type == CreatureType.BARBARIAN:
            self.barbarian = card
        if card.creature_type == CreatureType.BASILISK:
            self.basilisk = card
        if card.creature_type == CreatureType.BAT:
            self.bat = card
        if card.creature_type == CreatureType.BEAR:
            self.bear = card
        if card.creature_type == CreatureType.BEAST:
            self.beast = card
        if card.creature_type == CreatureType.BEEBLE:
            self.beeble = card
        if card.creature_type == CreatureType.BEHEMOTH:
            self.behemoth = card
        if card.creature_type == CreatureType.BERZERKER:
            self.berzerker = card
        if card.creature_type == CreatureType.BIRD:
            self.bird = card
        if card.creature_type == CreatureType.BLINKMOTH:
            self.blinkmoth = card
        if card.creature_type == CreatureType.BOAR:
            self.boar = card
        if card.creature_type == CreatureType.BRINGER:
            self.bringer = card
        if card.creature_type == CreatureType.BRUSHWAGG:
            self.brushwagg = card
        if card.creature_type == CreatureType.CAMARID:
            self.camarid = card
        if card.creature_type == CreatureType.CAMEL:
            self.camel = card
        if card.creature_type == CreatureType.CARIBOU:
            self.caribou = card
        if card.creature_type == CreatureType.CARRIER:
            self.carrier = card
        if card.creature_type == CreatureType.CAT:
            self.cat = card
        if card.creature_type == CreatureType.CENTAUR:
            self.centaur = card
        if card.creature_type == CreatureType.CEPHALID:
            self.cephalid = card
        if card.creature_type == CreatureType.CHIMERA:
            self.chimera = card
        if card.creature_type == CreatureType.CITIZEN:
            self.citizen = card
        if card.creature_type == CreatureType.CLERIC:
            self.cleric = card
        if card.creature_type == CreatureType.COCKATRICE:
            self.cockatrice = card
        if card.creature_type == CreatureType.CONSTRUCT:
            self.construct = card
        if card.creature_type == CreatureType.COWARD:
            self.coward = card
        if card.creature_type == CreatureType.CRAB:
            self.crab = card
        if card.creature_type == CreatureType.CROCODILE:
            self.crocodile = card
        if card.creature_type == CreatureType.CYCLOPS:
            self.cyclops = card
        if card.creature_type == CreatureType.DAUTHI:
            self.dauthi = card
        if card.creature_type == CreatureType.DEMON:
            self.demon = card
        if card.creature_type == CreatureType.DESERTER:
            self.deserter = card
        if card.creature_type == CreatureType.DEVIL:
            self.devil = card
        if card.creature_type == CreatureType.DINOSAUR:
            self.dinosaur = card
        if card.creature_type == CreatureType.DJINN:
            self.djinn = card
        if card.creature_type == CreatureType.DRAGON:
            self.dragon = card
        if card.creature_type == CreatureType.DRAKE:
            self.drake = card
        if card.creature_type == CreatureType.DREADNOUGHT:
            self.dreadnought = card
        if card.creature_type == CreatureType.DRONE:
            self.drone = card
        if card.creature_type == CreatureType.DRUID:
            self.druid = card
        if card.creature_type == CreatureType.DRYAD:
            self.dryad = card
        if card.creature_type == CreatureType.DWARF:
            self.dwarf = card
        if card.creature_type == CreatureType.EFREET:
            self.efreet = card
        if card.creature_type == CreatureType.EGG:
            self.egg = card
        if card.creature_type == CreatureType.ELDER:
            self.elder = card
        if card.creature_type == CreatureType.ELDRAZI:
            self.eldrazi = card
        if card.creature_type == CreatureType.ELEMENTAL:
            self.elemental = card
        if card.creature_type == CreatureType.ELEPHANT:
            self.elephant = card
        if card.creature_type == CreatureType.ELF:
            self.elf = card
        if card.creature_type == CreatureType.ELK:
            self.elk = card
        if card.creature_type == CreatureType.EYE:
            self.eye = card
        if card.creature_type == CreatureType.FAERIE:
            self.faerie = card
        if card.creature_type == CreatureType.FERRET:
            self.ferret = card
        if card.creature_type == CreatureType.FISH:
            self.fish = card
        if card.creature_type == CreatureType.FLAGBEARER:
            self.flagbearer = card
        if card.creature_type == CreatureType.FOX:
            self.fox = card
        if card.creature_type == CreatureType.FROG:
            self.frog = card
        if card.creature_type == CreatureType.FUNGUS:
            self.fungus = card
        if card.creature_type == CreatureType.GARGOYLE:
            self.gargoyle = card
        if card.creature_type == CreatureType.GERM:
            self.germ = card
        if card.creature_type == CreatureType.GIANT:
            self.giant = card
        if card.creature_type == CreatureType.GNOME:
            self.gnome = card
        if card.creature_type == CreatureType.GOAT:
            self.goat = card
        if card.creature_type == CreatureType.GOBLIN:
            self.goblin = card
        if card.creature_type == CreatureType.GOD:
            self.god = card
        if card.creature_type == CreatureType.GOLEM:
            self.golem = card
        if card.creature_type == CreatureType.GORGON:
            self.gorgon = card
        if card.creature_type == CreatureType.GRAVEBORN:
            self.graveborn = card
        if card.creature_type == CreatureType.GREMLIN:
            self.gremlin = card
        if card.creature_type == CreatureType.GRIFFIN:
            self.griffin = card
        if card.creature_type == CreatureType.HAG:
            self.hag = card
        if card.creature_type == CreatureType.HALF:
            self.half = card
        if card.creature_type == CreatureType.HARPY:
            self.harpy = card
        if card.creature_type == CreatureType.HELLION:
            self.hellion = card
        if card.creature_type == CreatureType.HIPPO:
            self.hippo = card
        if card.creature_type == CreatureType.HIPPOGRIFF:
            self.hippogriff = card
        if card.creature_type == CreatureType.HOMARID:
            self.homarid = card
        if card.creature_type == CreatureType.HOMUNCULUS:
            self.homunculus = card
        if card.creature_type == CreatureType.HORROR:
            self.horror = card
        if card.creature_type == CreatureType.HORSE:
            self.horse = card
        if card.creature_type == CreatureType.HOUND:
            self.hound = card
        if card.creature_type == CreatureType.HUMAN:
            self.human = card
        if card.creature_type == CreatureType.HYDRA:
            self.hydra = card
        if card.creature_type == CreatureType.HYENA:
            self.hyena = card
        if card.creature_type == CreatureType.ILLUSION:
            self.illusion = card
        if card.creature_type == CreatureType.IMP:
            self.imp = card
        if card.creature_type == CreatureType.INCARNATION:
            self.incarnation = card
        if card.creature_type == CreatureType.INSECT:
            self.insect = card
        if card.creature_type == CreatureType.JACKAL:
            self.jackal = card
        if card.creature_type == CreatureType.JELLYFISH:
            self.jellyfish = card
        if card.creature_type == CreatureType.JUGGERNAUT:
            self.juggernaut = card
        if card.creature_type == CreatureType.KAVU:
            self.kavu = card
        if card.creature_type == CreatureType.KIRIN:
            self.kirin = card
        if card.creature_type == CreatureType.KITHKIN:
            self.kithkin = card
        if card.creature_type == CreatureType.KNIGHT:
            self.knight = card
        if card.creature_type == CreatureType.KOBOLD:
            self.kobold = card
        if card.creature_type == CreatureType.KOR:
            self.kor = card
        if card.creature_type == CreatureType.KRAKEN:
            self.kraken = card
        if card.creature_type == CreatureType.LAMIA:
            self.lamia = card
        if card.creature_type == CreatureType.LAMMASU:
            self.lammasu = card
        if card.creature_type == CreatureType.LEECH:
            self.leech = card
        if card.creature_type == CreatureType.LEVIATHAN:
            self.leviathan = card
        if card.creature_type == CreatureType.LHURGOYF:
            self.lhurgoyf = card
        if card.creature_type == CreatureType.LICID:
            self.licid = card
        if card.creature_type == CreatureType.LIZARD:
            self.lizard = card
        if card.creature_type == CreatureType.MANTICORE:
            self.manticore = card
        if card.creature_type == CreatureType.MASTICORE:
            self.masticore = card
        if card.creature_type == CreatureType.MERCENARY:
            self.mercenary = card
        if card.creature_type == CreatureType.MERFOLK:
            self.merfolk = card
        if card.creature_type == CreatureType.METATHRAN:
            self.metathran = card
        if card.creature_type == CreatureType.MINION:
            self.minion = card
        if card.creature_type == CreatureType.MINOTAUR:
            self.minotaur = card
        if card.creature_type == CreatureType.MOLE:
            self.mole = card
        if card.creature_type == CreatureType.MONGER:
            self.monger = card
        if card.creature_type == CreatureType.MONGOOSE:
            self.mongoose = card
        if card.creature_type == CreatureType.MONK:
            self.monk = card
        if card.creature_type == CreatureType.MONKEY:
            self.monkey = card
        if card.creature_type == CreatureType.MOONFOLK:
            self.moonfolk = card
        if card.creature_type == CreatureType.MUTANT:
            self.mutant = card
        if card.creature_type == CreatureType.MYR:
            self.myr = card
        if card.creature_type == CreatureType.MYSTIC:
            self.mystic = card
        if card.creature_type == CreatureType.NAAGA:
            self.naaga = card
        if card.creature_type == CreatureType.NAGA:
            self.naga = card
        if card.creature_type == CreatureType.NAUTILUS:
            self.nautilus = card
        if card.creature_type == CreatureType.NEPHILIM:
            self.nephilim = card
        if card.creature_type == CreatureType.NIGHTMARE:
            self.nightmare = card
        if card.creature_type == CreatureType.NIGHTSTALKER:
            self.nightstalker = card
        if card.creature_type == CreatureType.NINJA:
            self.ninja = card
        if card.creature_type == CreatureType.NOGGLE:
            self.noggle = card
        if card.creature_type == CreatureType.NOMAD:
            self.nomad = card
        if card.creature_type == CreatureType.NYPH:
            self.nymph = card
        if card.creature_type == CreatureType.OCTOPUS:
            self.octopus = card
        if card.creature_type == CreatureType.OGRE:
            self.ogre = card
        if card.creature_type == CreatureType.OOZE:
            self.ooze = card
        if card.creature_type == CreatureType.ORACLE:
            self.oracle = card
        if card.creature_type == CreatureType.ORC:
            self.orc = card
        if card.creature_type == CreatureType.ORGG:
            self.orgg = card
        if card.creature_type == CreatureType.OTTER:
            self.otter = card
        if card.creature_type == CreatureType.OUPHE:
            self.ouphe = card
        if card.creature_type == CreatureType.OYSTER:
            self.oyster = card
        if card.creature_type == CreatureType.PEGASUS:
            self.pegasus = card
        if card.creature_type == CreatureType.PENTAVITE:
            self.pentavite = card
        if card.creature_type == CreatureType.PEST:
            self.pest = card
        if card.creature_type == CreatureType.PHANTASM:
            self.phantasm = card
        if card.creature_type == CreatureType.PHOENIX:
            self.phoenix = card
        if card.creature_type == CreatureType.PILOT:
            self.pilot = card
        if card.creature_type == CreatureType.PINCHER:
            self.pincher = card
        if card.creature_type == CreatureType.PIRATE:
            self.pirate = card
        if card.creature_type == CreatureType.PLANT:
            self.plant = card
        if card.creature_type == CreatureType.PRAETOR:
            self.praetor = card
        if card.creature_type == CreatureType.PRISM:
            self.prism = card
        if card.creature_type == CreatureType.PROCESSOR:
            self.processor = card
        if card.creature_type == CreatureType.PYRROL:
            self.pyrrol = card
        if card.creature_type == CreatureType.RABBIT:
            self.rabbit = card
        if card.creature_type == CreatureType.RAT:
            self.rat = card
        if card.creature_type == CreatureType.REBEL:
            self.rebel = card
        if card.creature_type == CreatureType.REFLECTION:
            self.reflection = card
        if card.creature_type == CreatureType.RHINO:
            self.rhino = card
        if card.creature_type == CreatureType.RIGGER:
            self.rigger = card
        if card.creature_type == CreatureType.ROGUE:
            self.rogue = card
        if card.creature_type == CreatureType.SABLE:
            self.sable = card
        if card.creature_type == CreatureType.SALAMANDER:
            self.salamander = card
        if card.creature_type == CreatureType.SAMURAI:
            self.samurai = card
        if card.creature_type == CreatureType.SAND:
            self.sand = card
        if card.creature_type == CreatureType.SAPROLING:
            self.saproling = card
        if card.creature_type == CreatureType.SATYR:
            self.satyr = card
        if card.creature_type == CreatureType.SCARECROW:
            self.scarecrow = card
        if card.creature_type == CreatureType.SCION:
            self.scion = card
        if card.creature_type == CreatureType.SCORPION:
            self.scorpion = card
        if card.creature_type == CreatureType.SCOUT:
            self.scout = card
        if card.creature_type == CreatureType.SERF:
            self.serf = card
        if card.creature_type == CreatureType.SERPENT:
            self.serpent = card
        if card.creature_type == CreatureType.SERVITOR:
            self.servitor = card
        if card.creature_type == CreatureType.SHAMAN:
            self.shaman = card
        if card.creature_type == CreatureType.SHAPESHIFTER:
            self.shapeshifter = card
        if card.creature_type == CreatureType.SHARK:
            self.shark = card
        if card.creature_type == CreatureType.SHEEP:
            self.sheep = card
        if card.creature_type == CreatureType.SIREN:
            self.siren = card
        if card.creature_type == CreatureType.SKELETON:
            self.skeleton = card
        if card.creature_type == CreatureType.SLITH:
            self.slith = card
        if card.creature_type == CreatureType.SLIVER:
            self.sliver = card
        if card.creature_type == CreatureType.SLUG:
            self.slug = card
        if card.creature_type == CreatureType.SNAKE:
            self.snake = card
        if card.creature_type == CreatureType.SOLDIER:
            self.soldier = card
        if card.creature_type == CreatureType.SOLTARI:
            self.soltari = card
        if card.creature_type == CreatureType.SPAWN:
            self.spawn = card
        if card.creature_type == CreatureType.SPECTER:
            self.specter = card
        if card.creature_type == CreatureType.SPELLSHAPER:
            self.spellshaper = card
        if card.creature_type == CreatureType.SPHINX:
            self.sphinx = card
        if card.creature_type == CreatureType.SPIDER:
            self.spider = card
        if card.creature_type == CreatureType.SPIRIT:
            self.spirit = card
        if card.creature_type == CreatureType.SPLINTER:
            self.splinter = card
        if card.creature_type == CreatureType.SPONGE:
            self.sponge = card
        if card.creature_type == CreatureType.SQUID:
            self.squid = card
        if card.creature_type == CreatureType.SQUIRREL:
            self.squirrel = card
        if card.creature_type == CreatureType.STARFISH:
            self.starfish = card
        if card.creature_type == CreatureType.SURRAKAR:
            self.surrakar = card
        if card.creature_type == CreatureType.SURVIVOR:
            self.survivor = card
        if card.creature_type == CreatureType.TETRAVITE:
            self.tetravite = card
        if card.creature_type == CreatureType.THALAKOS:
            self.thalakos = card
        if card.creature_type == CreatureType.THEURGE:
            self.theurge = card
        if card.creature_type == CreatureType.THIRL:
            self.thirl = card
        if card.creature_type == CreatureType.THORN:
            self.thorn = card
        if card.creature_type == CreatureType.THRULL:
            self.thrull = card
        if card.creature_type == CreatureType.TREEFOLK:
            self.treefolk = card
        if card.creature_type == CreatureType.TRISKELAVITE:
            self.triskelavite = card
        if card.creature_type == CreatureType.TROLL:
            self.troll = card
        if card.creature_type == CreatureType.TURTLE:
            self.turtle = card
        if card.creature_type == CreatureType.UNICORN:
            self.unicorn = card
        if card.creature_type == CreatureType.VAMPIRE:
            self.vampire = card
        if card.creature_type == CreatureType.VEDALKEN:
            self.vedalken = card
        if card.creature_type == CreatureType.VIASHINO:
            self.viashino = card
        if card.creature_type == CreatureType.VOLVER:
            self.volver = card
        if card.creature_type == CreatureType.WALL:
            self.wall = card
        if card.creature_type == CreatureType.WARRIOR:
            self.warrior = card
        if card.creature_type == CreatureType.WEIRD:
            self.weird = card
        if card.creature_type == CreatureType.WEREWOLF:
            self.werewolf = card
        if card.creature_type == CreatureType.WHALE:
            self.whale = card
        if card.creature_type == CreatureType.WIZARD:
            self.wizard = card
        if card.creature_type == CreatureType.WOLF:
            self.wolf = card
        if card.creature_type == CreatureType.WOLVERINE:
            self.wolverine = card
        if card.creature_type == CreatureType.WOMBAT:
            self.wombat = card
        if card.creature_type == CreatureType.WORM:
            self.worm = card
        if card.creature_type == CreatureType.WRAITH:
            self.wraith = card
        if card.creature_type == CreatureType.WURM:
            self.wurm = card
        if card.creature_type == CreatureType.YETI:
            self.yeti = card
        if card.creature_type == CreatureType.ZOMBIE:
            self.zombie = card
        if card.creature_type == CreatureType.ZUBERA:
            self.zubera = card

        if card.land_type == LandType.PLAINS:
            self.plains = card
        if card.land_type == LandType.ISLAND:
            self.island = card
        if card.land_type == LandType.SWAMP:
            self.swamp = card
        if card.land_type == LandType.MOUNTAIN:
            self.mountain = card
        if card.land_type == LandType.FOREST:
            self.forest = card
        if card.land_type == LandSubType.DESERT:
            self.desert = card
        if card.land_type == LandSubType.GATE:
            self.gate = card
        if card.land_type == LandSubType.LAIR:
            self.lair = card
        if card.land_type == LandSubType.LOCUS:
            self.locus = card
        if card.land_type == LandSubType.MINE:
            self.mine = card
        if card.land_type == LandSubType.PHYREXIA:
            self.phyrexia = card
        if card.land_type == LandSubType.POWER_PLANT:
            self.power_plant = card
        if card.land_type == LandSubType.TOWER:
            self.tower = card
        if card.land_type == LandSubType.TOWN:
            self.town = card
        if card.land_type == LandSubType.URZA:
            self.urza = card
        if card.land_type == LandSubType.WASTE:
            self.waste = card
        if card.land_type == LandSubType.WORKSHOP:
            self.workshop = card

    def applies_to_phase(self, phase):
        return phase in self.phases

    def process(self):
        if self.id == AbilitySpecificType.AFFLICT:
            self.process_afflict()
        elif self.id == AbilitySpecificType.AMASS:
            self.process_amass()
        elif self.id == AbilitySpecificType.ANNIHILATOR:
            self.process_annihilator()
        elif self.id == AbilitySpecificType.ASCEND:
            self.process_ascend()
        elif self.id == AbilitySpecificType.BANDING:
            self.process_banding()
        elif self.id == AbilitySpecificType.BATTALION:
            self.process_battalion()
        elif self.id == AbilitySpecificType.BLOODTHIRST:
            self.process_bloodthirst()
        elif self.id == AbilitySpecificType.BUSHIDO:
            self.process_bushido()
        elif self.id == AbilitySpecificType.BUYBACK:
            self.process_buyback()
        elif self.id == AbilitySpecificType.CASCADE:
            self.process_cascade()
        elif self.id == AbilitySpecificType.CHAMPION:
            self.process_champion()
        elif self.id == AbilitySpecificType.CHANGELING:
            self.process_changeling()
        elif self.id == AbilitySpecificType.CIPHER:
            self.process_cipher()
        elif self.id == AbilitySpecificType.CLASH:
            self.process_clash()
        elif self.id == AbilitySpecificType.CONSPIRE:
            self.process_conspire()
        elif self.id == AbilitySpecificType.CONVOKE:
            self.process_convoke()
        elif self.id == AbilitySpecificType.CREW:
            self.process_crew()
        elif self.id == AbilitySpecificType.CUMULATIVE_UPKEEP:
            self.process_cumulative_upkeep()
        elif self.id == AbilitySpecificType.CYCLING:
            self.process_cycling()
        elif self.id == AbilitySpecificType.DASH:
            self.process_dash()
        elif self.id == AbilitySpecificType.DEATHTOUCH:
            self.process_deathtouch()
        elif self.id == AbilitySpecificType.DEFENDER:
            self.process_defender()
        elif self.id == AbilitySpecificType.DELVE:
            self.process_delve()
        elif self.id == AbilitySpecificType.DETAIN:
            self.process_detain()
        elif self.id == AbilitySpecificType.DETHRONE:
            self.process_dethrone()
        elif self.id == AbilitySpecificType.DEVOID:
            self.process_devoid()
        elif self.id == AbilitySpecificType.DEVOUR:
            self.process_devour()
        elif self.id == AbilitySpecificType.DOUBLE_STRIKE:
            self.process_double_strike()
        elif self.id == AbilitySpecificType.DREDGE:
            self.process_dredge()
        elif self.id == AbilitySpecificType.ECHO:
            self.process_echo()
        elif self.id == AbilitySpecificType.EMBALM:
            self.process_embalm()
        elif self.id == AbilitySpecificType.EMERGE:
            self.process_emerge()
        elif self.id == AbilitySpecificType.EMINENCE:
            self.process_eminence()
        elif self.id == AbilitySpecificType.ENCHANT:
            self.process_enchant()
        elif self.id == AbilitySpecificType.ENRAGE:
            self.process_enrage()
        elif self.id == AbilitySpecificType.ENTWINE:
            self.process_entwine()
        elif self.id == AbilitySpecificType.EPIC:
            self.process_epic()
        elif self.id == AbilitySpecificType.EQUIP:
            self.process_equip()
        elif self.id == AbilitySpecificType.ESCAPE:
            self.process_escape()
        elif self.id == AbilitySpecificType.EVOKE:
            self.process_evoke()
        elif self.id == AbilitySpecificType.EVOLVE:
            self.process_evolve()
        elif self.id == AbilitySpecificType.EXALTED:
            self.process_exalted()
        elif self.id == AbilitySpecificType.EXPLOIT:
            self.process_exploit()
        elif self.id == AbilitySpecificType.EXPLORE:
            self.process_explore()
        elif self.id == AbilitySpecificType.EXTORT:
            self.process_extort()
        elif self.id == AbilitySpecificType.FABRICATE:
            self.process_fabricate()
        elif self.id == AbilitySpecificType.FADING:
            self.process_fading()
        elif self.id == AbilitySpecificType.FEAR:
            self.process_fear()
        elif self.id == AbilitySpecificType.FEROCIOUS:
            self.process_ferocious()
        elif self.id == AbilitySpecificType.FIGHT:
            self.process_fight()
        elif self.id == AbilitySpecificType.FIRST_STRIKE:
            self.process_first_strike()
        elif self.id == AbilitySpecificType.FLANKING:
            self.process_flanking()
        elif self.id == AbilitySpecificType.FLASH:
            self.process_flash()
        elif self.id == AbilitySpecificType.FLASHBACK:
            self.process_flashback()
        elif self.id == AbilitySpecificType.FLIP:
            self.process_flip()
        elif self.id == AbilitySpecificType.FLYING:
            self.process_flying()
        elif self.id == AbilitySpecificType.FORECAST:
            self.process_forecast()
        elif self.id == AbilitySpecificType.FORTIFY:
            self.process_fortify()
        elif self.id == AbilitySpecificType.FRENZY:
            self.process_frenzy()
        elif self.id == AbilitySpecificType.FUSE:
            self.process_fuse()
        elif self.id == AbilitySpecificType.GRAFT:
            self.process_graft()
        elif self.id == AbilitySpecificType.GRAVESTORM:
            self.process_gravestorm()
        elif self.id == AbilitySpecificType.HASTE:
            self.process_haste()
        elif self.id == AbilitySpecificType.HAUNT:
            self.process_haunt()
        elif self.id == AbilitySpecificType.HELLBENT:
            self.process_hellbent()
        elif self.id == AbilitySpecificType.HEROIC:
            self.process_heroic()
        elif self.id == AbilitySpecificType.HEXPROOF:
            self.process_hexproof()
        elif self.id == AbilitySpecificType.HIDEAWAY:
            self.process_hideaway()
        elif self.id == AbilitySpecificType.HORSEMANSHIP:
            self.process_horsemanship()
        elif self.id == AbilitySpecificType.IMPRINT:
            self.process_imprint()
        elif self.id == AbilitySpecificType.INDESTRUCTIBLE:
            self.process_indestructible()
        elif self.id == AbilitySpecificType.INFECT:
            self.process_infect()
        elif self.id == AbilitySpecificType.INGEST:
            self.process_ingest()
        elif self.id == AbilitySpecificType.INTIMIDATE:
            self.process_intimidate()
        elif self.id == AbilitySpecificType.INVESTIGATE:
            self.process_investigate()
        elif self.id == AbilitySpecificType.JOIN:
            self.process_join()
        elif self.id == AbilitySpecificType.JUMP_START:
            self.process_jump_start()
        elif self.id == AbilitySpecificType.KICKER:
            self.process_kicker()
        elif self.id == AbilitySpecificType.KINSHIP:
            self.process_kinship()
        elif self.id == AbilitySpecificType.LANDFALL:
            self.process_landfall()
        elif self.id == AbilitySpecificType.LEVEL:
            self.process_level()
        elif self.id == AbilitySpecificType.LIFELINK:
            self.process_lifelink()
        elif self.id == AbilitySpecificType.LIVING_WEAPON:
            self.process_living_weapon()
        elif self.id == AbilitySpecificType.MADNESS:
            self.process_madness()
        elif self.id == AbilitySpecificType.MEGAMORPH:
            self.process_megamorph()
        elif self.id == AbilitySpecificType.MELEE:
            self.process_melee()
        elif self.id == AbilitySpecificType.MENACE:
            self.process_menace()
        elif self.id == AbilitySpecificType.MENTOR:
            self.process_mentor()
        elif self.id == AbilitySpecificType.MIRACLE:
            self.process_miracle()
        elif self.id == AbilitySpecificType.MODULAR:
            self.process_modular()
        elif self.id == AbilitySpecificType.MONSTROSITY:
            self.process_monstrosity()
        elif self.id == AbilitySpecificType.MORPH:
            self.process_morph()
        elif self.id == AbilitySpecificType.MULTIKICKER:
            self.process_multikicker()
        elif self.id == AbilitySpecificType.MUTATE:
            self.process_mutate()
        elif self.id == AbilitySpecificType.MYRIAD:
            self.process_myriad()
        elif self.id == AbilitySpecificType.NINJUTSU:
            self.process_ninjutsu()
        elif self.id == AbilitySpecificType.OFFERING:
            self.process_offering()
        elif self.id == AbilitySpecificType.OUTLAST:
            self.process_outlast()
        elif self.id == AbilitySpecificType.OVERLOAD:
            self.process_overload()
        elif self.id == AbilitySpecificType.PARTNER:
            self.process_partner()
        elif self.id == AbilitySpecificType.PERSIST:
            self.process_persist()
        elif self.id == AbilitySpecificType.PHASING:
            self.process_phasing()
        elif self.id == AbilitySpecificType.POISONOUS:
            self.process_poisonous()
        elif self.id == AbilitySpecificType.POPULATE:
            self.process_populate()
        elif self.id == AbilitySpecificType.PROLIFERATE:
            self.process_proliferate()
        elif self.id == AbilitySpecificType.PROVOKE:
            self.process_provoke()
        elif self.id == AbilitySpecificType.PROWESS:
            self.process_prowess()
        elif self.id == AbilitySpecificType.PROWL:
            self.process_prowl()
        elif self.id == AbilitySpecificType.RAID:
            self.process_raid()
        elif self.id == AbilitySpecificType.RALLY:
            self.process_rally()
        elif self.id == AbilitySpecificType.RAMPAGE:
            self.process_rampage()
        elif self.id == AbilitySpecificType.REACH:
            self.process_reach()
        elif self.id == AbilitySpecificType.REBOUND:
            self.process_rebound()
        elif self.id == AbilitySpecificType.RECOVER:
            self.process_recover()
        elif self.id == AbilitySpecificType.REINFORCE:
            self.process_reinforce()
        elif self.id == AbilitySpecificType.RENOWN:
            self.process_renown()
        elif self.id == AbilitySpecificType.REPLICATE:
            self.process_replicate()
        elif self.id == AbilitySpecificType.RETRACE:
            self.process_retrace()
        elif self.id == AbilitySpecificType.RIPPLE:
            self.process_ripple()
        elif self.id == AbilitySpecificType.RUSH:
            self.process_rush()
        elif self.id == AbilitySpecificType.SACRIFICE:
            self.process_sacrifice()
        elif self.id == AbilitySpecificType.SCAVENGE:
            self.process_scavenge()
        elif self.id == AbilitySpecificType.SHADOW:
            self.process_shadow()
        elif self.id == AbilitySpecificType.SHROUD:
            self.process_shroud()
        elif self.id == AbilitySpecificType.SKULK:
            self.process_skulk()
        elif self.id == AbilitySpecificType.SLIVERCYCLING:
            self.process_slivercycling()
        elif self.id == AbilitySpecificType.SOULBOND:
            self.process_soulbond()
        elif self.id == AbilitySpecificType.SOULSHIFT:
            self.process_soulshift()
        elif self.id == AbilitySpecificType.SPECTACLE:
            self.process_spectacle()
        elif self.id == AbilitySpecificType.SPLICE:
            self.process_splice()
        elif self.id == AbilitySpecificType.SPLIT:
            self.process_split()
        elif self.id == AbilitySpecificType.STORM:
            self.process_storm()
        elif self.id == AbilitySpecificType.SUNBURST:
            self.process_sunburst()
        elif self.id == AbilitySpecificType.SUPPORT:
            self.process_support()
        elif self.id == AbilitySpecificType.SURGE:
            self.process_surge()
        elif self.id == AbilitySpecificType.SUSPEND:
            self.process_suspend()
        elif self.id == AbilitySpecificType.TOTEM_ARMOR:
            self.process_totem_armor()
        elif self.id == AbilitySpecificType.TRAMPLE:
            self.process_trample()
        elif self.id == AbilitySpecificType.TRANSFIGURE:
            self.process_transfigure()
        elif self.id == AbilitySpecificType.TRANSFORM:
            self.process_transform()
        elif self.id == AbilitySpecificType.TRANSMUTE:
            self.process_transmute()
        elif self.id == AbilitySpecificType.TRIBUTE:
            self.process_tribute()
        elif self.id == AbilitySpecificType.TYPECYCLING:
            self.process_typecycling()
        elif self.id == AbilitySpecificType.UNDAUNTED:
            self.process_undaunted()
        elif self.id == AbilitySpecificType.UNDYING:
            self.process_undying()
        elif self.id == AbilitySpecificType.UNEARTH:
            self.process_unearth()
        elif self.id == AbilitySpecificType.UNLEASH:
            self.process_unleash()
        elif self.id == AbilitySpecificType.VANISHING:
            self.process_vanishing()
        elif self.id == AbilitySpecificType.VIGILANCE:
            self.process_vigilance()
        elif self.id == AbilitySpecificType.WITHER:
            self.process_wither()
        elif self.id == AbilitySpecificType.JOIN:
            self.process_join()
        elif self.id == AbilitySpecificType.LEVEL:
            self.process_level()
        elif self.id == AbilitySpecificType.FIRST_STRIKE:
            self.process_first_strike()

    def process_afflict(self):
        # Afflict ability might cause the opponent to lose life whenever this
        # creature is blocked
        self.creature.afflict()
        print(
            'Afflict ability activated. Opponent loses life when creature is '
            'blocked.')

    def process_amass(self):
        # Amass ability might allow the player to create a Zombie Army token
        # and put +1/+1 counters on it
        self.player.amass()
        print('Amass ability activated. Zombie Army token created.')

    def process_annihilator(self):
        # Annihilator ability might force the opponent to sacrifice
        # permanents when this creature attacks
        self.creature.annihilator()
        print(
            'Annihilator ability activated. Opponent must sacrifice '
            'permanents when creature attacks.')

    def process_ascend(self):
        # Ascend ability might give the player a bonus if they control ten or
        # more permanents
        if self.player.has_ten_permanents():
            self.player.ascend()
        print('Ascend ability activated. Player has ten or more permanents.')

    def process_banding(self):
        # Banding ability might allow a creature to attack with another
        # creature and share damage
        self.creature.banding()
        print('Banding ability activated. Creature has banding.')

    def process_battalion(self):
        # Battalion ability might trigger an effect when a creature attacks
        # with two other creatures
        self.creature.battalion()
        print(
            'Battalion ability activated. Effect triggered when creature '
            'attacks with two other creatures.')
        pass

    def process_bloodthirst(self):
        # Bloodthirst ability might increase the power of the player's units
        # if the opponent has lost health this turn
        if self.opponent.lost_health_this_turn:
            self.player.increase_unit_power()
        print('Bloodthirst ability activated. Player units power increased.')

    def process_bushido(self):
        # Bushido ability might increase the power and toughness of a unit
        # during combat
        if self.in_combat:
            self.unit.increase_power_and_toughness()
        print('Bushido ability activated. Unit power and toughness increased.')

    def process_buyback(self):
        # Buyback ability might allow a spell to be put back into the
        # player's hand after it's cast
        self.player.return_spell_to_hand(self.spell)
        print('Buyback ability activated. Spell returned to hand.')

    def process_cascade(self):
        # Cascade ability might allow the player to cast another spell from
        # their deck for free when they cast this spell
        self.player.cast_spell_for_free()
        print('Cascade ability activated. Free spell cast.')

    def process_champion(self):
        # Champion ability might allow a unit to be replaced with another
        # unit until this unit leaves play
        self.player.replace_unit(self.unit, self.replacement_unit)
        print('Champion ability activated. Unit replaced.')

    def process_crew(self):
        # Crew ability might allow a non-creature artifact to become a
        # creature until end of turn
        self.artifact.become_creature()
        print('Crew ability activated. Artifact became a creature.')

    def process_cumulative_upkeep(self):
        # Cumulative upkeep ability might require the player to pay an
        # increasing cost each turn
        self.player.pay_cumulative_upkeep(self.cost)
        print('Cumulative upkeep ability activated. Player paid upkeep cost.')

    def process_cycling(self):
        # Cycling ability might allow the player to discard this card and
        # draw a new one
        self.player.discard_and_draw(self.card)
        print('Cycling ability activated. Card discarded and new one drawn.')

    def process_dash(self):
        # Dash ability might allow the player to cast a creature for a lower
        # cost with haste, but it returns to hand at end of turn
        self.player.cast_with_dash(self.creature)
        print('Dash ability activated. Creature cast with dash.')

    def process_deathtouch(self):
        # Deathtouch ability might cause any creature dealt damage by this
        # creature to be destroyed
        self.creature.gain_deathtouch()
        print('Deathtouch ability activated. Creature gained deathtouch.')

    def process_defender(self):
        # Defender ability might prevent a creature from attacking
        self.creature.prevent_attack()
        print('Defender ability activated. Creature cannot attack.')

    def process_delve(self):
        # Delve ability might allow the player to exile cards from their
        # graveyard to help pay for a spell
        self.player.exile_cards_for_spell(self.spell)
        print('Delve ability activated. Cards exiled to help pay for spell.')

    def process_detain(self):
        # Detain ability might prevent a creature from attacking or blocking
        # until the next turn
        self.creature.detain()
        print(
            'Detain ability activated. Creature cannot attack or block until '
            'next turn.')

    def process_dethrone(self):
        # Dethrone ability might increase a creature's power and toughness
        # when attacking the player with the most life
        if self.player.is_at_most_life():
            self.creature.increase_power_and_toughness()
        print(
            'Dethrone ability activated. Creature power and toughness '
            'increased.')

    def process_devoid(self):
        # Devoid ability might make a card colorless, regardless of its mana
        # cost
        self.card.make_colorless()
        print('Devoid ability activated. Card is now colorless.')

    def process_devour(self):
        # Devour ability might allow a creature to consume other creatures to
        # gain power and toughness
        self.creature.devour()
        print(
            'Devour ability activated. Creature devoured others to gain power '
            'and toughness.')

    def process_double_strike(self):
        # Double Strike ability might allow a creature to deal its combat
        # damage twice
        self.creature.double_strike()
        print(
            'Double Strike ability activated. Creature can deal its combat '
            'damage twice.')

    def process_dredge(self):
        # Dredge ability might allow the player to return a card from their
        # graveyard to their hand
        self.player.dredge(self.card)
        print('Dredge ability activated. Card returned from graveyard to hand.')

    def process_echo(self):
        # Echo ability might require the player to pay the card's mana cost
        # again at the beginning of the next turn
        self.player.pay_echo(self.card)
        print('Echo ability activated. Player paid echo cost.')

    def process_embalm(self):
        # Embalm ability might allow the player to create a token copy of a
        # creature card in their graveyard
        self.player.embalm(self.creature)
        print('Embalm ability activated. Token copy of creature created.')

    def process_emerge(self):
        # Emerge ability might allow the player to cast a creature by
        # sacrificing another creature and paying the difference in their costs
        self.player.emerge(self.creature, self.sacrifice)
        print('Emerge ability activated. Creature cast by sacrificing another.')

    def process_eminence(self):
        # Eminence ability might give the player an advantage as long as this
        # card is in the command zone or on the battlefield
        self.player.eminence(self.card)
        print('Eminence ability activated. Player gains advantage.')

    def process_enchant(self):
        # Enchant ability might attach this card to a target creature,
        # providing some benefit or detriment
        self.player.enchant(self.card, self.target)
        print('Enchant ability activated. Card attached to target creature.')

    def process_enrage(self):
        # Enrage ability might trigger an effect whenever this creature is
        # dealt damage
        self.creature.enrage()
        print(
            'Enrage ability activated. Effect triggered when creature is '
            'dealt damage.')

    def process_entwine(self):
        # Entwine ability might allow the player to choose all modes of a
        # modal spell by paying an additional cost
        self.player.choose_all_modes(self.spell)
        print('Entwine ability activated. All modes of spell chosen.')

    def process_epic(self):
        # Epic ability might prevent the player from casting other spells for
        # the rest of the game, but allows them to copy this spell each turn
        self.player.prevent_casting(self.spell)
        print(
            'Epic ability activated. Player can only copy this spell each turn.'
        )

    def process_equip(self):
        # Equip ability might allow the player to attach an Equipment card to
        # a creature, providing some benefit
        self.player.equip(self.equipment, self.creature)
        print('Equip ability activated. Equipment attached to creature.')

    def process_escape(self):
        # Escape ability might allow the player to cast a card from their
        # graveyard by paying an additional cost and exiling other cards from
        # their graveyard
        self.player.escape(self.card)
        print('Escape ability activated. Card cast from graveyard.')

    def process_evoke(self):
        # Evoke ability might allow the player to cast a creature for a lower
        # cost, but it's sacrificed when it enters the battlefield
        self.player.cast_with_evoke(self.creature)
        print('Evoke ability activated. Creature cast with evoke.')

    def process_evolve(self):
        # Evolve ability might allow a creature to get a +1/+1 counter
        # whenever a bigger creature enters the battlefield under your control
        self.creature.evolve()
        print('Evolve ability activated. Creature can get +1/+1 counters.')

    def process_exalted(self):
        # Exalted ability might give a creature +1/+1 until end of turn
        # whenever it attacks alone
        self.creature.exalted()
        print(
            'Exalted ability activated. Creature gets +1/+1 when it attacks '
            'alone.')

    def process_exploit(self):
        # Exploit ability might allow the player to sacrifice a creature when
        # this creature enters the battlefield
        self.player.exploit(self.creature)
        print('Exploit ability activated. Player sacrificed a creature.')

    def process_extort(self):
        # Extort ability might allow the player to pay an additional cost
        # whenever they cast a spell to drain life from their opponents
        self.player.extort(self.spell)
        print('Extort ability activated. Player drained life from opponents.')

    def process_fabricate(self):
        # Fabricate ability might allow the player to put +1/+1 counters on a
        # creature when it enters the battlefield or create a number of 1/1
        # colorless Servo artifact creature tokens
        self.player.fabricate(self.creature)
        print(
            'Fabricate ability activated. Player put +1/+1 counters or '
            'created Servo tokens.')

    def process_fading(self):
        # Fading ability might cause a creature to be sacrificed when its
        # fade counter reaches 0
        self.creature.fading()
        print(
            'Fading ability activated. Creature will be sacrificed when fade '
            'counter reaches 0.')

    def process_fear(self):
        # Fear ability might prevent a creature from being blocked except by
        # artifact creatures and/or black creatures
        self.creature.fear()
        print(
            'Fear ability activated. Creature cannot be blocked except by '
            'artifact creatures and/or black creatures.')

    def process_ferocious(self):
        # Ferocious ability might trigger an effect when a creature with
        # power 4 or greater enters the battlefield
        self.creature.ferocious()
        print(
            'Ferocious ability activated. Effect triggered when creature with '
            'power 4 or greater enters the battlefield.')

    def process_fight(self):
        # Fight ability might allow a creature to deal damage to another
        # creature when it enters the battlefield
        self.creature.fight(self.target)
        print('Fight ability activated. Creature fought another creature.')

    def process_first_strike(self):
        # First Strike ability might allow a creature to deal combat damage
        # before creatures without First Strike
        self.creature.first_strike()
        print(
            'First Strike ability activated. Creature can deal combat damage '
            'before others.')

    def process_flanking(self):
        # Flanking ability might cause a creature to be blocked by an
        # additional creature when it's blocked
        self.creature.flanking()
        print(
            'Flanking ability activated. Creature is blocked by an additional '
            'creature.')

    def process_flash(self):
        # Flash ability might allow a creature to be cast at any time you
        # could cast an instant
        self.creature.flash()
        print('Flash ability activated. Creature can be cast at any time.')

    def process_flashback(self):
        # Flashback ability might allow the player to cast a spell from their
        # graveyard by paying an additional cost
        self.player.flashback(self.spell)
        print('Flashback ability activated. Spell cast from graveyard.')

    def process_flip(self):
        # Flip ability might allow a card to be turned over to reveal a
        # different card
        self.card.flip()
        print('Flip ability activated. Card turned over.')

    def process_flying(self):
        # Flying ability might allow a creature to be blocked only by other
        # creatures with flying or reach
        self.creature.flying()
        print(
            'Flying ability activated. Creature can only be blocked by other '
            'creatures with flying or reach.')

    def process_forecast(self):
        # Forecast ability might allow the player to reveal a card from their
        # hand and get a benefit
        self.player.forecast(self.card)
        print('Forecast ability activated. Card revealed from hand.')

    def process_fortify(self):
        # Fortify ability might allow the player to attach a Fortification
        # card to a land, providing some benefit
        self.player.fortify(self.fortification, self.land)
        print('Fortify ability activated. Fortification attached to land.')

    def process_frenzy(self):
        # Frenzy ability might allow a creature to attack each turn if able
        self.creature.frenzy()
        print(
            'Frenzy ability activated. Creature must attack each turn if able.')

    def process_fuse(self):
        # Fuse ability might allow the player to cast two spells for the cost
        # of one
        self.player.fuse(self.spell1, self.spell2)
        print('Fuse ability activated. Two spells cast for the cost of one.')

    def process_graft(self):
        # Graft ability might allow a creature to move +1/+1 counters to
        # another creature when it enters the battlefield
        self.creature.graft(self.target)
        print(
            'Graft ability activated. Creature moved +1/+1 counters to '
            'another creature.')

    def process_gravestorm(self):
        # Gravestorm ability might trigger an effect for each spell cast
        # before it this turn
        self.player.gravestorm(self.spell)
        print(
            'Gravestorm ability activated. Effect triggered for each spell '
            'cast before this one.')

    def process_haste(self):
        # Haste ability might allow a creature to attack or use abilities the
        # turn it enters the battlefield
        self.creature.haste()
        print(
            'Haste ability activated. Creature can attack or use abilities '
            'the turn it enters the battlefield.')

    def process_haunt(self):
        # Haunt ability might allow a creature to exile another creature when
        # it dies, then return to the battlefield
        self.creature.haunt(self.target)
        print(
            'Haunt ability activated. Creature exiled another creature when '
            'it died.')

    def process_hellbent(self):
        # Hellbent ability might trigger an effect when the player has no
        # cards in hand
        self.player.hellbent()
        print(
            'Hellbent ability activated. Effect triggered when player has no '
            'cards in hand.')

    def process_heroic(self):
        # Heroic ability might trigger an effect when a spell targets this
        # creature
        self.creature.heroic(self.spell)
        print(
            'Heroic ability activated. Effect triggered when spell targets '
            'creature.')

    def process_hexproof(self):
        # Hexproof ability might prevent a creature from being targeted by
        # spells or abilities
        self.creature.hexproof()
        print(
            'Hexproof ability activated. Creature cannot be targeted by '
            'spells or abilities.')

    def process_hideaway(self):
        # Hideaway ability might allow the player to exile a card face-down
        # and cast it later
        self.player.hideaway(self.card)
        print(
            'Hideaway ability activated. Card exiled face-down for later '
            'casting.')

    def process_horsemanship(self):
        # Horsemanship ability might allow a creature to be blocked only by
        # other creatures with horsemanship
        self.creature.horsemanship()
        print(
            'Horsemanship ability activated. Creature can only be blocked by '
            'other creatures with horsemanship.')

    def process_imprint(self):
        # Imprint ability might allow an artifact to gain the abilities of
        # another card
        self.artifact.imprint(self.card)
        print(
            'Imprint ability activated. Artifact gained abilities of another '
            'card.')

    def process_indestructible(self):
        # Indestructible ability might prevent a creature from being destroyed
        self.creature.indestructible()
        print('Indestructible ability activated. Creature cannot be destroyed.')

    def process_infect(self):
        # Infect ability might cause a creature to deal damage in the form of
        # poison counters
        self.creature.infect()
        print(
            'Infect ability activated. Creature deals damage in the form of '
            'poison counters.')

    def process_ingest(self):
        # Ingest ability might allow a creature to exile cards from an
        # opponent's library
        self.creature.ingest(self.opponent)
        print(
            'Ingest ability activated. Creature exiled cards from opponent\'s '
            'library.')

    def process_intimidate(self):
        # Intimidate ability might prevent a creature from being blocked
        # except by artifact creatures and/or black creatures
        self.creature.intimidate()
        print(
            'Intimidate ability activated. Creature cannot be blocked except '
            'by artifact creatures and/or black creatures.')

    def process_investigate(self):
        # Investigate ability might allow the player to create a Clue token,
        # which can be sacrificed to draw a card
        self.player.investigate()
        print('Investigate ability activated. Clue token created.')

    def process_join_forces(self):
        # Join Forces ability might allow the player to combine forces with
        # other players to cast a spell
        self.player.join_forces(self.spell)
        print(
            'Join Forces ability activated. Players combined forces to cast '
            'spell.')

    def process_jump_start(self):
        # Jump-Start ability might allow the player to cast a spell from
        # their graveyard by discarding a card
        self.player.jump_start(self.spell)
        print(
            'Jump-Start ability activated. Spell cast from graveyard by '
            'discarding a card.')

    def process_kicker(self):
        # Kicker ability might allow the player to pay an additional cost for
        # an extra effect when casting a spell
        self.player.kicker(self.spell)
        print(
            'Kicker ability activated. Additional cost paid for extra effect.')

    def process_kinship(self):
        # Kinship ability might trigger an effect when a creature with the
        # same creature type enters the battlefield
        self.creature.kinship()
        print(
            'Kinship ability activated. Effect triggered when creature with '
            'same type enters battlefield.')

    def process_landfall(self):
        # Landfall ability might trigger an effect whenever a land enters the
        # battlefield under your control
        self.player.landfall()
        print(
            'Landfall ability activated. Effect triggered when land enters '
            'battlefield.')

    def process_last_strike(self):
        # Last Strike ability might allow a creature to deal combat damage
        # after creatures without First Strike
        self.creature.last_strike()
        print(
            'Last Strike ability activated. Creature can deal combat damage '
            'after others.')

    def process_lifelink(self):
        # Lifelink ability might cause a creature to gain life equal to the
        # damage it deals
        self.creature.lifelink()
        print(
            'Lifelink ability activated. Creature gains life equal to damage '
            'dealt.')

    def process_living_weapon(self):
        # Living Weapon ability might allow a creature to create a Germ token
        # when it enters the battlefield
        self.creature.living_weapon()
        print('Living Weapon ability activated. Creature created Germ token.')

    def process_madness(self):
        # Madness ability might allow the player to cast a card from their
        # graveyard by discarding it
        self.player.madness(self.card)
        print(
            'Madness ability activated. Card cast from graveyard by '
            'discarding it.')

    def process_megamorph(self):
        # Megamorph ability might allow a creature to be turned face-up for a
        # cost, gaining power and toughness
        self.creature.megamorph()
        print(
            'Megamorph ability activated. Creature turned face-up for a cost.')

    def process_melee(self):
        # Melee ability might trigger an effect when a creature attacks alone
        self.creature.melee()
        print(
            'Melee ability activated. Effect triggered when creature attacks '
            'alone.')

    def process_menace(self):
        # Menace ability might prevent a creature from being blocked except by
        # two or more creatures
        self.creature.menace()
        print(
            'Menace ability activated. Creature cannot be blocked except by two or more creatures.')

    def process_mentor(self):
        # Mentor ability might allow a creature to put a +1/+1 counter on
        # another attacking creature with less power
        self.creature.mentor(self.target)
        print(
            'Mentor ability activated. Creature put +1/+1 counter on another attacking creature.')

    def process_miracle(self):
        # Miracle ability might allow the player to cast a spell for a reduced
        # cost if it's the first card drawn that turn
        self.player.miracle(self.spell)
        print('Miracle ability activated. Spell cast for reduced cost.')

    def process_modular(self):
        # Modular ability might allow a creature to move +1/+1 counters to
        # another artifact creature when it dies
        self.creature.modular(self.target)
        print(
            'Modular ability activated. Creature moved +1/+1 counters to another artifact creature.')

    def process_monstrosity(self):
        # Monstrosity ability might allow a creature to gain +1/+1 counters and
        # other abilities
        self.creature.monstrosity()
        print(
            'Monstrosity ability activated. Creature gained +1/+1 counters and other abilities.')

    def process_morph(self):
        # Morph ability might allow a player to cast a creature face-down for a
        # reduced cost
        self.player.morph(self.creature)
        print(
            'Morph ability activated. Creature cast face-down for reduced cost.')

    def process_multikicker(self):
        # Multikicker ability might allow the player to pay an additional cost
        # for an extra effect when casting a spell
        self.player.multikicker(self.spell)
        print(
            'Multikicker ability activated. Additional cost paid for extra effect.')

    def process_mutate(self):
        # Mutate ability might allow a creature to combine with another creature
        # to gain abilities
        self.creature.mutate(self.target)
        print(
            'Mutate ability activated. Creature combined with another to gain abilities.')

    def process_myriad(self):
        # Myriad ability might create token copies of a creature that can attack
        # different opponents
        self.creature.myriad()
        print('Myriad ability activated. Token copies of creature created.')

    def process_ninjutsu(self):
        # Ninjutsu ability might allow a player to swap a creature in their hand
        # with an unblocked attacking creature
        self.player.ninjutsu(self.creature)
        print(
            'Ninjutsu ability activated. Creature swapped with unblocked attacker.')

    def process_offering(self):
        # Offering ability might allow the player to cast a creature for a
        # reduced cost if an opponent has a creature of the same type
        self.player.offering(self.creature)
        print('Offering ability activated. Creature cast for reduced cost.')

    def process_outlast(self):
        # Outlast ability might allow a creature to put +1/+1 counters on itself
        # for a cost
        self.creature.outlast()
        print(
            'Outlast ability activated. Creature put +1/+1 counters on itself.')

    def process_overload(self):
        # Overload ability might allow the player to cast a spell for a higher
        # cost with additional effects
        self.player.overload(self.spell)
        print(
            'Overload ability activated. Spell cast for higher cost with additional effects.')

    def process_partner(self):
        # Partner ability might allow the player to combine forces with another
        # player to cast a spell
        self.player.partner(self.spell)
        print(
            'Partner ability activated. Players combined forces to cast spell.')

    def process_persist(self):
        # Persist ability might allow a creature to return to the battlefield
        # with a -1/-1 counter when it dies
        self.creature.persist()
        print(
            'Persist ability activated. Creature returned to battlefield with -1/-1 counter.')

    def process_phasing(self):
        # Phasing ability might cause a creature to be removed from the game
        # until the next turn
        self.creature.phasing()
        print(
            'Phasing ability activated. Creature removed from game until next turn.')

    def process_poisonous(self):
        # Poisonous ability might cause a creature to deal damage in the form of
        # poison counters
        self.creature.poisonous()
        print(
            'Poisonous ability activated. Creature deals damage in the form of poison counters.')

    def process_populate(self):
        # Populate ability might allow the player to create a token copy of a
        # creature token they control
        self.player.populate(self.token)
        print('Populate ability activated. Token copy of creature created.')

    def process_proliferate(self):
        # Proliferate ability might allow the player to add +1/+1 counters,
        # loyalty counters, or poison counters to permanents
        self.player.proliferate(self.target)
        print('Proliferate ability activated. Added counters to permanents.')

    def process_provoke(self):
        # Provoke ability might force a creature to block this creature when it
        # attacks
        self.creature.provoke(self.target)
        print(
            'Provoke ability activated. Creature forced to block this creature.')

    def process_prowess(self):
        # Prowess ability might trigger an effect whenever the player casts a
        # non-creature spell
        self.player.prowess(self.spell)
        print(
            'Prowess ability activated. Effect triggered when non-creature spell cast.')

    def process_prowl(self):
        # Prowl ability might allow the player to cast a spell for a reduced
        # cost if a creature dealt combat damage this turn
        self.player.prowl(self.spell)
        print('Prowl ability activated. Spell cast for reduced cost.')

    def process_raid(self):
        # Raid ability might trigger an effect when a creature attacks after
        # another creature has attacked
        self.creature.raid()
        print(
            'Raid ability activated. Effect triggered when creature attacks after another.')

    def process_rally(self):
        # Rally ability might trigger an effect when a creature with the same
        # creature type enters the battlefield
        self.creature.rally()
        print(
            'Rally ability activated. Effect triggered when creature with same type enters battlefield.')

    def process_rampage(self):
        # Rampage ability might allow a creature to get +1/+1 for each creature
        # blocking it beyond the first
        self.creature.rampage()
        print(
            'Rampage ability activated. Creature gets +1/+1 for each creature blocking it beyond the first.')

    def process_reach(self):
        # Reach ability might allow a creature to block flying creatures
        self.creature.reach()
        print('Reach ability activated. Creature can block flying creatures.')

    def process_rebound(self):
        # Rebound ability might allow the player to cast a spell from their
        # graveyard without paying its mana cost
        self.player.rebound(self.spell)
        print(
            'Rebound ability activated. Spell cast from graveyard without paying cost.')

    def process_recover(self):
        # Recover ability might allow the player to return a card from their
        # graveyard to their hand
        self.player.recover(self.card)
        print(
            'Recover ability activated. Card returned from graveyard to hand.')

    def process_reinforce(self):
        # Reinforce ability might allow the player to put +1/+1 counters on a
        # creature for a cost
        self.player.reinforce(self.creature)
        print(
            'Reinforce ability activated. Creature put +1/+1 counters on itself.')

    def process_renown(self):
        # Renown ability might allow a creature to get +1/+1 counters when it
        # deals combat damage to a player
        self.creature.renown()
        print(
            'Renown ability activated. Creature gets +1/+1 counters when it deals combat damage.')

    def process_replicate(self):
        # Replicate ability might allow the player to copy a spell for each time
        # they pay the replicate cost
        self.player.replicate(self.spell)
        print(
            'Replicate ability activated. Spell copied for each replicate cost paid.')

    def process_retrace(self):
        # Retrace ability might allow the player to cast a spell from their
        # graveyard by discarding a land card
        self.player.retrace(self.spell)
        print(
            'Retrace ability activated. Spell cast from graveyard by discarding land card.')

    def process_ripple(self):
        # Ripple ability might allow the player to reveal cards from their
        # library and cast a spell for free
        self.player.ripple(self.spell)
        print('Ripple ability activated. Spell cast for free.')

    def process_rush(self):
        # Rush ability might allow a creature to gain haste when it enters the
        # battlefield
        self.creature.rush()
        print('Rush ability activated. Creature gains haste.')

    def process_sacrifice(self):
        # Sacrifice ability might allow the player to destroy a creature to gain
        # an advantage
        self.player.sacrifice(self.creature)
        print(
            'Sacrifice ability activated. Creature destroyed to gain advantage.')

    def process_scavenge(self):
        # Scavenge ability might allow the player to exile a creature card from
        # their graveyard to put +1/+1 counters on a creature
        self.player.scavenge(self.creature)
        print(
            'Scavenge ability activated. Creature card exiled to put +1/+1 counters on creature.')

    def process_scry(self):
        # Scry ability might allow the player to look at the top cards of their
        # library and put them back in any order
        self.player.scry()
        print('Scry ability activated. Player looked at top cards of library.')

    def process_search(self):
        # Search ability might allow the player to look for a card in their
        # library and put it into their hand
        self.player.search(self.card)
        print(
            'Search ability activated. Card found in library and put into hand.')

    def process_soulbond(self):
        # Soulbond ability might allow a creature to gain abilities when paired
        # with another creature
        self.creature.soulbond(self.target)
        print(
            'Soulbond ability activated. Creature gained abilities when paired with another.')

    def process_soulshift(self):
        # Soulshift ability might allow the player to return a spirit card from
        # their graveyard to their hand
        self.player.soulshift(self.card)
        print(
            'Soulshift ability activated. Spirit card returned from graveyard to hand.')

    def process_splice(self):
        # Splice ability might allow the player to combine two spells for a
        # reduced cost
        self.player.splice(self.spell1, self.spell2)
        print('Splice ability activated. Two spells combined for reduced cost.')

    def process_split_second(self):
        # Split Second ability might prevent players from casting spells or activating abilities in response to this spell
        self.spell.split_second()
        print(
            'Split Second ability activated. Players cannot respond to this spell.')

    def process_storm(self):
        # Storm ability might trigger an effect for each spell cast before it this turn
        self.player.storm(self.spell)
        print(
            'Storm ability activated. Effect triggered for each spell cast before this one.')

    def process_sunburst(self):
        # Sunburst ability might allow a creature to gain +1/+1 counters for each color of mana spent to cast it
        self.creature.sunburst()
        print(
            'Sunburst ability activated. Creature gains +1/+1 counters for each color of mana spent.')

    def process_suspend(self):
        # Suspend ability might allow the player to cast a spell for a reduced cost after a certain number of turns
        self.player.suspend(self.spell)
        print(
            'Suspend ability activated. Spell cast for reduced cost after certain number of turns.')

    def process_sweep(self):
        # Sweep ability might allow the player to cast a spell for a higher cost with additional effects
        self.player.sweep(self.spell)
        print(
            'Sweep ability activated. Spell cast for higher cost with additional effects.')

    def process_tap(self):
        # Tap ability might prevent a creature from attacking or using abilities until it untaps
        self.creature.tap()
        print(
            'Tap ability activated. Creature cannot attack or use abilities until it untaps.')

    def process_threshold(self):
        # Threshold ability might trigger an effect when the player has seven or more cards in their graveyard
        self.player.threshold()
        print(
            'Threshold ability activated. Effect triggered when player has seven or more cards in graveyard.')

    def process_totem_armor(self):
        # Totem Armor ability might prevent a creature from being destroyed, instead destroying an Aura attached to it
        self.creature.totem_armor()
        print(
            'Totem Armor ability activated. Creature cannot be destroyed, Aura is destroyed instead.')

    def process_transfigure(self):
        # Transfigure ability might allow the player to search their library for a creature card with the same converted mana cost
        self.player.transfigure(self.creature)
        print('Transfigure ability activated. Creature card found in library.')

    def process_transmute(self):
        # Transmute ability might allow the player to search their library for a card with the same converted mana cost
        self.player.transmute(self.card)
        print('Transmute ability activated. Card found in library.')

    def process_tutor(self):
        # Tutor ability might allow the player to search their library for a card and put it into their hand
        self.player.tutor(self.card)
        print(
            'Tutor ability activated. Card found in library and put into hand.')

    def process_unearth(self):
        # Unearth ability might allow the player to return a creature card from their graveyard to the battlefield
        self.player.unearth(self.creature)
        print(
            'Unearth ability activated. Creature card returned from graveyard to battlefield.')

    def process_untap(self):
        # Untap ability might allow a creature to untap during the untap step
        self.creature.untap()
        print('Untap ability activated. Creature untapped during untap step.')

    def process_vanishing(self):
        # Vanishing ability might cause a creature to be sacrificed when its vanish counter reaches 0
        self.creature.vanishing()
        print(
            'Vanishing ability activated. Creature will be sacrificed when vanish counter reaches 0.')

    def process_vigilance(self):
        # Vigilance ability might allow a creature to attack without tapping
        self.creature.vigilance()
        print(
            'Vigilance ability activated. Creature can attack without tapping.')

    def process_wither(self):
        # Wither ability might cause a creature to deal damage in the form of -1/-1 counters
        self.creature.wither()
        print(
            'Wither ability activated. Creature deals damage in the form of -1/-1 counters.')

    def process_wrath(self):
        # Wrath ability might allow the player to destroy all creatures on the battlefield
        self.player.wrath()
        print(
            'Wrath ability activated. All creatures destroyed on battlefield.')

    def process_x(self):
        # X ability might allow the player to choose the value of X when casting a spell
        self.player.choose_x(self.spell)
        print(
            'X ability activated. Player chose value of X when casting spell.')

    def process_yank(self):
        # Yank ability might allow the player to return a permanent to its owner's hand
        self.player.yank(self.permanent)
        print('Yank ability activated. Permanent returned to owner\'s hand.')

    def process_zendikar(self):
        # Zendikar ability might trigger an effect when a land enters the battlefield under your control
        self.player.zendikar()
        print(
            'Zendikar ability activated. Effect triggered when land enters battlefield.')

    def process_zombie(self):
        # Zombie ability might allow the player to create a Zombie token when a creature dies
        self.player.zombie(self.creature)
        print(
            'Zombie ability activated. Zombie token created when creature died.')

    def process_zurgo(self):
        # Zurgo ability might allow the player to return a creature from their graveyard to the battlefield
        self.player.zurgo(self.creature)
        print(
            'Zurgo ability activated. Creature returned from graveyard to battlefield.')

    def process_changeling(self):
        # Changeling ability might allow a creature to have all creature types
        self.creature.changeling()
        print('Changeling ability activated. Creature has all creature types.')

    def process_cipher(self):
        # Cipher ability might allow the player to exile a spell and cast it for free when the creature deals combat damage
        self.player.cipher(self.spell)
        print(
            'Cipher ability activated. Spell exiled and cast for free when creature deals combat damage.')

    def process_join(self):
        # Join ability might allow the player to combine forces with another player to cast a spell
        self.player.join(self.spell)
        print('Join ability activated. Players combined forces to cast spell.')

    def process_level(self):
        # Level ability might allow a creature to gain +1/+1 counters and abilities when it levels up
        self.creature.level()
        print(
            'Level ability activated. Creature gained +1/+1 counters and abilities when it leveled up.')

    def process_shadow(self):
        # Shadow ability might prevent a creature from being blocked except by other creatures with shadow
        self.creature.shadow()
        print(
            'Shadow ability activated. Creature cannot be blocked except by other creatures with shadow.')

    def process_shroud(self):
        # Shroud ability might prevent a creature from being targeted by spells or abilities
        self.creature.shroud()
        print(
            'Shroud ability activated. Creature cannot be targeted by spells or abilities.')

    def process_support(self):
        # Support ability might allow a creature to put +1/+1 counters on another creature when it enters the battlefield
        self.creature.support(self.target)
        print(
            'Support ability activated. Creature put +1/+1 counters on another creature.')

    def process_skulk(self):
        # Skulk ability might prevent a creature from being blocked except by creatures with greater power
        self.creature.skulk()
        print(
            'Skulk ability activated. Creature cannot be blocked except by creatures with greater power.')

    def process_surge(self):
        # Surge ability might allow the player to cast a spell for a reduced cost if another spell was cast this turn
        self.player.surge(self.spell)
        print(
            'Surge ability activated. Spell cast for reduced cost if another spell was cast this turn.')

    def process_slivercycling(self):
        # Slivercycling ability might allow the player to search their library for a Sliver card
        self.player.slivercycling(self.card)
        print('Slivercycling ability activated. Sliver card found in library.')

    def process_trample(self):
        # Trample ability might allow a creature to deal excess combat damage to the defending player
        self.creature.trample()
        print(
            'Trample ability activated. Creature can deal excess combat damage to defending player.')

    def process_split(self):
        # Split ability might allow the player to cast two spells for the cost of one
        self.player.split(self.spell1, self.spell2)
        print('Split ability activated. Two spells cast for the cost of one.')

    def process_spectacle(self):
        # Spectacle ability might allow the player to cast a spell for a reduced cost if an opponent lost life this turn
        self.player.spectacle(self.spell)
        print(
            'Spectacle ability activated. Spell cast for reduced cost if opponent lost life this turn.')

    def process_transform(self):
        # Transform ability might allow a card to be turned over to reveal a different card
        self.card.transform()
        print('Transform ability activated. Card turned over.')

    def process_tribute(self):
        # Tribute ability might allow the player to choose between two effects when a creature enters the battlefield
        self.player.tribute(self.creature)
        print(
            'Tribute ability activated. Player chose between two effects when creature entered battlefield.')

    def process_typecycling(self):
        # Typecycling ability might allow the player to search their library for a card with a specific type
        self.player.typecycling(self.card)
        print(
            'Typecycling ability activated. Card with specific type found in library.')

    def process_undaunted(self):
        # Undaunted ability might allow the player to cast a spell for a reduced cost for each opponent
        self.player.undaunted(self.spell)
        print(
            'Undaunted ability activated. Spell cast for reduced cost for each opponent.')

    def process_undying(self):
        # Undying ability might allow a creature to return to the battlefield with a +1/+1 counter when it dies
        self.creature.undying()
        print(
            'Undying ability activated. Creature returned to battlefield with +1/+1 counter.')

    def process_unleash(self):
        # Unleash ability might allow a creature to enter the battlefield with a +1/+1 counter and be unable to block
        self.creature.unleash()
        print(
            'Unleash ability activated. Creature entered battlefield with +1/+1 counter and unable to block.')

    def process_explore(self):
        # Explore ability might allow the player to reveal the top card of their library and put it into their hand
        self.player.explore()
        print(
            'Explore ability activated. Top card of library revealed and put into hand.')

    def process_clash(self):
        # Clash ability might allow the player to reveal cards from the top of their library and win a clash
        self.player.clash()
        print(
            'Clash ability activated. Cards revealed from top of library and clash won.')

    def process_conspire(self):
        # Conspire ability might allow the player to copy a spell for free if they tap two creatures
        self.player.conspire(self.spell)
        print(
            'Conspire ability activated. Spell copied for free if two creatures tapped.')

    def process_convoke(self):
        # Convoke ability might allow the player to cast a spell for a reduced cost by tapping creatures
        self.player.convoke(self.spell)
        print(
            'Convoke ability activated. Spell cast for reduced cost by tapping creatures.')


class EventLoop:
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.event_emitter = EventEmitter()

        self.player = Player()
        self.phase = EventType.E_PHASE_UNTAP
        self.turn = PlayerType.PLAYER

        self.event_emitter.on(EventType.E_PHASE_UNTAP, self.on_e_phase_untap)
        self.event_emitter.on(EventType.E_PHASE_UPKEEP, self.on_e_phase_upkeep)
        self.event_emitter.on(EventType.E_PHASE_DRAW, self.on_e_phase_draw)
        self.event_emitter.on(EventType.E_PHASE_COMBAT_START,
                              self.on_e_phase_combat_start)
        self.event_emitter.on(EventType.E_PHASE_COMBAT_DECLARE_ATTACKERS,
                              self.on_e_phase_combat_declare_attackers)
        self.event_emitter.on(EventType.E_PHASE_COMBAT_DAMAGE,
                              self.on_e_phase_combat_damage)
        self.event_emitter.on(EventType.E_PHASE_COMBAT_END,
                              self.on_e_phase_combat_end)
        self.event_emitter.on(EventType.E_PHASE_END, self.on_e_phase_end)
        self.event_emitter.on(EventType.E_PHASE_CLEANUP,
                              self.on_e_phase_cleanup)
        self.event_emitter.on(EventType.E_START_NEXT_TURN,
                              self.on_e_start_next_turn)
        self.event_emitter.on(EventType.E_START_NEXT_PHASE,
                              self.on_e_start_next_phase)
        self.event_emitter.on(EventType.E_MOD_PLAYER_HEALTH,
                              self.on_e_mod_player_health)
        self.event_emitter.on(EventType.E_MOD_CARD_HEALTH,
                              self.on_e_mod_card_health)
        self.event_emitter.on(EventType.E_PROCESS_ABILITIES,
                              self.on_e_process_abilities)
        self.event_emitter.on(EventType.E_GAME_WON, self.on_e_game_won)
        self.event_emitter.on(EventType.E_GAME_START, self.on_e_game_start)
        self.event_emitter.on(EventType.E_GAME_STOP, self.on_e_game_stop)
        self.event_emitter.on(EventType.E_DECK_EDIT, self.on_e_deck_edit)
        self.event_emitter.on(EventType.E_CONFIG_EDIT, self.on_e_config_edit)

    def run(self):
        try:
            self.loop.run_forever()
        except KeyboardInterrupt:
            self.loop.close()

    @staticmethod
    def trigger(event):
        return event.callback(event)

    def on_e_phase_untap(self, event: Event):
        print("Untap phase")

        self.event_emitter.emit(Event(EventType.E_START_NEXT_PHASE))

    def on_e_phase_upkeep(self, event: Event):
        print("Upkeep phase")

        self.event_emitter.emit(Event(EventType.E_PROCESS_ABILITIES))

        self.event_emitter.emit(Event(EventType.E_START_NEXT_PHASE))

    def on_e_phase_draw(self, event: Event):
        print("Draw phase")

        self.event_emitter.emit(Event(EventType.E_PROCESS_ABILITIES))

        self.player.hand.append(self.player.stack.pop())
        self.event_emitter.emit(Event(EventType.E_START_NEXT_PHASE))

    def on_e_phase_combat_start(self, event: Event):
        print("Combat start phase")

        self.event_emitter.emit(Event(EventType.E_PROCESS_ABILITIES))

        self.event_emitter.emit(Event(EventType.E_START_NEXT_PHASE))

    def on_e_phase_combat_declare_attackers(self, event: Event):
        print("Combat declare attackers phase")

        self.event_emitter.emit(Event(EventType.E_PROCESS_ABILITIES))

        card = self.player.table.pop()
        self.player.combat.append(card) if card is not None else None

        self.event_emitter.emit(Event(EventType.E_START_NEXT_PHASE))

    def on_e_phase_combat_damage(self, event: Event):
        print("Combat damage phase")

        self.event_emitter.emit(Event(EventType.E_PROCESS_ABILITIES))

        for card in self.player.combat:
            for blocker in card.get_blockers():
                card.attack(blocker)
                blocker.attack(card)
                if not blocker.can_survive():
                    blocker.destroy()
                    continue
            if not card.can_survive():
                card.destroy()
                continue

        self.event_emitter.emit(Event(EventType.E_START_NEXT_PHASE))

    def on_e_phase_combat_end(self, event: Event):
        print("Combat end phase")

        self.event_emitter.emit(Event(EventType.E_PROCESS_ABILITIES))

        self.event_emitter.emit(Event(EventType.E_START_NEXT_PHASE))

    def on_e_phase_end(self, event: Event):
        print("End phase")

        self.event_emitter.emit(Event(EventType.E_PROCESS_ABILITIES))

        self.event_emitter.emit(Event(EventType.E_START_NEXT_PHASE))

    def on_e_phase_cleanup(self, event: Event):
        print("Cleanup phase")

        self.event_emitter.emit(Event(EventType.E_START_NEXT_PHASE))

    def on_e_start_next_turn(self, event: Event):
        print("Starting next turn")

        self.turn = PlayerType(not int(self.turn))

    def on_e_start_next_phase(self, event: Event):
        print("Starting next phase")
        self.phase = (int(self.phase) + 1) % 8
        if self.phase == 0:
            self.event_emitter.emit(Event(EventType.E_START_NEXT_TURN))

    def on_e_mod_player_health(self, event: Event):
        print("Modifying player health")

        points = event.data[0]
        if points > 0:
            self.player.heal(points)
        else:
            self.player.attack(points)

    def on_e_mod_card_health(self, event: Event):
        print("Modifying card health")
        card, power, toughness = event.data
        card.power += power
        card.toughness += toughness

    def on_e_process_abilities(self, event: Event):
        print("Processing abilities")
        for card in self.player.table:
            for ability in card.abilities:
                if ability.applies_to_phase(self.phase):
                    ability.process()

    def on_e_game_won(self, event: Event):
        print("Game won")
        winner, loser = event.data
        print(f'{winner.name} won the game against {loser.name}')

    def on_e_game_start(self, event: Event):
        print("Game started")
        self.turn = PlayerType(random.Random().randint(0, 1))

    def on_e_game_stop(self, event: Event):
        print("Game stopped")

    def on_e_deck_edit(self, event: Event):
        print("Editing deck")

    def on_e_config_edit(self, event: Event):
        print("Editing config")
