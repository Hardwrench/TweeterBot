import random

#articles of speech


opener = ["Fun Fact:","Fun Fact!", "Did you know", "Hey Y'all!", "Yo guys,", "Tip of the Day:", "Hey all you people!", "Hey all you sheeple",
"PEOPLE OF TWITTER:", "TIL", "Here's a new one:", "Morning Sunshine,",
"My father once told me,", "My grandmother once told me:", "My grandson once told me:", "My mother once told me:", "My sister once told me:",
"My estranged brother once told me:", "My penpal from Bangledesh once told me:", "Auntie always told me,", "My dog once farted and it sounded like it said:",
"Leading scientists agree that","1 doctor once wrote", "A wise man once said", "I heard whispered on the wind that", "I read in a book once", "Survey Says:",
"Harry Potter taught me that", "I learnt from Twilight that", "In vietnam, they told me", "While traveling abroad I was told", "My senpai taught me",
"A wise monk at the top of Mont. Fuji once told me", "The old lady on public transit once said to me", "While backstage the lead singer revealed",
"Confucius says:" ]

verb = ["eating", "swallowing", "consuming", "doing", "playing with", "having sex with", "petting", "rockin' out to", "cooking", "tasting a little",
        "firmly grasping", "poking", "watering", "tickling", "obessively checking", "stalking", "fondling", "listening to", "painting", "using", "driving", "combing",
        "going to church with", "cutting", "slicing", "baking", "looking at", "researching", "writing", "reading", "hanging out with", "calling", "brushing",
        "masterbating to", "masterbating on", "putting on", "smooching", "mooching off of", "talking with a 50's accent to", "going to prison with", "going to the mall with",
        "seeing your mom and dad checking out", "burning", "shouting out to", "yelling at", "jumping", "running", "walking", "swimming in", "defrosting", "drinking",
        "hammering", "giving", "making", "creating", "texting", "tweeting", "setting on fire", "burping out", "taking a bath with",]


nouns = ["apples", "your sister", "stray dogs", "cute dogs", "wittle kitties", "old indian men playing the sitar", "Kung Fu experts", "kawaii school girlsdesu",
"little girls", "facebook", "your cellphone", "your twitter feed", "Russian strong men", "Russian pastries", "skinny French women", "the English", "doughnuts"
"white South Africans", "Turkish folks", "elderly French Canadians", "clocks", "bananas", "watermelons", "lawns", "anorexics", "hot soup",
"bulimics", "pumpkins", "carrots", "oscars", "questionable juices", "mild poisons", "nothing", "everything", "your favourite singer", "grandma", "gingers",
"the souls of the innocent", "cars", "monsters", "monster trucks", "music", "your boss", "your coworkers", "your daughter's best friend", "creepy guy next door",
"that homeless man", "shirtless homeless man", "Evanescence", "grandpa's teeth", "lead singer of Evanescence", "chewing gum", "daffy duck", "spicy memes",
"dank memes", "garlic bread", "Spongebob", "studio ghibli", "eyes", "job interviews", "an existential crisis" "pancakes",
"your mom's homemade blueberry pie", "your stepsister's clothes", "your plants", "local artists", "your barber", "your estranged brother", "your mother", "your sister",
"your penpal", "your auntie", "your dog", "your leading scientist", "soldiers", "doctors", "dentists", "dental hygienists", "cops", "boarder patrol", "Heman", "Skeletor",
"senpai", "pretty nurses", "ovens", "the Isrealites", "cancer", "good books", "photographs", "Nickleback", "wild horses", "kissin' cousins", "digusting smokers",
"people who vape", ]

frequency = ["always", "usually", "regularly", "normally", "often", "sometimes", "occassionally", "rarely", "seldom", "never", "hardly ever", "generally",
"once in a blue moon", "once a day", "just once"]

outcome = ["brings world peace.", "causes cancer.", "ends world hunger.", "cures cancer.", "cures aids.", "prevents death.", "causes death.", "keeps the doctor away.",
           "leads to a better life.", "angers the Japanese.", "starts world war 3.", "causes stupidity.", "caused the Titanic to sink.", "makes the baby Jesus cry.",
           "kills me a little inside.", "gives me chills...", "gives me hope for the future.", "makes me appreciate great sex.", "causes testiscular engrossment.",
           "makes me sick.", "causes little girls to cry.", "is more likely than being struck by lightning.", "makes my mom regret I was born...",
           "causes Snape to kill Dumbledore.", "causes kids to go gay.", "brings me to tears.", "makes me want to go dancing!", "makes me wish for death.",
           "makes mama proud.", "gives black bears a spook.", "gives me a spook!", "causes pregnancy.", "gives me time.", "angers the ghost of Adolf Hitler.",
           "sends nan into a coma.", "causes the war in the middle east.", "put me in a weird position.", "gives me PTSD", "leads to a better love life.",
           "is why we need Feminism", "is the key to success.",]

Tweet = ("")

apples = True

def tweeterBot():
        first = random.choice(opener)
        second = random.choice(verb)
        third = random.choice(nouns)
        fourth = random.choice(frequency)
        fifth = random.choice(outcome)
        
        apples = True
        while apples == True:
                Tweet = ("%s %s %s %s %s ") % ((first),(second),(third),(fourth),(fifth))
                print Tweet
                apples = False


tweeterBot()

