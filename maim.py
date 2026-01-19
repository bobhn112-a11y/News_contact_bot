from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

ADMIN_ID = 123456789  # سنعدله بعد قليل

async def receive(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message

    if msg.text:
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text="📩 خبر جديد:\n\n" + msg.text
        )

    elif msg.photo:
        await context.bot.send_photo(
            chat_id=ADMIN_ID,
            photo=msg.photo[-1].file_id,
            caption="📸 صورة خبر جديد"
        )

    elif msg.video:
        await context.bot.send_video(
            chat_id=ADMIN_ID,
            video=msg.video.file_id,
            caption="🎥 فيديو خبر جديد"
        )

    await msg.reply_text("✅ تم استلام الخبر، شكرًا لك.")

app = ApplicationBuilder().token("PUT_YOUR_BOT_TOKEN_HERE").build()
app.add_handler(MessageHandler(filters.ALL, receive))
app.run_polling()
