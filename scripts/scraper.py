from dotenv import load_dotenv
import os
import pandas as pd
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest

# Load credentials from .telegram.env
load_dotenv(dotenv_path="telegram.env")

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient('session', api_id, api_hash)

# Telegram channels to fetch from
channels = [
    "@ZemenExpress",
    "@ethio_brand_collection",
    "@Shewabrand",
    "@Fashiontera",
    "@kuruwear",
    "@belaclassic",
    "@marakisat2",
    "@aradabrand2",
    "@marakibrand",
    "@classybrands",
    "@AwasMart"
]

async def fetch_all_messages(channel_username, max_total=2000):
    entity = await client.get_entity(channel_username)
    all_messages = []
    offset_id = 0

    while True:
        history = await client(
            GetHistoryRequest(
                peer=entity,
                limit=1000,
                offset_id=offset_id,
                offset_date=None,
                max_id=0,
                min_id=0,
                add_offset=0,
                hash=0
            )
        )

        messages = history.messages
        if not messages:
            break

        for msg in messages:
            if msg.message:
                media_path = f"{msg.id}_media" if msg.media else "N/A"
                all_messages.append([
                    entity.title,
                    channel_username,
                    msg.id,
                    msg.message,
                    msg.date.strftime('%Y-%m-%d %H:%M:%S'),
                    media_path
                ])

        offset_id = messages[-1].id
        print(f"[{channel_username}] Collected: {len(all_messages)}")

        if len(all_messages) >= max_total:
            break

    return all_messages

async def main():
    await client.start()
    all_data = []

    for channel in channels:
        try:
            data = await fetch_all_messages(channel, max_total=2000)
            all_data.extend(data)
        except Exception as e:
            print(f"❌ Error with {channel}: {e}")

    # Save to CSV
    os.makedirs("data/raw", exist_ok=True)
    df = pd.DataFrame(all_data, columns=[
        "Channel Title", "Channel Username", "ID", "Message", "Date", "Media Path"
    ])
    df.to_csv("data/raw/telegram_messages.csv", index=False, encoding="utf-8")
    print(f"✅ Scraping complete. {len(df)} messages saved to data/raw/telegram_messages.csv")

# Run it
with client:
    client.loop.run_until_complete(main())