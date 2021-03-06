# Credits: @ANDXINN

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="โข ๐ง๐ฒ๐ป๐๐ฎ๐ป๐ด ๐ฆ๐ฎ๐๐ฎ โข", callback_data="about"),
                InlineKeyboardButton(text="โข ๐ง๐๐๐๐ฝ โข", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="๐๐ผ๐ถ๐ป ๐๐ฟ๐ผ๐๐ฝ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="โข ๐ง๐ฒ๐ป๐๐ฎ๐ป๐ด ๐ฆ๐ฎ๐๐ฎ โข", callback_data="about"),
                InlineKeyboardButton(text="โข ๐ง๐๐๐๐ฝ โข", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="แดแดษชษด แดสแดษดษดแดส", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="โข แดแดษดแดแดษดษข sแดสแด โข", callback_data="about"),
                InlineKeyboardButton(text="โข แดแดแดแดแด โข", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="โข แดแดษดแดแดษดษข sแดสแด โข", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="๐๐ผ๐ถ๐ป ๐๐ต๐ฎ๐ป๐ป๐ฒ๐น", url=client.invitelink),
                InlineKeyboardButton(text="๐๐ผ๐ถ๐ป ๐๐ฟ๐ผ๐๐ฝ", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="โข ๐ง๐๐๐๐ฝ โข", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="๐๐ผ๐ถ๐ป ๐๐ฟ๐ผ๐๐ฝ", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="๐๐ผ๐ฏ๐ฎ ๐๐ฎ๐ด๐ถ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="แดแดษชษด แดสแดษดษดแดส", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="๐๐ผ๐ฏ๐ฎ ๐๐ฎ๐ด๐ถ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="๐๐ผ๐ถ๐ป ๐๐ต๐ฎ๐ป๐ป๐ฒ๐น", url=client.invitelink),
                InlineKeyboardButton(text="๐๐ผ๐ถ๐ป ๐๐ฟ๐ผ๐๐ฝ", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="๐๐ผ๐ฏ๐ฎ ๐๐ฎ๐ด๐ถ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
