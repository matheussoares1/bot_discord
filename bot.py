
import discord
import subprocess
import os
from discord.ext import commands
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Configuração do bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!git ", intents=intents)

# Comando para clonar um repositório
@bot.command()
async def clone(ctx, repo_url: str):
    try:
        subprocess.run(["git", "clone", repo_url], check=True)
        await ctx.send(f"Repositório clonado com sucesso: {repo_url}")
    except subprocess.CalledProcessError as e:
        await ctx.send(f"Erro ao clonar repositório: {e}")

# Comando para verificar status do repositório
@bot.command()
async def status(ctx):
    try:
        result = subprocess.run(["git", "status"], capture_output=True, text=True, check=True)
        await ctx.send(f"```{result.stdout}```")
    except subprocess.CalledProcessError as e:
        await ctx.send(f"Erro ao verificar status: {e}")

# Comando para fazer commit
@bot.command()
async def commit(ctx, *, message: str):
    try:
        subprocess.run(["git", "add", "-A"], check=True)
        subprocess.run(["git", "commit", "-m", message], check=True)
        await ctx.send(f"Commit realizado com a mensagem: {message}")
    except subprocess.CalledProcessError as e:
        await ctx.send(f"Erro ao fazer commit: {e}")

# Comando para puxar atualizações
@bot.command()
async def pull(ctx):
    try:
        result = subprocess.run(["git", "pull"], capture_output=True, text=True, check=True)
        await ctx.send(f"```{result.stdout}```")
    except subprocess.CalledProcessError as e:
        await ctx.send(f"Erro ao puxar atualizações: {e}")

# Comando para enviar mudanças
@bot.command()
async def push(ctx):
    try:
        result = subprocess.run(["git", "push"], capture_output=True, text=True, check=True)
        await ctx.send(f"```{result.stdout}```")
    except subprocess.CalledProcessError as e:
        await ctx.send(f"Erro ao enviar mudanças: {e}")

# Rodar o bot
bot.run(TOKEN)
