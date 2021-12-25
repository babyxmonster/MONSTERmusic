from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def check_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"ɢʀᴜᴘ ᴘʟᴀʏʟɪꜱᴛ",
                callback_data=f"playlist_check {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]} ᴅᴀꜰᴛᴀʀ ᴘᴜᴛᴀʀ",
                callback_data=f"playlist_check {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
    ]
    return buttons


def playlist_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"ɢʀᴜᴘ ᴘʟᴀʏʟɪꜱᴛ",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]} ᴅᴀꜰᴛᴀʀ ᴘᴜᴛᴀʀ",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
    ]
    return buttons


def play_genre_playlist(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"ʙᴏʟʟʏᴡᴏᴏᴅ",
                callback_data=f"play_playlist {user_id}|{type}|Bollywood",
            ),
            InlineKeyboardButton(
                text=f"ʜᴏʟʟʏᴡᴏᴏᴅ",
                callback_data=f"play_playlist {user_id}|{type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ᴘᴀʀᴛʏ",
                callback_data=f"play_playlist {user_id}|{type}|Party",
            ),
            InlineKeyboardButton(
                text=f"ʟᴏғɪ",
                callback_data=f"play_playlist {user_id}|{type}|Lofi",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"sᴀᴅ",
                callback_data=f"play_playlist {user_id}|{type}|Sad",
            ),
            InlineKeyboardButton(
                text=f"ᴡᴇᴇʙ",
                callback_data=f"play_playlist {user_id}|{type}|Weeb",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ᴘᴜɴᴊᴀʙɪ",
                callback_data=f"play_playlist {user_id}|{type}|Punjabi",
            ),
            InlineKeyboardButton(
                text=f"ʟᴀɪɴɴʏᴀ",
                callback_data=f"play_playlist {user_id}|{type}|Others",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ᴛᴏᴍʙᴏʟ ᴋᴇᴍʙᴀʟɪ",
                callback_data=f"main_playlist {videoid}|{type}|{user_id}",
            ),
            InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
        ],
    ]
    return buttons


def add_genre_markup(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"✚ ᴡᴇᴇʙ",
                callback_data=f"add_playlist {videoid}|{type}|Weeb",
            ),
            InlineKeyboardButton(
                text=f"✚ sᴀᴅ",
                callback_data=f"add_playlist {videoid}|{type}|Sad",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ ᴘᴀʀᴛʏ",
                callback_data=f"add_playlist {videoid}|{type}|Party",
            ),
            InlineKeyboardButton(
                text=f"✚ ʟᴏғɪ",
                callback_data=f"add_playlist {videoid}|{type}|Lofi",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ ʙᴏʟʟʏᴡᴏᴏᴅ",
                callback_data=f"add_playlist {videoid}|{type}|Bollywood",
            ),
            InlineKeyboardButton(
                text=f"✚ ʜᴏʟʟʏᴡᴏᴏᴅ",
                callback_data=f"add_playlist {videoid}|{type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ ᴘᴜɴᴊᴀʙɪ",
                callback_data=f"add_playlist {videoid}|{type}|Punjabi",
            ),
            InlineKeyboardButton(
                text=f"✚ ʟᴀɪɴɴʏᴀ",
                callback_data=f"add_playlist {videoid}|{type}|Others",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ᴛᴏᴍʙᴏʟ ᴋᴇᴍʙᴀʟɪ", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
        ],
    ]
    return buttons


def check_genre_markup(type, videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"ᴡᴇᴇʙ", callback_data=f"check_playlist {type}|Weeb"
            ),
            InlineKeyboardButton(
                text=f"sᴀᴅ", callback_data=f"check_playlist {type}|Sad"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ᴘᴀʀᴛʏ", callback_data=f"check_playlist {type}|Party"
            ),
            InlineKeyboardButton(
                text=f"ʟᴏғɪ", callback_data=f"check_playlist {type}|Lofi"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ʙᴏʟʟʏᴡᴏᴏᴅ",
                callback_data=f"check_playlist {type}|Bollywood",
            ),
            InlineKeyboardButton(
                text=f"ʜᴏʟʟʏᴡᴏᴏᴅ",
                callback_data=f"check_playlist {type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"ᴘᴜɴᴊᴀʙɪ",
                callback_data=f"check_playlist {type}|Punjabi",
            ),
            InlineKeyboardButton(
                text=f"ʟᴀɪɴɴʏᴀ", callback_data=f"check_playlist {type}|Others"
            ),
        ],
        [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
    ]
    return buttons


def third_playlist_markup(user_name, user_id, third_name, userid, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"ɢʀᴜᴘ ᴘʟᴀʏʟɪꜱᴛ",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]} ᴅᴀꜰᴛᴀʀ ᴘᴜᴛᴀʀ",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{third_name[:16]} ᴅᴀꜰᴛᴀʀ ᴘᴜᴛᴀʀ",
                callback_data=f"show_genre {userid}|third|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
    ]
    return buttons


def paste_queue_markup(url):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"resumecb"),
            InlineKeyboardButton(text="II", callback_data=f"pausecb"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"skipcb"),
            InlineKeyboardButton(text="▢", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton(text="ʟɪʜᴀᴛ ᴀɴᴛʀɪᴀɴ ᴅᴀꜰᴛᴀʀ ᴘᴜᴛᴀʀ", url=f"{url}")],
        [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data=f"close")],
    ]
    return buttons


def fetch_playlist(user_name, type, genre, user_id, url):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Play {user_name[:10]} {genre} ᴘʟᴀʏʟɪsᴛ",
                callback_data=f"play_playlist {user_id}|{type}|{genre}",
            ),
        ],
        [InlineKeyboardButton(text="ʟɪʜᴀᴛ ᴀɴᴛʀɪᴀɴ ᴅᴀꜰᴛᴀʀ ᴘᴜᴛᴀʀ", url=f"{url}")],
        [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data=f"close")],
    ]
    return buttons


def delete_playlist_markuup(type, genre):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"ʏᴀ! ʜᴀᴘᴜꜱ",
                callback_data=f"delete_playlist {type}|{genre}",
            ),
            InlineKeyboardButton(text="ᴛɪᴅᴀᴋ!", callback_data=f"close"),
        ],
    ]
    return buttons
