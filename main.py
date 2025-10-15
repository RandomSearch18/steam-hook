from steam.webapi import WebAPI
from dotenv import load_dotenv
from os import getenv


def main():
    steam = WebAPI(key=getenv("STEAM_API_KEY"))

    print(steam.ISteamWebAPIUtil.GetServerInfo())
    print(steam.call("ISteamWebAPIUtil.GetServerInfo"))


if __name__ == "__main__":
    load_dotenv()
    main()
