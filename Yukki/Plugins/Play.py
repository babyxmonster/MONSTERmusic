import asyncio
from os import path

from pyrogram import filters
from pyrogram.types import (InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto, Message,
                            Voice)
from youtube_search import YoutubeSearch

from Yukki import (BOT_USERNAME, DURATION_LIMIT, DURATION_LIMIT_MIN,
                   MUSIC_BOT_NAME, app, db_mem)
from Yukki.Core.PyTgCalls.Converter import convert
from Yukki.Core.PyTgCalls.Downloader import download
from Yukki.Decorators.assistant import AssistantAdd
from Yukki.Decorators.checker import checker
from Yukki.Decorators.permission import PermissionCheck
from Yukki.Decorators.admins import AdminRightsCheck
from Yukki.Inline import (playlist_markup, search_markup, search_markup2,
                          url_markup, url_markup2)
from Yukki.Utilities.changers import seconds_to_min, time_to_seconds
from Yukki.Utilities.chat import specialfont_to_normal
from Yukki.Utilities.stream import start_stream, start_stream_audio
from Yukki.Utilities.theme import check_theme
from Yukki.Utilities.thumbnails import gen_thumb
from Yukki.Utilities.url import get_url
from Yukki.Utilities.youtube import (get_yt_info_id, get_yt_info_query,
                                     get_yt_info_query_slider)
import os

from pyrogram.types import InlineKeyboardButton

UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL")
from pyrogram.errors import UserNotParticipant

loop = asyncio.get_event_loop()


DISABLED_GROUPS = []
useer = "NaN"


@app.on_message(filters.command(["player", f"player@{BOT_USERNAME}"])& ~filters.edited & ~filters.bot & ~filters.private)
@AdminRightsCheck
async def music_onoff(_, message: Message):
    user_id = message.from_user.id
    chat_title = message.chat.title
    global DISABLED_GROUPS
    try:
        user_id
    except:
        return
    if len(message.command) != 2:
        return await message.reply_text(
            "😕 **Ngetik yang bener bro :v.**\n\n» Coba `/musicplayer on` atau `/musicplayer off`"
        )
    status = message.text.split(None, 1)[1]
    message.chat.id
    if status in ("ON", "on", "On"):
        lel = await message.reply("`Processing...`")
        if not message.chat.id in DISABLED_GROUPS:
            return await lel.edit("» **Musiknya dah hidup Bro...**")
        DISABLED_GROUPS.remove(message.chat.id)
        await lel.edit(f"✅ **Musik dihidupin.**\n\n• Kalo bapak lu gabisa dihidupin...")

    elif status in ("OFF", "off", "Off"):
        lel = await message.reply("`Processing...`")

        if message.chat.id in DISABLED_GROUPS:
            return await lel.edit("» **Musiknya udah mati kek bapak lu...**")
        DISABLED_GROUPS.append(message.chat.id)
        await lel.edit(f"✅ **Musik dimatiin.**\n\n• Biar bisa nemenin bapak lu yg mati...")
    else:
        return await message.reply_text(
            "😕 **Ngetik yang bener bro :v.**\n\n» Coba `/musicplayer on` atau `/musicplayer off`"
        )


@app.on_message(
    filters.command(["play", f"play@{BOT_USERNAME}"]) & filters.group
)
@checker
@PermissionCheck
@AssistantAdd
async def play(_, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    rpk = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    update_channel = UPDATES_CHANNEL
    if update_channel:
        try:
            user = await app.get_chat_member(update_channel, user_id)
            if user.status == "kicked":
                await app.send_message(
                    chat_id,
                    text=f"**❌ {rpk} anda telah di blokir dari grup dukungan\n\n🔻 Klik tombol dibawah untuk menghubungi admin grup**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "✨ ɢʀᴇʏ ✨",
                                    url="https://t.me/greyupdate",
                                )
                            ]
                        ]
                    ),
                    parse_mode="markdown",
                    disable_web_page_preview=True,
                )
                return
        except UserNotParticipant:
            await app.send_message(
                chat_id,
                text=f"**👋🏻 Halo {rpk}\nʙɪᴀʀ ʏᴀɴɢ ᴍᴀᴋᴇ ɢᴀ ᴛᴇʀʟᴀʟᴜ ʙᴇʀʟᴇʙɪʜᴀɴ ʙᴏᴛ ɪɴɪ ᴋʜᴜꜱᴜꜱ ʙᴜᴀᴛ ʏᴀɴɢ ᴜᴅᴀʜ ᴊᴏɪɴ ᴄʜ ᴋᴀᴍɪ !! ᴛᴏʟᴏɴɢ ᴋᴇʀᴊᴀ ꜱᴀᴍᴀɴʏᴀ ʏᴀ ᴛᴏᴅ!​!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "💬 ᴊᴏɪɴ ᴄʜ sᴜᴘᴘᴏʀᴛ 💬",
                                url=f"https://t.me/{update_channel}",
                            )
                        ]
                    ]
                ),
                parse_mode="markdown",
            )
            return               
    global useer
    if message.chat.id in DISABLED_GROUPS:
        return await message.reply_text(f"😕 **Tolol {message.from_user.mention}, Musiknya dimatiin sama admin**")
    if message.chat.id not in db_mem:
        db_mem[message.chat.id] = {}
    if message.sender_chat:
        return await message.reply_text(
            "Lu admin __Anonymous Admin__ Di gc ini goblog !\nKembali ke admin biasa bego Jangan anon."
        )
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    url = get_url(message)
    if audio:
        mystic = await message.reply_text(
            "🔄 Memproses Audio tolol ...SABARR!"
        )

        if audio.file_size > 157286400:
            return await mystic.edit_text(
                "Ukuran audio harus kurang dari 150 mb"
            )
        duration_min = seconds_to_min(audio.duration)
        duration_sec = audio.duration
        if (audio.duration) > DURATION_LIMIT:
            return await mystic.edit_text(
                f"**Durasinya Kepanjangan Sayang**\n\n**Yang Boleh Cuman segini: **{DURATION_LIMIT_MIN} minute(s)\n**Yang Diterima:** {duration_min} minute(s)"
            )
        file_name = (
            audio.file_unique_id
            + "."
            + (
                (audio.file_name.split(".")[-1])
                if (not isinstance(audio, Voice))
                else "ogg"
            )
        )
        file_name = path.join(path.realpath("downloads"), file_name)
        file = await convert(
            (await message.reply_to_message.download(file_name))
            if (not path.isfile(file_name))
            else file_name,
        )
        return await start_stream_audio(
            message,
            file,
            "smex1",
            "Given Audio Via Telegram",
            duration_min,
            duration_sec,
            mystic,
        )
    elif url:
        mystic = await message.reply_text("🔄 Memproses URL... SABARR-YAA!")
        query = message.text.split(None, 1)[1]
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = get_yt_info_query(query)
        await mystic.delete()
        buttons = url_markup2(videoid, duration_min, message.from_user.id)
        return await message.reply_photo(
            photo=thumb,
            caption=f"☞JUDUL: **{title}\n\n☞DURASI:** {duration_min} Mins\n\n__[Lihat Info](https://t.me/{BOT_USERNAME}?start=info_{videoid})__",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        if len(message.command) < 2:
            buttons = playlist_markup(
                message.from_user.first_name, message.from_user.id, "abcd"
            )
            await message.reply_photo(
                photo="https://telegra.ph/file/09f3f39dd43de5b66d538.jpg",
                caption=(
                    "**Pakai:** /play [Judul lagu atau Link YouTube atau Reply to Audio]\n\nKALAU MAU MILIH! PILIH AJA NOH SENDIRI DI BAWAH JANGAN MANJA."
                ),
                reply_markup=InlineKeyboardMarkup(buttons),
            )
            return
        mystic = await message.reply_text("🔍 **MENCARI DULU COKK**...")
        query = message.text.split(None, 1)[1]
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = get_yt_info_query(query)
        await mystic.delete()
        buttons = url_markup(
            videoid, duration_min, message.from_user.id, query, 0
        )
        return await message.reply_photo(
            photo=thumb,
            caption=f"☞Judulnya: **{title}\n\n☞Durasinya:** {duration_min} Menit\n\n__[Lihat Info](https://t.me/{BOT_USERNAME}?start=info_{videoid})__",
            reply_markup=InlineKeyboardMarkup(buttons),
        )


@app.on_callback_query(filters.regex(pattern=r"Yukki"))
async def startyuplay(_, CallbackQuery):
    if CallbackQuery.message.chat.id not in db_mem:
        db_mem[CallbackQuery.message.chat.id] = {}
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    chat_id = CallbackQuery.message.chat.id
    chat_title = CallbackQuery.message.chat.title
    videoid, duration, user_id = callback_request.split("|")
    if str(duration) == "None":
        return await CallbackQuery.answer(
            f"Sorry! Its a Live Video.", show_alert=True
        )
    if CallbackQuery.from_user.id != int(user_id):
        return await CallbackQuery.answer(
            "SABAR INI BUKAN BUAT LU! CARI LAGU LU SENDIRI.", show_alert=True
        )
    await CallbackQuery.message.delete()
    title, duration_min, duration_sec, thumbnail = get_yt_info_id(videoid)
    if duration_sec > DURATION_LIMIT:
        return await CallbackQuery.message.reply_text(
            f"**Durasi kepanjangan anjing**\n\n**Yang boleh cuman segini: **{DURATION_LIMIT_MIN} minute(s)\n**Yang di terima:** {duration_min} minute(s)"
        )
    await CallbackQuery.answer(f"Sabar TOD:- {title[:20]}", show_alert=True)
    mystic = await CallbackQuery.message.reply_text(
        f"**{MUSIC_BOT_NAME} SABAR ASYUU**\n\n**JUDUL:** {title[:50]}\n\n0% ▓▓▓▓▓▓▓▓▓▓▓▓ 100%"
    )
    downloaded_file = await loop.run_in_executor(
        None, download, videoid, mystic, title
    )
    raw_path = await convert(downloaded_file)
    theme = await check_theme(chat_id)
    chat_title = await specialfont_to_normal(chat_title)
    thumb = await gen_thumb(thumbnail, title, user_id, theme, chat_title)
    if chat_id not in db_mem:
        db_mem[chat_id] = {}
    await start_stream(
        CallbackQuery,
        raw_path,
        videoid,
        thumb,
        title,
        duration_min,
        duration_sec,
        mystic,
    )


@app.on_callback_query(filters.regex(pattern=r"Search"))
async def search_query_more(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    query, user_id = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        return await CallbackQuery.answer(
            "CARI MUSIK LU SENDIRI. Lu ga boleh make tombol ini.",
            show_alert=True,
        )
    await CallbackQuery.answer("Cari Lebih Banyak Hasil")
    results = YoutubeSearch(query, max_results=5).to_dict()
    med = InputMediaPhoto(
        media="https://telegra.ph/file/b4712e461cb67f4a287b3.jpg",
        caption=(
            f"1️☞<b>{results[0]['title']}</b>\n  ┗  ↘ <u>__[Lihat info](https://t.me/{BOT_USERNAME}?start=info_{results[0]['id']})__</u>\n\n2️☞<b>{results[1]['title']}</b>\n  ┗  ↘ <u>__[Lihat Info](https://t.me/{BOT_USERNAME}?start=info_{results[1]['id']})__</u>\n\n3️☞<b>{results[2]['title']}</b>\n  ┗  ↘ <u>__[Lihat Info](https://t.me/{BOT_USERNAME}?start=info_{results[2]['id']})__</u>\n\n4️☞<b>{results[3]['title']}</b>\n  ┗  ↘ <u>__[Lihat Info](https://t.me/{BOT_USERNAME}?start=info_{results[3]['id']})__</u>\n\n5️☞<b>{results[4]['title']}</b>\n  ┗  ↘ <u>__[Lihat Info](https://t.me/{BOT_USERNAME}?start=info_{results[4]['id']})__</u>"
        ),
    )
    buttons = search_markup(
        results[0]["id"],
        results[1]["id"],
        results[2]["id"],
        results[3]["id"],
        results[4]["id"],
        results[0]["duration"],
        results[1]["duration"],
        results[2]["duration"],
        results[3]["duration"],
        results[4]["duration"],
        user_id,
        query,
    )
    return await CallbackQuery.edit_message_media(
        media=med, reply_markup=InlineKeyboardMarkup(buttons)
    )


@app.on_callback_query(filters.regex(pattern=r"popat"))
async def popat(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    userid = CallbackQuery.from_user.id
    i, query, user_id = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        return await CallbackQuery.answer(
            "Ini bukan buat lu tolol! Cari lagu lu sendiri", show_alert=True
        )
    results = YoutubeSearch(query, max_results=10).to_dict()
    if int(i) == 1:
        buttons = search_markup2(
            results[5]["id"],
            results[6]["id"],
            results[7]["id"],
            results[8]["id"],
            results[9]["id"],
            results[5]["duration"],
            results[6]["duration"],
            results[7]["duration"],
            results[8]["duration"],
            results[9]["duration"],
            user_id,
            query,
        )
        await CallbackQuery.edit_message_text(
            f"6️☞<b>{results[5]['title']}</b>\n  ┗  ↘ <u>__[Lihat Info](https://t.me/{BOT_USERNAME}?start=info_{results[5]['id']})__</u>\n\n7️☞<b>{results[6]['title']}</b>\n  ┗  ↘ <u>__[Lihat Info](https://t.me/{BOT_USERNAME}?start=info_{results[6]['id']})__</u>\n\n8️☞<b>{results[7]['title']}</b>\n  ┗  ↘ <u>__[Lihat Info](https://t.me/{BOT_USERNAME}?start=info_{results[7]['id']})__</u>\n\n9️☞<b>{results[8]['title']}</b>\n  ┗  ↘ <u>__[Lihat Info](https://t.me/{BOT_USERNAME}?start=info_{results[8]['id']})__</u>\n\n10☞<b>{results[9]['title']}</b>\n  ┗  ↘ <u>__[Lihat Info](https://t.me/{BOT_USERNAME}?start=info_{results[9]['id']})__</u>",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        disable_web_page_preview = True
        return
    if int(i) == 2:
        buttons = search_markup(
            results[0]["id"],
            results[1]["id"],
            results[2]["id"],
            results[3]["id"],
            results[4]["id"],
            results[0]["duration"],
            results[1]["duration"],
            results[2]["duration"],
            results[3]["duration"],
            results[4]["duration"],
            user_id,
            query,
        )
        await CallbackQuery.edit_message_text(
            f"1️☞<b>{results[0]['title']}</b>\n  ┗  ↘ <u>__[Lihat Info](https://t.me/{BOT_USERNAME}?start=info_{results[0]['id']})__</u>\n\n2️☞<b>{results[1]['title']}</b>\n  ┗  ↘ <u>__[Lihat Info](https://t.me/{BOT_USERNAME}?start=info_{results[1]['id']})__</u>\n\n3️☞<b>{results[2]['title']}</b>\n  ┗  ↘ <u>__[Lihat Info](https://t.me/{BOT_USERNAME}?start=info_{results[2]['id']})__</u>\n\n4️☞<b>{results[3]['title']}</b>\n  ┗  ↘ <u>__[Liat Info](https://t.me/{BOT_USERNAME}?start=info_{results[3]['id']})__</u>\n\n5️☞<b>{results[4]['title']}</b>\n  ┗  ↘ <u>__[Lihat Info](https://t.me/{BOT_USERNAME}?start=info_{results[4]['id']})__</u>",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        disable_web_page_preview = True
        return


@app.on_callback_query(filters.regex(pattern=r"slider"))
async def slider_query_results(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    what, type, query, user_id = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        return await CallbackQuery.answer(
            "CARI MUSIK LU SENDIRI. lu ga bole make tombol ini.",
            show_alert=True,
        )
    what = str(what)
    type = int(type)
    if what == "F":
        if type == 9:
            query_type = 0
        else:
            query_type = int(type + 1)
        await CallbackQuery.answer("Dapatkan hasil berikutnya", show_alert=True)
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = get_yt_info_query_slider(query, query_type)
        buttons = url_markup(
            videoid, duration_min, user_id, query, query_type
        )
        med = InputMediaPhoto(
            media=thumb,
            caption=f"☞Judulnya: **{title}\n\n☞Durasinya:** {duration_min} Menit\n\n__[Lihat Info](https://t.me/{BOT_USERNAME}?start=info_{videoid})__",
        )
        return await CallbackQuery.edit_message_media(
            media=med, reply_markup=InlineKeyboardMarkup(buttons)
        )
    if what == "B":
        if type == 0:
            query_type = 9
        else:
            query_type = int(type - 1)
        await CallbackQuery.answer("Mendapatkan hasil sebelumnya", show_alert=True)
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = get_yt_info_query_slider(query, query_type)
        buttons = url_markup(
            videoid, duration_min, user_id, query, query_type
        )
        med = InputMediaPhoto(
            media=thumb,
            caption=f"☞Judulnya: **{title}\n\n☞Durasinya:** {duration_min} Menit\n\n__[Lihat Info](https://t.me/{BOT_USERNAME}?start=info_{videoid})__",
        )
        return await CallbackQuery.edit_message_media(
            media=med, reply_markup=InlineKeyboardMarkup(buttons)
        )
