#!/usr/bin/env python
#
# Electrum - lightweight Bitcoin client
# Copyright (C) 2011 thomasv@gitorious
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.



# list of words from http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Contemporary_poetry

words = [
"like",
"just",
"love",
"one",
"know",
"never",
"want",
"see",
"time",
"now",
"out",
"feel",
"there",
"life",
"make",
"look",
"eye",
"say",
"day",
"down",
"only",
"think",
"heart",
"back",
"then",
"into",
"come",
"about",
"more",
"away",
"still",
"way",
"them",
"take",
"thing",
"even",
"through",
"long",
"always",
"world",
"too",
"friend",
"tell",
"try",
"hand",
"face",
"thought",
"over",
"here",
"word",
"other",
"where",
"need",
"smile",
"again",
"much",
"cry",
"been",
"night",
"ever",
"little",
"said",
"end",
"some",
"than",
"live",
"fall",
"those",
"pain",
"around",
"mind",
"people",
"girl",
"leave",
"dream",
"left",
"turn",
"myself",
"right",
"tear",
"head",
"give",
"nothing",
"really",
"off",
"before",
"something",
"find",
"hold",
"man",
"walk",
"wish",
"good",
"once",
"place",
"light",
"call",
"ask",
"lie",
"stop",
"hear",
"keep",
"watch",
"seem",
"year",
"sit",
"die",
"everything",
"without",
"though",
"lost",
"these",
"wait",
"got",
"care",
"yet",
"made",
"remember",
"start",
"alone",
"which",
"last",
"run",
"hope",
"maybe",
"believe",
"body",
"hate",
"after",
"close",
"talk",
"hard",
"stand",
"old",
"own",
"each",
"well",
"hurt",
"while",
"help",
"home",
"god",
"soul",
"new",
"many",
"two",
"inside",
"should",
"true",
"move",
"first",
"fear",
"mean",
"better",
"may",
"play",
"another",
"gone",
"change",
"use",
"wonder",
"knew",
"same",
"someone",
"hair",
"cold",
"open",
"best",
"any",
"behind",
"miss",
"arm",
"happen",
"star",
"water",
"dark",
"laugh",
"stay",
"forever",
"name",
"work",
"show",
"sky",
"break",
"far",
"came",
"deep",
"door",
"put",
"room",
"black",
"together",
"upon",
"boy",
"happy",
"such",
"great",
"white",
"does",
"matter",
"side",
"fill",
"past",
"fight",
"sun",
"please",
"burn",
"cause",
"enough",
"touch",
"cannot",
"moment",
"soon",
"voice",
"scream",
"anything",
"stare",
"most",
"sound",
"red",
"everyone",
"hide",
"kiss",
"truth",
"death",
"beautiful",
"mine",
"blood",
"broken",
"very",
"pass",
"next",
"forget",
"tree",
"wrong",
"air",
"mother",
"must",
"done",
"found",
"understand",
"lip",
"hit",
"wall",
"else",
"beat",
"memory",
"saw",
"wind",
"sleep",
"free",
"high",
"realize",
"school",
"bad",
"late",
"went",
"felt",
"might",
"skin",
"sweet",
"perfect",
"blue",
"kill",
"breath",
"dance",
"rain",
"dead",
"against",
"fly",
"between",
"grow",
"strong",
"car",
"took",
"under",
"listen",
"bring",
"full",
"sometimes",
"speak",
"big",
"pull",
"person",
"become",
"family",
"part",
"begin",
"ground",
"real",
"small",
"father",
"sure",
"hell",
"kind",
"bed",
"feet",
"rest",
"young",
"finally",
"land",
"across",
"today",
"seen",
"different",
"guy",
"line",
"fire",
"reason",
"lay",
"reach",
"second",
"slowly",
"write",
"ear",
"eat",
"sing",
"smell",
"mouth",
"step",
"learn",
"three",
"gave",
"floor",
"promise",
"breathe",
"darkness",
"push",
"earth",
"guess",
"save",
"song",
"till",
"above",
"along",
"both",
"color",
"house",
"almost",
"sorry",
"anymore",
"yes",
"brother",
"okay",
"dear",
"game",
"fade",
"already",
"apart",
"warm",
"beauty",
"heard",
"notice",
"question",
"shine",
"began",
"piece",
"whole",
"shadow",
"secret",
"street",
"within",
"finger",
"point",
"morning",
"whisper",
"child",
"fun",
"moon",
"green",
"read",
"story",
"glass",
"kid",
"lose",
"silence",
"pick",
"cut",
"fast",
"since",
"soft",
"yourself",
"empty",
"shall",
"angel",
"answer",
"baby",
"bright",
"dad",
"path",
"worry",
"hour",
"drop",
"fell",
"follow",
"power",
"war",
"half",
"flow",
"heaven",
"wake",
"act",
"chance",
"fact",
"least",
"tired",
"children",
"near",
"quite",
"scare",
"afraid",
"rise",
"sea",
"taste",
"window",
"cover",
"nice",
"trust",
"lot",
"sad",
"cool",
"force",
"peace",
"return",
"wear",
"blind",
"easy",
"ready",
"roll",
"rose",
"shit",
"drive",
"held",
"music",
"share",
"beneath",
"hang",
"mom",
"paint",
"emotion",
"quiet",
"slow",
"clear",
"cloud",
"few",
"pretty",
"bird",
"outside",
"paper",
"picture",
"front",
"rock",
"simple",
"top",
"anyone",
"meant",
"reality",
"road",
"sense",
"waste",
"bit",
"leaf",
"thank",
"happiness",
"meet",
"men",
"smoke",
"truly",
"decide",
"self",
"age",
"book",
"form",
"hot",
"alive",
"carry",
"met",
"escape",
"damn",
"instead",
"shake",
"able",
"ice",
"minute",
"throw",
"catch",
"four",
"leg",
"ring",
"course",
"goodbye",
"lead",
"poem",
"sick",
"corner",
"desire",
"fine",
"known",
"problem",
"ran",
"remind",
"shoulder",
"suppose",
"toward",
"wave",
"drink",
"jump",
"woman",
"pretend",
"sister",
"week",
"human",
"joy",
"crack",
"dare",
"grey",
"pray",
"surprise",
"dry",
"knee",
"less",
"ride",
"search",
"short",
"bleed",
"caught",
"clean",
"embrace",
"future",
"king",
"son",
"sorrow",
"chest",
"hug",
"remain",
"sat",
"wing",
"worth",
"blow",
"daddy",
"final",
"parent",
"tight",
"also",
"create",
"lonely",
"safe",
"cross",
"dress",
"evil",
"silent",
"bone",
"fate",
"perhaps",
"anger",
"class",
"scar",
"sight",
"snow",
"tiny",
"tonight",
"wanna",
"continue",
"control",
"dog",
"edge",
"fool",
"mirror",
"month",
"suddenly",
"comfort",
"given",
"loud",
"quickly",
"gaze",
"plan",
"rush",
"slip",
"stone",
"town",
"ass",
"battle",
"ignore",
"spirit",
"stood",
"stupid",
"yours",
"brown",
"build",
"dust",
"food",
"hey",
"kept",
"pay",
"phone",
"twist",
"although",
"ball",
"beyond",
"drown",
"fit",
"hidden",
"nose",
"taken",
"fail",
"float",
"lock",
"pure",
"sand",
"somehow",
"wash",
"wrap",
"angry",
"cheek",
"creature",
"forgotten",
"heat",
"hole",
"rip",
"single",
"space",
"special",
"weak",
"whatever",
"yell",
"anyway",
"blame",
"job",
"choose",
"country",
"curse",
"drift",
"echo",
"figure",
"gold",
"grew",
"herself",
"laughter",
"neck",
"suffer",
"worse",
"yeah",
"bear",
"disappear",
"foot",
"forward",
"knife",
"mess",
"nor",
"race",
"somewhere",
"stomach",
"storm",
"beg",
"idea",
"lift",
"offer",
"tall",
"breeze",
"field",
"five",
"often",
"round",
"simply",
"stuck",
"thin",
"win",
"allow",
"confuse",
"enjoy",
"except",
"flower",
"seek",
"strength",
"calm",
"grin",
"gun",
"heavy",
"hill",
"himself",
"large",
"ocean",
"shoe",
"sigh",
"straight",
"summer",
"tongue",
"accept",
"crazy",
"everyday",
"exist",
"fake",
"grass",
"mistake",
"sent",
"shut",
"sin",
"surround",
"table",
"ache",
"brain",
"destroy",
"heal",
"nature",
"shout",
"sign",
"stain",
"choice",
"doubt",
"glance",
"glow",
"mountain",
"queen",
"send",
"shot",
"spent",
"stranger",
"throat",
"tomorrow",
"city",
"either",
"fish",
"flame",
"mad",
"rather",
"shape",
"spin",
"spread",
"wide",
"ash",
"distance",
"fallen",
"finish",
"image",
"imagine",
"important",
"nobody",
"shatter",
"warmth",
"became",
"bore",
"fat",
"feed",
"flesh",
"funny",
"lust",
"shirt",
"trouble",
"yellow",
"attention",
"bare",
"bite",
"cat",
"lack",
"money",
"protect",
"amaze",
"appear",
"born",
"choke",
"completely",
"daughter",
"fresh",
"friendship",
"gentle",
"probably",
"six",
"trap",
"beast",
"deserve",
"expect",
"grab",
"middle",
"nightmare",
"river",
"thousand",
"weight",
"worst",
"wound",
"barely",
"bottle",
"cream",
"lover",
"low",
"mile",
"regret",
"relationship",
"stick",
"test",
"whose",
"crush",
"endless",
"fault",
"itself",
"rage",
"rule",
"spill",
"art",
"circle",
"join",
"kick",
"mask",
"master",
"passion",
"quick",
"raise",
"smooth",
"unless",
"wander",
"actually",
"broke",
"chair",
"deal",
"favorite",
"gift",
"note",
"number",
"shed",
"suck",
"sweat",
"tale",
"box",
"chill",
"clothes",
"hall",
"lady",
"mark",
"park",
"poor",
"sadness",
"tie",
"animal",
"belong",
"brush",
"consume",
"dawn",
"forest",
"grave",
"innocent",
"pen",
"pride",
"stream",
"thick",
"clay",
"complete",
"count",
"draw",
"faith",
"press",
"silver",
"struggle",
"surface",
"taught",
"teach",
"wet",
"bless",
"chase",
"climb",
"enter",
"letter",
"melt",
"metal",
"movie",
"stretch",
"swing",
"ten",
"vision",
"wife",
"beside",
"crash",
"forgot",
"guide",
"haunt",
"joke",
"knock",
"plant",
"pour",
"prove",
"reveal",
"steal",
"stuff",
"trip",
"wood",
"wrist",
"bother",
"bottom",
"crawl",
"crowd",
"fix",
"forgive",
"frown",
"grace",
"loose",
"lucky",
"party",
"release",
"seat",
"surely",
"survive",
"teacher",
"gently",
"grip",
"speed",
"suicide",
"travel",
"treat",
"vein",
"written",
"cage",
"chain",
"conversation",
"date",
"enemy",
"fair",
"however",
"interest",
"million",
"page",
"pink",
"proud",
"sway",
"themselves",
"track",
"winter",
"church",
"cruel",
"cup",
"demon",
"experience",
"freedom",
"pair",
"pop",
"purpose",
"respect",
"shoot",
"softly",
"state",
"store",
"strange",
"toy",
"bar",
"beach",
"birth",
"curl",
"dirt",
"excuse",
"hat",
"lake",
"lord",
"lovely",
"monster",
"order",
"pack",
"pants",
"pool",
"scene",
"seven",
"shame",
"slide",
"ugly",
"whom",
"among",
"blade",
"blonde",
"closet",
"creek",
"deny",
"drug",
"eternity",
"gain",
"grade",
"handle",
"key",
"linger",
"pale",
"prepare",
"swallow",
"swim",
"torn",
"tremble",
"wheel",
"won",
"cast",
"cigarette",
"claim",
"college",
"direction",
"dirty",
"gather",
"ghost",
"hundred",
"loss",
"lung",
"orange",
"present",
"swear",
"swirl",
"twice",
"wild",
"bitter",
"blanket",
"case",
"doctor",
"everywhere",
"flash",
"grown",
"knowledge",
"numb",
"pressure",
"radio",
"repeat",
"ruin",
"spend",
"unknown",
"buy",
"clock",
"devil",
"early",
"false",
"fantasy",
"pound",
"precious",
"refuse",
"sheet",
"shell",
"spoke",
"teeth",
"welcome",
"add",
"ahead",
"block",
"bury",
"caress",
"content",
"depth",
"despite",
"distant",
"marry",
"purple",
"threw",
"thus",
"tone",
"whenever",
"bomb",
"dull",
"easily",
"grasp",
"hospital",
"innocence",
"normal",
"receive",
"reply",
"rhyme",
"shade",
"someday",
"sword",
"toe",
"visit",
"asleep",
"bell",
"bought",
"center",
"consider",
"flat",
"hero",
"history",
"ink",
"insane",
"muscle",
"mystery",
"pocket",
"reflection",
"shove",
"silently",
"smart",
"soldier",
"spot",
"stress",
"train",
"type",
"view",
"whether",
"bus",
"energy",
"explain",
"holy",
"hunger",
"inch",
"lean",
"magic",
"mix",
"noise",
"nowhere",
"prayer",
"presence",
"shock",
"snap",
"spider",
"study",
"thunder",
"trail",
"admit",
"agree",
"bag",
"bang",
"bound",
"butterfly",
"cute",
"exactly",
"explode",
"familiar",
"fold",
"further",
"lit",
"pierce",
"reflect",
"scent",
"selfish",
"sell",
"sharp",
"sink",
"spring",
"stumble",
"universe",
"weep",
"women",
"wonderful",
"action",
"ancient",
"attempt",
"avoid",
"birthday",
"branch",
"chocolate",
"core",
"depress",
"drunk",
"especially",
"focus",
"fruit",
"honest",
"match",
"palm",
"perfectly",
"pillow",
"pity",
"poison",
"roar",
"shift",
"slightly",
"thump",
"truck",
"tune",
"twenty",
"unable",
"wipe",
"wrote",
"bow",
"coat",
"constant",
"dinner",
"drove",
"egg",
"eternal",
"flight",
"flood",
"frame",
"freak",
"gasp",
"glad",
"hollow",
"motion",
"peer",
"plastic",
"root",
"screen",
"season",
"sting",
"strike",
"team",
"unlike",
"victim",
"volume",
"warn",
"weird",
"attack",
"await",
"awake",
"built",
"charm",
"crave",
"despair",
"fought",
"grant",
"grief",
"horse",
"limit",
"message",
"ripple",
"sanity",
"scatter",
"serve",
"split",
"string",
"trick",
"whore",
"annoy",
"blur",
"boat",
"brave",
"clearly",
"cling",
"connect",
"fist",
"forth",
"hip",
"imagination",
"iron",
"jock",
"judge",
"lesson",
"milk",
"misery",
"nail",
"naked",
"ourselves",
"poet",
"possible",
"princess",
"sail",
"seed",
"size",
"snake",
"society",
"stroke",
"tip",
"torture",
"toss",
"trace",
"wise",
"bloom",
"bullet",
"cell",
"check",
"cost",
"darling",
"during",
"footstep",
"fragile",
"hallway",
"hardly",
"horizon",
"invisible",
"journey",
"midnight",
"mood",
"mud",
"nod",
"pause",
"relax",
"shiver",
"sudden",
"thee",
"value",
"youth",
"abuse",
"admire",
"blink",
"breast",
"bruise",
"constantly",
"couple",
"creep",
"curve",
"difference",
"dumb",
"emptiness",
"gotta",
"honor",
"plain",
"planet",
"recall",
"rub",
"ship",
"slam",
"soar",
"somebody",
"spit",
"tightly",
"weather",
"adore",
"approach",
"bond",
"bread",
"burst",
"candle",
"cave",
"coffee",
"cousin",
"crime",
"desert",
"flutter",
"frozen",
"grand",
"heel",
"hello",
"language",
"level",
"luck",
"movement",
"pleasure",
"powerful",
"random",
"rhythm",
"settle",
"silly",
"slap",
"sort",
"spoken",
"steel",
"tail",
"threaten",
"tumble",
"upset",
"aside",
"awkward",
"bee",
"bend",
"blank",
"board",
"button",
"card",
"carefully",
"complain",
"crap",
"crown",
"deeply",
"discover",
"dive",
"drag",
"dread",
"effort",
"entire",
"fairy",
"giant",
"gotten",
"greet",
"illusion",
"jeans",
"leap",
"liquid",
"march",
"mend",
"nervous",
"nine",
"pace",
"replace",
"rope",
"spine",
"stole",
"terror",
"accident",
"apple",
"balance",
"bet",
"boom",
"childhood",
"collect",
"cook",
"demand",
"depression",
"eight",
"eventually",
"faint",
"gate",
"glare",
"goal",
"group",
"honey",
"kitchen",
"laid",
"limb",
"machine",
"mere",
"mold",
"murder",
"nerve",
"painful",
"pin",
"poetry",
"prince",
"rabbit",
"sake",
"seal",
"seep",
"shelter",
"shop",
"shore",
"shower",
"soothe",
"stair",
"steady",
"sunlight",
"tangle",
"tease",
"treasure",
"uncle",
"wine",
"begun",
"bliss",
"bush",
"canvas",
"cheer",
"claw",
"clutch",
"commit",
"crimson",
"crystal",
"cure",
"delight",
"dip",
"doll",
"ease",
"existence",
"express",
"fog",
"football",
"gay",
"goose",
"guard",
"hatred",
"illuminate",
"mass",
"math",
"mourn",
"pot",
"ray",
"rich",
"rough",
"skip",
"stir",
"student",
"style",
"support",
"thorn",
"tick",
"tough",
"wore",
"yard",
"yearn",
"yesterday",
"advice",
"appreciate",
"autumn",
"bank",
"beam",
"bowl",
"capture",
"carve",
"chose",
"collapse",
"confusion",
"creation",
"dove",
"feather",
"girlfriend",
"glory",
"government",
"harsh",
"hop",
"inner",
"loser",
"meal",
"moonlight",
"neighbor",
"neither",
"peach",
"pig",
"praise",
"screw",
"shield",
"shimmer",
"sneak",
"stab",
"subject",
"sweep",
"throughout",
"thrown",
"tower",
"twirl",
"woke",
"wow",
"army",
"arrive",
"bathroom",
"bump",
"cease",
"cookie",
"couch",
"courage",
"dim",
"guilt",
"howl",
"hum",
"husband",
"insult",
"led",
"lunch",
"mock",
"mostly",
"natural",
"nearly",
"needle",
"nerd",
"peaceful",
"perfection",
"pile",
"price",
"remove",
"roam",
"sanctuary",
"serious",
"shiny",
"shook",
"sob",
"stolen",
"tap",
"vain",
"void",
"warrior",
"wrinkle",
"affection",
"apologize",
"band",
"bind",
"blossom",
"bounce",
"bridge",
"cheap",
"crumble",
"decision",
"descend",
"desperately",
"dig",
"dot",
"flaw",
"flip",
"frighten",
"heartbeat",
"huge",
"lazy",
"lick",
"lower",
"odd",
"opinion",
"process",
"puzzle",
"quietly",
"retreat",
"rot",
"score",
"sentence",
"separate",
"situation",
"skill",
"soak",
"square",
"stray",
"taint",
"task",
"tide",
"underneath",
"veil",
"whistle",
"anywhere",
"bedroom",
"bid",
"bloody",
"boot",
"burden",
"careful",
"compare",
"concern",
"curtain",
"decay",
"defeat",
"describe",
"double",
"dreamer",
"driver",
"dwell",
"evening",
"flare",
"flicker",
"grandma",
"guitar",
"harm",
"hid",
"horrible",
"hung",
"hungry",
"indeed",
"lace",
"melody",
"monkey",
"nation",
"object",
"obviously",
"pit",
"rainbow",
"salt",
"scratch",
"shown",
"shy",
"stage",
"stun",
"third",
"tickle",
"useless",
"weakness",
"worship",
"worthless",
"afternoon",
"beard",
"boyfriend",
"bubble",
"busy",
"certain",
"chin",
"concrete",
"desk",
"diamond",
"doom",
"drawn",
"due",
"felicity",
"freeze",
"frost",
"garden",
"glide",
"harmony",
"hopefully",
"hunt",
"jealous",
"lightning",
"mama",
"mercy",
"peel",
"physical",
"position",
"pulse",
"punch",
"quit",
"rant",
"respond",
"salty",
"sane",
"satisfy",
"savior",
"sheep",
"slept",
"social",
"sore",
"sport",
"tuck",
"utter",
"valley",
"wolf",
"aid",
"aim",
"alas",
"alter",
"arrow",
"awaken",
"beaten",
"belief",
"brand",
"ceiling",
"cheese",
"clue",
"confidence",
"connection",
"daily",
"disguise",
"eager",
"erase",
"essence",
"everytime",
"expression",
"fan",
"flag",
"flirt",
"foul",
"fur",
"giggle",
"glorious",
"ignorance",
"law",
"lifeless",
"measure",
"mighty",
"muse",
"north",
"opposite",
"paradise",
"patience",
"patient",
"pencil",
"petal",
"plane",
"plate",
"ponder",
"possibly",
"practice",
"slice",
"spell",
"stock",
"strife",
"strip",
"struck",
"suffocate",
"suit",
"tender",
"tool",
"trade",
"velvet",
"verse",
"waist",
"witch",
"worn",
"aunt",
"bay",
"bench",
"bold",
"cap",
"certainly",
"click",
"companion",
"condom",
"creator",
"dart",
"delicate",
"determine",
"dish",
"dragon",
"drama",
"drum",
"dude",
"everybody",
"feast",
"forehead",
"former",
"fright",
"fully",
"gas",
"gut",
"hook",
"hurl",
"invite",
"juice",
"manage",
"moral",
"pill",
"possess",
"raw",
"rebel",
"royal",
"scale",
"scary",
"several",
"slight",
"stubborn",
"swell",
"talent",
"tea",
"terrible",
"thread",
"thy",
"torment",
"trickle",
"usually",
"vast",
"violence",
"weave",
"yea",
"acid",
"agony",
"ashamed",
"awe",
"belly",
"blend",
"blush",
"character",
"cheat",
"common",
"company",
"coward",
"creak",
"danger",
"deadly",
"defense",
"define",
"depend",
"desperate",
"destination",
"dew",
"duck",
"dusty",
"embarrass",
"engine",
"example",
"explore",
"foe",
"freely",
"frustrate",
"generation",
"glove",
"guilty",
"health",
"hurry",
"idiot",
"impossible",
"inhale",
"jaw",
"kingdom",
"mention",
"mist",
"moan",
"mumble",
"mutter",
"observe",
"ode",
"pathetic",
"pattern",
"pie",
"prefer",
"puff",
"rape",
"rare",
"revenge",
"rude",
"scrape",
"sip",
"spiral",
"squeeze",
"strain",
"sunset",
"suspend",
"sympathy",
"thigh",
"thou",
"throne",
"total",
"unseen",
"weapon",
"weary"
]



n = 1626

# Note about US patent no 5892470: Here each word does not represent a given digit.
# Instead, the digit represented by a word is variable, it depends on the previous word.

def mn_encode( message ):
    out = []
    for i in range(len(message)/8):
        word = message[8*i:8*i+8]
        x = int(word, 16)
        w1 = (x%n)
        w2 = ((x/n) + w1)%n
        w3 = ((x/n/n) + w2)%n
        out += [ words[w1], words[w2], words[w3] ]
    return out

def mn_decode( wlist ):
    out = ''
    for i in range(len(wlist)/3):
        word1, word2, word3 = wlist[3*i:3*i+3]
        w1 =  words.index(word1)
        w2 = (words.index(word2))%n
        w3 = (words.index(word3))%n
        x = w1 +n*((w2-w1)%n) +n*n*((w3-w2)%n)
        out += '%x'%x
    return out




if __name__ == '__main__':
    import sys
    print len(words)
    key = '6a8657c1f2566290be460fd51bb9f7fc'
    ss = mn_encode(key)
    print key
    print ss
    print mn_decode(ss)


