#!/usr/bin/env python3
"""Add commonly-searched combo/prepared items to both foods and trash."""

import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FOODS_PATH = os.path.join(SCRIPT_DIR, "..", "src", "data", "foods.json")
TRASH_PATH = os.path.join(SCRIPT_DIR, "..", "src", "data", "trash.json")

with open(FOODS_PATH) as f:
    foods = json.load(f)
with open(TRASH_PATH) as f:
    trash = json.load(f)

food_names = {item["name"].lower() for item in foods}
trash_names = {item["name"].lower() for item in trash}
all_names = food_names | trash_names

new_foods = []
new_trash = []

def add_food(name, category, aliases, fun_fact, score, calories):
    if name.lower() in all_names:
        return
    all_names.add(name.lower())
    new_foods.append({
        "name": name, "category": category, "aliases": aliases,
        "fun_fact": fun_fact, "score": score, "calories": calories
    })

def add_trash(name, category, aliases, reason, score, calories):
    if name.lower() in all_names:
        return
    all_names.add(name.lower())
    new_trash.append({
        "name": name, "category": category, "aliases": aliases,
        "reason": reason, "score": score, "calories": calories
    })

# ============================================================
# FOOD — Traditional whole-food preparations people will search
# ============================================================
add_food("steak", "meat", ["steaks", "beef steak", "grilled steak"], "A properly rested steak redistributes juices — cutting too early loses 40% of the moisture.", 85, 271)
add_food("sushi", "fermented", ["sushi roll", "nigiri", "maki", "sashimi plate"], "Originally a fermentation method — fish was packed in rice for months. Modern sushi is a shortcut.", 85, 150)
add_food("bone broth soup", "beverage", ["broth", "stock", "beef broth", "chicken stock"], "Real broth gels when cold — that's the collagen. If it stays liquid, it wasn't simmered long enough.", 88, 31)
add_food("stew", "meat", ["beef stew", "lamb stew", "irish stew", "meat stew"], "Low and slow cooking breaks down tough cuts into fork-tender perfection.", 82, 150)
add_food("curry", "spice", ["curries", "chicken curry", "lamb curry", "thai curry", "indian curry"], "The word 'curry' is a British colonial invention — no single Indian dish is called that.", 82, 200)
add_food("roast chicken", "poultry", ["roasted chicken", "whole roast chicken", "rotisserie"], "Thomas Keller's famous recipe: salt the bird, put it in a hot oven. That's it.", 86, 190)
add_food("scrambled eggs", "egg", ["scrambled egg"], "Gordon Ramsay's soft scrambled eggs take 10 minutes of patient stirring on low heat.", 88, 149)
add_food("omelette", "egg", ["omelet", "french omelette", "frittata"], "A French omelette should have zero color — golden means you've overcooked it.", 87, 154)
add_food("boiled egg", "egg", ["hard boiled egg", "soft boiled egg", "poached egg", "boiled eggs"], "The green ring around an overcooked yolk is iron sulfide — harmless but a sign of overcooking.", 90, 155)
add_food("fried egg", "egg", ["fried eggs", "sunny side up", "over easy", "over hard"], "Baste the top with hot butter for a perfect sunny-side-up with set whites.", 85, 196)
add_food("guacamole", "fruit", ["guac"], "The Aztec word 'ahuacamolli' means 'avocado sauce' — they invented it.", 88, 160)
add_food("hummus", "legume", ["hommus", "houmous", "chickpea dip"], "A 7,000-year-old recipe — the perfect hummus ratio is debated across the entire Middle East.", 86, 166)
add_food("salsa", "vegetable", ["pico de gallo", "salsa fresca", "salsa verde", "fresh salsa"], "Pico de gallo means 'rooster's beak' — nobody knows why.", 88, 36)
add_food("kimchi", "fermented", ["kimchee", "gimchi", "korean pickled vegetables"], "Korea's national dish — there are over 200 varieties, not just cabbage.", 90, 15)
add_food("salad", "vegetable", ["green salad", "mixed salad", "garden salad", "side salad"], "The word comes from Latin 'sal' (salt) — Romans dressed greens with nothing but salt.", 88, 20)
add_food("coleslaw", "vegetable", ["slaw", "cabbage slaw"], "The Dutch 'koolsla' (cabbage salad) — only trash when made with mayo from seed oils.", 78, 82)
add_food("grilled fish", "fish", ["grilled salmon", "grilled trout", "bbq fish"], "The simplest preparation for the best fish — heat, salt, and time.", 88, 150)
add_food("ceviche", "fish", ["cebiche", "seviche"], "Not technically 'cooked' — citric acid denatures the proteins just like heat does.", 87, 120)
add_food("smoked salmon", "fish", ["lox", "gravlax", "cold smoked salmon", "nova"], "Gravlax means 'buried salmon' — Vikings literally buried it in sand to cure it.", 86, 117)
add_food("sardines in olive oil", "fish", ["tinned sardines", "canned sardines", "sardine tin"], "Vintage sardine tins are aged like wine — some sell for over $50 a tin.", 90, 208)
add_food("beef jerky", "meat", ["jerky", "biltong", "dried meat"], "Real jerky is just meat, salt, and smoke. Check the label — most commercial jerky adds sugar and seed oils.", 78, 116)
add_food("pulled pork", "meat", ["slow cooked pork", "bbq pork", "carnitas"], "Low and slow for 12+ hours until it falls apart with a fork.", 80, 210)
add_food("meatballs", "meat", ["meat balls", "polpette", "kottbullar", "kofte"], "Every culture has their own — Swedish, Italian, Turkish, and dozens more.", 80, 250)
add_food("liver pate", "meat", ["pate", "chicken liver pate", "liverwurst spread"], "Nutrient-dense organ meat made delicious — nature's multivitamin in spreadable form.", 84, 319)
add_food("tacos", "meat", ["taco", "street tacos", "fish tacos", "carne asada taco"], "A corn tortilla, meat, onion, and cilantro. That's a real taco. Everything else is extra.", 82, 226)
add_food("burrito bowl", "grain", ["burrito bowls", "chipotle bowl"], "Skip the tortilla and you've got rice, beans, meat, and salsa — all whole foods.", 80, 500)
add_food("rice and beans", "grain", ["rice and bean", "gallo pinto", "moros y cristianos"], "A complete protein when combined — the peasant dish that fed civilizations.", 86, 200)
add_food("congee", "grain", ["jook", "rice porridge", "kanji", "cháo"], "Rice cooked in 10x water until it's silk — Asian comfort food for 3,000 years.", 82, 46)
add_food("porridge", "grain", ["oatmeal porridge", "hot oats", "overnight oats"], "Scottish law once made it illegal to make porridge with anything other than oats, water, and salt.", 86, 71)
add_food("risotto", "grain", ["risottos", "mushroom risotto"], "The secret is patience — each ladle of stock must be absorbed before adding the next.", 80, 170)
add_food("fried rice", "grain", ["egg fried rice", "chinese fried rice", "nasi goreng"], "Day-old rice fries best — fresh rice is too moist and gets mushy.", 78, 163)
add_food("miso soup", "fermented", ["miso shiru"], "Drunk at breakfast in Japan for centuries — a probiotic way to start the day.", 88, 40)
add_food("borscht", "vegetable", ["borsch", "beet soup", "beetroot soup"], "Ukraine's national dish — there are over 30 regional variations.", 84, 50)
add_food("minestrone", "vegetable", ["minestrone soup"], "Italian for 'big soup' — a peasant dish that uses whatever vegetables are in season.", 84, 80)
add_food("pho", "meat", ["pho bo", "pho ga", "vietnamese soup"], "Simmered for 24 hours — the broth is the star, not the noodles.", 82, 215)
add_food("ratatouille", "vegetable", ["ratatouilles"], "A Provencal stew of summer vegetables — the Pixar movie made it world-famous.", 86, 55)
add_food("chili", "legume", ["chili con carne", "chilli", "texas chili", "bean chili"], "In Texas, real chili has no beans and no tomatoes — just meat and chilies.", 80, 200)
add_food("dal", "legume", ["dhal", "daal", "lentil curry", "tarka dal"], "India's daily comfort food — there are as many dal recipes as there are Indian households.", 86, 120)
add_food("falafel", "legume", ["falafels"], "Deep-fried chickpea balls — Egypt and Israel both claim to have invented them.", 82, 333)
add_food("roasted vegetables", "vegetable", ["roast vegetables", "roasted veggies", "sheet pan vegetables"], "High heat caramelizes the natural sugars — the Maillard reaction makes everything better.", 88, 80)
add_food("grilled vegetables", "vegetable", ["grilled veggies", "charred vegetables"], "Char adds smoky complexity — zucchini, peppers, and eggplant are the holy trinity.", 88, 50)
add_food("mashed potato", "vegetable", ["mashed potatoes", "mash", "potato puree"], "Joel Robuchon's famous recipe uses equal parts butter and potato. Yes, really.", 78, 115)
add_food("baked potato", "vegetable", ["jacket potato", "baked potatoes"], "A potato baked in its skin — top with butter and you've got a complete meal.", 82, 93)
add_food("sweet potato fries", "vegetable", ["sweet potato chips", "baked sweet potato fries"], "Only food if baked or fried in good fat — most restaurants deep-fry them in seed oil.", 75, 150)
add_food("sauerkraut", "fermented", ["raw sauerkraut", "homemade sauerkraut", "fermented cabbage"], "Real sauerkraut is alive with probiotics — the pasteurized stuff on hot dogs is dead.", 90, 19)
add_food("sourdough bread", "grain", ["real sourdough", "naturally leavened bread"], "The long fermentation breaks down gluten and phytic acid — easier to digest than commercial bread.", 82, 240)
add_food("butter on toast", "dairy", ["buttered toast", "toast with butter"], "Simple, satisfying, and whole-food based — if the bread is real sourdough.", 78, 250)
add_food("cheese board", "dairy", ["charcuterie board", "cheese platter"], "Whole food cheeses, cured meats, nuts, and fruit — the original grazing plate.", 82, 350)
add_food("yogurt bowl", "dairy", ["yogurt parfait", "greek yogurt bowl"], "Full-fat yogurt with fruit and nuts — only trash if it's low-fat with added sugar.", 85, 200)
add_food("acai bowl", "fruit", ["acai bowls", "acai smoothie bowl"], "Frozen acai blended thick, topped with fruit and granola — a Brazilian beach staple.", 80, 300)
add_food("fruit salad", "fruit", ["fruit salads", "mixed fruit", "fruit bowl"], "Nature's dessert — no sugar needed when the fruit is ripe.", 90, 60)
add_food("trail mix", "nut", ["trail mixes", "nut mix", "gorp"], "Nuts, seeds, and dried fruit — the original energy bar, minus the wrapper.", 82, 462)
add_food("peanut butter", "nut", ["natural peanut butter", "pb", "groundnut paste"], "Real peanut butter is just peanuts and salt. If the label lists anything else, it's not real.", 85, 588)
add_food("almond butter", "nut", ["almond butters"], "Almonds ground into paste — that's it. Check labels: most add seed oils.", 85, 614)
add_food("tahini dressing", "seed", ["tahini sauce", "tahini dip"], "Sesame paste thinned with lemon and garlic — the sauce that ties a falafel plate together.", 84, 300)
add_food("olive tapenade", "oil", ["tapenade", "olive spread", "olive dip"], "Crushed olives, capers, and olive oil — a Provencal condiment older than France.", 84, 300)
add_food("pickled vegetables", "fermented", ["pickled vegs", "quick pickles", "lacto fermented veggies"], "Naturally fermented pickles are full of probiotics — vinegar pickles are just sour.", 85, 20)
add_food("coconut cream", "fruit", ["coconut creams", "thick coconut milk"], "The thick layer that rises to the top of coconut milk — pure coconut fat.", 82, 330)
add_food("dried fruit", "fruit", ["dried fruits", "dehydrated fruit", "sun dried fruit"], "Concentrated fruit sugar and nutrients — eat them sparingly, they're calorie-dense.", 78, 240)
add_food("beef bone broth", "meat", ["bone broth", "beef stock", "beef bone stock"], "24-hour simmered beef bones — rich in collagen, glycine, and minerals.", 88, 31)

# ============================================================
# TRASH — Processed combo items people will search for
# ============================================================
add_trash("hamburger", "ultra-processed", ["hamburgers", "big mac", "quarter pounder", "whopper", "cheeseburger", "fast food burger"], "The bun is refined flour, the patty is factory-farmed, the sauce is seed oil. The whole package is engineered to override your satiety signals.", 15, 354)
add_trash("pizza", "ultra-processed", ["pizzas", "delivery pizza", "dominos", "papa johns", "pizza hut"], "Commercial pizza dough is refined flour, the cheese is processed, and the sauce often contains added sugar and seed oils.", 15, 266)
add_trash("spaghetti bolognese", "ultra-processed", ["spag bol", "spaghetti bolognaise", "pasta bolognese", "meat sauce pasta"], "Store-bought pasta is refined wheat stripped of nutrients. The jarred sauce is loaded with sugar, seed oils, and preservatives.", 20, 220)
add_trash("mac and cheese", "ultra-processed", ["macaroni and cheese", "mac n cheese", "kraft mac and cheese", "kraft dinner"], "Refined pasta + processed cheese powder + seed oils. The orange color comes from annatto and chemicals, not real cheese.", 10, 310)
add_trash("fish and chips", "ultra-processed", ["fish n chips", "battered fish", "fish & chips"], "The batter is refined flour, deep-fried in industrial seed oil. The chips too. All the omega-3 benefits of the fish are cancelled out.", 20, 450)
add_trash("fried chicken", "ultra-processed", ["kfc", "popeyes", "fried chicken sandwich", "crispy chicken"], "Coated in refined flour and deep-fried in seed oil at industrial scale. The chicken itself is fine — it's everything around it.", 15, 320)
add_trash("chicken sandwich", "ultra-processed", ["chick fil a", "mcchicken", "chicken burger"], "Processed bun, breaded chicken fried in seed oil, mayo made from soybean oil. A whole-food ingredient buried under processing.", 15, 400)
add_trash("fish sticks", "ultra-processed", ["fish fingers", "frozen fish sticks", "fish stick"], "Mystery fish coated in refined breadcrumbs and pre-fried in seed oil. The fish is the least of the ingredients.", 15, 220)
add_trash("chicken tenders", "ultra-processed", ["chicken strips", "chicken fingers", "dino nuggets"], "Mechanically separated chicken, breaded with refined flour, fried in seed oil. Not the same as actual chicken.", 15, 271)
add_trash("mcdonalds", "ultra-processed", ["mcdonald's", "maccas", "mickey d's"], "A masterclass in food engineering — every item is designed in a lab to be hyper-palatable and override your body's stop signals.", 5, 500)
add_trash("burger king", "ultra-processed", ["bk", "whopper meal"], "Flame-grilled sounds healthy until you read the ingredient list — the buns alone contain over 20 ingredients.", 10, 500)
add_trash("wendys", "ultra-processed", ["wendy's", "baconator", "frosty"], "Fresh, never frozen beef — cooked in seed oil and served on a refined flour bun.", 10, 500)
add_trash("subway", "ultra-processed", ["subway sandwich", "sub sandwich"], "Their 'fresh bread' contains over 40 ingredients. A real loaf needs 4.", 10, 400)
add_trash("taco bell", "ultra-processed", ["taco bell burrito", "crunchwrap"], "A taco in name only — the 'beef' is 36% beef, the rest is fillers, flavoring, and seed oils.", 5, 450)
add_trash("ramen noodles", "ultra-processed", ["cup noodles", "cup ramen", "maruchan", "nissin"], "Pre-fried in palm oil, the seasoning packet is mostly salt and MSG. Real ramen takes 12+ hours.", 10, 380)
add_trash("microwave meal", "ultra-processed", ["tv dinner", "frozen dinner", "lean cuisine", "hungry man", "ready meal"], "Designed to survive months in a freezer — that shelf stability comes from industrial processing.", 10, 350)
add_trash("granola bar", "ultra-processed", ["granola bars", "nature valley", "kind bar", "cliff bar"], "Sugar, seed oils, and 'natural flavors' held together with corn syrup. A candy bar in a hiking wrapper.", 15, 200)
add_trash("breakfast sandwich", "ultra-processed", ["egg mcmuffin", "sausage mcmuffin", "mcgriddle"], "Real eggs on a refined English muffin with processed cheese and factory pork — the whole being worse than its parts.", 15, 300)
add_trash("pancakes", "ultra-processed", ["pancake", "flapjacks", "pancake mix", "aunt jemima"], "Refined flour, sugar, and seed oil — then drowned in corn syrup marketed as 'maple'. Real pancakes need none of this.", 15, 227)
add_trash("waffles", "ultra-processed", ["waffle", "eggo waffles", "frozen waffles"], "The frozen kind: refined flour, sugar, seed oils, and enough preservatives to last months in your freezer.", 15, 310)
add_trash("croissant", "ultra-processed", ["croissants"], "A real French croissant uses only butter. Commercial ones replace it with margarine and seed oils to cut costs.", 20, 406)
add_trash("bagel", "ultra-processed", ["bagels", "everything bagel"], "Dense refined wheat — one bagel has the same carbs as 4 slices of bread. And that's before the cream cheese.", 20, 270)
add_trash("white bread", "ultra-processed", ["sliced bread", "sandwich bread", "wonder bread", "toast bread"], "Refined flour stripped of all nutrients, then 'enriched' by adding synthetic vitamins back. A factory product.", 10, 265)
add_trash("tortilla chips", "ultra-processed", ["nacho chips", "nachos", "corn chips"], "Corn ground, fried in seed oil, and salted. Real nachos don't come from a bag.", 15, 489)
add_trash("potato chips", "ultra-processed", ["crisps", "kettle chips", "baked chips"], "Sliced, fried in seed oil, and engineered for 'bet you can't eat just one'. That's not a challenge, it's a design spec.", 10, 536)
add_trash("chocolate bar", "ultra-processed", ["candy bar", "milk chocolate", "hersheys", "cadbury"], "Sugar, milk powder, and cocoa butter — modern chocolate bars are mostly sugar with a hint of cacao.", 10, 535)
add_trash("ice cream", "ultra-processed", ["haagen dazs", "ben and jerrys", "gelato", "soft serve"], "Commercial ice cream: sugar, cream, corn syrup, guar gum, carrageenan, 'natural flavors'. Real ice cream needs 3 ingredients.", 20, 207)
add_trash("donuts", "ultra-processed", ["donut", "doughnut", "krispy kreme", "dunkin donuts"], "Refined flour deep-fried in seed oil and coated in sugar. A triple threat of processed ingredients.", 5, 452)
add_trash("muffin", "ultra-processed", ["muffins", "blueberry muffin", "chocolate muffin"], "A cupcake pretending to be breakfast — most muffins have more sugar than a candy bar.", 15, 426)
add_trash("cake", "ultra-processed", ["birthday cake", "chocolate cake", "layer cake", "sheet cake"], "Refined flour, sugar, seed oils, artificial colors and flavors — assembled into something your grandmother wouldn't recognize.", 10, 350)
add_trash("cookies", "ultra-processed", ["cookie", "chocolate chip cookies", "oreo cookies", "biscuits"], "Refined flour + sugar + seed oils = the unholy trinity of ultra-processed baking.", 10, 488)
add_trash("brownie", "ultra-processed", ["brownies", "chocolate brownies"], "Sugar, refined flour, and cheap chocolate — the boxed mix kind has ingredients you can't pronounce.", 15, 466)
add_trash("cereal bar", "ultra-processed", ["breakfast bar", "nutri-grain bar", "fiber one bar"], "Marketed as healthy — check the label: it's a cookie with added fiber and a health claim.", 10, 200)
add_trash("sports drink", "ultra-processed", ["powerade", "body armor", "prime hydration"], "Water, sugar, artificial colors, and electrolytes you could get from a banana and a pinch of salt.", 10, 80)
add_trash("diet soda", "ultra-processed", ["diet coke", "coke zero", "diet pepsi", "zero sugar soda"], "No calories, but artificial sweeteners trick your brain and may disrupt gut bacteria.", 10, 0)
add_trash("energy drink", "ultra-processed", ["bang energy", "celsius", "reign", "ghost energy"], "Caffeine, taurine, artificial sweeteners, and synthetic B-vitamins. Just drink coffee.", 10, 120)
add_trash("fruit juice", "ultra-processed", ["tropicana", "minute maid", "simply orange", "ocean spray"], "Fiber removed, pasteurized dead, often from concentrate with added sugar. Eat the whole fruit instead.", 15, 112)
add_trash("flavored yogurt", "ultra-processed", ["strawberry yogurt", "vanilla yogurt", "yoplait", "dannon"], "More sugar per cup than a candy bar — the fruit is usually just jam and the yogurt is low-fat.", 15, 100)
add_trash("protein shake", "ultra-processed", ["whey shake", "muscle milk", "ensure", "boost"], "Isolated protein powder + artificial sweeteners + seed oil emulsifiers. Eat real food.", 15, 230)
add_trash("meal replacement", "ultra-processed", ["soylent", "huel", "slim fast", "meal replacement shake"], "Science fiction food — synthetic nutrients suspended in seed oil and maltodextrin. Humans aren't machines.", 5, 400)
add_trash("vegan cheese", "ultra-processed", ["plant based cheese", "dairy free cheese", "cashew cheese"], "Starch, seed oils, coconut oil, and 'natural flavors' — trying very hard to be something it's not.", 10, 250)
add_trash("beyond meat", "ultra-processed", ["beyond burger", "plant based meat", "fake meat"], "Pea protein isolate, canola oil, methylcellulose, and 20+ ingredients. Plants don't naturally form burgers.", 10, 230)
add_trash("sausage roll", "ultra-processed", ["sausage rolls"], "Mystery meat in refined pastry — the British gas station staple.", 15, 340)
add_trash("corn syrup", "ultra-processed", ["high fructose corn syrup", "hfcs", "glucose-fructose syrup"], "Invented in 1957. Obesity epidemic started in the 1970s when it replaced sugar in everything. Coincidence?", 5, 281)
add_trash("white sugar", "ultra-processed", ["table sugar", "refined sugar", "granulated sugar", "sucrose"], "Sugarcane stripped of every mineral and vitamin until pure sucrose remains — empty calories by design.", 10, 387)
add_trash("powdered sugar", "ultra-processed", ["confectioners sugar", "icing sugar"], "Refined sugar ground even finer with added cornstarch — processing on top of processing.", 5, 389)
add_trash("agave nectar", "ultra-processed", ["agave syrup"], "Marketed as 'natural' but processed like high fructose corn syrup — up to 90% fructose.", 10, 310)
add_trash("ketchup", "ultra-processed", ["catsup", "tomato ketchup", "heinz ketchup"], "More sugar per tablespoon than ice cream. Tomato-flavored candy sauce.", 15, 112)
add_trash("bbq sauce", "ultra-processed", ["barbecue sauce", "sweet baby rays"], "Check the first ingredient — it's almost always high fructose corn syrup, not tomatoes.", 15, 172)
add_trash("teriyaki sauce", "ultra-processed", ["store bought teriyaki", "teriyaki glaze"], "Real teriyaki is soy, mirin, and sake. Bottled versions add corn syrup, seed oils, and caramel color.", 15, 89)
add_trash("salad dressing", "ultra-processed", ["bottled dressing", "thousand island", "italian dressing", "caesar dressing"], "Seed oil, sugar, and emulsifiers in a bottle — just use olive oil and vinegar.", 10, 200)
add_trash("soy milk", "ultra-processed", ["soymilk", "silk soy"], "Processed soybeans, added sugar, seed oil emulsifiers, and synthetic vitamins. A far cry from traditional tofu.", 15, 54)
add_trash("coffee drink", "ultra-processed", ["starbucks frappuccino", "bottled coffee", "mocha latte"], "Coffee buried under sugar, cream substitutes, and seed oil derivatives — a dessert pretending to be a drink.", 10, 250)
add_trash("wrap", "ultra-processed", ["wraps", "flour tortilla wrap", "spinach wrap"], "A refined flour tortilla with green food coloring doesn't make it healthy — it's just a flat piece of white bread.", 15, 300)
add_trash("breadsticks", "ultra-processed", ["breadstick", "garlic bread", "texas toast"], "Refined flour sticks brushed with seed oil and garlic powder. Real garlic bread uses butter.", 15, 300)
add_trash("trail mix", "ultra-processed", ["commercial trail mix", "planters trail mix"], "Sounds healthy until you read the label — candy, seed-oil roasted nuts, and added sugar.", 15, 462)

# ============================================================
# Write both files
# ============================================================
all_foods = foods + new_foods
all_foods.sort(key=lambda x: (x["category"], x["name"]))

all_trash = trash + new_trash
all_trash.sort(key=lambda x: (x["category"], x["name"]))

with open(FOODS_PATH, "w") as f:
    json.dump(all_foods, f, indent=2, ensure_ascii=False)

with open(TRASH_PATH, "w") as f:
    json.dump(all_trash, f, indent=2, ensure_ascii=False)

print(f"Foods: {len(foods)} → {len(all_foods)} (+{len(new_foods)})")
print(f"Trash: {len(trash)} → {len(all_trash)} (+{len(new_trash)})")
print(f"Combined total: {len(all_foods) + len(all_trash)}")
