import asyncio

from pyrogram import Client

TG = """
Pirated Repo😬 https://github.coM/TG-MUSICS/telegrAM_VC_BOT
"""

print(TG)
api_id = input("Enter Your API ID: \n")
api_hash = input("Enter Your API HASH : \n")


async def main():
    async with Client(":memory:", api_id=int(input("API ID:")), api_hash=input("API HASH:")) as app:
        print(await app.export_session_string())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
