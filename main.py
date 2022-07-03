import disnake
from disnake.ext import commands
import os

intents = disnake.Intents.default()
intents.members = True

bot = commands.Bot(
    command_prefix = "?",
    intents = intents,
    help_command=None,
    owner_ids = [836773084056649818]
)

bot.load_extension("jishaku")

for filename in os.listdir("Cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"Cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    print(f"Login as {bot.user.name}")



bot.run("ODY0NzkyOTAyMTQ3Mzc1MTU0.Gx5KEr.HxYv-QKeSFT7oO9AuJkPa7qOlqnvPFzlJrkJ2g")