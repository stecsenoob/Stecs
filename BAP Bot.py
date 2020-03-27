import discord

from discord.ext import commands, tasks

from itertools import cycle

import random


client=commands.Bot(command_prefix = '+')

status=cycle(['with KUR','with PICKA','with majka ti','with baba ti','with sestra ti'])

@client.event



async def on_ready():
	change_status.start()
	await client.change_presence(status=discord.Status.online, activity=discord.Game('with yo mamma'))

	print('Bot is ready')


@tasks.loop(seconds=2)
async def change_status():
	await client.change_presence(activity=discord.Game(next(status)))



@client.command()



async def laze(ctx):



	await ctx.send( "Laze\n"



		"he spent the day at home, playing video games and generally lazing around\n"



		"a person who sits around and does nothing; a detriment to society\n"



		'"Wow what a laze," exclaimed Bethany, "All Laze does is watch porn and eat chips."')









@client.command()



async def koko(cx):



	await cx.send("Koko\n"



		"Koko means the most important thing.\n\n"



"People with this name tend to be quite sarcastic.\n"



"They like to see the beauty in all things and usually act shy when you first meet them.\n"



"And NO Koko isn’t a slang :)\n"



"Wow!! Look at that koko walking by")





@client.command()



async def fetus(ctx):



	await ctx.send("Fetus\n"



		"someone who acts or looks like a small child\n"



		"younger version of yourself.\n"



                         "you when you were little\n"



"man look at this picture of fetus me\n"



"dude, you were so cute!")







@client.command()



async def boki(ctx):



	await ctx.send("Boki\n"

		"A male friend that you happen to like a lot and they like you back, but you aren't dating at the moment.\n"



		"Note: They are very very hot!\n\n"



"I wish Lafaunda would stop flirting with her boki.")









@client.command()



async def gole(ctx):

	await ctx.send("Gole\n\n"

"Looks like a 12 year old boy and constantly gets asked for I.D while at a club. Can be often mistaken for a rat due to his unusual eating habits.\n\n"



"Guy 1: Hey there's a rat eating our popcorn.\n"

"Guy 2: No, thats just my mate Gole.\n")





@client.command()



async def viks(ctx):

	await ctx.send("Viks\n"

		"He is very cute , usually has ABS and he's tall.\n"

		"A wonderful guy to have in your life. he is worth every moment of your time\n"

		"because he's the most amazing, caring, gentle and kind hearted person you will ever know.\n"

		"He is a strong person and is as his name suggests always the victorious one.\n "

		"He loves his friends and family, and adores his ducks. Fond of nature, the magic in life, laughing, smiling and making people happy.")





@client.command()



async def ace(ctx):

	await ctx.send("Ace\n"

		"someone who is really close to you\n"

		"someone you can relate to. \n"

		"someone that you can easily talk to. \n"

		"someone who listens. \n"

		"someone who really care for you. \n"

		"someone who share the same interests.\n\n"

		"THAT'S MY ACE!\n\n"

		"I LOVE MY ACE!")



@client.command()



async def kice(ctx):

	await ctx.send("Hirohito\n"

		"A vicious dictator of Japan (until WW2). Under his rule, Japanese were taught that they were the master race and that all other races were inferoir.\n"

		"When Japan invaded China during WW2, his Imperial Army slaughtered between 2 million and 6 million Chinese and other non-japanese Asians, and millions more died in the ensuing famine. Not as well known as Hitler, but just as bad.\n\n"

		 "Hirohito says he knew nothing about the WW2 atrocities, but he surely did - it was his own army!")



@client.command()



async def marce(ctx):

	await ctx.send("Marce\n"

		"One of the greatest guys you will ever meet. Gentleman, and is very good at treating women with respect.\n"

		"Genuinely nice to everyone he meets, and is very forgiving.\n"

		"Usually the guy who plays pokemon like it's his religion. He's contemptuous, however not in a rude sarcastic way, but a funny sarcastic way.\n"

		"Has an incredible taste in music. Commonly tall, and athletic. \n"

		"Enjoys running. A Marco is a funny guy that you could joke with anytime.\n"

		"Always there to be a shoulder to cry on whenever you meet him. \n"

		" If you meet a Marco in your life, keep him there for as long as you live.\n\n"

		"Did you meet that guy over there yet?\n\n"

		"Yeah, he's a Marco for sure.\n\n"

		"Definitely."



		)



@client.command()



async def leon(ctx):

	await ctx.send("Leon\n"

			"Leon is a very kind and smart person.\n"

			"He has trouble understanding peoples' feelings and finds that hard sometimes.\n"

			"But he is said to be a good kisser and will always stay by your side even at the hardest of times.\n\n"

"Oh look it's Leon")
@client.command()
async def cum(ctx):
	await ctx.send('cum\n'
		'The fluid containing sperm ejaculated from a man when he has an erection.\n'
r"Sarah was sitting on the chair, in only a red thong. She had her legs spread wide over the chair, and her brown hair flowed over her bare boobs. I was getting excited, Sarah was so hot. She ripped off the thong as she stood up, walked right past me and shut the door I had just passed through. She turned to face me, her feet strongly planted, and forced her hand down my pants. I unblocked my belt, and she tore my pants down to my ankles. She fell to her knees and removed my boxers. I could feel it, my dick was already starting to swell up. God, Sarah was hot. She started on the tip of my dick. She swirled her tongue around it a little. She almost immediately started to massage my balls vigorously. She then took on my whole dick, deep throating it. I could feel it, I was gonna cum. My balls were urging for it to come out. I moaned, it felt so good. I grunted a little as it started, and I cummed inside of her mouth. She pulled away, and swallowed, then smiled. My shirt was torn off and she was rubbing my dick with her hands. Then, she was on her hands and knees. I rubbed my dick, and slipped on the condom from the bowl. My dick was throbbing and I was excited. I slowly slid into her pussy and she squeaked quietly. I began to thrust myself. Faster and faster, I wasn't controlling myself, and she bounced and bounced, moaning and moaning until she screamed. We changed positions a few times, then my cum splurged out at work just thinking about it. Then my assistant asked for some.")



@client.command(aliases=['8ball','test'])




async def q(ctx,*,question):

	responses=[  "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]

	await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')






@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send('Invalid command used.')





























client.run('NjkwOTgxMzk2NjU0NTg3OTU1.Xn4vmA.PApFPi3c8sqvWT9Mvq1DqB1BeNM')