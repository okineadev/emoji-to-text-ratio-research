from pyrogram.client import Client
from pyrogram.types import Message
import emoji
from typing import List, Tuple
from progress.bar import IncrementalBar
from dotenv import load_dotenv
import argparse
import os

# Import uvloop if it was installed
try:
    import uvloop

    uvloop.install()
except ImportError:
    pass

load_dotenv()

# Identification data for Pyrogram
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
APP_NAME = "Emoji-to-text ratio analyzer"

CLIENT_OPTIONS = {"no_updates": True, "hide_password": True}
"Parameters of `pyrogram.Client`\n\nhttps://docs.pyrogram.org/api/client#pyrogram.Client"

DEFAULT_MESSAGE_LIMIT: int = 200
"Default number of messages for analysis"


def clean_text(text: str) -> str:
    """
    Cleans text

    :param text: Text for cleaning
    :return: Cleaned text
    """
    return text.encode("utf-8", "ignore").decode("utf-8")


def analyze_messages(messages: List[Message]) -> Tuple[int, int]:
    """
    Analyzes messages for text and emojis.

    :param messages: List of messages to analyze.
    :return: Number of emojis and total number of characters.
    """
    total_emojis: int = 0
    total_chars: int = 0

    for message in messages:
        if message.text:
            total_chars += len(message.text)
            total_emojis += emoji.emoji_count(clean_text(message.text))

    return total_emojis, total_chars


def format_result(chat_name: str, total_emojis: int, total_chars: int) -> str:
    """
    Formats the result for output.

    :param chat_name: Name of the chat for the result.
    :param total_emojis: Total number of emojis in the chat.
    :param total_chars: Total number of characters in the chat.
    :return: A string with the percentage ratio of emojis to text.
    """
    if total_chars == 0:
        emoji_percentage: float = 0.0
    else:
        emoji_percentage = (total_emojis / total_chars) * 100

    return f"{chat_name}: {emoji_percentage:.2f}% ({total_emojis} emojis per {total_chars} characters)\n"


async def main(chats: List[str], message_limit: int) -> None:
    async with Client(
        APP_NAME, api_id=API_ID, api_hash=API_HASH, **CLIENT_OPTIONS
    ) as app:
        for chat in chats:
            messages: List[Message] = []

            # Get chat information
            chat_info = await app.get_chat(chat)

            # Fetch message history
            with IncrementalBar(
                f"Analyzing messages in {chat_info.title}", max=message_limit
            ) as bar:
                async for message in app.get_chat_history(chat_info.id, limit=message_limit):  # type: ignore
                    messages.append(message)
                    bar.next()

            # Analyze the messages
            total_emojis, total_chars = analyze_messages(messages)

            # Output the result
            print(format_result(chat_info.title, total_emojis, total_chars))


if __name__ == "__main__":
    import asyncio

    # Command-line argument parsing
    parser = argparse.ArgumentParser(
        description="Analyze emoji-to-text ratio in Telegram chat messages."
    )
    parser.add_argument(
        "--chats",
        nargs="+",
        help="List of chat usernames or IDs to analyze.",
        required=True,
    )
    parser.add_argument(
        "--message-limit",
        type=int,
        default=DEFAULT_MESSAGE_LIMIT,
        help=f"Number of messages to analyze per chat (default: {DEFAULT_MESSAGE_LIMIT}).",
    )

    args = parser.parse_args()

    # Run the main function with the parsed arguments
    asyncio.run(main(chats=args.chats, message_limit=args.message_limit))
