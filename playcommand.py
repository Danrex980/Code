import os

import discord
from discord.ext import commands
import youtube_dl


class PlayCommand(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

    @commands.command(name='play')
    async def play(self, ctx, url):
        voicec = ctx.author.voice
        if voicec:
            channel = voicec.channel
            if channel:
                songname = f'songs/{ctx.guild.id}_current.mp3'
                song_there = os.path.isfile(songname)
                try:
                    if song_there:
                        os.remove(songname)
                        print('Removed old song file')
                except PermissionError:
                    print('Trying to delte file , buit its beeing played')
                    await ctx.send('Error: Music playing')
                    return

                voice = await channel.connect()
                ydl_opts = {
                    'format': "bestaudio/best",
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192'
                    }]
                }

                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    print('Donwloading audio now\n')
                    ydl.download([url])

                for file in os.listdir('./'):
                    if file.endswith('.mp3'):
                        print(f'Renamed file: {file}\n')
                        os.rename(file, songname)

                voice.play(discord.FFmpegPCMAudio(songname), after=lambda e: print('Song zu ende.'))
                voice.source = discord.PCMVolumeTransformer(voice.source)

                print('Ok.')

        #################################################


async def setup(bot):
    await bot.add_cog(PlayCommand(bot))
