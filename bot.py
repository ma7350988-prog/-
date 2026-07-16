import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# تحميل المتغيرات من ملف .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

if not TOKEN:
    raise ValueError("DISCORD_TOKEN is not set in environment variables!")

# إعداد البوت
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# قاموس الردود التلقائية
auto_responses = {
    'السلام عليكم': 'وعليكم السلام ورحمة الله وبركاته 👋',
    'مرحبا': 'أهلا وسهلا بك! 😊',
    'hello': 'Hello! Welcome! 👋',
    'كيفك': 'الحمد لله أنا بخير، وأنت كيف حالك؟',
    'شكرا': 'لا شكر على واجب 😊',
    'thank you': 'You\'re welcome! 😊',
    'صباح الخير': 'صباح النور والسرور 🌞',
    'مساء الخير': 'مساء النور 🌙',
}

# عند تشغيل البوت بنجاح
@bot.event
async def on_ready():
    print(f'{bot.user} تم تسجيل الدخول بنجاح!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="الرسائل"))

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
        
        await welcome_channel.send(embed=embed)

# رد تلقائي على الرسائل
@bot.event
async def on_message(message):
    # تجنب الرد على رسائل البوت
    if message.author == bot.user:
        return
    
    # البحث عن كلمات مفتاحية والرد عليها
    message_content = message.content.lower().strip()
    
    for keyword, response in auto_responses.items():
        if keyword in message_content:
            await message.reply(response)
            return
    
    # معالجة الأوامر العادية
    await bot.process_commands(message)

# معالجة الأخطاء
@bot.event
async def on_error(event, *args, **kwargs):
    print(f'خطأ في {event}:')
    import traceback
    traceback.print_exc()

# تشغيل البوت
try:
    bot.run(TOKEN)
except Exception as e:
    print(f"فشل تشغيل البوت: {e}")
