# 📊 Emoji-to-Text Ratio Research

I have always had a suspicion that Arabs (or Persians) use emojis in messages more than others, and somehow I decided to google this question, to which I did not find any answer, nor could the AI ​​say anything about it, the only person who except I guessed about it only in the comments under one video, who wrote "The Arabic language is cool, almost every letter is a smiley"

And I decided to solve this issue once and for all.

So I wrote this script that reads messages in chats and outputs the emoji to text ratio in the messages

<br>

I took [**Pyrogram FA**](https://t.me/PyrogramFA), [**Pyrogram Inn**](https://t.me/pyrogramchat) and [**Pyrogram UA**](https://t.me/UaPyrogram) chats as a basis, the results were as follows:

- 🥇 [Pyrogram FA](https://t.me/PyrogramFA): **0.68%** (52 emojis per 7633 characters)
- 🥈 [Pyrogram UA](https://t.me/UaPyrogram): **0.17%** (10 emojis per 5766 characters)
- 🥉 [Pyrogram Inn](https://t.me/pyrogramchat): **0.14%** (17 emojis per 12343 characters)

My guesses were confirmed!

Iranians are more than **4** times more likely to use emojis than others

<sup>My original Telegram post is https://t.me/okinea_blog/121</sup>

## 🚀 Features

- Analyze messages from multiple Telegram chats.
- Calculate the percentage of emojis used in the messages.

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/okineadev/emoji-to-text-ratio-research.git --depth=1
cd emoji-to-text-ratio-research
```

### 2. Deploy a virtual environment with .venv

> [!NOTE]
> Optional, but highly recommended to avoid conflicts with other packages that could lead to unexpected errors

```bash
python3 -m venv .venv
```

To enter the virtual environment, run the command below:

```bash
source .venv/bin/activate
```

If you're on **Windows**, run this command:

```powershell
.venv\Scripts\Activate.ps1
```

---

To exit the virtual environment:

```bash
deactivate
```

### 3. Install the required dependencies

Use `pip` to install the basic dependencies:

```bash
pip install -r requirements.txt
```

### 4. Optional Dependencies

To improve performance, you can install the optional dependencies:

```bash
pip install -r optional-requirements.txt
```

List of optional dependencies:

- [`tgcrypto`](https://pypi.org/project/TgCrypto/) - Speeds up cryptographic operations in [**🔥Pyrogram**](https://pyrogram.org/)
- [`uvloop`](https://pypi.org/project/uvloop/) - Makes `asyncio` **2-4x** faster

The script will still work without these, but with slightly reduced performance.

Dependencies list taken from https://docs.pyrogram.org/topics/speedups#speedups

## 🧑‍💻 Usage

Run the script with the following command:

```bash
python script.py --chats [CHATS] --message-limit [NUMBER_OF_MESSAGES]
```

### Command-Line Arguments:
- `--chats`: List of chat usernames or IDs you want to analyze (e.g. `PyrogramFA pyrogramchat`)
- `--message-limit`: Number of messages to analyze per chat (default is `200`)

### Example:

```bash
python scan.py --chats PyrogramFA pyrogramchat --message-limit 1000
```

This command will analyze the first 1000 messages from the `PyrogramFA` and `pyrogramchat` chats.

> [!TIP]
> The larger the `--message-limit`, the more accurate the results

## 📈 Output Example

```
Analyzing messages in 🔥 𝗣𝘆𝗿𝗼𝗴𝗿𝗮𝗺 𝗙𝗔 |████████████████████████████████| 1000/1000
🔥 𝗣𝘆𝗿𝗼𝗴𝗿𝗮𝗺 𝗙𝗔: 0.59% (219 emojis per 36918 characters)

Analyzing messages in Pyrogram Inn |████████████████████████████████| 1000/1000
Pyrogram Inn: 0.11% (75 emojis per 67860 characters)
```

## 💡 Notes

- If `tgcrypto` is installed, encryption performance will be improved
- If `uvloop` is installed, the event loop will automatically switch to `uvloop` for faster execution

## ⚠️ API Configuration

Ensure you have your API ID and API Hash from **Telegram** before running the script. You can get them by [creating a new Telegram application](https://my.telegram.org/apps).

Fill in the `API_ID` and `API_HASH` parameters in the [`.env.example`](.env.example) file:

```toml
API_ID=your_api_id_here
API_HASH="your_api_hash_here"
```

Then rename it to `.env` to make everything work

## 🤝 Contributing

Feel free to fork this repository and submit pull requests if you'd like to improve the script!

## 📜 License

This project is licensed under the Unlicense.
