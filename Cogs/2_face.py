import disnake
from disnake.ext import commands
import requests
import json
# from disnake.commands import 

client_id = "TikMmw1Tk3I8YAmbAXIb"
client_secret = "79SyD7Wwo0"


class face(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    # upload = SlashCommandGroup("업로드", "업로드 관련 명령어입니다.")
    @commands.command(name = "얼굴인식")
    async def _face(ctx,arg):
        await ctx.reply("인식할 얼굴의 사진을 보내주세요.",mention_author=False)
        
    
        url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식
        files = {'image': open('lee.jpg', 'rb')}
        headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
        response = requests.post(url,  files=files, headers=headers)
        rescode = response.status_code
        if rescode == 200:
            data = json.loads(response.text)
            faces = data["faces"][0]["celebrity"]["value"]
            print(faces)

def setup(bot):
    bot.add_cog(face(bot))