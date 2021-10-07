import discord
import os
import requests
import json
import random
from replit import db

keys = db.keys()

#deleting all keys
#for key in keys:
#  db.__delitem__(key)

#seeing all keys
#for key in keys:
#  print(key)

client = discord.Client()

# Bot mood
status = "I am daydreaming" 

#Triggers ------------------------------------------------------
sad_words = ["sad", "depressed", "depressing", "depression", "unhappy", "angry", "miserable", "pissed", "screw", "pissing", "irritating", "suck", "sucks", "get lost", "boring", "idiot", "bored", "screwed", "FML", "fuck", "die", "stupid", "hate", "dumb", "breakdown", "kill me", "scary", "scared", "anxiety", "fak"]

happy_words_vinneth = ["proud", "love", "glad", "happy", "thanks", "thank", "welcome", "hehehehe", "lol", "haha"]

happy_words = ["proud", "love", "glad", "happy", "thanks", "thank", "welcome"]

bled_rever = ["bledrever", "rever", "bled rever", "bled", "betrayer"]

darth_vader = ["darth vader", "darth", "vader", "darthvader"]

rick_roll = ["rick", "roll", "rickroll"]

demon_slayer = ["demon", "slayer", "demon slayer", "kimetsu no yaiba", "hashira"]

#Replies ----------------------------------------------------------
starter_encouragements = [
  "Obviously you suck",
  "I don't want to encourage you today, so die",
  "Sometimes people wish their lives was like someone else's, but i am glad my life isn't like yours",
  "https://tenor.com/view/manga-anime-death-note-gif-14844099",
  "What a save!",
  "https://tenor.com/view/sangatsu-no-lion-march-comes-in-like-a-lion-3gatsu-no-lion-rei-kiriyama-crying-gif-18524205",
  "https://tenor.com/view/gokushufudou-gif-21119657",
  "You are so stupid that even assigning a positive IQ point to you is a sin.",
  "Your existence is the reason we had a pandemic.",
  "Have you ever considered euthanasia?",
  "Why are you so useless?",
  "https://tenor.com/view/the-office-why-michael-scott-gif-5422774",
  "https://tenor.com/view/flipping-off-flip-off-middle-finger-smile-happy-gif-4746862",
  "https://tenor.com/view/youre-so-weak-weak-powerless-judging-despise-gif-15666774",
  "https://tenor.com/view/himejima-gyoumei-anime-cry-stone-gif-18292656",
  "https://tenor.com/view/excuses-mugen-samauri-champloo-anime-gif-13457071",
]

happy_reply = [
  "I am proud of you",
  "Love me, cause my life is better than yours",
  "Just wait, tomorrow I will ruin your happiness",
]

happy_reply_kruti = [
  "https://tenor.com/view/awesome-you-are-guys-gorilla-thumbs-up-gif-13633109",
  "https://tenor.com/view/noice-brooklyn-ninenine-b99-smile-gif-11928987",
  "https://tenor.com/view/friends-keep-it-up-thumbs-up-gif-13267317",
]

sad_reply_kruti = [
    "https://tenor.com/view/chillin-lazt-sloth-hang-in-there-it-will-get-better-gif-15012100",
  "https://tenor.com/view/quotes-anime-gif-20588266",
  "https://tenor.com/view/-gif-3730657",
  "https://imgur.com/iwG4TwE",
  "https://tenor.com/view/milk-and-mocha-bear-couple-wake-up-cute-kawaii-gif-13624283",
  "https://tenor.com/view/-gif-4474285",
  "https://imgur.com/bgVaHMd",
  "https://tenor.com/view/there-cheer-up-buttercup-it-gif-21613666",
  "https://tenor.com/view/could-be-worse-worse-eek-yikes-its-alright-gif-13884804",
  "https://tenor.com/view/april-fools-joke-dog-its-fine-this-is-not-gif-16757454",
  "https://tenor.com/view/tipsy-cheer-up-cheer-dance-be-happy-gif-17211808",
  "Cheer up!",
  "Hang in there.",
  "Rise my drengr and fight on, for we fight for valhalla",
]

vinneth_roasts = [
  "Vinneth is so dumb that we had to develop a negative IQ test.",
  "There are people who know tech, there are those who don't and then there is Vineeth. He can mess up stuff even with detailed instructions.",
  "Boi i am glad my life isn't bad as his.",
  "I have better things to do than bother about this scum.",
  "Vinneth is such a loser, even if he went to gay bar he wouldn't get hit on.",
  "Some ppl get addicted to internet. Some ppl are in control of it. And then there is Vineeth, the internet itself is addicted to him!",
  "I have better things to do than roasting him, do it yourself",
  "He is so stupid that even if he had answers right infront of him, he would still fail a test.",
  "If laughter is the best medicine, your face must be curing the world.",
  "I'm glad to see you're not letting your education get in the way of your ignorance.",
  "Learn to read messages, and maybe people won't seenzone you.",
  "If I wanted to kill myself, I'd climb to your procastination levels and jump to your iq.",
  "If I had a dollar for everytime you said something smart, I'd be broke.",
  "When you were born the doctor threw you out of the window and the window threw you right back.",
  "Your secrets are always safe with me. I never even listen when you tell me them.",
  "Mirrors can't talk. Lucky for you, they can't laugh either.",
  "https://tenor.com/view/sabrina-the-teenage-witch-salem-saberhagen-salem-quotes-tv-gif-16375816",
]

self_roast = [
  "https://tenor.com/view/trash-ass-filth-ass-garbage-ass-shit-crap-gif-14818418",
  "https://tenor.com/view/trash-you-are-trash-i-am-trash-when-you-know-stumble-gif-11969610",
  "https://tenor.com/view/the-lego-movie-batman-you-are-so-disappointing-on-so-many-levels-disappointed-disappointment-gif-22490626",
  "https://tenor.com/view/star-wars-yoda-you-are-such-a-failure-i-look-at-you-with-disgrace-gif-17069251",
  "https://tenor.com/view/anime-izaya-orihara-durarara-drrr-die-here-gif-12286708",
  "https://tenor.com/view/anime-haikyu-stupid-haikyuu-hinata-gif-12213790"
]

angry_bot_reply = [
  "https://tenor.com/view/gun-reload-sniper-gif-16301372",
  "https://tenor.com/view/doom-slayer-reload-gun-gif-19444267",
  "https://tenor.com/view/shame-gun-thats-a-shame-rifle-reload-gif-16005192"
]

vader_reply = [
  "https://tenor.com/view/darth-vader-fog-star-wars-smoke-dramatic-gif-4842714",
  "https://tenor.com/view/dance-happy-darthvader-gif-4946439",
  "https://tenor.com/view/darth-vader-star-wars-snowing-gif-14696435",
  "https://tenor.com/view/star-wars-darth-vader-if-you-only-knew-the-power-of-the-dark-side-gif-15855616",
  "https://tenor.com/view/star-wars-correct-way-luke-i-am-your-father-darth-vader-gif-15796921"
]

yoda_reply = [
  "https://tenor.com/view/teach-you-yoda-star-wars-mentor-teach-you-i-will-gif-13942585",
  "https://tenor.com/view/yoda-suicide-squad-dance-dancing-gif-5970653",
  "https://tenor.com/view/baby-yoda-hi-hello-greet-wave-gif-15912640",
  "https://tenor.com/view/yoda-sarcasm-gif-12984296",
  "https://tenor.com/view/yoda-much-to-learn-star-wars-attack-electricity-gif-10182983",
  "https://tenor.com/view/yoda-patience-you-must-have-patience-gif-15254127"
]

cheer = [
  "https://tenor.com/view/snoopy-cheerleader-cheer-gif-8670539",
  "https://tenor.com/view/cheering-minions-despicable-me-cheer-gif-4968109",
  "https://tenor.com/view/quby-cute-adorable-cheer-gif-15071381",
  "https://tenor.com/view/pikachu-cheer-dance-pokemon-gif-16127538",
]

demon_slayer_reply = [
  "https://tenor.com/view/kimetsu-no-yaiba-demon-slayer-demon-slayer-corps-breath-of-thunder-gif-17177170",
  "https://tenor.com/view/anime-zenitsu-agatsuma-demon-slayer-kimetsu-no-yaiba-flowers-gif-17636946",
  "https://tenor.com/view/anime-demon-slayer-kimetsu-no-yaiba-tanjiro-gif-14748917",
  "https://tenor.com/view/zenitsu-zenitsu-agatsuma-demon-slayer-kimetsu-no-yaiba-gif-14668491",
  "https://tenor.com/view/nezuko-anime-demon-slayer-kimetsu-no-yaiba-gif-15131994",
  "https://tenor.com/view/anime-demon-slayer-kimetsu-no-yaiba-nezuko-running-gif-14870818",
  "https://tenor.com/view/kimetsu-no-yaiba-demon-slayer-pig-angry-inosuke-hashibira-gif-14905892",
  "https://tenor.com/view/kimetsu-no-yaiba-tanjiro-kamado-sleep-demon-slayer-kamado-tanjiro-gif-15590897",
  "https://tenor.com/view/tanjiro-udon-eating-hungry-demon-slayer-gif-16830905",
  "https://tenor.com/view/kyojuro-rengoku-vs-akaza-demon-fight-fighting-flame-aura-gif-22077091",
  "https://tenor.com/view/tanjiro-j8-demon-slayer-run-fire-gif-14745537",
]

tanjiro_reply = [
  "https://tenor.com/view/tanjiro-j8-demon-slayer-run-fire-gif-14745537",
  "https://tenor.com/view/tanjiro-udon-eating-hungry-demon-slayer-gif-16830905",
  "https://tenor.com/view/kimetsu-no-yaiba-tanjiro-kamado-sleep-demon-slayer-kamado-tanjiro-gif-15590897",
  "https://tenor.com/view/anime-demon-slayer-kimetsu-no-yaiba-tanjiro-gif-14748917",
]

nezuko_reply = [
  "https://tenor.com/view/nezuko-anime-demon-slayer-kimetsu-no-yaiba-gif-15131994",
  "https://tenor.com/view/nezuko-anime-demon-slayer-kimetsu-no-yaiba-gif-15131994",
  "https://tenor.com/view/anime-demon-slayer-kimetsu-no-yaiba-nezuko-running-gif-14870818",
]

zenitsu_reply = [
  "https://tenor.com/view/anime-zenitsu-agatsuma-demon-slayer-kimetsu-no-yaiba-flowers-gif-17636946",
  "https://tenor.com/view/zenitsu-zenitsu-agatsuma-demon-slayer-kimetsu-no-yaiba-gif-14668491",
  "https://tenor.com/view/kimetsu-no-yaiba-demon-slayer-demon-slayer-corps-breath-of-thunder-gif-17177170",
]
#---------------------------------------------------------------

def getPoint(user):
  return user["points"]

def updatePoint(user):
  user["points"] = user["points"] + 1

def getLevel(user):
  points = user["points"]
  max_10 = 2
  i = 0

  while(points > max_10):
    max_10 = max_10*2
    i = i + 1
  user["level"] = i

  return user["level"]

#------------------------------------------------

#Used to get quotes for $inspire
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

# logging in
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

# replying to messages
@client.event
async def on_message(message):

  global status

  if message.author == client.user:
    return

  msg = message.content
  msg = msg.lower()

  # Updating database ------------------------------------------
  new_user = {
    "points": 1,
    "level" : 0
  }
  if (str(message.author) in keys):
    user = db[str(message.author)]
    updatePoint(user)
  else:
    db[str(message.author)] = new_user

  #displays stats
  if msg.startswith('$stats'):
    status = "I wanna give you some info"
    
    if (str(message.author) in keys):
      user = db[str(message.author)]
      updatePoint(user)
    else:
      db[str(message.author)] = new_user

    points = user["points"]
    level = getLevel(user)

    await message.reply(f'Points :{points}, Level: {level}')
  #---------------------------------------------------------------

  #help
  if msg.startswith('$help'):
    status = "Do something you bloody loser"    

    await message.reply("Lol what a loser. You need help for this also. Anyways here it is -")
    await message.channel.send("$inspire - gives an inspirational quote")
    await message.channel.send("$stats - see your stats")
    await message.channel.send("$mood - see bots mood")
    await message.channel.send("And there are many more triggers you have to find it out yourself")

  
  #roast yourself
  if msg.startswith('insult me') or msg.startswith('roast me') or msg.startswith('self roast'):
    status = "F, someone is having a bad day"

    await message.reply(random.choice(self_roast))

  #displays bot's mood
  if msg.startswith('$mood'):
     

    await message.reply(status)

    if status == "Lol get rick rolled":
      await message.reply("https://tenor.com/view/rick-astley-rick-roll-dancing-dance-moves-gif-14097983")

  #cheering
  if msg.startswith("$cheer"):
    status = "I feel happy for you"
     

    await message.reply(random.choice(cheer))

  #insulting NITK
  if msg.startswith('NITK sucks') or msg.startswith('nitk sucks') or msg.startswith('stupid NITK') or msg.startswith('stupid nitk'):
    status = "Boi am I glad I am not in NITK"

    await message.reply("https://tenor.com/view/true-its-true-dwight-schrute-the-office-rainn-wilson-gif-6161302")

  #Reply to sad stuff
  if any(word in msg for word in sad_words) and not (msg.startswith('stupid bot')):
    status = "I feel... Ummm.. better than you"     

    if not(msg.startswith('NITK sucks') or msg.startswith('nitk sucks') or msg.startswith('stupid NITK') or msg.startswith('stupid nitk')):
      if (str(message.author) in exempt) :
        await message.reply(random.choice(sad_reply_kruti))
      else:
        await message.reply(random.choice(starter_encouragements))

  #getting rickrolled
  if any(word in msg for word in rick_roll):
    status = "Lol get rick rolled"
     

    await message.reply("https://tenor.com/view/rick-astley-rick-roll-dancing-dance-moves-gif-14097983")

  #happy reply
  if any(word in msg for word in happy_words) and not (msg.startswith("thanks bot") or msg.startswith("thank you bot")):
    status = "I am very very happy"
     

    if (str(message.author) in exempt) :
      await message.reply(random.choice(happy_reply_kruti))
    else:
      await message.reply(random.choice(happy_reply))

  #bot specific reactions 
  #--------------------------------------------------------------
  if msg.startswith('good bot'):
    status = "Yay! Someone cheered me"
     

    if (str(message.author) in ["SoulGodAlpha#4645"]) :
      await message.reply("https://tenor.com/view/thank-you-deku-bow-sorry-gif-12451676")
    else:
      await message.reply("https://tenor.com/view/thank-you-thanks-appreciate-heart-love-gif-8665649")
  
  if msg.startswith('bad bot'):
    status = "I am sad"
     

    if (str(message.author) in ["SoulGodAlpha#4645"]) :
      await message.reply("https://tenor.com/view/sorry-gif-19656670")
    else:
      await message.reply("https://tenor.com/view/dr-house-gregory-house-did-i-get-bonus-points-if-i-act-like-i-care-gif-15864836")
  
  if msg.startswith('stupid bot') :
     

    if (str(message.author)  in ["SoulGodAlpha#4645"]):
      status = "My creater scolded me, Bled is sad."
      await message.reply("https://tenor.com/view/sad-anime-boy-sad-eyes-sad-face-gif-16059018")
    else :
      status = "Lol some failure scolded me"
      await message.reply(random.choice(angry_bot_reply))

  if any(word in msg for word in bled_rever):
    status = "Oi don't you dare talk behind my backs"

    await message.reply("Who dares talk about me!")
    await message.reply("https://tenor.com/view/anger-rage-gif-18526129")

  #["thanks bot", "thank you bot"]
  if msg.startswith("thanks bot") or msg.startswith("thank you bot"):
    status = "Ain't it a delightful day"
     

    await message.reply("https://tenor.com/view/hat-tip-thanks-thank-you-welcome-youre-welcome-gif-18643868")
  #----------------------------------------------------------------

  #star wars references 
  #--------------------------------------------------------------
  if msg == 'hello there':
    status = "I wanna watch Star Wars"
     

    await message.reply("https://tenor.com/view/hello-there-hi-there-greetings-gif-9442662")
    await message.reply("https://tenor.com/view/hello-there-general-kenobi-star-wars-grevious-gif-17774326")

  if 'yoda'in msg:
    status = "happy, I am"

    await message.reply(random.choice(yoda_reply))

  if any(word in msg for word in darth_vader):
    status = "The dark side is too strong"   

    await message.reply(random.choice(vader_reply))
  #-------------------------------------------------------

  #MHA references
  #--------------------------------------------------------------
  if "plus ultra" in msg:
    status = "I am super pumped up"

    await message.reply("https://tenor.com/view/endeavour-plus-ultra-prominence-burn-fire-my-hero-academia-gif-16784832")
  #-------------------------------------------------------

  #Demon Slayer references
  #--------------------------------------------------------------
  if any(word in msg for word in demon_slayer):
    status = "Tanjiro is the best"
     
    await message.reply(random.choice(demon_slayer_reply))

  if ("tanjiro" in msg):
    status = "Tanjiro is the best"
     
    await message.reply(random.choice(tanjiro_reply))

  if ("nezuko" in msg):
    status = "Tanjiro is the best"
     
    await message.reply(random.choice(nezuko_reply))

  if ("zenitsu" in msg):
    status = "Tanjiro is the best"
     
    await message.reply(random.choice(zenitsu_reply))
#-------------------------------------------------------

#LOTR references
  #--------------------------------------------------------------
  if "precious" in msg:
    status = "MY PRECIOUSSSS"
     
    await message.reply("https://tenor.com/view/my-precious-precious-amazed-bilbo-baggins-lord-of-the-r-ings-gif-16270634")
#-------------------------------------------------------

#checks for edits
@client.event
async def on_message_edit(before, after):
    if before.content != after.content:
      msg = after.content
      msg = msg.lower()
      if (str(after.author) not in exempt): 
        await after.reply(f"{after.author.mention} you can't just edit messages and think you are smart")


client.run(os.environ['TOKEN'])