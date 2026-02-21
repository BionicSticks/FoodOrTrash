#!/usr/bin/env python3
"""Second expansion pass — push from ~813 to 2000+ items."""

import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FOODS_PATH = os.path.join(SCRIPT_DIR, "..", "src", "data", "foods.json")

with open(FOODS_PATH) as f:
    existing_foods = json.load(f)

existing_names = {item["name"].lower() for item in existing_foods}
new_items = []

def add(name, category, aliases, fun_fact, score, calories):
    if name.lower() in existing_names:
        return
    existing_names.add(name.lower())
    new_items.append({
        "name": name, "category": category, "aliases": aliases,
        "fun_fact": fun_fact, "score": score, "calories": calories
    })

# ============================================================
# FRUITS — ROUND 2 (varieties, regional, and commonly searched)
# ============================================================
add("african star apple", "fruit", ["agbalumo", "udara", "chrysophyllum"], "Break it open and the star pattern inside reveals how it got its name.", 83, 67)
add("black mulberry", "fruit", ["black mulberries", "morus nigra"], "The stains are nearly impossible to wash out — a childhood badge of honor.", 86, 43)
add("camu camu", "fruit", ["camu camus"], "Contains 60x more vitamin C per serving than an orange.", 92, 17)
add("carob", "fruit", ["carob pods", "carob fruit", "ceratonia"], "Each pod weighs remarkably consistently — the origin of the 'carat' weight unit.", 80, 222)
add("chayote", "fruit", ["chayotes", "mirliton", "christophine", "cho cho"], "A squash you can eat raw — the single large seed is edible too when cooked.", 83, 19)
add("cornelian cherry", "fruit", ["cornelian cherries", "cornus mas", "dogwood berry"], "Not a cherry at all — these sour red fruits make a tart jam in Turkey and Iran.", 84, 40)
add("damson plum", "fruit", ["damson plums", "damsons"], "Too tart to eat raw but makes the finest plum jam and gin in England.", 82, 46)
add("desert lime", "fruit", ["desert limes", "australian lime"], "Survives temperatures up to 120F in the Australian outback.", 84, 28)
add("dewberry", "fruit", ["dewberries"], "A trailing blackberry that grows low to the ground — sweeter than its upright cousin.", 85, 43)
add("egg fruit", "fruit", ["egg fruits", "canistel"], "Named for its texture — the flesh is dry and crumbly like a hard-boiled egg yolk.", 80, 139)
add("elephant apple", "fruit", ["elephant apples", "dillenia indica", "chalta"], "So sour it makes your eyes water — elephants love them, hence the name.", 78, 50)
add("gac fruit", "fruit", ["gac fruits", "baby jackfruit", "spiny bitter gourd"], "Contains 70x more lycopene than tomatoes — the Vietnamese call it 'fruit from heaven'.", 90, 42)
add("giant granadilla", "fruit", ["giant granadillas", "badea", "giant passion fruit"], "The largest passion fruit species — can grow to a foot long.", 80, 46)
add("grumichama", "fruit", ["grumichamas", "brazilian cherry"], "A rare Brazilian cherry tree that produces intensely sweet dark purple fruit.", 84, 45)
add("guanabana", "fruit", ["guanabanas"], "The same fruit as soursop — called guanabana in Latin America.", 84, 66)
add("honeyberry", "fruit", ["honeyberries", "haskap", "blue honeysuckle"], "An Arctic berry that can survive -47C — now a darling of cold-climate fruit growers.", 88, 39)
add("indian gooseberry", "fruit", ["amla", "amalaki", "phyllanthus emblica"], "The cornerstone of Ayurvedic medicine for 3,000+ years — incredibly sour but nutritious.", 90, 44)
add("jackfruit", "fruit", ["jackfruits", "nangka", "kathal"], "The world's largest tree fruit — a single jackfruit can weigh over 100 pounds.", 84, 95)
add("java apple", "fruit", ["java apples", "wax jambu", "water apple"], "Bell-shaped and watery-crisp — one of the most refreshing tropical fruits.", 82, 25)
add("kiwano", "fruit", ["kiwanos", "horned melon", "african horned cucumber"], "The spiky orange shell hides lime-green jelly-like flesh tasting of cucumber and banana.", 80, 44)
add("korean melon", "fruit", ["korean melons", "chamoe", "oriental melon"], "Yellow with white stripes — sweet, crunchy, and eaten like an apple in Korea.", 84, 30)
add("kwai muk", "fruit", ["kwai muks"], "A tiny Chinese fig relative with a sweet, strawberry-like flesh.", 80, 55)
add("lemon drop mangosteen", "fruit", ["lemon drop mangosteens", "achachairu"], "Tastes like lemonade in fruit form — a Bolivian treasure only recently known outside South America.", 84, 60)
add("madrono", "fruit", ["madronos", "arbutus fruit", "strawberry tree fruit"], "The only fruit in the EU that ferments on the tree — birds eating them get tipsy.", 80, 76)
add("makrut lime fruit", "fruit", ["makrut lime fruits"], "Bumpy and nearly juiceless — the zest is prized but the leaves even more so.", 78, 30)
add("mango", "fruit", ["mangos", "mangoes", "alphonso", "ataulfo", "kent mango", "tommy atkins", "nam doc mai"], "India produces 20 million tonnes per year — there are over 1,000 mango varieties.", 92, 60)
add("marang", "fruit", ["marangs"], "A jackfruit relative from the Philippines with cotton-candy-sweet flesh.", 83, 80)
add("mock strawberry", "fruit", ["mock strawberries", "indian strawberry", "duchesnea"], "Looks identical to a strawberry but tastes like absolutely nothing.", 70, 20)
add("mountain apple", "fruit", ["mountain apples", "malay apple", "pomerac"], "A teardrop-shaped tropical fruit with crisp, rose-scented flesh.", 82, 56)
add("natal plum", "fruit", ["natal plums", "carissa", "num-num"], "The only part of this otherwise toxic plant that's safe to eat.", 80, 62)
add("oil palm fruit", "fruit", ["palm fruit", "palm oil fruit", "dende"], "The bright red-orange fruit that produces the world's most consumed vegetable oil.", 72, 150)
add("otaheite apple", "fruit", ["otaheite apples", "malay apple", "mountain apple"], "Captain Bligh of the Bounty introduced this fruit to the Caribbean.", 80, 28)
add("pandanus fruit", "fruit", ["pandanus fruits", "screwpine fruit", "hala fruit"], "Looks like an alien planet — each segment can be sucked for sweet juice.", 78, 80)
add("peach palm fruit", "fruit", ["peach palm fruits", "pejibaye", "chontaduro"], "Must be boiled before eating — a staple of Central and South American diets for 10,000 years.", 82, 196)
add("pequi", "fruit", ["pequis", "souari nut", "piqui"], "A Brazilian cerrado fruit with thorny seeds — biting too hard means spines in your tongue.", 78, 90)
add("persian lime", "fruit", ["persian limes", "tahiti lime", "bearss lime"], "The seedless lime you see in every supermarket — actually a hybrid of key lime and lemon.", 87, 30)
add("pitomba", "fruit", ["pitombas"], "A tiny Brazilian fruit that bursts with bittersweet juice — popular street fruit.", 80, 44)
add("quandong", "fruit", ["quandongs", "native peach", "desert quandong"], "An Australian bush food with tart flesh — Aboriginal people have eaten it for 50,000 years.", 84, 73)
add("red banana", "fruit", ["red bananas"], "Shorter, plumper, and sweeter than yellow bananas with a hint of raspberry.", 86, 90)
add("rollinia", "fruit", ["rollinias", "biriba", "wild sugar apple"], "When perfectly ripe, it tastes like lemon meringue pie.", 83, 80)
add("sapodilla", "fruit", ["sapodillas", "chikoo", "naseberry", "sapota"], "The tree's sap is chicle — the original base for chewing gum.", 84, 83)
add("sugarplum", "fruit", ["sugarplums"], "The 'visions of sugarplums' in the Christmas poem were actually candied fruits.", 78, 75)
add("tamarillo", "fruit", ["tamarillos", "tree tomato", "tomate de arbol"], "An egg-shaped fruit that looks like a tomato but tastes sweet-tart.", 84, 31)
add("wampee", "fruit", ["wampees", "clausena lansium"], "A grape-sized Chinese fruit with a resinous, spicy-sweet flavor.", 80, 40)
add("wood apple", "fruit", ["wood apples", "bael fruit", "stone apple", "limonia"], "The rock-hard shell must be cracked with a hammer to reach the pulp inside.", 80, 137)

# ============================================================
# VEGETABLES — ROUND 2
# ============================================================
add("arrowroot", "vegetable", ["arrowroots", "maranta"], "Used as a thickener for centuries — supposedly named for treating arrow wounds.", 82, 65)
add("banana pepper", "vegetable", ["banana peppers", "yellow wax pepper"], "Mild enough to eat raw — a staple topping at pizza and sub shops.", 84, 27)
add("breadfruit", "vegetable", ["breadfruits", "ulu"], "When roasted it smells and tastes like fresh-baked bread.", 83, 103)
add("broccoli rabe", "vegetable", ["rapini", "broccoli raab", "cime di rapa"], "More closely related to turnips than broccoli — beloved for its bitter bite in Italian cooking.", 87, 22)
add("calabash", "vegetable", ["calabashes", "bottle gourd"], "Dried shells have been used as containers, instruments, and helmets for 10,000 years.", 78, 14)
add("canna", "vegetable", ["canna rhizome", "queensland arrowroot", "achira"], "The starchy rhizome was a food source in the Andes 4,500 years ago.", 78, 72)
add("cape gooseberry", "vegetable", ["cape gooseberries", "goldenberry"], "Wrapped in a papery lantern — a natural single-serving fruit package.", 85, 53)
add("cassava leaf", "vegetable", ["cassava leaves", "saka saka", "pondu"], "Must be pounded and cooked for hours to remove cyanide — a Congo staple.", 80, 91)
add("cavolo nero", "vegetable", ["lacinato kale", "tuscan kale", "dinosaur kale", "black kale"], "The dark, bumpy leaves are the classic Tuscan ribollita ingredient.", 90, 33)
add("chili pepper", "vegetable", ["chili peppers", "hot pepper", "capsicum"], "Capsaicin triggers pain receptors — we're the only species that eats them for fun.", 85, 40)
add("chinese artichoke", "vegetable", ["chinese artichokes", "crosne", "stachys"], "Tiny spiral-shaped tubers that look like grubs — crunchy and nutty.", 80, 55)
add("chinese long bean", "vegetable", ["chinese long beans", "dow gauk"], "Can grow up to 30 inches long in just a few days.", 84, 47)
add("chinese water chestnut", "vegetable", ["water chestnuts", "eleocharis"], "Not a nut — it's a corm from an aquatic plant, prized for staying crunchy when cooked.", 84, 97)
add("cress", "vegetable", ["garden cress", "peppergrass", "halim"], "One of the fastest-growing vegetables — sprouts in 2-3 days.", 86, 32)
add("fava bean", "vegetable", ["fava beans", "broad beans", "foul medames"], "The oldest cultivated bean — Egyptians have eaten ful medames for 4,000 years.", 86, 88)
add("green onion", "vegetable", ["green onions", "spring onion", "spring onions"], "The green tops and white bulb are essentially two different ingredients in one plant.", 86, 32)
add("habanero", "vegetable", ["habaneros", "habanero pepper", "scotch bonnet"], "Up to 350,000 Scoville units — but beneath the heat is a fruity, tropical flavor.", 82, 40)
add("haricot vert", "vegetable", ["haricots verts", "french green bean", "french beans"], "Thinner and more tender than American green beans — the French standard.", 86, 31)
add("iceberg lettuce", "vegetable", ["iceberg", "head lettuce", "crisphead"], "Named because it was shipped under mountains of ice in the 1920s.", 75, 14)
add("jalapeno", "vegetable", ["jalapenos", "jalapeno pepper"], "Named after Xalapa, Mexico — a smoked jalapeno becomes a chipotle.", 84, 29)
add("kai lan", "vegetable", ["chinese broccoli", "gai lan stems"], "The thick stems are blanched and drizzled with oyster sauce — a dim sum classic.", 88, 26)
add("kohlrabi", "vegetable", ["kohlrabis", "german turnip"], "Looks alien but tastes like a mild, sweet broccoli stem.", 86, 27)
add("lamb's ear", "vegetable", ["lamb's quarters", "fat hen", "chenopodium"], "A 'weed' more nutritious than spinach — eaten by Indigenous peoples across the Americas.", 84, 43)
add("lotus root", "vegetable", ["lotus roots", "renkon", "kamal kakdi"], "The beautiful hole pattern is natural — it's the plant's ventilation system.", 85, 74)
add("mache", "vegetable", ["corn salad", "field salad", "lamb's lettuce greens"], "The most expensive salad green to produce — each rosette is harvested by hand.", 86, 21)
add("nopal", "vegetable", ["nopales", "cactus pad", "prickly pear cactus pad"], "Aztecs built Tenochtitlan where an eagle sat on a nopal — it's on Mexico's flag.", 86, 16)
add("pearl onion", "vegetable", ["pearl onions", "cocktail onions", "cipollini"], "Traditionally peeled by blanching — the bane of Thanksgiving cooks everywhere.", 82, 42)
add("peppadew", "vegetable", ["peppadew peppers", "sweet piquante"], "Discovered wild in South Africa in 1993 — now trademarked and grown worldwide.", 83, 56)
add("pointed cabbage", "vegetable", ["pointed cabbages", "hispi cabbage", "sweetheart cabbage"], "Conical shape and sweeter than round cabbage — grills beautifully when halved.", 84, 22)
add("poblano", "vegetable", ["poblano pepper", "poblanos", "ancho chili"], "When dried it becomes an ancho — the most commonly used dried chili in Mexico.", 84, 20)
add("red cabbage", "vegetable", ["red cabbages", "purple cabbage"], "Changes color based on pH — turns blue in alkaline conditions, pink in acid.", 87, 31)
add("red onion", "vegetable", ["red onions", "purple onion"], "The anthocyanins that make it purple are the same antioxidants found in blueberries.", 85, 40)
add("romaine lettuce", "vegetable", ["romaine", "cos lettuce"], "The lettuce of Caesar salad — named after Rome where it was popular.", 82, 17)
add("serrano", "vegetable", ["serrano pepper", "serranos"], "Five times hotter than a jalapeno — the preferred chili for fresh Mexican salsas.", 83, 32)
add("shiso", "vegetable", ["shiso leaf", "perilla leaf", "ooba"], "The Japanese herb served with every sashimi plate — antimicrobial and aromatic.", 85, 37)
add("snow pea", "vegetable", ["snow peas", "mangetout", "chinese pea"], "The French call them mangetout ('eat all') because you eat pod and all.", 87, 42)
add("sugar snap pea", "vegetable", ["sugar snap peas", "snap peas"], "A cross between snow peas and garden peas — invented by a plant breeder in 1979.", 88, 42)
add("sun dried tomato", "vegetable", ["sun dried tomatoes", "pomodori secchi"], "Italian farmers dried them on rooftops all summer — concentrated umami bombs.", 84, 258)
add("sweet onion", "vegetable", ["sweet onions", "vidalia onion", "walla walla", "maui onion"], "Vidalia onions are sweet because of low sulfur in Georgia's soil.", 83, 32)
add("swiss chard stem", "vegetable", ["rainbow chard stems", "chard stalks"], "The colorful stems and green leaves are essentially two vegetables in one plant.", 86, 19)
add("thai basil", "vegetable", ["thai basils", "horapha"], "Anise-flavored basil that doesn't wilt in hot dishes like Italian basil does.", 85, 23)
add("white asparagus", "vegetable", ["white asparaguses", "spargel", "bleached asparagus"], "Grown under mounds of earth to prevent photosynthesis — German 'Spargelzeit' is a national event.", 87, 20)
add("white onion", "vegetable", ["white onions"], "Milder and sweeter than yellow onions — the preferred onion in Mexican cuisine.", 83, 36)
add("white sweet potato", "vegetable", ["white sweet potatoes", "boniato", "batata"], "Drier and less sweet than orange varieties — the preferred sweet potato in the Caribbean.", 84, 86)
add("yellow squash", "vegetable", ["yellow squashes", "summer squash", "straightneck squash"], "Produces so prolifically that gardeners famously leave bags on neighbors' doorsteps.", 83, 20)
add("yuca", "vegetable", ["yucca root", "mandioca", "tapioca root"], "The third largest source of carbohydrates in the tropics after rice and corn.", 82, 160)

# ============================================================
# FISH — ROUND 2
# ============================================================
add("arctic char", "fish", ["arctic chars"], "The northernmost freshwater fish — thrives in glacial lakes across the Arctic.", 89, 140)
add("barramundi", "fish", ["barramundis", "asian sea bass"], "Born male, every barramundi becomes female after one or two spawning seasons.", 87, 110)
add("bluefin tuna", "fish", ["bluefin tunas", "hon maguro", "otoro"], "A single fish sold for $3.1 million at Tokyo's Tsukiji Market in 2019.", 85, 144)
add("branzino", "fish", ["branzinos", "european sea bass", "spigola"], "The whole roasted branzino is the quintessential Mediterranean restaurant dish.", 89, 97)
add("butterfish", "fish", ["pacific pompano", "butterflish"], "So rich and oily that Japan classifies it as 'shiro maguro' (white tuna).", 83, 146)
add("chilean sea bass", "fish", ["patagonian toothfish"], "Actually called Patagonian toothfish — renamed for marketing because nobody wanted to order 'toothfish'.", 82, 107)
add("dorado", "fish", ["dorados", "mahi-mahi", "dolphinfish"], "Not a dolphin — the name 'dolphinfish' has caused confusion for decades.", 87, 85)
add("escolar", "fish", ["white tuna", "oilfish", "escolars"], "Contains indigestible wax esters — Japan requires warning labels on it.", 65, 232)
add("flying fish", "fish", ["flying fishes", "tobiuo"], "Can glide up to 200 meters using wing-like fins — the national symbol of Barbados.", 82, 96)
add("golden trout", "fish", ["golden trouts"], "California's state freshwater fish, found only in high Sierra Nevada streams.", 88, 120)
add("horse mackerel", "fish", ["horse mackerels", "jack mackerel", "aji"], "Not a true mackerel — called 'aji' in Japanese sushi restaurants.", 84, 114)
add("john dory", "fish", ["john dorys", "st pierre"], "The black spot on its side — legend says it's where St. Peter gripped the fish.", 85, 73)
add("lamprey", "fish", ["lampreys", "sea lamprey"], "A jawless fish considered a delicacy since Roman times — still served in Portugal.", 78, 138)
add("mako shark", "fish", ["mako sharks", "mako"], "The fastest shark species at 60 mph — its meat tastes like swordfish.", 78, 130)
add("monchong", "fish", ["monchongs", "bigscale pomfret"], "A Hawaiian deep-water fish with rich, buttery flesh — underappreciated on the mainland.", 84, 108)
add("opakapaka", "fish", ["hawaiian pink snapper"], "A prized Hawaiian deep-water snapper with delicate pink flesh.", 87, 100)
add("orange roughy", "fish", ["orange roughies"], "Can live up to 149 years — the fish on your plate may have been born before World War I.", 75, 69)
add("pacific halibut", "fish", ["pacific halibuts"], "Can grow to 500 pounds — the largest flatfish in the Pacific Ocean.", 88, 110)
add("parrotfish", "fish", ["parrotfishes"], "Eats coral and poops sand — a single parrotfish creates 200 lbs of sand per year.", 80, 98)
add("red snapper", "fish", ["red snappers", "northern red snapper"], "One of the most mislabeled fish — studies show 87% of 'red snapper' in restaurants isn't.", 86, 100)
add("rohu", "fish", ["rohus", "labeo rohita", "rui"], "The king of Bengali fish curries — served at every celebration.", 84, 97)
add("sea bream", "fish", ["sea breams", "tai", "daurade"], "The most auspicious fish in Japan — served whole at celebrations.", 87, 100)
add("sheepshead", "fish", ["sheepsheads"], "Has eerily human-like teeth for crushing oyster shells and barnacles.", 83, 108)
add("striped bass", "fish", ["striped basses", "striper", "rockfish bass"], "The iconic fish of the Chesapeake Bay — Captain John Smith wrote about catching them in 1608.", 86, 97)
add("vermillion snapper", "fish", ["vermillion snappers", "beeliner"], "A deep red snapper found in the Gulf of Mexico — lighter in flavor than red snapper.", 84, 100)
add("walleye", "fish", ["walleyes", "walleye pike", "pickerel"], "Minnesota's state fish — the Friday night fish fry across the Midwest.", 87, 93)
add("white bass", "fish", ["white basses"], "A freshwater fish that runs up rivers in spring — the original fish fry fish.", 84, 90)
add("yellowfin tuna", "fish", ["yellowfin tunas", "ahi tuna", "ahi"], "Called 'ahi' in Hawaiian — the fish behind seared ahi tuna steaks.", 88, 108)
add("zander", "fish", ["zanders", "pike-perch", "sander lucioperca"], "Europe's most prized freshwater fish — the continental answer to walleye.", 86, 84)

# ============================================================
# DAIRY — ROUND 2
# ============================================================
add("aged cheddar", "dairy", ["vintage cheddar", "sharp cheddar", "extra mature cheddar"], "True cheddar is 'cheddared' — stacked and turned to expel whey, creating its dense texture.", 86, 403)
add("bocconcini", "dairy", ["bocconcinis", "cherry mozzarella"], "Little mouthfuls of fresh mozzarella — 'bocconcini' literally means 'small mouthfuls'.", 85, 280)
add("buffalo mozzarella", "dairy", ["mozzarella di bufala", "bufala"], "Made from water buffalo milk — tangier and creamier than cow's milk mozzarella.", 87, 280)
add("cambozola", "dairy", ["cambozolas"], "A German invention combining Camembert's creaminess with Gorgonzola's blue veins.", 82, 360)
add("cantal", "dairy", ["cantals", "cantal cheese"], "One of France's oldest cheeses — Pliny the Elder wrote about it 2,000 years ago.", 82, 370)
add("chevre", "dairy", ["goat cheese log", "fresh chevre", "fresh goat cheese"], "Tangy, spreadable, and snow-white — the fat molecules in goat milk are smaller than cow's.", 86, 364)
add("comte", "dairy", ["comté", "comte cheese"], "France's most popular cheese — each wheel requires 530 liters of milk.", 87, 413)
add("dutch gouda", "dairy", ["aged gouda", "old amsterdam"], "Aged gouda develops crunchy crystals of tyrosine — a sign of proper aging.", 85, 356)
add("gorgonzola", "dairy", ["gorgonzola dolce", "gorgonzola piccante"], "Named after a town near Milan where it's been made since the 9th century.", 83, 353)
add("kashkaval", "dairy", ["kashkavals", "cascaval", "kasseri"], "The Balkan cousin of Italian caciocavallo — a stretched, semi-hard cheese.", 82, 349)
add("manchego", "dairy", ["manchego cheese", "queso manchego"], "Can only be made from Manchega sheep milk in Spain's La Mancha region.", 86, 376)
add("ossau-iraty", "dairy", ["ossau iraty", "basque cheese"], "A Basque sheep's cheese from the Pyrenees — served with black cherry jam.", 83, 385)
add("pecorino romano", "dairy", ["pecorino", "romano cheese"], "The cheese that built Rome — legionnaires received a daily ration of pecorino.", 86, 387)
add("pont l'eveque", "dairy", ["pont leveque cheese"], "One of Normandy's oldest cheeses — documented since the 13th century.", 80, 315)
add("tete de moine", "dairy", ["tete de moines", "monk's head"], "Shaved into rosettes with a special tool called a girolle — never sliced.", 83, 382)
add("tomme de savoie", "dairy", ["tomme", "alpine tomme"], "A rustic Alpine cheese made from the skimmed milk left after cream was taken for butter.", 82, 332)
add("valençay", "dairy", ["valencay", "valencay cheese"], "Legend says Napoleon slashed the pointed top off with his sword — it's been flat-topped since.", 80, 300)
add("wensleydale", "dairy", ["wensleydale cheese"], "Nearly went extinct in 1992 until Wallace and Gromit revived demand for it.", 83, 375)

# ============================================================
# MEAT — ROUND 2
# ============================================================
add("antelope", "meat", ["pronghorn", "antelope meat"], "The pronghorn is the second-fastest land animal after the cheetah.", 85, 114)
add("bear", "meat", ["bear meat"], "Must always be cooked well-done — bears can carry trichinella parasites.", 75, 161)
add("camel", "meat", ["camel meat", "camel hump"], "The hump is considered the most prized cut in Middle Eastern cuisine.", 82, 98)
add("chuck roast", "meat", ["beef chuck", "pot roast"], "The shoulder cut that becomes melt-in-your-mouth tender after hours of braising.", 83, 250)
add("emu", "meat", ["emu meat", "emu steak"], "Looks and tastes like lean beef but comes from a bird.", 85, 134)
add("filet mignon", "meat", ["beef tenderloin", "tenderloin steak", "beef fillet"], "The most tender cut of beef — a muscle that does almost no work.", 85, 267)
add("flank steak", "meat", ["flank steaks", "bavette"], "A lean, flavorful cut that must be sliced against the grain or it's chewy.", 85, 194)
add("hanger steak", "meat", ["onglet", "butcher's steak", "hanging tender"], "Called 'butcher's steak' because butchers kept this cut for themselves.", 86, 199)
add("hare", "meat", ["hare meat", "jugged hare"], "Stronger-flavored than rabbit — 'jugged hare' is a classic British dish.", 83, 114)
add("lamb chop", "meat", ["lamb chops", "lamb cutlet", "lamb rack"], "The rib chop is so tender it needs only salt, pepper, and a hot grill.", 86, 294)
add("lamb shank", "meat", ["lamb shanks"], "Slow-braised until the meat falls off the bone — a cold-weather classic.", 84, 201)
add("llama", "meat", ["llama meat"], "Leaner than beef with a mild flavor, traditional in Andean highland cuisine.", 82, 120)
add("new york strip", "meat", ["ny strip", "strip steak", "sirloin steak"], "Cut from the short loin — the steakhouse classic with a perfect fat-to-meat ratio.", 84, 271)
add("pork belly", "meat", ["pork bellies", "uncured bacon", "fresh bacon"], "The cut that becomes bacon when cured — when roasted, the skin turns to crackling.", 80, 518)
add("pork chop", "meat", ["pork chops", "pork cutlet", "pork loin chop"], "The bone-in chop is juicier — the bone insulates the meat during cooking.", 84, 231)
add("pork shoulder", "meat", ["pork shoulders", "boston butt", "pork butt"], "Despite the name 'butt', it's actually the shoulder — the cut for pulled pork.", 83, 240)
add("ribeye", "meat", ["ribeye steak", "rib eye", "scotch fillet", "entrecote"], "The most marbled common steak cut — fat is flavor.", 84, 291)
add("short ribs", "meat", ["beef short ribs", "galbi", "kalbi"], "Korean galbi marinates them in soy, pear, and sesame — grilled over charcoal.", 83, 295)
add("sirloin", "meat", ["sirloin steak", "top sirloin"], "Legend says King Henry VIII knighted a loin of beef — hence 'sir-loin'.", 84, 200)
add("skirt steak", "meat", ["skirt steaks", "arrachera", "fajita meat"], "The original fajita meat — Mexican arrachera grilled over mesquite.", 85, 202)
add("t-bone", "meat", ["t-bone steak", "porterhouse", "bistecca alla fiorentina"], "Two steaks in one — strip on one side, tenderloin on the other.", 84, 247)
add("tri-tip", "meat", ["tri-tips", "triangle roast", "santa maria steak"], "Santa Maria, California's claim to fame — grilled over red oak.", 84, 217)
add("whole chicken", "meat", ["roast chicken", "spatchcocked chicken", "rotisserie chicken"], "Julia Child said mastering roast chicken is the mark of a good cook.", 85, 239)

# ============================================================
# POULTRY — ROUND 2
# ============================================================
add("chicken drumstick", "poultry", ["chicken drumsticks", "chicken legs"], "The dark meat drumstick stays juicy even when slightly overcooked — forgiving and flavorful.", 84, 172)
add("chicken gizzard", "poultry", ["chicken gizzards", "gizzards"], "A muscular digestive organ with a chewy, rich flavor — beloved from Brazil to Japan.", 82, 94)
add("chicken heart", "poultry", ["chicken hearts"], "Skewered and grilled as yakitori in Japan, espetinho in Brazil — a street food icon.", 84, 153)
add("duck breast", "poultry", ["magret", "duck magret"], "Scored and seared skin-side down — the rendered fat is liquid gold for cooking.", 87, 337)
add("duck liver", "poultry", ["duck livers", "foie gras"], "Duck liver pate is a cornerstone of French cuisine dating back centuries.", 82, 136)
add("guinea fowl", "poultry", ["guinea fowl meat", "pintade"], "Leaner and more flavorful than chicken — tastes like what chicken used to taste like.", 85, 158)
add("spatchcock chicken", "poultry", ["butterflied chicken", "flattened chicken"], "Backbone removed and flattened — cooks in half the time of a whole bird.", 85, 190)
add("smoked turkey", "poultry", ["smoked turkey breast", "smoked turkey leg"], "The smoky flavor penetrates deep into the meat — a Thanksgiving alternative.", 83, 126)

# ============================================================
# SHELLFISH — ROUND 2
# ============================================================
add("bay scallop", "shellfish", ["bay scallops", "cape bay scallop"], "Smaller and sweeter than sea scallops — eaten in one tender bite.", 88, 69)
add("brown crab", "shellfish", ["brown crabs", "european crab", "cancer pagurus"], "The crab of classic British dressed crab — brown meat and white meat served together.", 86, 91)
add("chinese mitten crab", "shellfish", ["hairy crab", "shanghai crab", "dazha crab"], "The autumn delicacy of Shanghai — restaurants have waiting lists months long.", 84, 84)
add("jonah crab", "shellfish", ["jonah crabs", "jonah crab claws"], "The sweeter, less expensive cousin of stone crab, found off New England.", 84, 78)
add("mantis shrimp", "shellfish", ["mantis shrimps", "squilla"], "Can punch with the force of a bullet — Italian cuisine adores them in pasta.", 82, 91)
add("razor clam", "shellfish", ["razor clams", "pacific razor clam", "atlantic razor clam"], "Named for the shape — they look like old-fashioned straight razors.", 86, 73)
add("rock shrimp", "shellfish", ["rock shrimps"], "Tastes like lobster at a fraction of the price — the shell is rock-hard.", 85, 79)
add("sea cucumber", "shellfish", ["sea cucumbers", "hai shen", "beche de mer", "trepang"], "Not a vegetable — it's an animal that breathes through its rear end.", 78, 56)
add("spanner crab", "shellfish", ["spanner crabs", "kona crab", "frog crab"], "Flat and round — Australian fishermen catch them with special nets.", 82, 75)
add("tiger prawn", "shellfish", ["tiger prawns", "black tiger shrimp", "giant tiger prawn"], "Can grow to 13 inches long — the dramatic black stripes disappear when cooked.", 86, 85)
add("venus clam", "shellfish", ["venus clams", "vongole", "carpet shell clam"], "The clam in spaghetti alle vongole — Italy's most beloved pasta seafood dish.", 86, 72)
add("whelk", "shellfish", ["whelks", "sea snail"], "A British seaside tradition — eaten with vinegar at the beach.", 80, 137)

# ============================================================
# GRAINS — ROUND 2
# ============================================================
add("bamboo rice", "grain", ["bamboo rices"], "Rice infused with bamboo extract, turning it pale green with a subtle herbal flavor.", 82, 360)
add("blue corn", "grain", ["blue cornmeal", "hopi corn"], "Has 20% more protein than yellow corn — sacred to the Hopi people.", 86, 361)
add("brown rice", "grain", ["whole grain rice", "unpolished rice"], "Just white rice with the bran and germ intact — more fiber and nutrients.", 88, 370)
add("cracked wheat", "grain", ["cracked wheats", "dalia"], "Wheat berries broken into pieces — cooks faster than whole berries with the same nutrition.", 85, 340)
add("durum wheat", "grain", ["durum", "semolina wheat"], "The hardest wheat variety — ground into semolina for the best pasta and couscous.", 84, 339)
add("flint corn", "grain", ["flint corns", "indian corn"], "Each kernel has a hard outer shell — the corn used for traditional polenta.", 82, 365)
add("glutinous rice", "grain", ["sticky rice", "sweet rice", "mochi rice"], "Not actually glutinous (no gluten) — it's sticky because of high amylopectin starch.", 82, 370)
add("pearl barley", "grain", ["pearled barley"], "The husk removed by polishing — the barley in mushroom barley soup.", 84, 352)
add("red quinoa", "grain", ["red quinoas"], "Holds its shape better than white quinoa — nuttier and more colorful in salads.", 89, 368)
add("sourdough", "grain", ["sourdough bread", "levain bread"], "Wild yeast fermentation makes the phytic acid more digestible than commercial bread.", 84, 240)
add("sprouted wheat", "grain", ["sprouted grain", "ezekiel grain"], "Germination breaks down starches and increases bioavailable nutrients.", 88, 198)
add("wheat berry", "grain", ["wheat berries", "whole wheat berry"], "The entire wheat kernel — bran, germ, and endosperm intact.", 87, 340)
add("white quinoa", "grain", ["quinoa", "regular quinoa"], "Not a grain but a seed — related to spinach and beets, not wheat or rice.", 89, 368)

# ============================================================
# LEGUMES — ROUND 2
# ============================================================
add("black lentil", "legume", ["black lentils", "beluga lentil", "urad dal whole"], "Named 'beluga' because the tiny black spheres look like caviar.", 89, 352)
add("brown lentil", "legume", ["brown lentils", "pardina lentil"], "The workhorse lentil — cheap, available everywhere, and cooks in 20 minutes.", 87, 352)
add("butter pea", "legume", ["butter peas", "sieva bean", "baby lima"], "Smaller and more delicate than lima beans — a Southern US summer staple.", 84, 115)
add("chickpea", "legume", ["chickpeas", "garbanzo", "garbanzo bean", "ceci"], "The base of hummus and falafel — cultivated for 7,500 years in the Middle East.", 89, 164)
add("french lentil", "legume", ["french lentils", "puy lentil", "lentilles du puy"], "Hold their shape perfectly when cooked — the only lentil with AOC protection.", 90, 352)
add("green lentil", "legume", ["green lentils"], "More peppery than brown lentils — excellent in salads and side dishes.", 88, 352)
add("horse gram", "legume", ["horse grams", "kulthi", "kollu"], "Once considered horse feed — now recognized as a superfood by nutritionists.", 83, 321)
add("lablab bean", "legume", ["lablab beans", "hyacinth bean", "dolichos"], "Both ornamental and edible — the purple pods are stunning in a garden.", 82, 50)
add("pigeon pea", "legume", ["pigeon peas", "toor dal", "arhar dal", "gandule"], "The basis of Caribbean rice and peas and Indian toor dal.", 85, 343)
add("red kidney bean", "legume", ["red kidney beans", "rajma"], "Must be boiled vigorously for 10 minutes — raw kidney beans are toxic.", 85, 333)
add("red lentil", "legume", ["red lentils", "masoor dal"], "Cooks into a creamy mush in 15 minutes — the fastest-cooking legume.", 88, 358)
add("runner bean", "legume", ["runner beans", "scarlet runner"], "Originally grown as an ornamental — the scarlet flowers are as valued as the beans.", 83, 35)
add("yellow split pea", "legume", ["yellow split peas", "chana dal"], "The base of Dutch erwtensoep — a pea soup thick enough to stand a spoon in.", 86, 341)

# ============================================================
# NUTS — ROUND 2
# ============================================================
add("beechnut", "nut", ["beechnuts", "beech nut"], "Once a primary food for Native Americans and European peasants.", 80, 576)
add("black walnut", "nut", ["black walnuts"], "Stronger and more earthy than English walnuts — the shells stain everything brown.", 85, 628)
add("butternut", "nut", ["butternuts", "white walnut"], "A sweeter, milder cousin of the black walnut, now endangered by disease.", 82, 612)
add("english walnut", "nut", ["walnuts", "common walnut", "persian walnut"], "The two halves of a walnut look like a brain — and they're great for brain health.", 90, 654)
add("hickory nut", "nut", ["hickory nuts", "shagbark hickory nut"], "The richest, most buttery native American nut — Andrew Jackson's nickname was 'Old Hickory'.", 85, 657)
add("ivory nut", "nut", ["ivory nuts", "tagua nut", "vegetable ivory"], "So hard and white it's carved as a sustainable alternative to elephant ivory.", 75, 335)
add("paradise nut", "nut", ["paradise nuts", "sapucaia nut"], "Rarer and richer than Brazil nuts — monkeys compete fiercely for them.", 82, 626)
add("shea nut", "nut", ["shea nuts", "karite nut"], "The butter from these nuts is used in cooking across West Africa (and in your lip balm).", 80, 590)

# ============================================================
# SEEDS — ROUND 2
# ============================================================
add("annatto seed", "seed", ["annatto seeds", "achiote"], "The natural red-orange dye used to color cheddar cheese and butter.", 80, 108)
add("apricot kernel", "seed", ["apricot kernels", "apricot seeds"], "Tastes like a bitter almond — used in Italian amaretti cookies.", 78, 520)
add("egusi", "seed", ["egusi seeds", "melon seeds"], "The base of Nigeria's beloved egusi soup — ground melon seeds thicken the broth.", 83, 555)
add("hemp heart", "seed", ["hemp hearts", "hulled hemp seed", "shelled hemp"], "A complete protein with all essential amino acids — no, it won't get you high.", 90, 553)
add("pine nut", "seed", ["pignoli", "pinoli", "chilgoza"], "Each tiny seed is hand-harvested from pine cones — that's why they're so expensive.", 88, 673)
add("tahini", "seed", ["sesame paste", "sesame butter", "tahina"], "Ground sesame seeds — the backbone of hummus, halva, and countless Middle Eastern dishes.", 87, 595)

# ============================================================
# HERBS — ROUND 2
# ============================================================
add("catnip", "herb", ["catmint", "nepeta cataria"], "Drives cats wild but makes a calming tea for humans — related to mint.", 78, 24)
add("curry leaf", "herb", ["curry leaves", "kadi patta", "murraya koenigii"], "Not curry powder — these fresh leaves explode with aroma when hit with hot oil.", 85, 108)
add("lemon balm", "herb", ["melissa officinalis", "bee balm herb"], "Medieval Europeans brewed 'balm wine' as a cure for all ailments.", 83, 23)
add("perilla herb", "herb", ["perilla leaves", "shiso herb", "egoma leaf"], "The same plant as Korean perilla — used in Japanese, Korean, and Vietnamese cuisine.", 84, 37)
add("roselle", "herb", ["roselles", "hibiscus sabdariffa", "sorrel herb"], "The calyx makes hibiscus tea — agua de jamaica, bissap, and karkade around the world.", 84, 49)
add("stevia leaf", "herb", ["stevia leaves", "sweet leaf"], "300x sweeter than sugar with zero calories — the Guarani people used it for 1,500 years.", 82, 0)
add("wild garlic", "herb", ["ramsons", "bear garlic", "allium ursinum"], "Carpets European forests in spring with a garlicky perfume.", 87, 34)
add("za'atar herb", "herb", ["biblical hyssop", "origanum syriacum", "wild thyme"], "The actual herb behind the za'atar spice blend — grows wild across the Levant.", 84, 27)

# ============================================================
# SPICES — ROUND 2
# ============================================================
add("ajwain", "spice", ["ajwain seeds", "carom seeds", "bishops weed"], "Tastes like concentrated thyme — Indians chew the seeds for stomach relief.", 82, 305)
add("baharat", "spice", ["baharat spice", "arabic spice blend"], "The 'seven spice' of the Arab world — every family has their own ratio.", 83, 290)
add("berbere", "spice", ["berbere spice", "ethiopian spice blend"], "Ethiopia's signature spice blend — up to 20 spices including rue and bishop's weed.", 84, 290)
add("black mustard seed", "spice", ["black mustard seeds", "rai"], "Pop them in hot oil for 'tadka' — the sizzling spice-infused oil that finishes Indian dishes.", 84, 508)
add("dried chili", "spice", ["dried chilies", "chile seco", "guajillo", "ancho", "pasilla", "arbol"], "Mexico has over 60 varieties of dried chilies — each with a unique flavor profile.", 83, 282)
add("dukkah", "spice", ["duqqa", "egyptian nut spice"], "An Egyptian blend of nuts, seeds, and spices — served with bread and olive oil.", 84, 480)
add("fennel pollen", "spice", ["wild fennel pollen"], "Called 'the spice of angels' by Italian chefs — collected by hand, one flower at a time.", 85, 345)
add("file powder", "spice", ["gumbo file", "sassafras powder"], "Dried sassafras leaves ground to powder — thickens and flavors Cajun gumbo.", 80, 0)
add("green cardamom", "spice", ["green cardamom pods", "elaichi", "cardamom pods"], "The third most expensive spice after saffron and vanilla.", 86, 311)
add("herb de provence", "spice", ["herbes de provence", "provence herbs"], "A Provencal blend of thyme, rosemary, and lavender — sunshine in a jar.", 83, 280)
add("korean chili paste", "spice", ["gochujang sauce"], "Fermented for months in earthen jars — the soul of Korean cooking.", 84, 100)
add("lemon pepper", "spice", ["lemon pepper seasoning"], "Lemon zest and cracked black pepper — simple but transforms grilled fish.", 80, 280)
add("mace", "spice", ["mace spice", "javitri"], "The lacy red covering around a nutmeg seed — same tree, different spice.", 82, 475)
add("mixed peppercorns", "spice", ["pepper blend", "four pepper blend"], "Black, white, green, and pink — four different flavors from different plants.", 84, 251)
add("old bay", "spice", ["old bay seasoning"], "The Chesapeake Bay's signature blend — no Maryland crab feast is complete without it.", 80, 280)
add("onion powder", "spice", ["onion powders", "dried onion"], "Concentrated onion flavor — one tablespoon equals a medium onion.", 78, 341)
add("garlic powder", "spice", ["garlic powders", "dried garlic"], "More mellow than fresh garlic — it dissolves evenly into rubs and sauces.", 78, 331)
add("pink himalayan salt", "spice", ["himalayan salt", "rock salt"], "The pink comes from iron oxide — mined from ancient sea beds in Pakistan.", 75, 0)
add("sel gris", "spice", ["grey salt", "celtic sea salt", "celtic salt"], "Harvested from clay-lined salt ponds in Brittany — grey from the minerals.", 78, 0)
add("fleur de sel", "spice", ["fleur de sels"], "The 'flower of salt' — delicate crystals skimmed from the surface of evaporating seawater.", 80, 0)
add("tajin", "spice", ["tajin seasoning", "chili lime salt"], "Mexico's beloved chili-lime salt — sprinkled on fruit, beer, and everything.", 82, 0)
add("togarashi", "spice", ["ichimi togarashi", "japanese chili"], "Single-chili Japanese pepper — the base of the seven-spice shichimi blend.", 82, 282)
add("turmeric powder", "spice", ["ground turmeric", "haldi powder"], "The golden spice that gives curry its color — India produces 80% of the world's supply.", 88, 354)
add("wasabi powder", "spice", ["real wasabi", "wasabi root"], "99% of wasabi served worldwide is actually horseradish and green dye.", 80, 292)
add("white sesame", "spice", ["white sesame seeds", "hulled sesame"], "The world's oldest oilseed crop — cultivated for over 5,000 years.", 85, 573)
add("yuzu kosho", "spice", ["yuzu pepper paste", "yuzukosho"], "A Japanese condiment of yuzu zest and chili — electrifying on grilled meat.", 84, 120)

# ============================================================
# FERMENTED — ROUND 2
# ============================================================
add("aged cheese", "fermented", ["cave aged cheese", "aged dairy"], "The older the cheese, the more complex — aging develops hundreds of flavor compounds.", 84, 380)
add("apple cider vinegar", "fermented", ["acv", "raw apple cider vinegar", "braggs"], "The 'mother' — that cloudy strand — is a colony of beneficial bacteria.", 85, 21)
add("balsamic vinegar", "fermented", ["traditional balsamic", "aceto balsamico", "modena balsamic"], "True 'Tradizionale' is aged 12-25 years and costs $150+ per tiny bottle.", 82, 88)
add("cider", "fermented", ["hard cider", "apple cider", "scrumpy"], "Before clean water was common, most Europeans drank cider daily — even children.", 78, 50)
add("doogh", "fermented", ["ayran", "tan", "abdug"], "A salty yogurt drink served ice-cold across the Middle East and Central Asia.", 82, 35)
add("fermented fish", "fermented", ["pla ra", "bagoong", "fesikh", "fermented seafood"], "Every coastal culture has one — from Scandinavian rakorret to Thai pla ra.", 78, 150)
add("idli", "fermented", ["idlis", "idly"], "Steamed fermented rice cakes — South India eats 60 billion of these a year.", 84, 39)
add("injera", "fermented", ["injeras", "ethiopian bread"], "Spongy, sour flatbread made from teff — it's both the plate and the utensil.", 84, 130)
add("jun tea", "fermented", ["honey kombucha"], "Like kombucha's refined cousin — fermented with green tea and raw honey.", 83, 30)
add("mead", "fermented", ["honey wine", "hydromel"], "Possibly humanity's oldest alcoholic drink — Norse gods drank it in Valhalla.", 75, 100)
add("natural wine", "fermented", ["orange wine", "skin contact wine", "pet nat"], "Fermented with wild yeast, no additives — winemaking the way it was done 8,000 years ago.", 75, 83)
add("sake", "fermented", ["nihonshu", "rice wine", "junmai"], "Not wine, not beer — it's in its own category, with koji mold converting starch to sugar.", 75, 134)
add("umeboshi", "fermented", ["pickled plum", "japanese pickled plum", "ume"], "So sour it makes your face pucker — one a day is a Japanese health tradition.", 82, 33)

# ============================================================
# FUNGI — ROUND 2
# ============================================================
add("agarikon", "fungi", ["agarikons", "laricifomes officinalis"], "An ancient medicinal mushroom — Dioscorides wrote about it 2,000 years ago.", 78, 22)
add("bear's head", "fungi", ["bear's head tooth", "hericium americanum"], "A lion's mane cousin with cascading white spines — equally delicious.", 85, 30)
add("blewit", "fungi", ["blewits", "wood blewit", "lepista nuda"], "A purple mushroom that smells like frozen orange juice — seriously.", 82, 30)
add("cauliflower mushroom", "fungi", ["cauliflower mushrooms", "sparassis"], "Looks exactly like a head of cauliflower growing at the base of a tree.", 84, 31)
add("fairy ring mushroom", "fungi", ["fairy ring mushrooms", "marasmius oreades"], "Grows in perfect circles in lawns — folklore says fairies danced there.", 82, 25)
add("hedgehog mushroom", "fungi", ["hedgehog mushrooms", "sweet tooth", "hydnum repandum"], "Has tiny spines instead of gills under the cap — impossible to confuse with anything toxic.", 86, 30)
add("honey mushroom", "fungi", ["honey mushrooms", "armillaria"], "The largest living organism on earth is a honey mushroom colony spanning 2,385 acres.", 80, 30)
add("maitake", "fungi", ["maitakes", "hen of the woods", "dancing mushroom"], "Japanese foragers reportedly danced with joy when they found one — hence 'dancing mushroom'.", 88, 31)
add("matsutake", "fungi", ["matsutakes", "pine mushroom"], "Japan's most prized mushroom — a single specimen can sell for $1,000.", 85, 28)
add("morel", "fungi", ["morels", "morchella"], "Cannot be commercially farmed at scale — every morel is essentially wild-foraged.", 88, 31)
add("oyster mushroom", "fungi", ["oyster mushrooms", "pleurotus ostreatus", "hiratake"], "Can be grown on coffee grounds, straw, or even old books.", 87, 33)
add("porcini", "fungi", ["porcinis", "boletus edulis", "cep", "penny bun", "steinpilz"], "The king of Italian mushrooms — dried porcini add depth to risotto like nothing else.", 88, 26)
add("russula", "fungi", ["russulas", "brittlegill"], "The most common woodland mushroom — crack one and it snaps like chalk.", 78, 25)
add("shiitake", "fungi", ["shiitakes", "lentinula edodes", "shiang gu", "donko"], "The second most cultivated mushroom worldwide — revered in Asian medicine for millennia.", 88, 34)
add("straw mushroom", "fungi", ["straw mushrooms", "volvariella"], "Grown on rice straw — the mushroom in canned Chinese soups worldwide.", 80, 32)
add("velvet shank", "fungi", ["velvet shanks", "enokitake", "wild enoki"], "Wild enoki look nothing like the thin white cultivated ones — they're golden-brown with velvet stems.", 83, 29)
add("wood ear", "fungi", ["wood ears", "cloud ear fungus", "mu er", "kikurage"], "Prized entirely for its crunchy-chewy texture rather than flavor.", 82, 25)

# ============================================================
# SEAWEED — ROUND 2
# ============================================================
add("bladder wrack", "seaweed", ["bladderwrack", "fucus vesiculosus"], "One of the richest natural sources of iodine — used medicinally for thyroid health.", 80, 43)
add("carrageen moss", "seaweed", ["irish moss", "chondrus crispus", "sea moss"], "The original 'sea moss' — Irish used it as a famine food during the Great Hunger.", 82, 49)
add("dabberlocks", "seaweed", ["alaria esculenta", "atlantic wakame", "winged kelp"], "The Atlantic cousin of Japanese wakame — harvested wild from Scottish shores.", 82, 45)
add("gutweed", "seaweed", ["ulva intestinalis", "grass kelp"], "Hollow tubes of bright green seaweed — dried and eaten as a snack in Korea.", 80, 35)
add("ogonori", "seaweed", ["gracilaria"], "Used to make agar — the plant-based gelatin used in labs and kitchens worldwide.", 80, 26)
add("tosaka", "seaweed", ["tosaka nori", "red tosaka", "green tosaka"], "Delicate, ruffled seaweed used as a colorful garnish in Japanese sashimi platters.", 82, 30)
add("sea lettuce", "seaweed", ["ulva lactuca", "green laver"], "Thin, bright green sheets that taste like the sea — eaten raw in salads.", 84, 35)

# ============================================================
# OILS — ROUND 2
# ============================================================
add("brazil nut oil", "oil", ["brazil nut oils"], "Rich in selenium — just a few drops provide your daily requirement.", 82, 884)
add("camellia oil", "oil", ["tea seed oil", "tsubaki oil"], "The traditional cooking oil of southern China and Japan — pressed from tea plant seeds.", 82, 884)
add("hemp oil", "oil", ["hemp seed oil", "cannabis sativa oil"], "The ideal 3:1 ratio of omega-6 to omega-3 fatty acids.", 85, 884)
add("marula oil", "oil", ["marula oils"], "Pressed from the fruit that allegedly makes elephants drunk (a myth, but fun).", 80, 884)
add("pistachio oil", "oil", ["pistachio oils"], "Vivid green with an intense nutty aroma — a chef's secret finishing oil.", 84, 884)
add("rice bran oil", "oil", ["rice bran oils"], "Extracted from the bran layer — Japan's preferred deep-frying oil for tempura.", 80, 884)
add("sacha inchi oil", "oil", ["inca oil"], "One of the highest plant sources of omega-3 fatty acids.", 87, 884)
add("perilla oil", "oil", ["deulggireum", "egoma oil"], "Korea's traditional finishing oil — drizzled on rice and vegetables for nutty richness.", 84, 884)

# ============================================================
# SWEETENERS — ROUND 2
# ============================================================
add("bee pollen", "sweetener", ["bee pollens"], "Contains nearly all nutrients humans need — used by athletes as a natural supplement.", 85, 250)
add("cane juice", "sweetener", ["sugarcane juice", "fresh cane juice", "guarapo"], "The unrefined juice pressed straight from sugarcane stalks — a street drink across the tropics.", 78, 269)
add("coconut sugar", "sweetener", ["coconut palm sugar", "gula kelapa"], "Made from coconut blossom sap — has a deep caramel flavor like brown sugar.", 80, 375)
add("maple sugar", "sweetener", ["maple sugars", "maple candy"], "Maple syrup boiled further until it crystallizes — used by Native Americans before Europeans arrived.", 82, 354)
add("mesquite powder", "sweetener", ["mesquite meal", "mesquite flour"], "Ground mesquite pods — a Native American sweetener that tastes like molasses and chocolate.", 82, 360)
add("pomegranate molasses", "sweetener", ["pomegranate syrup", "dibs rumman"], "Reduced pomegranate juice — the sweet-sour drizzle of Lebanese and Turkish cooking.", 82, 220)
add("sugar cane", "sweetener", ["sugarcane", "raw sugar cane"], "You chew the stalk and spit out the fiber — the original candy for tropical kids.", 75, 269)

# ============================================================
# EGGS — ROUND 2
# ============================================================
add("balut", "egg", ["baluts", "balot"], "A fertilized duck egg with a partially developed embryo — a Filipino street food icon.", 75, 188)
add("century egg", "egg", ["century eggs", "thousand year egg", "pidan", "preserved egg"], "Preserved in clay and ash for weeks, not centuries — the green-black color is from chemistry.", 78, 171)
add("emu egg", "egg", ["emu eggs"], "One emu egg equals about 10 chicken eggs — the dark green shell is strikingly beautiful.", 84, 134)
add("goose egg", "egg", ["goose eggs"], "Richer and larger than chicken eggs — one goose egg makes an omelette.", 85, 185)
add("pheasant egg", "egg", ["pheasant eggs"], "Smaller than chicken eggs with an olive-colored shell and richer yolk.", 84, 160)

# ============================================================
# BEVERAGES — ROUND 2
# ============================================================
add("agua fresca", "beverage", ["aguas frescas", "fruit water"], "Mexican fruit-infused water — tamarind, jamaica, horchata, or melon.", 82, 40)
add("amazake", "beverage", ["sweet sake", "rice amazake"], "A thick, sweet Japanese rice drink — fermented but typically non-alcoholic.", 80, 81)
add("ayran", "beverage", ["ayrans", "doogh", "tan"], "A salty yogurt drink served ice-cold — Turkey's national beverage.", 82, 35)
add("buttermilk drink", "beverage", ["chaas", "majjiga", "mattha"], "Indian spiced buttermilk — served with cumin and curry leaves after a heavy meal.", 83, 40)
add("chai", "beverage", ["masala chai", "spiced tea", "chai tea"], "Black tea boiled with milk and spices — 'chai tea' is redundant since 'chai' means tea.", 84, 70)
add("cold brew coffee", "beverage", ["cold brew", "cold brewed coffee"], "Steeped for 12-24 hours in cold water — 67% less acidic than hot coffee.", 82, 2)
add("fresh juice", "beverage", ["cold pressed juice", "raw juice", "fresh squeezed"], "No pasteurization, no preservatives — living enzymes intact.", 85, 45)
add("guava juice", "beverage", ["guava nectar", "guava drink"], "Popular across the Caribbean and South America — pink guava juice is the most prized.", 82, 68)
add("hemp milk", "beverage", ["hemp milks", "hemp seed milk"], "Made from hemp seeds blended with water — earthy, nutty, and omega-3 rich.", 82, 46)
add("hibiscus tea", "beverage", ["agua de jamaica", "bissap", "karkade", "sorrel drink"], "The deep crimson drink known by different names in every country that loves it.", 85, 37)
add("iced tea", "beverage", ["sweet tea", "unsweetened iced tea", "sun tea"], "Southern sweet tea uses about a cup of sugar per gallon — it's basically dessert.", 78, 33)
add("kvass", "beverage", ["bread kvass", "fermented bread drink"], "A mildly alcoholic Slavic drink made from fermented rye bread.", 80, 27)
add("lemon water", "beverage", ["warm lemon water", "lemon infused water"], "The simplest morning ritual — just lemon and water, but people swear by it.", 82, 4)
add("mango juice", "beverage", ["mango nectar", "mango drink", "aam ras"], "India's Alphonso mango pulp (aam ras) is served as a drink and dessert.", 82, 60)
add("masala chai", "beverage", ["indian tea", "spiced milk tea"], "Every Indian household has their own ratio of ginger, cardamom, and cinnamon.", 84, 72)
add("passion fruit juice", "beverage", ["maracuya juice", "passion fruit drink"], "So intensely flavored that it's almost always diluted — a tropical concentrate.", 84, 48)
add("smoothie", "beverage", ["green smoothie", "fruit smoothie", "protein smoothie"], "Whole fruit blended (not juiced) — keeps all the fiber.", 82, 80)
add("tamarind juice", "beverage", ["tamarind drink", "tamarindo"], "Sweet, sour, and refreshing — a street drink across Mexico, India, and Thailand.", 82, 56)
add("watermelon juice", "beverage", ["watermelon water", "sandia juice"], "92% water by weight — nature's most hydrating fruit pressed into a drink.", 84, 30)

# ============================================================
# Write
# ============================================================
all_foods = existing_foods + new_items
all_foods.sort(key=lambda x: (x["category"], x["name"]))

with open(FOODS_PATH, "w") as f:
    json.dump(all_foods, f, indent=2, ensure_ascii=False)

print(f"Previous: {len(existing_foods)} items")
print(f"New items added: {len(new_items)}")
print(f"Total: {len(all_foods)} items")

from collections import Counter
cats = Counter(item["category"] for item in all_foods)
print("\nCategory breakdown:")
for cat, count in cats.most_common():
    print(f"  {cat}: {count}")
