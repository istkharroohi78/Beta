from PritiMusic.misc import SUDOERS
from PritiMusic.utils.database import get_lang, is_maintenance
from strings import get_string
from config import SUPPORT_CHAT

# 🟢 'app' ka import hata diya gaya hai kyunki ab hum dynamic client use karenge

def language(mystic):
    async def wrapper(client, message, **kwargs):
        if await is_maintenance() is False:
            if message.from_user.id not in SUDOERS:
                # 🟢 CLONE FIX: Sahi bot ka naam (mention) nikalne ke liye
                try:
                    bot = await client.get_me()
                    bot_mention = bot.mention
                except:
                    bot_mention = "Bᴏᴛ"
                    
                return await message.reply_text(
                    text=f"{bot_mention} ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ, ᴠɪsɪᴛ <a href={SUPPORT_CHAT}>sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ</a> ғᴏʀ ᴋɴᴏᴡɪɴɢ ᴛʜᴇ ʀᴇᴀsᴏɴ.",
                    disable_web_page_preview=True,
                )
        try:
            await message.delete()
        except:
            pass

        try:
            language_code = await get_lang(message.chat.id)
            language_str = get_string(language_code)
        except:
            language_str = get_string("en")
            
        return await mystic(client, message, language_str)

    return wrapper


def languageCB(mystic):
    async def wrapper(client, CallbackQuery, **kwargs):
        if await is_maintenance() is False:
            if CallbackQuery.from_user.id not in SUDOERS:
                # 🟢 CLONE FIX
                try:
                    bot = await client.get_me()
                    bot_mention = bot.mention
                except:
                    bot_mention = "Bᴏᴛ"
                    
                return await CallbackQuery.answer(
                    f"{bot_mention} ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ, ᴠɪsɪᴛ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ ғᴏʀ ᴋɴᴏᴡɪɴɢ ᴛʜᴇ ʀᴇᴀsᴏɴ.",
                    show_alert=True,
                )
        try:
            language_code = await get_lang(CallbackQuery.message.chat.id)
            language_str = get_string(language_code)
        except:
            language_str = get_string("en")
            
        return await mystic(client, CallbackQuery, language_str)

    return wrapper


def LanguageStart(mystic):
    async def wrapper(client, message, **kwargs):
        try:
            language_code = await get_lang(message.chat.id)
            language_str = get_string(language_code)
        except:
            language_str = get_string("en")
            
        return await mystic(client, message, language_str)

    return wrapper
