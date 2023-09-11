import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import Button, View
import openai

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents= discord.Intents.all())

dst = 'MTEzMjc3NTkyMTgxNjk4MTUwNg.GWrDHM.PvYnMBJuu-YyLJy5eWuYwSW0l520-OyiFrPwRo'
openai.api_key = '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'

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    try: 
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(e)

@bot.tree.command(name = "ask")
@app_commands.describe(prompt='subject')
async def gpt(interaction: discord.Interaction, prompt:str):
    
    if interaction.channel.id == 1150809963208380477:

        text_content = prompt

        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo-0301",
            messages= [{"role": "user", "content": text_content}]
        )

        print(prompt)
        print(response.choices[0].message.content)

        await interaction.response.send_message(response.choices[0].message.content, ephemeral=True)

    else:

        await interaction.response.send_message(f"vist me in my library child", ephemeral=True)

bot.run(dst)