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
bled_rever = ["bledrever", "rever", "bled rever", "bled", "betrayer"]

rick_roll = ["rick", "roll", "rickroll"]
#Replies ----------------------------------------------------------

angry_bot_reply = [
  "https://tenor.com/view/gun-reload-sniper-gif-16301372",
  "https://tenor.com/view/doom-slayer-reload-gun-gif-19444267",
  "https://tenor.com/view/shame-gun-thats-a-shame-rifle-reload-gif-16005192"
]

# Points and levels manager
#---------------------------------------------------------------

def getPoint(user):
  return user["points"]

def updatePoint(user, i=1):
  user["points"] = user["points"] + i

def getLevel(user):
  points = user["points"]
  max_10 = 2
  i = 0

  while(points > max_10):
    max_10 = max_10*2
    i = i + 1
  user["level"] = i

  return user["level"]

#---------------------------------------------------------------

# Snakes and Ladders
#---------------------------------------------------------------
game_status = ""
player = []
players_game = {}
player_turn = 0
player_number = 0
next_turn = False
ladder_trig = [1, 4, 8, 21, 28, 50, 71, 80]
snake_trig = [32, 36, 48, 62, 88, 95, 97]
ladders = {1:38, 4:14, 8:30, 21:42, 28:76, 50:67, 71:92, 80:99}
snakes = {32:10, 36:6, 48:26, 62:18, 88:24, 95:56, 97:78}

#updates the tile
def update_tile(tile, roll):
  condn = "" #stores condition of the user
  tile = tile + roll
  if tile > 100:
    condn = "pseudo win"
    return (tile-roll), condn
  elif tile == 100:
    condn = "win"
    return tile, condn
  elif tile in ladder_trig:
    condn = "ladder"
    return ladders[tile], condn
  elif tile in snake_trig:
    condn = "snake"
    return snakes[tile], condn
  else :
    return tile, condn

def get_turn():
  return player_turn

def update_turn():
  global player_turn
  if player_turn == len(player) - 1:
    player_turn = 0
  else:
    player_turn = player_turn + 1

#---------------------------------------------------------------

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
  await client.change_presence(activity=discord.Game('$help'))

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
  if (str(message.author.id) in keys):
    user = db[str(message.author.id)]
    updatePoint(user)
  else:
    db[str(message.author.id)] = new_user

  #displays stats
  if msg.startswith('$stats'):
    status = "I wanna give you some info"
    
    if (str(message.author.id) in keys):
      user = db[str(message.author.id)]
      updatePoint(user)
    else:
      db[str(message.author.id)] = new_user

    points = user["points"]
    level = getLevel(user)

    await message.reply(f'Points :{points}, Level: {level}')
  #---------------------------------------------------------------

  #help---------------------------------------------------
  if msg.startswith('$help'):
    status = "Do something you bloody loser"    
    
    info = "Lol what a loser. You need help for this also. Anyways here it is -\n$inspire - gives an inspirational quote\n$stats - see your stats\n$mood - see bots mood\n$game - to play snakes and ladders\n$gameboard - displays the gameboard\nAnd there are many more triggers you have to find it out yourself"
    await message.reply(info)
  #-------------------------------------------------------

  #Snakes and Ladders
  #-------------------------------------------------------
  global player_number
  global player
  global game_status
  global players_game
  global next_turn
  global player_turn

  if msg.startswith('$gameboard'): 
    status = "Showing my gameboard"
    await message.channel.send("This is your gameboard")
    await message.channel.send("https://imgur.com/a/mhElTD1")

  if msg.startswith('$game'): 
    status = "Playing Snakes and Ladders"

    if game_status == 'completed':
      player = []
      players_game = {}
      player_turn = 0
      player_number = 0
      next_turn = False

    new_player = message.author.id

    if game_status == 'started':
      await message.channel.send("Wait for the previous game to get over you dumb twat.")
    else:
      game_status = "waiting"
      if player_number == 0:
        await message.channel.send("You have been registered for snakes and ladders, waiting for more players")
        player.append(new_player)
        players_game[new_player] = 0
        player_number = player_number + 1

      elif player_number < 4:
        await message.channel.send("Minimum players satisfied. Do you want to start the game (yes/no)?")
        player.append(new_player)
        players_game[new_player] = 0
        player_number = player_number + 1

      elif player_number == 4:
        await message.channel.send("Max players reached, try some other time.")
        player_number = player_number + 1
        game_status = "started"

        await message.channel.send("This is your gameboard")
        await message.channel.send("https://imgur.com/a/mhElTD1")
        turn = get_turn()
        ping = player[turn]
        await message.channel.send(f"<@{ping}>, its your turn. Use $roll to roll the dice")
        next_turn = True

  if msg == 'yes' and message.author.id == player[0] and game_status=='waiting':
    game_status = "started"
    await message.channel.send("This is your gameboard")
    await message.channel.send("https://imgur.com/a/mhElTD1")
    turn = get_turn()
    ping = player[turn]
    await message.channel.send(f"<@{ping}>, its your turn. Use $roll to roll the dice")
    next_turn = True
  
  if msg == '$cancel' and message.author.id == player[0]:
    game_status = 'completed'
    await message.channel.send("Game cancelled")
    next_turn = False

  if msg == '$forefeit' and game_status=='started':
    temp = message.author.id
    if player[0] == id:
      await message.channel.send(f"<@{player[1]}> id the new game leader")
    player.remove(temp)
    players_game.pop(id)
    if len(player) < 2:
      game_status = 'completed'
      await message.channel.send(f"<@{message.author.id}>, because of you the game had to end. What a sore loser.")
      next_turn = False

  if msg == "$roll":
    turn  = get_turn()
    if message.author.id == player[turn]:
      dice = random.randint(1,6)
      await message.reply(f"You rolled ..... {str(dice)}")

      tile, condn = update_tile(players_game[player[turn]], dice)
      players_game[player[turn]] = tile

      if condn == "win":
        user = db[str(message.author.id)]
        updatePoint(user, 100)
        game_status = "Completed"
        await message.reply(f"<@{player[turn]}>, You WIN!\nNow go do something productive you lazy bum.")
        await message.reply("https://tenor.com/view/doctor-who-productive-nothing-lazy-gif-10273802")
        next_turn = False
      elif condn == 'pseudo win':
        await message.reply(f"<@{player[turn]}>, So close yet so far away, you are now in {str(tile)}")
      elif condn == "ladder":
        await message.reply(f"<@{player[turn]}>, You got a ladder!, you are now in {str(tile)}")
      elif condn == "snake":
        await message.reply(f"Alas a snake, you fall into Hel to accompany Fenrir.\n<@{player[turn]}>, You got eaten by Jörmungandr!, you are now in {str(tile)}")
        await message.reply("https://tenor.com/view/god-of-war-world-serpent-snake-big-giant-gif-19204482")
      else :
          await message.reply(f"Thou hath encountered a ladder. Ride to Valhalla with the Valkyries.\n<@{player[turn]}>, you are now in {str(tile)}")
          await message.reply("https://tenor.com/view/odin-is-with-us-magnus-bruun-izuniy-assassins-creed-valhalla-viking-gif-17554992")

      if next_turn :
        update_turn()
        turn = get_turn()
        ping = player[turn]
        await message.channel.send(f"<@{ping}>, its your turn. Use $roll to roll the dice")
        
    else:
      await message.reply("Its not your turn, so get rickrolled.")
      await message.reply("https://tenor.com/view/rick-astley-rick-roll-dancing-dance-moves-gif-14097983")
  #-------------------------------------------------------

  #getting rickrolled
  if any(word in msg for word in rick_roll) and msg != '$roll':
    status = "Lol get rick rolled"

    await message.reply("https://tenor.com/view/rick-astley-rick-roll-dancing-dance-moves-gif-14097983")


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

#checks for edits
@client.event
async def on_message_edit(before, after):
    if before.content != after.content:
      msg = after.content
      msg = msg.lower()
      if (str(after.author) == "SoulGodAlpha#4645"): 
        await after.reply(f"{after.author.mention} you can't just edit messages and think you are smart")


client.run(os.environ['TOKEN'])