import os
import discord
import random
import datetime
import asyncio
from keep_alive import keep_alive

birthday_keyword = ["happy birthday", "happy bday", "happs"]

birthday_reply = [
  "Wow, you're old.",
  "Cha cha cha, chocolat!",
  "One year closer to death!",
  "Congrats on being a hag!",
  "Do you have back pains yet?",
  "Can you feel your hair turning grey?",
  "Time to retire from life...",
  "Your clock is ticking..."
]

pick_starters = [
  "The obvious choice is ",
  "I choose ",
  "You should definitely go with ",
  "Venti would pick ",
  "I am Jesus. And Jesus says ",
  "Bibbity bobbity... ",
  "rawr xD it would be soooo gnarly if you went with ",
  "Roses are red, violets are blue, and my answer is ",
  "Honk honk "
]

my_name = ["roselyn", "rwae"]

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content.lower()

  if msg.startswith('f!hello'):
    await message.channel.send('funkyyy')
    await message.channel.send('message two')

  # info

  if msg == 'info funkybot':
    embedInfo = discord.Embed(
      title = 'Stalker Notes',
      description = 'funkybot exists for two purposes: 1, being funky; and 2, being a bot.\n stay aware that funkybot is always watching over you, even when offline.',
      colour = 0x43bea9
    )

    embedInfo.set_footer(text='May the Anemo Archon protect you.')
    embedInfo.set_image(url='https://64.media.tumblr.com/bf8a09e249158c3708dee60b62195c82/1c02a351807a4b1f-de/s540x810/12769e4e078c824e2632636bd7ff6eebe7e11ab3.gif')
    #embedInfo.set_thumbnail(url='https://gmspors.com/wp-content/uploads/2021/08/5-Facts-About-Rapper-Mark-Lee-1.jpeg')
    embedInfo.set_author(name='funkybot', icon_url='https://cdn.discordapp.com/emojis/856256948964687902.png')
    embedInfo.add_field(name='birthday', value='July 31st', inline=True)
    embedInfo.add_field(name='favourite person', value='Venti (of course!)', inline=True)
    embedInfo.add_field(name='commands', value='"funky help"', inline=True)
    
    await message.channel.send(embed=embedInfo)

  # help

  if msg == 'funky help':
    embedHelp = discord.Embed(
      title = 'Commands',
      description = '',
      colour = 0x43bea9
    )

    embedHelp.set_author(name='funkybot', icon_url='https://cdn.discordapp.com/emojis/856256948964687902.png')
    embedHelp.add_field(name='info funkybot', value='bot info', inline=True)
    embedHelp.add_field(name='you can do it (@user)', value='cheer! (opt. mention)', inline=True)
    embedHelp.add_field(name='pls bonk me', value='bonk yourself', inline=True)
    embedHelp.add_field(name='bonk @user', value='bonk someone', inline=True)
    embedHelp.add_field(name='whack @user', value='whack someone', inline=True)
    embedHelp.add_field(name='repeat ___', value='i will do as you wish', inline=True)
    embedHelp.add_field(name='diluc lenny', value='/lenny', inline=True)
    embedHelp.add_field(name='venti dance', value='uwu', inline=True)
    embedHelp.add_field(name='venti cat', value='nya', inline=True)
    embedHelp.add_field(name='ehe', value='ehe!', inline=True)
    embedHelp.add_field(name='mark pinch', value='italian hands', inline=True)
    embedHelp.add_field(name='pick \_\_\_ or \_\_\_', value='make decisions', inline=True)

    await message.channel.send(embed=embedHelp)


  if msg.startswith('owo'):
    channel = client.get_channel(871253802462883890)
    await channel.send('wrong channel!')

  # repeat

  if msg.startswith('repeat'):
    split_message = message.content.split(' ', 1)[1]
    await message.channel.send(split_message)

  # birthday

  if any(word in msg for word in birthday_keyword):
    await message.channel.send(random.choice(birthday_reply))

  bday_kathia = datetime.date(2022, 1, 7) - datetime.date.today()
  bday_chow = datetime.date(2022, 1, 16) - datetime.date.today()
  bday_george = datetime.date(2022, 1, 27) - datetime.date.today()
  bday_korie = datetime.date(2022, 2, 28) - datetime.date.today()
  bday_cassidy = datetime.date(2022, 6, 20) - datetime.date.today()
  bday_ligird = datetime.date(2022, 7, 15) - datetime.date.today()
  bday_pepper = datetime.date(2021, 10, 13) - datetime.date.today()
  bday_rwae = datetime.date(2021, 11, 5) - datetime.date.today()
  bday_vika = datetime.date(2021, 11, 20) - datetime.date.today()
  
  if msg == "whnl birthdays":
    embedBirthday = discord.Embed(
        title = 'WHNL Birthday Countdown',
        description = 'How many days until the next birthday?',
        colour = 0x43bea9
      )

    embedBirthday.set_image(url='https://i.pinimg.com/originals/2f/25/f4/2f25f44be3d5af5d96b159dbe1fecfe9.gif')
    embedBirthday.set_author(name='funkybot', icon_url='https://cdn.discordapp.com/emojis/856256948964687902.png')
    embedBirthday.add_field(name='Kathia - 01/07', value=str(bday_kathia).strip("0: ,"), inline=True)
    embedBirthday.add_field(name='Chow - 01/16', value=str(bday_chow).strip("0: ,"), inline=True)
    embedBirthday.add_field(name='George - 01/27', value=str(bday_george).strip("0: ,"), inline=True)
    embedBirthday.add_field(name='Korie - 02/28', value=str(bday_korie).strip("0: ,"), inline=True)
    embedBirthday.add_field(name='Cassidy - 06/20', value=str(bday_cassidy).strip("0: ,"), inline=True)
    embedBirthday.add_field(name='Ligird - 07/15', value=str(bday_ligird).strip("0: ,"), inline=True)
    embedBirthday.add_field(name='Pepper - 10/13', value=str(bday_pepper).strip("0: ,"), inline=True)
    embedBirthday.add_field(name='RWAE - 11/05', value=str(bday_rwae).strip("0: ,"), inline=True)
    embedBirthday.add_field(name='Vika - 11/20', value=str(bday_vika).strip("0: ,"), inline=True)
    
    await message.channel.send(embed=embedBirthday)

  # pick

  if msg.startswith('pick'):
    if msg.count('or') == 1:
      space = msg.find(' ')
      new_message = msg[(space + 1):]
      choice = new_message.split(' or ', 1)
      await message.channel.send(random.choice(pick_starters) + '**' + random.choice(choice) + '!**')

  # you can do it

  if msg == ('you can do it'):
    await message.channel.send('you can do it !!!!!!!! i BELIEVE IN YOU! you are')
    await message.channel.send('https://pa1.narvii.com/6326/0ca8c02ca32fae5330434667cff6c1886edea372_hq.gif')

  if msg.startswith('you can do it'):
    for user in message.mentions:
      await message.channel.send('{}, you can do it !!!!!!!! {} BELIEVES IN YOU! you are'.format(user.display_name, message.author.display_name))
      await message.channel.send('https://pa1.narvii.com/6326/0ca8c02ca32fae5330434667cff6c1886edea372_hq.gif')

  # pings

  if any(word in msg for word in my_name):
    await message.channel.send('<@!379827741194977280>')

  if msg == '<@!759147695343665212>':
    await message.channel.send('<@!759147695343665212>')
    await message.channel.send('<@!759147695343665212>')
    await message.channel.send('<@!759147695343665212>')
    await message.channel.send('<@!759147695343665212>')
    await message.channel.send('<@!759147695343665212>')

  # bonks and whacks

  if msg == 'pls bonk me':
    await message.channel.send('{} **has been bonked.**'.format(message.author.mention))
    await message.channel.send('https://66.media.tumblr.com/b79632386fc0ab2b048c212717a8df94/46858d40606f3cce-44/s540x810/3202cfc9d15a9438afca56f2df2f9d45e837b587.png')

  if msg.startswith('bonk'):
    for user in message.mentions:
      await message.channel.send('{} **has been bonked.**'.format(user.mention))
      await message.channel.send('https://66.media.tumblr.com/b79632386fc0ab2b048c212717a8df94/46858d40606f3cce-44/s540x810/3202cfc9d15a9438afca56f2df2f9d45e837b587.png')

  if msg.startswith('whack'):
    for user in message.mentions:
      await message.channel.send('{} **has been whacked.**'.format(user.mention))
      await message.channel.send('https://cdn.discordapp.com/attachments/535232819853656114/877771799805460480/unknown.png')

  # single replies

  if msg.startswith('ehe'):
    await message.channel.send('https://media.discordapp.net/attachments/410600737169604621/825227765434810388/unknown.png?width=630&height=549')

  if msg.startswith('venti dance'):
    await message.channel.send('https://upload-os-bbs.mihoyo.com/upload/2021/02/11/85185140/96dd4cc7a5b9be7e05d5723ea970aeaf_3553930500572314640.gif')
  
  if msg.startswith('venti cat'):
    await message.channel.send('https://cdn.discordapp.com/emojis/815426268379742218.png?v=1')

  if msg.startswith('mark pinch'):
    await message.channel.send('https://i.pinimg.com/564x/fe/80/d4/fe80d476d04f3f287281a01a17729b1f.jpg')

  if msg.startswith('diluc lenny'):
    await message.channel.send('https://media.discordapp.net/attachments/410600737169604621/824692293340364920/Screen_Shot_2021-03-25_at_1.12.36_PM.png')
  
  if msg.startswith('hi is me'):
    await message.channel.send('https://cdn.discordapp.com/attachments/469569870053376002/469602724015636480/image.gif')

  # reactions

  if 'leg' in msg:
    leg_emoji = '<:leg:535232385873084456>'
    await message.add_reaction(leg_emoji)

  if 'thicc' in msg:
    thicc_emoji = '<:thicc:600161101648363530>'
    await message.add_reaction(thicc_emoji)
  
  if 'kms' in msg:
    kms_emoji = '<:kms:440259386842152991>'
    await message.add_reaction(kms_emoji)

  if 'bread' in msg:
    bread_emoji = '🍞'
    await message.add_reaction(bread_emoji)
  
  if '78' in msg:
    turkey_emoji = '🦃'
    await message.add_reaction(turkey_emoji)

  # bot activity status

async def ch_pr():
 await client.wait_until_ready()

 status_list = [
   "Genshin Impact",
   "The Holy Lyre der Himmel",
   "in Angel's Share",
   "the flute"
   ]

 while not client.is_closed():
   status = random.choice(status_list)
   await client.change_presence(activity=discord.Game(name=status))
   await asyncio.sleep(25)

client.loop.create_task(ch_pr())

keep_alive()
client.run(os.environ['TOKEN'])