# بوت Discord مع رد تلقائي وترحيب بصورة

## المميزات 🎉
- ✅ ترحيب تلقائي للأعضاء الجدد مع صورة
- ✅ رد تلقائي على رسائل معينة
- ✅ رسائل مزينة (Embeds) مع صور
- ✅ دعم اللغة العربية

## التثبيت 📦

### المتطلبات:
- Python 3.8+
- pip

### الخطوات:

1. استنساخ المشروع أو تحميل الملفات
```bash
git clone <repository_url>
cd <repository_folder>
```

2. تثبيت المتطلبات:
```bash
pip install -r requirements.txt
```

3. إنشاء بوت على Discord:
   - اذهب إلى [Discord Developer Portal](https://discord.com/developers/applications)
   - انقر على "New Application"
   - أعط البوت اسماً
   - اذهب إلى "Bot" وانقر "Add Bot"
   - انسخ التوكن

4. تعديل ملف `.env`:
```
DISCORD_TOKEN=your_bot_token_here
```

5. تشغيل البوت:
```bash
python bot.py
```

## الأوامر الأساسية 🎮

| الأمر | الوصف |
|------|-------|
| `!مرحبا` | يرد البوت بترحيب |
| `السلام عليكم` | رد تلقائي |
| `مرحبا` أو `hello` | رد تلقائي مع صورة |

## تخصيص الصور 🖼️

لإضافة صورتك الخاصة:
1. ارفع الصورة على Discord في أي قناة
2. انقر بزر الماوس الأيمن واختر "Copy Link"
3. استبدل `YOUR_IMAGE_URL` برابط الصورة في الكود

مثال:
```python
embed.set_image(url="https://media.discordapp.net/attachments/...")
```

## ملاحظات مهمة ⚠️

- تأكد من أن البوت لديه صلاحيات إرسال الرسائل في الخوادم
- أنشئ قناة باسم `welcome` للترحيب التلقائي
- لا تشارك توكن البوت مع أحد!

## الدعم 💬
للمزيد من المساعدة، اقرأ [وثائق discord.py](https://discordpy.readthedocs.io/)
