import json

from discord.ext import commands
import random
import os


class Bot(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.grixa_images = []
        self.channel = client.get_channel(746740813815480360)
        self.read_images()

    def read_images(self):
        cwd = os.getcwd()
        with open(f'{cwd}/cogs/griha.txt') as f:
            self.grixa_images = f.readlines()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot is running!')

    # @commands.Cog.listener()
    # async def on_command_error(self, context, error):
    #     senderStr = str(context.author).lower()
    #     index = senderStr.find('#')
    #     sender = senderStr[0:index]
    #     await context.send(f'блять, {sender} ты конченый? ты хоть сам понимаешь, блять, какую хуйню сейчас спизданул?'
    #                        f'иди в пизду, говна кусок, научись манерам хуила.'
    #                        f'животное, блять. отсоси мой бинарный хуй, сука.')

    @commands.command()
    async def test(self, context):
        await context.send('aaa')

    @commands.command()
    async def rpuxa(self, contex):
        image = random.choice(self.grixa_images)
        await contex.send(image)

    @commands.command()
    async def film(self, context):
        film = self.get_film()
        msg = f"""
        Что посмотреть? Надо подумать... Есть один фильм... Вчера посмотрел, думаю тебе точно должно понравиться, тебе вроде нравится этот режиссер. Лови ссылку, дружище, и приятного просмотра!
{film['name']}
Оценка на кинопоиске - {film['rating']}
{film['link']}
        """
        await context.send(msg)

    def get_film(self):
        cwd = os.getcwd()
        with open(f'{cwd}/cogs/films.txt') as file:
            films = json.load(file)
        return random.choice(films)


def setup(client):
    client.add_cog(Bot(client))
