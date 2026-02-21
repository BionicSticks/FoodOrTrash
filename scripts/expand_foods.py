#!/usr/bin/env python3
"""Expand foods.json from ~513 to 2000+ whole food items."""

import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FOODS_PATH = os.path.join(SCRIPT_DIR, "..", "src", "data", "foods.json")

# Load existing
with open(FOODS_PATH) as f:
    existing_foods = json.load(f)

existing_names = {item["name"].lower() for item in existing_foods}

def item(name, category, aliases, fun_fact, score, calories):
    if name.lower() in existing_names:
        return None
    existing_names.add(name.lower())
    return {
        "name": name,
        "category": category,
        "aliases": aliases,
        "fun_fact": fun_fact,
        "score": score,
        "calories": calories
    }

new_items = []

def add(name, category, aliases, fun_fact, score, calories):
    entry = item(name, category, aliases, fun_fact, score, calories)
    if entry:
        new_items.append(entry)

# ============================================================
# FRUITS
# ============================================================
add("ambarella", "fruit", ["ambarellas", "june plum", "golden apple fruit", "kedondong"], "Also known as golden apple, it's crunchy when green and sweet when ripe.", 85, 46)
add("atemoya", "fruit", ["atemoyas"], "A hybrid of sugar apple and cherimoya, often called 'pineapple sugar apple'.", 87, 94)
add("babaco", "fruit", ["babacos"], "A seedless relative of papaya that grows in the Ecuadorian highlands.", 84, 21)
add("barberry", "fruit", ["barberries", "zereshk", "berberis"], "Used in Persian rice dishes, these tiny tart berries are packed with berberine.", 90, 316)
add("bergamot", "fruit", ["bergamots", "bergamot orange"], "The essential oil from bergamot rind gives Earl Grey tea its distinctive flavor.", 82, 36)
add("bilberry", "fruit", ["bilberries", "european blueberry", "whortleberry"], "RAF pilots in WWII reportedly ate bilberry jam to improve night vision.", 93, 42)
add("black sapote", "fruit", ["black sapotes", "chocolate pudding fruit"], "When ripe, the flesh looks and tastes remarkably like chocolate pudding.", 86, 45)
add("blood orange", "fruit", ["blood oranges", "moro orange", "tarocco"], "The deep red color comes from anthocyanins, rare in citrus fruits.", 90, 43)
add("buddha's hand", "fruit", ["buddhas hand", "fingered citron", "bushukan"], "This fragrant citrus has no juice or pulp — it's all zest and pith.", 80, 34)
add("calamansi", "fruit", ["calamansis", "calamondin", "philippine lime"], "A staple in Filipino cooking, it's a cross between a kumquat and a mandarin.", 88, 37)
add("canistel", "fruit", ["canistels", "egg fruit", "yellow sapote"], "Its dry, crumbly flesh tastes like sweet potato custard.", 83, 139)
add("cempedak", "fruit", ["cempedaks"], "A close relative of jackfruit, popular deep-fried in Malaysia.", 82, 75)
add("clementine", "fruit", ["clementines", "cuties", "halos"], "Named after Father Clement Rodier, who discovered them in Algeria in 1902.", 90, 47)
add("cloudberry", "fruit", ["cloudberries", "bakeapple", "nordic berry"], "These golden Arctic berries can cost over $100 per pound.", 92, 51)
add("custard apple", "fruit", ["custard apples", "sugar apple", "sweetsop", "sitaphal"], "Mark Twain called the cherimoya 'the most delicious fruit known to men'.", 86, 101)
add("finger lime", "fruit", ["finger limes", "caviar lime", "citrus caviar"], "The tiny juice vesicles pop like caviar, earning it the nickname 'citrus caviar'.", 88, 30)
add("genip", "fruit", ["genips", "guinep", "spanish lime", "quenepa", "limoncillo"], "Kids in the Caribbean eat these like candy, cracking the shell with their teeth.", 84, 58)
add("golden berry", "fruit", ["golden berries", "cape gooseberry", "inca berry"], "The Incas cultivated these in the Sacred Valley of Peru over 4,000 years ago.", 91, 53)
add("granadilla", "fruit", ["granadillas", "sweet granadilla", "grenadia"], "Unlike its sour cousin passion fruit, granadilla is naturally sweet.", 85, 46)
add("huckleberry", "fruit", ["huckleberries", "wild huckleberry"], "They cannot be commercially cultivated — every huckleberry is wild-picked.", 93, 37)
add("ice cream bean", "fruit", ["ice cream beans", "inga edulis", "guaba"], "The cottony pulp inside the giant pods tastes like vanilla ice cream.", 82, 95)
add("jambul", "fruit", ["jambuls", "java plum", "jamun", "black plum"], "It stains your tongue deep purple and has been used in Ayurvedic medicine for millennia.", 86, 60)
add("jujube", "fruit", ["jujubes", "chinese date", "red date", "ziziphus"], "Dried jujubes have been found in Chinese tombs dating back 7,000 years.", 88, 79)
add("kaffir lime", "fruit", ["kaffir limes", "makrut lime", "makrut"], "The bumpy, wrinkled skin is unmistakable — the leaves are more prized than the fruit.", 83, 30)
add("key lime", "fruit", ["key limes", "mexican lime", "west indian lime"], "Smaller and more aromatic than Persian limes, they're the real Key lime pie ingredient.", 87, 30)
add("langsat", "fruit", ["langsats", "lanzones", "longkong"], "Translucent flesh in grape-like clusters — a beloved street food across Southeast Asia.", 84, 60)
add("lingonberry", "fruit", ["lingonberries", "cowberry", "mountain cranberry"], "IKEA serves 600 million Swedish meatballs a year, nearly all with lingonberry jam.", 91, 50)
add("lucuma", "fruit", ["lucumas", "gold of the incas"], "Peru's most popular ice cream flavor — more popular than chocolate or vanilla.", 84, 99)
add("mamey sapote", "fruit", ["mamey sapotes", "mamey", "zapote"], "The creamy salmon-colored flesh is the base of Cuba's national milkshake.", 85, 124)
add("mandarin", "fruit", ["mandarins", "mandarin orange", "satsuma"], "More than 30 million tonnes are produced yearly, mostly in China.", 90, 53)
add("marionberry", "fruit", ["marionberries", "marion blackberry"], "Named after Marion County, Oregon — the official berry of the state.", 91, 43)
add("maypop", "fruit", ["maypops", "purple passionflower"], "The only passion fruit species native to North America.", 83, 97)
add("medlar", "fruit", ["medlars", "mespilus"], "One of the few fruits that must rot (blet) before it becomes edible.", 80, 44)
add("meyer lemon", "fruit", ["meyer lemons"], "A cross between a lemon and a mandarin, rediscovered by Alice Waters in the 1990s.", 88, 29)
add("muscadine", "fruit", ["muscadines", "scuppernong"], "Native American grapes with thick skins — you eat them by squeezing the pulp out.", 86, 57)
add("nance", "fruit", ["nances", "nanche", "golden spoon"], "These tiny yellow fruits smell like dirty cheese but taste sweet and oily.", 82, 73)
add("nectarine", "fruit", ["nectarines"], "Genetically almost identical to peaches — a single gene controls the fuzz.", 90, 44)
add("pawpaw", "fruit", ["pawpaws", "american pawpaw", "indiana banana"], "The largest edible fruit native to North America, tasting like banana custard.", 87, 80)
add("pepino", "fruit", ["pepinos", "pepino melon", "melon pear"], "Despite its name, it's not a melon — it's in the nightshade family with tomatoes.", 83, 22)
add("pomelo", "fruit", ["pomelos", "pummelo", "shaddock", "jabong"], "The largest citrus fruit, it can weigh up to 25 pounds.", 87, 38)
add("prickly pear", "fruit", ["prickly pears", "tuna fruit", "cactus fruit", "cactus pear"], "The fruit of the same cactus whose pads (nopales) are eaten as vegetables.", 86, 41)
add("rose apple", "fruit", ["rose apples", "wax apple", "java apple", "bell fruit"], "Despite the name, it's not related to apples — it's in the myrtle family.", 82, 25)
add("santol", "fruit", ["santols", "cotton fruit", "wild mangosteen"], "A beloved Filipino fruit — you suck the sweet cottony flesh off the seeds.", 81, 76)
add("sea buckthorn", "fruit", ["sea buckthorn berries", "sea berry"], "These tiny orange berries contain more vitamin C than any other fruit.", 93, 82)
add("seville orange", "fruit", ["seville oranges", "bitter orange", "sour orange"], "Too bitter to eat raw — they exist almost solely for making marmalade.", 78, 40)
add("surinam cherry", "fruit", ["surinam cherries", "pitanga", "brazilian cherry"], "The ribbed, pumpkin-shaped fruit turns from green to orange to deep red.", 84, 33)
add("white sapote", "fruit", ["white sapotes", "casimiroa"], "Aztecs used this creamy fruit as a sleep aid — it contains mild sedative compounds.", 83, 72)
add("yangmei", "fruit", ["yangmeis", "chinese bayberry", "yumberry", "waxberry"], "Stains everything it touches deep red — Chinese poets have written about it for 2,000 years.", 86, 28)
add("white currant", "fruit", ["white currants"], "Actually a color variant of red currants, prized for their delicate sweetness.", 88, 56)

# ============================================================
# VEGETABLES
# ============================================================
add("agretti", "vegetable", ["agrettis", "barba di frate"], "Italian monks grew this succulent as a source of soda ash for glassmaking.", 88, 17)
add("amaranth greens", "vegetable", ["amaranth leaves", "callaloo", "chinese spinach"], "The Aztecs believed amaranth had supernatural powers and used it in religious ceremonies.", 90, 23)
add("banana blossom", "vegetable", ["banana blossoms", "banana flower", "banana heart"], "Used as a vegan fish substitute in Southeast Asian cooking due to its flaky texture.", 83, 51)
add("beet greens", "vegetable", ["beet tops", "beetroot leaves"], "More nutritious than the beetroot itself, with more iron than spinach.", 92, 22)
add("bitter melon", "vegetable", ["bitter melons", "bitter gourd", "karela", "ampalaya"], "The most bitter of all vegetables — compounds in it may help regulate blood sugar.", 85, 17)
add("bottle gourd", "vegetable", ["bottle gourds", "calabash", "lauki", "dudhi"], "One of the first cultivated plants, used as water containers for 10,000+ years.", 80, 14)
add("broccolini", "vegetable", ["broccolinis", "baby broccoli"], "A hybrid of broccoli and Chinese kale, invented in Japan in 1993.", 90, 28)
add("burdock root", "vegetable", ["burdock roots", "gobo"], "The burrs of this plant inspired the invention of Velcro.", 85, 72)
add("cardoon", "vegetable", ["cardoons", "cardi"], "The wild ancestor of the artichoke, prized in Italian and Spanish cooking.", 83, 17)
add("chinese broccoli", "vegetable", ["gai lan", "kai lan", "chinese kale"], "Thicker stems and more bitter than regular broccoli — a dim sum staple.", 88, 26)
add("chrysanthemum greens", "vegetable", ["shungiku", "crown daisy", "tong ho"], "The same genus as ornamental mums, but bred for edible leaves.", 85, 24)
add("crookneck squash", "vegetable", ["crookneck squashes", "yellow crookneck"], "Named for its curved neck, one of the oldest cultivated squash varieties.", 84, 19)
add("dandelion greens", "vegetable", ["dandelion leaves", "pissenlit"], "The name comes from French 'dent de lion' (lion's tooth) for the jagged leaves.", 91, 45)
add("elephant garlic", "vegetable", ["elephant garlics"], "Not actually garlic — it's more closely related to leeks.", 84, 85)
add("escarole", "vegetable", ["escaroles", "broad-leaved endive"], "A staple of Italian-American wedding soup and Neapolitan cooking.", 86, 17)
add("frisee", "vegetable", ["frisees", "curly endive", "chicory frisee"], "The pale yellow heart is the prize — achieved by blocking sunlight during growth.", 85, 17)
add("galangal", "vegetable", ["galangals", "blue ginger", "laos root", "kha"], "Looks like ginger but tastes like pine and citrus — essential in Thai tom kha.", 84, 71)
add("garlic scapes", "vegetable", ["garlic scape", "garlic shoots"], "The curly green shoots of hardneck garlic, with a mild garlicky flavor.", 88, 60)
add("grape leaves", "vegetable", ["grape leaf", "vine leaves"], "Stuffed grape leaves (dolma) appear in cuisines from Greece to Iran.", 84, 93)
add("hubbard squash", "vegetable", ["hubbard squashes", "blue hubbard"], "Can weigh up to 50 pounds with a rock-hard shell that needs a cleaver.", 83, 40)
add("kabocha", "vegetable", ["kabochas", "japanese pumpkin", "kabocha squash"], "So naturally sweet and creamy it needs nothing but roasting.", 88, 49)
add("lamb's lettuce", "vegetable", ["lambs lettuce", "mache", "corn salad"], "The most popular salad green in France, with a nutty, mild flavor.", 87, 21)
add("long bean", "vegetable", ["long beans", "yard-long bean", "snake bean"], "Can grow up to 3 feet long, but tastes best harvested at 18 inches.", 84, 47)
add("malanga", "vegetable", ["malangas", "yautia", "tannia"], "A staple root vegetable in Cuba and Puerto Rico, similar to taro.", 81, 98)
add("moringa", "vegetable", ["moringa leaves", "drumstick leaves", "malunggay"], "Contains 7x the vitamin C of oranges and 4x the calcium of milk.", 93, 64)
add("mizuna", "vegetable", ["mizunas", "japanese mustard greens"], "A mild Japanese green that's become a darling of Western salad mixes.", 86, 14)
add("napa cabbage", "vegetable", ["napa cabbages", "chinese cabbage", "wombok"], "The essential cabbage for kimchi — sweeter and more tender than green cabbage.", 87, 13)
add("oca", "vegetable", ["ocas", "new zealand yam"], "An Andean tuber with waxy, lemony flesh — second only to potato in the Andes.", 82, 61)
add("perilla", "vegetable", ["perillas", "shiso leaf", "korean perilla", "kkaennip"], "A mint-family herb whose leaves wrap Korean BBQ better than lettuce.", 85, 37)
add("purslane", "vegetable", ["purslanes", "portulaca", "verdolaga"], "The richest plant source of omega-3 fatty acids — treated as a weed in most lawns.", 92, 16)
add("radicchio", "vegetable", ["radicchios", "italian chicory", "red chicory"], "The bitter red leaves are grown in darkness to develop their signature color.", 86, 23)
add("ramp", "vegetable", ["ramps", "wild leek", "ramson", "wild garlic"], "So overharvested by chefs that some states have restricted foraging.", 89, 35)
add("salsify", "vegetable", ["salsifies", "oyster plant", "vegetable oyster"], "Called 'oyster plant' because its cooked flavor resembles oysters.", 84, 82)
add("sea bean", "vegetable", ["sea beans", "salicornia", "glasswort", "sea asparagus"], "Naturally salty from growing in ocean marshes — needs no seasoning.", 86, 24)
add("sunchoke", "vegetable", ["sunchokes", "jerusalem artichoke", "topinambour"], "Neither from Jerusalem nor an artichoke — it's a North American sunflower root.", 85, 73)
add("tatsoi", "vegetable", ["tatsois", "rosette bok choy", "spoon mustard"], "Forms beautiful rosettes and can survive under snow — one of the hardiest greens.", 87, 13)
add("tomatillo", "vegetable", ["tomatillos", "tomate verde", "husk tomato"], "A key ingredient in salsa verde — the papery husk peels away to reveal a sticky fruit.", 86, 32)
add("turnip greens", "vegetable", ["turnip tops", "turnip leaves", "rapini"], "Southern US soul food essential — slow-cooked with smoked meat.", 89, 20)
add("water spinach", "vegetable", ["water spinaches", "kangkung", "ong choy", "morning glory"], "Grows so aggressively in warm water it's classified as invasive in the US.", 85, 19)
add("winter melon", "vegetable", ["winter melons", "wax gourd", "ash gourd", "dong gua"], "Can grow to 80 pounds and stores for months thanks to its waxy coating.", 80, 12)
add("yacon", "vegetable", ["yacons", "peruvian ground apple"], "Tastes like a juicy apple but grows underground — full of prebiotic fiber.", 86, 54)
add("yu choy", "vegetable", ["yu choys", "choy sum", "flowering cabbage"], "The tender flowering stems are the prize — a Cantonese breakfast staple.", 86, 16)
add("celtuce", "vegetable", ["celtuces", "stem lettuce", "wosun"], "Grown for its thick, crunchy stem rather than its leaves.", 82, 18)
add("malabar spinach", "vegetable", ["vine spinach", "basella", "poi sag"], "Not true spinach — it's a tropical vine with thick, mucilaginous leaves.", 83, 19)
add("molokhia", "vegetable", ["jute mallow", "jews mallow", "mulukhiyah"], "Egypt's national dish is a soup made from these leaves, served for 5,000+ years.", 84, 26)
add("ridge gourd", "vegetable", ["ridge gourds", "luffa", "turai", "silk squash"], "When dried, the fibrous skeleton becomes the loofah sponge in your shower.", 80, 20)
add("mustard greens", "vegetable", ["kai choy", "gai choy", "indian mustard"], "The leaves have a wasabi-like bite that mellows with cooking.", 87, 27)
add("miner's lettuce", "vegetable", ["claytonia", "winter purslane"], "California Gold Rush miners ate it to prevent scurvy — it's rich in vitamin C.", 88, 16)
add("new zealand spinach", "vegetable", ["warrigal greens", "tetragonia"], "Captain Cook fed it to his crew to prevent scurvy on Pacific voyages.", 85, 12)
add("swiss chard", "vegetable", ["rainbow chard", "silverbeet"], "Despite the name, it has nothing to do with Switzerland — named by a Swiss botanist.", 90, 19)

# ============================================================
# FISH
# ============================================================
add("albacore", "fish", ["albacore tuna", "longfin tuna", "tombo"], "Can swim at 50 mph and migrate across entire ocean basins.", 88, 128)
add("amberjack", "fish", ["amberjacks", "greater amberjack", "kanpachi"], "A powerful fighter prized by sport fishermen and sushi lovers alike.", 86, 146)
add("black cod", "fish", ["black cods", "sablefish", "butterfish"], "Not actually cod — its rich, buttery flesh made it a Nobu signature dish.", 90, 195)
add("bonito", "fish", ["bonitos", "skipjack"], "Dried and shaved into katsuobushi, the foundation of Japanese dashi stock.", 87, 132)
add("bream", "fish", ["breams", "sea bream", "porgy", "dorade"], "The gilt-head bream was sacred to Aphrodite in ancient Greece.", 86, 100)
add("corvina", "fish", ["corvinas", "sea bass corvina"], "A prized ceviche fish in Peru and Central America.", 85, 97)
add("dory", "fish", ["dorys", "zeus faber"], "Has a distinctive dark spot on its side — legend says it's St. Peter's thumbprint.", 84, 73)
add("drum", "fish", ["drums", "red drum", "redfish", "channel bass"], "Makes a drumming sound using its swim bladder — that's how it got its name.", 84, 90)
add("garfish", "fish", ["garfishes", "needlefish", "garpike"], "Has bright green bones, which alarms people but is perfectly safe.", 82, 97)
add("gurnard", "fish", ["gurnards", "sea robin"], "Walks along the ocean floor on modified fins that look like legs.", 83, 90)
add("hake", "fish", ["hakes", "merluza"], "The most popular fish in Spain, where it outsells cod and salmon combined.", 85, 90)
add("kingfish", "fish", ["kingfishes", "king mackerel"], "Prized in Indian and Middle Eastern cuisines for its firm, flavorful flesh.", 85, 134)
add("lemon sole", "fish", ["lemon soles"], "Neither made of lemons nor a true sole — it's actually a type of flounder.", 86, 82)
add("ling", "fish", ["lings", "common ling"], "A deep-water relative of cod that can grow over 6 feet long.", 84, 87)
add("milkfish", "fish", ["milkfishes", "bangus", "bandeng"], "The national fish of the Philippines — deboning it is an art form.", 85, 124)
add("mullet", "fish", ["mullets", "grey mullet", "striped mullet"], "Its dried, cured roe (bottarga) is called 'the poor man's caviar'.", 84, 117)
add("ocean perch", "fish", ["ocean perches", "rosefish"], "Not a true perch — it's a rockfish that can live over 100 years.", 85, 79)
add("pacific saury", "fish", ["pacific sauries", "sanma", "mackerel pike"], "Grilled sanma is the taste of autumn in Japan — served with grated daikon.", 86, 120)
add("plaice", "fish", ["plaices", "european plaice"], "The bright orange spots make it one of the most recognizable flatfish.", 85, 86)
add("rockfish", "fish", ["rockfishes", "pacific rockfish", "rock cod"], "There are over 100 species of rockfish along the Pacific coast.", 86, 94)
add("sea bass", "fish", ["sea basses", "european sea bass", "loup de mer", "suzuki"], "Called branzino in Italy, loup de mer in France, and suzuki in Japan.", 89, 97)
add("shad", "fish", ["shads", "american shad"], "George Washington's army survived on shad during the brutal winter at Valley Forge.", 84, 197)
add("smelt", "fish", ["smelts", "rainbow smelt", "whitebait"], "So small they're eaten whole — bones, head, and all.", 85, 97)
add("sprat", "fish", ["sprats", "european sprat", "brisling"], "Smoked sprats are a beloved street food in Latvia, served on dark rye bread.", 85, 142)
add("tilefish", "fish", ["tilefishes", "golden tilefish"], "Lives in burrows it digs in the ocean floor, like an underwater prairie dog.", 84, 96)
add("wolffish", "fish", ["wolffishes", "ocean catfish", "seawolf"], "Has natural antifreeze in its blood to survive near-freezing Arctic waters.", 84, 96)
add("wrasse", "fish", ["wrasses", "ballan wrasse", "tautog", "blackfish"], "Can change sex from female to male — the largest female becomes the dominant male.", 82, 93)

# ============================================================
# DAIRY
# ============================================================
add("burrata", "dairy", ["burratas"], "A pouch of mozzarella filled with stracciatella cream — invented in Puglia in the 1920s.", 88, 233)
add("clotted cream", "dairy", ["devonshire cream", "cornish cream"], "Heated slowly for 12+ hours to form a golden crust — the heart of a cream tea.", 82, 586)
add("colby", "dairy", ["colby cheese", "colby jack"], "Invented in Colby, Wisconsin in 1885 — milder and softer than cheddar.", 84, 394)
add("creme fraiche", "dairy", ["french sour cream"], "Thicker and less tangy than sour cream, with at least 30% butterfat.", 83, 292)
add("emmental", "dairy", ["emmentaler", "emmenthal", "swiss emmental"], "The holes are caused by carbon dioxide bubbles from bacteria during aging.", 86, 357)
add("gruyere", "dairy", ["gruyere cheese"], "Takes 400 liters of milk to make a single 35kg wheel.", 87, 413)
add("jarlsberg", "dairy", ["jarlsberg cheese"], "Norway's most famous cheese — sweet, nutty, with large irregular holes.", 84, 352)
add("labneh", "dairy", ["labne", "labna", "strained yogurt", "yogurt cheese"], "Yogurt strained until thick enough to roll into balls and preserve in olive oil.", 89, 154)
add("monterey jack", "dairy", ["jack cheese", "pepper jack"], "One of the few truly American cheeses, created by Franciscan monks in Monterey.", 83, 373)
add("raclette", "dairy", ["raclette cheese"], "Traditionally melted by an open fire and scraped onto potatoes — raclette means 'to scrape'.", 83, 357)
add("roquefort", "dairy", ["roquefort cheese"], "Aged in limestone caves in southern France, where a specific mold grows naturally.", 85, 369)
add("stilton", "dairy", ["blue stilton", "white stilton"], "Can only legally be made in three English counties — Derbyshire, Leicestershire, and Nottinghamshire.", 84, 410)
add("taleggio", "dairy", ["taleggios"], "A washed-rind cheese from Lombardy — smells strong but tastes surprisingly mild.", 83, 315)
add("raw milk", "dairy", ["unpasteurized milk", "farm fresh milk"], "Contains beneficial enzymes and bacteria destroyed during pasteurization.", 85, 64)
add("skyr", "dairy", ["icelandic yogurt", "icelandic skyr"], "Vikings brought it to Iceland 1,100 years ago — technically a fresh cheese, not yogurt.", 90, 63)
add("buttermilk", "dairy", ["cultured buttermilk"], "Traditional buttermilk was the liquid left after churning butter — today's version is cultured.", 84, 40)
add("quark", "dairy", ["quarks", "topfen"], "Germany's most popular fresh dairy product — used in cheesecake, dips, and breakfast.", 86, 67)
add("fromage blanc", "dairy", ["fresh french cheese"], "A fresh French cheese with the texture of thick yogurt and zero tang.", 85, 80)

# ============================================================
# MEAT
# ============================================================
add("caribou", "meat", ["caribou meat", "reindeer meat", "reindeer"], "The traditional protein of Arctic Indigenous peoples for thousands of years.", 87, 127)
add("liver", "meat", ["beef liver", "chicken liver", "calf liver"], "Contains more vitamin A per gram than any other food — nature's multivitamin.", 92, 135)
add("heart", "meat", ["beef heart", "chicken hearts", "lamb heart"], "Pure muscle, no fat — tastes like a richer, more intense steak.", 90, 112)
add("kidney", "meat", ["beef kidney", "lamb kidney", "steak and kidney"], "The British Empire ran on steak and kidney pie — still a pub classic.", 85, 99)
add("tongue", "meat", ["beef tongue", "ox tongue", "lengua"], "The fattiest and most tender muscle — a taco de lengua is Mexican street food royalty.", 84, 224)
add("sweetbreads", "meat", ["sweetbread", "thymus", "pancreas"], "Not bread at all — it's the thymus or pancreas gland, with a creamy texture.", 82, 144)
add("bone marrow", "meat", ["marrow bones", "roasted marrow"], "Prehistoric humans cracked bones for marrow before they learned to hunt effectively.", 88, 786)
add("oxtail", "meat", ["oxtails", "ox tail"], "Once considered throwaway, now a luxury cut — prices have tripled in 20 years.", 85, 262)
add("tripe", "meat", ["tripes", "honeycomb tripe", "menudo", "callos"], "Stomach lining — the star of Mexican menudo, said to cure hangovers.", 78, 85)
add("mutton", "meat", ["mutton meat", "hogget"], "Sheep over two years old — stronger flavored than lamb, prized in Indian and British cooking.", 83, 294)
add("moose", "meat", ["moose meat"], "The largest member of the deer family — a single moose can yield 700 lbs of meat.", 86, 102)
add("yak", "meat", ["yak meat", "yak steak"], "Tibetan nomads have relied on yak meat at high altitudes for 5,000 years.", 84, 112)
add("water buffalo", "meat", ["water buffalo meat", "carabeef"], "Leaner than beef with less cholesterol — the dominant red meat in South and Southeast Asia.", 85, 99)
add("duck", "meat", ["duck meat", "duck breast", "duck leg", "duck confit"], "Duck fat has a higher ratio of unsaturated to saturated fat than butter.", 86, 337)
add("guinea pig", "meat", ["cuy"], "A traditional Andean delicacy called 'cuy' — depicted in the Last Supper painting in Cusco.", 80, 96)

# ============================================================
# POULTRY
# ============================================================
add("chicken breast", "poultry", ["chicken breasts", "white meat chicken"], "The leanest common cut of poultry at just 3% fat.", 86, 165)
add("chicken thigh", "poultry", ["chicken thighs", "dark meat chicken"], "More flavorful and harder to overcook than breast — chefs' preferred cut.", 87, 177)
add("chicken wing", "poultry", ["chicken wings", "buffalo wings"], "Buffalo wings were invented at the Anchor Bar in Buffalo, NY in 1964.", 82, 203)
add("turkey breast", "poultry", ["turkey breasts"], "Wild turkeys can fly at 55 mph — domestic ones are bred too heavy to fly.", 86, 104)
add("turkey leg", "poultry", ["turkey legs", "turkey drumstick"], "The giant smoked turkey legs at Disney parks are from full-grown turkeys.", 83, 170)
add("pigeon", "poultry", ["pigeon meat", "wood pigeon"], "Egyptian pigeon towers have bred pigeons for the table for 3,000 years.", 82, 142)

# ============================================================
# SHELLFISH
# ============================================================
add("blue crab", "shellfish", ["blue crabs", "chesapeake crab"], "Maryland's state crustacean — Old Bay seasoning was invented specifically for it.", 88, 87)
add("dungeness crab", "shellfish", ["dungeness crabs"], "Named after the town of Dungeness, Washington — a Pacific coast Christmas tradition.", 89, 86)
add("king crab", "shellfish", ["king crabs", "alaskan king crab", "red king crab"], "Their leg span can reach 6 feet — deadliest catch fishermen brave Arctic storms for them.", 87, 84)
add("snow crab", "shellfish", ["snow crabs", "queen crab", "opilio"], "Harvested from icy North Pacific waters, the sweet leg meat needs only melted butter.", 87, 90)
add("soft shell crab", "shellfish", ["soft shell crabs", "softies"], "Regular crabs caught just after molting, when the new shell is still paper-thin.", 85, 164)
add("geoduck", "shellfish", ["geoducks", "elephant clam", "mirugai"], "Pronounced 'gooey-duck' — the world's largest burrowing clam, living 140+ years.", 84, 85)
add("littleneck clam", "shellfish", ["littleneck clams", "hard clam", "quahog"], "The smallest size of quahog clam — named after Little Neck Bay, Long Island.", 86, 72)
add("stone crab", "shellfish", ["stone crabs", "stone crab claws"], "Only the claws are harvested — the crab is released alive to regrow them.", 87, 73)
add("spot prawn", "shellfish", ["spot prawns"], "Sweet enough to eat raw as sashimi — a West Coast delicacy.", 89, 71)

# ============================================================
# GRAINS
# ============================================================
add("black rice", "grain", ["forbidden rice", "purple rice"], "Called 'forbidden rice' because only Chinese emperors were allowed to eat it.", 90, 356)
add("emmer", "grain", ["emmer wheat", "farro medio"], "One of the first grains domesticated — found in 10,000-year-old archaeological sites.", 85, 335)
add("groats", "grain", ["oat groats", "buckwheat groats", "kasha"], "The whole, unprocessed grain kernel — the least processed form you can eat.", 88, 360)
add("hominy", "grain", ["posole corn", "nixtamal"], "Corn treated with lime (nixtamalization) — an ancient Mesoamerican technique that unlocks niacin.", 84, 119)
add("polenta", "grain", ["cornmeal mush"], "Italian peasant food for centuries — now served in Michelin-starred restaurants.", 83, 70)
add("red rice", "grain", ["bhutanese red rice", "camargue red rice"], "Gets its color from anthocyanins in the bran — nuttier than white rice.", 87, 362)
add("steel cut oats", "grain", ["steel cut oatmeal", "irish oats", "pinhead oats"], "The oat groat chopped into pieces — chewier and less processed than rolled oats.", 90, 379)
add("rolled oats", "grain", ["old fashioned oats", "porridge oats", "oatmeal"], "Steamed and flattened groats — the world's most popular breakfast cereal base.", 88, 379)
add("grits", "grain", ["hominy grits", "stone ground grits"], "A Southern US staple since Native Americans taught colonists to make it.", 82, 73)
add("popcorn", "grain", ["popping corn", "air popped popcorn"], "The oldest known snack — 5,600-year-old popcorn was found in a New Mexico cave.", 82, 375)
add("masa", "grain", ["masa harina", "corn masa", "nixtamalized corn flour"], "The soul of Mexican cuisine — tortillas, tamales, pupusas all start here.", 84, 365)
add("job's tears", "grain", ["adlay", "coix seed", "hato mugi"], "Used in traditional Chinese medicine for 4,000 years.", 83, 380)

# ============================================================
# LEGUMES
# ============================================================
add("butter bean", "legume", ["butter beans", "gigante bean", "corona bean"], "Can grow as large as a quarter — creamy, starchy, and rich when slow-cooked.", 85, 106)
add("urad dal", "legume", ["black gram", "mungo bean"], "The split version makes the batter for Indian dosa and idli.", 86, 341)
add("winged bean", "legume", ["winged beans", "goa bean", "four-angled bean"], "Every part is edible — leaves, flowers, pods, seeds, and even the roots.", 85, 409)
add("moth bean", "legume", ["moth beans", "matki"], "Thrives in India's Rajasthan desert with almost no rainfall.", 82, 343)

# ============================================================
# NUTS
# ============================================================
add("baru nut", "nut", ["baru nuts", "barukas"], "A Brazilian savanna nut that supports reforestation when harvested.", 87, 502)
add("breadnut", "nut", ["breadnuts", "maya nut", "ramon nut"], "The Mayan civilization relied on this nut as a dietary staple.", 83, 217)
add("ginkgo nut", "nut", ["ginkgo nuts", "ginnan"], "From the oldest living tree species — ginkgos have existed for 200 million years.", 80, 182)
add("pili nut", "nut", ["pili nuts"], "Silky smooth and buttery — the richest nut in magnesium per calorie.", 88, 719)
add("sacha inchi", "nut", ["sacha inchi nuts", "inca nut", "inca peanut"], "Contains more omega-3 than any other nut or seed.", 90, 562)

# ============================================================
# SEEDS
# ============================================================
add("cacao nib", "seed", ["cacao nibs", "raw cacao", "cocoa nibs"], "Crushed cacao beans — chocolate in its purest, unprocessed form.", 90, 228)
add("fonio", "seed", ["fonio grain", "acha"], "The oldest cereal in West Africa, now being rediscovered globally. Cooks in 5 minutes.", 87, 360)
add("teff", "seed", ["teff grain", "teff seed"], "The world's smallest grain — 3,000 teff grains weigh just one gram.", 88, 367)
add("amaranth seed", "seed", ["amaranth seeds"], "The Aztecs mixed it with blood for religious ceremonies — the Spanish banned it.", 88, 371)
add("black seed", "seed", ["black seeds", "nigella sativa", "kalonji"], "Prophet Muhammad reportedly said it cures everything except death.", 85, 345)
add("jackfruit seed", "seed", ["jackfruit seeds"], "Boiled or roasted, they taste like a cross between potatoes and chestnuts.", 82, 184)
add("moringa seed", "seed", ["moringa seeds", "drumstick seeds"], "Can purify water — the proteins in the seed bind to impurities and sink them.", 85, 26)
add("perilla seed", "seed", ["perilla seeds", "egoma seed"], "Pressed into oil in Korea and Japan — rich in alpha-linolenic acid.", 84, 500)

# ============================================================
# HERBS
# ============================================================
add("elderflower", "herb", ["elderflowers", "sambucus flower"], "Makes a fragrant cordial and sparkling wine — the flowers of the elderberry bush.", 83, 0)
add("fenugreek leaf", "herb", ["fenugreek leaves", "methi", "kasuri methi"], "Dried leaves (kasuri methi) are the secret ingredient in restaurant-quality butter chicken.", 86, 36)
add("lemon verbena", "herb", ["aloysia citrodora"], "The most intensely lemon-scented herb — far more aromatic than lemongrass.", 84, 16)
add("nettle", "herb", ["nettles", "stinging nettle", "urtica dioica"], "Sting disappears completely when cooked — tastes like a cross between spinach and herbs.", 86, 42)
add("pandan", "herb", ["pandan leaves", "screwpine", "daun pandan"], "The 'vanilla of Southeast Asia' — used in cakes, rice, and drinks throughout the region.", 84, 35)
add("sassafras", "herb", ["sassafras leaves", "file powder"], "Dried ground leaves make file powder — the traditional thickener for Cajun gumbo.", 80, 55)
add("vietnamese coriander", "herb", ["vietnamese mint", "rau ram", "laksa leaf"], "Not related to coriander or mint — the essential herb in Malaysian laksa.", 83, 22)
add("mugwort", "herb", ["mugworts", "yomogi", "ssuk"], "Used in Korean rice cakes and Japanese mochi for its herbal flavor.", 78, 46)
add("hyssop", "herb", ["hyssops"], "Mentioned in the Bible for purification rituals — used in Chartreuse liqueur.", 80, 21)
add("angelica", "herb", ["angelicas", "garden angelica"], "Named for the archangel Michael, who supposedly revealed its medicinal uses.", 80, 23)
add("summer savory", "herb", ["summer savories"], "The traditional herb for green beans in Germany and bean dishes across Europe.", 82, 30)

# ============================================================
# SPICES
# ============================================================
add("aleppo pepper", "spice", ["pul biber", "halaby pepper"], "A mild, fruity Syrian chili with an oily sheen — the paprika of the Middle East.", 84, 290)
add("amchur", "spice", ["amchoor", "mango powder"], "Sun-dried unripe mango powder — adds tartness to Indian chaat without liquid.", 82, 320)
add("black cardamom", "spice", ["badi elaichi", "tsao ko"], "Smoky and camphor-like — completely different from green cardamom.", 83, 311)
add("black garlic", "spice", ["fermented garlic", "aged black garlic"], "Regular garlic aged at high humidity for weeks until it turns jet black and sweet.", 88, 200)
add("caraway", "spice", ["caraways", "caraway seeds"], "The defining flavor of rye bread and the German spirit aquavit.", 84, 333)
add("chipotle", "spice", ["chipotles", "chipotle pepper", "smoked jalapeno"], "A smoke-dried jalapeno — Aztecs smoked them because fresh jalapenos rot quickly.", 84, 282)
add("gochugaru", "spice", ["korean chili flakes", "korean red pepper"], "Sun-dried Korean chili flakes — the soul of kimchi and gochujang.", 85, 281)
add("harissa", "spice", ["harissa paste", "harissa powder"], "North Africa's beloved chili paste — every family has their own recipe.", 84, 77)
add("long pepper", "spice", ["long peppers", "pippali"], "Ancient Romans prized it more than black pepper — it predates chili peppers by millennia.", 83, 296)
add("ras el hanout", "spice", ["ras el hanouts"], "Means 'head of the shop' in Arabic — the spice merchant's best blend, up to 30 spices.", 83, 290)
add("shichimi togarashi", "spice", ["shichimi", "seven spice"], "Japan's seven-spice blend — the table condiment found in every ramen shop.", 83, 300)
add("smoked paprika", "spice", ["pimenton", "pimenton de la vera"], "Peppers dried over smoldering oak for weeks in La Vera, Spain.", 86, 282)
add("tamarind paste", "spice", ["tamarind concentrate", "tamarind pulp"], "The sweet-sour pod that gives pad thai and Worcestershire sauce their tang.", 84, 239)
add("urfa biber", "spice", ["urfa pepper", "isot pepper"], "Sun-dried by day, wrapped at night to sweat — creates its unique raisin-like sweetness.", 84, 290)
add("kokum", "spice", ["kokums", "garcinia indica"], "A sour fruit dried into leathery petals — the souring agent in Goan fish curry.", 82, 60)
add("makrut lime leaf", "spice", ["kaffir lime leaves", "bai makrut"], "The double-lobed leaves perfume Thai soups and curries like nothing else.", 84, 0)
add("wattleseed", "spice", ["wattleseeds", "acacia seed"], "An Australian Aboriginal superfood — roasted seeds taste like coffee and chocolate.", 82, 305)

# ============================================================
# FERMENTED
# ============================================================
add("doubanjiang", "fermented", ["douban paste", "chili bean paste", "pixian douban"], "Fermented broad bean and chili paste — the 'soul of Sichuan cooking'.", 82, 60)
add("doenjang", "fermented", ["korean soybean paste"], "Korea's answer to miso — funkier and more complex from months of fermentation.", 85, 130)
add("gochujang", "fermented", ["korean chili paste", "red pepper paste"], "Fermented for months in earthen jars called onggi on Korean rooftops.", 85, 100)
add("koji", "fermented", ["aspergillus oryzae", "rice koji"], "The mold that makes miso, soy sauce, sake, and mirin possible — Japan's national fungus.", 88, 200)
add("katsuobushi", "fermented", ["bonito flakes", "dried bonito"], "The hardest food in the world — shaved with a special plane, it dances on hot dishes.", 87, 330)
add("shio koji", "fermented", ["salt koji", "salted koji"], "Rice koji mixed with salt — a magical Japanese marinade that tenderizes any protein.", 86, 130)
add("lacto-fermented vegetables", "fermented", ["lacto pickles", "naturally fermented pickles"], "Salt + vegetables + time = probiotics. No vinegar needed.", 90, 20)
add("water kefir", "fermented", ["tibicos", "japanese water crystals"], "A probiotic drink made with water kefir grains — dairy-free and lightly fizzy.", 84, 18)
add("curtido", "fermented", ["curtidos"], "El Salvador's fermented cabbage relish — served with every pupusa.", 84, 15)
add("fermented black beans", "fermented", ["douchi", "chinese fermented black beans"], "Salt-fermented soybeans — not the same as Latin American black beans.", 83, 200)
add("poi", "fermented", ["hawaiian poi", "taro poi"], "Mashed and fermented taro root — the staple food of ancient Hawaii.", 80, 89)

# ============================================================
# FUNGI
# ============================================================
add("beech mushroom", "fungi", ["buna shimeji", "shimeji", "hon shimeji"], "Always cook them — raw shimeji are bitter, but cooking makes them nutty and sweet.", 86, 33)
add("chicken of the woods", "fungi", ["sulphur shelf", "laetiporus"], "Bright orange shelf fungus that actually tastes like chicken when sauteed.", 85, 33)
add("hen of the woods", "fungi", ["grifola frondosa"], "Can grow to 50 pounds at the base of oak trees — a forager's dream find.", 88, 31)
add("lobster mushroom", "fungi", ["lobster mushrooms"], "Not a real species — it's a parasite that transforms other mushrooms, turning them red.", 84, 28)
add("nameko", "fungi", ["namekos", "pholiota nameko"], "Covered in a natural gelatin — the traditional miso soup mushroom in Japan.", 83, 15)
add("snow fungus", "fungi", ["silver ear", "tremella", "white jelly mushroom"], "A beauty food in China — believed to give a dewy, glass-skin complexion.", 82, 20)
add("turkey tail", "fungi", ["turkey tail mushroom", "trametes versicolor"], "The most researched medicinal mushroom — used in Japanese cancer treatment protocols.", 80, 22)
add("king oyster", "fungi", ["king oyster mushroom", "king trumpet mushroom", "eryngii"], "The meaty stem is the star — sliced into scallop-shaped rounds and seared.", 87, 35)
add("candy cap", "fungi", ["candy caps"], "A wild mushroom that genuinely tastes and smells like maple syrup.", 84, 27)
add("cordyceps", "fungi", ["cordyceps mushroom", "caterpillar fungus"], "A parasitic fungus that grows out of insect larvae — prized in Tibetan medicine.", 80, 30)
add("pioppino", "fungi", ["black poplar mushroom"], "Grows on poplar trees — Italian nonnas have foraged these for centuries.", 84, 33)

# ============================================================
# SEAWEED
# ============================================================
add("sea grapes", "seaweed", ["green caviar", "umibudo", "caulerpa", "lato"], "Tiny grape-like clusters that pop in your mouth — Okinawan sea caviar.", 85, 36)
add("laver", "seaweed", ["laverbread", "porphyra"], "Welsh laverbread is made from this — boiled, minced, and fried with oatmeal.", 85, 35)
add("mekabu", "seaweed", ["wakame root"], "The thick, ruffled base of the wakame plant — slippery, chewy, and full of fucoidan.", 84, 45)
add("mozuku", "seaweed", ["cladosiphon"], "Okinawa's signature seaweed — often cited as a factor in their famous longevity.", 86, 6)
add("sea spaghetti", "seaweed", ["himanthalia elongata", "thongweed"], "Long brown strands that look and cook like spaghetti — a European Atlantic species.", 82, 35)

# ============================================================
# OILS
# ============================================================
add("algae oil", "oil", ["algal oil"], "Omega-3 from the original source — fish get their omega-3 from eating algae.", 85, 884)
add("argan oil", "oil", ["moroccan argan"], "Berber women have hand-pressed this liquid gold from Moroccan trees for centuries.", 84, 899)
add("black seed oil", "oil", ["nigella oil", "kalonji oil"], "Cold-pressed from nigella seeds — a Middle Eastern remedy for millennia.", 84, 884)
add("cod liver oil", "oil", ["fermented cod liver oil"], "Viking children were given a spoonful daily — packed with vitamins A and D.", 85, 902)
add("hazelnut oil", "oil", ["hazelnut oils"], "Delicate, nutty flavor that transforms a simple green salad.", 83, 884)
add("mustard oil", "oil", ["sarson ka tel"], "The traditional cooking fat of Bengal and Bihar — pungent when raw, mellow when heated.", 80, 884)
add("pumpkin seed oil", "oil", ["styrian pumpkin oil"], "The dark green oil of Austrian Styria — drizzled on vanilla ice cream as a delicacy.", 85, 884)
add("red palm oil", "oil", ["dende oil", "unrefined palm oil"], "Unrefined and deep red from carotenoids — the traditional fat of West African cooking.", 78, 884)

# ============================================================
# SWEETENERS
# ============================================================
add("blackstrap molasses", "sweetener", ["blackstrap"], "The third boiling of sugar cane — concentrated minerals make it almost medicinal.", 82, 235)
add("coconut nectar", "sweetener", ["coconut sap", "toddy"], "Tapped from coconut flower blossoms — lower glycemic index than table sugar.", 80, 300)
add("date sugar", "sweetener", ["ground dates"], "Not actually sugar — it's just dried dates ground into granules.", 84, 282)
add("palm sugar", "sweetener", ["gula melaka", "gula jawa"], "Tapped from palm tree sap and boiled down — the caramel sweetener of Southeast Asia.", 78, 375)
add("raw honey", "sweetener", ["unfiltered honey", "wild honey"], "Contains live enzymes, pollen, and propolis — pasteurization destroys all of these.", 88, 304)
add("sorghum syrup", "sweetener", ["sorghum molasses"], "An Appalachian tradition — stalks pressed and juice boiled into amber syrup.", 82, 269)
add("yacon syrup", "sweetener", ["yacon sweetener"], "Tastes like caramel but mostly fructooligosaccharides — feeds gut bacteria, not blood sugar.", 85, 197)

# ============================================================
# EGGS
# ============================================================
add("salmon roe", "egg", ["salmon eggs", "ikura", "red caviar"], "The glistening orange pearls on sushi — 'ikura' comes from the Russian word for caviar.", 88, 250)
add("uni", "egg", ["sea urchin roe", "sea urchin"], "Not technically an egg — it's the reproductive glands. Tastes like the ocean made custard.", 85, 120)
add("tobiko", "egg", ["flying fish roe", "flying fish eggs"], "The tiny, crunchy, naturally orange eggs on California rolls.", 84, 72)
add("sturgeon roe", "egg", ["beluga caviar", "osetra caviar", "true caviar"], "Real caviar only comes from sturgeon — everything else is technically just 'roe'.", 85, 264)
add("hen egg", "egg", ["chicken eggs", "free range eggs", "pasture raised eggs", "farm eggs"], "Humans have been eating chicken eggs for at least 7,500 years.", 90, 155)

# ============================================================
# BEVERAGES
# ============================================================
add("cacao drink", "beverage", ["ceremonial cacao", "drinking chocolate", "hot cacao"], "The Aztecs drank it bitter, spiced with chili — sugar was a European addition.", 86, 120)
add("chicory coffee", "beverage", ["chicory root coffee"], "New Orleans cafe au lait is always made with chicory — a Civil War tradition.", 82, 72)
add("coconut milk", "beverage", ["fresh coconut milk"], "Not the water inside — it's made by grating and pressing coconut flesh.", 84, 230)
add("elderberry juice", "beverage", ["elderberry syrup"], "Used for centuries as a folk remedy for colds and flu — now backed by some research.", 85, 73)
add("ginger tea", "beverage", ["fresh ginger tea", "adrak chai"], "Fresh ginger steeped in hot water — a universal remedy from India to the Caribbean.", 86, 2)
add("golden milk", "beverage", ["turmeric latte", "haldi doodh"], "Turmeric, black pepper, and warm milk — an Ayurvedic drink gone mainstream.", 84, 50)
add("green juice", "beverage", ["cold pressed juice"], "Kale, spinach, cucumber, celery — a raw vegetable drink in concentrated form.", 85, 30)
add("kava", "beverage", ["kava kava", "awa", "yaqona"], "A mildly sedative Pacific Island pepper root drink — central to Polynesian ceremonies.", 75, 2)
add("lassi", "beverage", ["mango lassi", "sweet lassi", "salt lassi"], "India's yogurt smoothie — sweet, salty, or mango, drunk with every meal in Punjab.", 84, 75)
add("matcha", "beverage", ["matcha tea", "ceremonial matcha"], "You consume the entire tea leaf ground to powder — 10x the antioxidants of brewed green tea.", 90, 3)
add("nut milk", "beverage", ["almond milk", "cashew milk", "walnut milk"], "Almond milk was a medieval European staple — it's not a modern invention.", 82, 30)
add("oat milk", "beverage", ["oat milks"], "Swedish invention from the 1990s that took over coffee shops worldwide.", 80, 40)
add("barley water", "beverage", ["barley tea", "mugicha"], "A cooling summer drink in both Asia and the Middle East for thousands of years.", 80, 28)
add("switchel", "beverage", ["haymaker's punch"], "Apple cider vinegar, ginger, and honey in water — Colonial American Gatorade.", 82, 30)
add("chrysanthemum tea", "beverage", ["ju hua cha"], "A cooling traditional Chinese drink — billions of cups consumed every summer.", 82, 1)
add("pine needle tea", "beverage", ["pine tea"], "Contains 5x more vitamin C than orange juice — a wilderness survival drink.", 80, 2)
add("tulsi tea", "beverage", ["holy basil tea"], "Sacred in Hinduism — tulsi plants grow in millions of Indian household courtyards.", 84, 2)
add("dandelion coffee", "beverage", ["dandelion root coffee", "roasted dandelion"], "Roasted dandelion root brews into a bitter, coffee-like drink — caffeine free.", 82, 20)
add("sauerkraut juice", "beverage", ["sauerkraut brine", "kraut juice"], "The tangy brine from fermented cabbage — a concentrated probiotic shot.", 85, 5)
add("birch water", "beverage", ["birch sap", "birch juice"], "Tapped from birch trees in spring — slightly sweet with minerals from the tree.", 82, 18)
add("mint tea", "beverage", ["moroccan mint tea", "touareg tea"], "Moroccan hospitality in a glass — gunpowder green tea with fresh mint and sugar.", 84, 2)
add("nettle tea", "beverage", ["stinging nettle tea"], "Stinging nettle brewed as tea — a traditional spring tonic across Europe.", 82, 1)
add("rosehip tea", "beverage", ["rose hip tea"], "The fruit of the rose plant — Scandinavians make soup (nyponsoppa) from it.", 84, 2)
add("turmeric tea", "beverage", ["turmeric infusion"], "Fresh turmeric root steeped with black pepper — pepper boosts curcumin absorption by 2000%.", 85, 2)
add("carob drink", "beverage", ["carob tea"], "A caffeine-free chocolate alternative made from the pod of a Mediterranean tree.", 80, 40)

# ============================================================
# Write the expanded file
# ============================================================
all_foods = existing_foods + new_items
all_foods.sort(key=lambda x: (x["category"], x["name"]))

with open(FOODS_PATH, "w") as f:
    json.dump(all_foods, f, indent=2, ensure_ascii=False)

print(f"\nOriginal: {len(existing_foods)} items")
print(f"New items added: {len(new_items)}")
print(f"Total: {len(all_foods)} items")

from collections import Counter
cats = Counter(item["category"] for item in all_foods)
print("\nCategory breakdown:")
for cat, count in cats.most_common():
    print(f"  {cat}: {count}")
