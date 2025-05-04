import discord
import random
import json
import config


def pick_weather():
    with open(config.data_dir + "/fishing.json", "r") as file:
       data = json.load(file)
       if data:
          waters = data['waters']
          weights = []
          for w in waters:
              weights.append(w['chance'])
              
          return random.choices(waters, weights=weights)[0]
       else:
           return None

async def initilize_guild(guild: discord.Guild, bot):
    db = bot.mongoConnect['shark8']
    guild_collection = db["guild_data"]
    guild_id = str(guild.id)
    
    guild_data = await guild_collection.find_one({"_id": guild_id})
     
    if not guild_data:
       guild_data = {"_id": guild_id}       
       
    waters = pick_weather()   
    if "weather" not in guild_data:
        guild_data['weather'] = {}
    
    weather = guild_data['weather']
    weather['id'] = waters['id']
    weather['status'] = waters['status']   
       
    await guild_collection.update_one({"_id": guild_id}, {"$set": guild_data}, upsert=True)     


  #WDStudio PROPERTY owned by WDStudio
#© WDStudio 2024      