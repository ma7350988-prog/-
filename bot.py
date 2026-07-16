import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# تحميل المتغيرات من ملف .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# إعداد البوت
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# عند تشغيل البوت بنجاح
@bot.event
async def on_ready():
    print(f'{bot.user} تم تسجيل الدخول بنجاح!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="المساعدة"))

# ترحيب عند انضمام عضو جديد
@bot.event
async def on_member_join(member):
    # البحث عن قناة welcome
    welcome_channel = discord.utils.get(member.guild.channels, name='welcome')
    
    if welcome_channel:
        embed = discord.Embed(
            title=f"مرحباً بك في {member.guild.name} 🎉",
            description=f"أهلا وسهلا {member.mention}!\nنتمنى لك وقتاً ممتعاً معنا",
            color=discord.Color.green()
        )
        embed.set_thumbnail(url=member.avatar.url)
        embed.set_image(url="https://media.discordapp.net/attachments/YOUR_IMAGE_URL")
        
        await welcome_channel.send(embed=embed)

# رد تلقائي على رسائل معينة
@bot.event
async def on_message(message):
    # تجنب الرد على رسائل البوت
    if message.author == bot.user:
        return
    
    # رد تلقائي على كلمات معينة
    if 'السلام عليكم' in message.content:
        await message.reply('وعليكم السلام ورحمة الله وبركاته 👋')
    
    if 'مرحبا' in message.content or 'hello' in message.content.lower():
        embed = discord.Embed(
            title="مرحباً!",
            description=f"مرحباً {message.author.mention}",
            color=discord.Color.blue()
        )
        embed.set_image(url="https://media.discordapp.net/attachments/YOUR_IMAGE_URL")
        await message.reply(embed=embed)
    
    # معالجة الأوامر العادية
    await bot.process_commands(message)

# أمر بسيط للاختبار
@bot.command(name='مرحبا')
async def hello(ctx):
    embed = discord.Embed(
        title="أهلا وسهلا!",
        description=f"السلام عليكم {ctx.author.mention}",
        color=discord.Color.purple()
    )
    embed.set_image(url="https://media.discordapp.net/attachments/YOUR_IMAGE_URL")
    embed.set_footer(text="بواسطة بوتك الخاص")
    
    await ctx.send(embed=embed)

# تشغيل البوت
bot.run(TOKEN)
