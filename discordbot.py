import discord
from discord.ext import commands
import config
import database

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=config.c.prefix, description=description, intents=intents)

DB = database.DBClient(config.c.db_host,config.c.db_username,config.c.db_password)
#userinfo = DB.getUsers()
#print(userinfo[0])

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_member_join(ctx):
    DB.adduser(ctx.id,ctx.name)

@bot.command()
async def getusers(ctx):
    await ctx.send(DB.getUsers())

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def getUserInfo(ctx):
    userinfo = DB.getUserInfo(ctx.author.id)
    await ctx.send(userinfo)

@bot.command()
async def addUser(ctx):
    DB.adduser(ctx.author.id,ctx.author.name)

@bot.command()
async def setBirthday(ctx,month,day,year):
    birthday = "{0}-{1}-{2}".format(year,month,day)
    #await ctx.send(birthday)
    DB.setBirthday(ctx.author.id,birthday)

@bot.command()
async def getBalance(ctx):
    balance = DB.getBalance(ctx.author.id)
    response = "You have {}$".format(balance)
    await ctx.send(response)

@bot.command()
async def gamble(ctx,wager,bet):
    roll = random.randint(0,36)
    if bet is int:
        if bet == roll:
            newbal = 3*wager
    else:
        if bet is str:
            if bet == "even" and bet%2==0:
                newbal = 2*wager
            if bet == "odd" and bet%2>0:
                newbal = 2*wager
        else:
            newbal = -wager;

    if newbal>0:
        response = "You won {}$".format(newbal)
    else:
        response = "You lost {}$".format(newbal)
    DB.updateBalance(ctx.author.id,newbal,"add")
    await ctx.send(response)

@bot.command()
async def work(ctx):
    paycheck = random.randin(0,100)
    DB.updateBalance(ctx.author.id,paycheck,"add")
    response = "You earned {}$".format(paycheck)
    await ctx.send(response)


bot.run(config.c.token)

"""
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run(token)
"""
