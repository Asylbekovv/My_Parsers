import asyncio

import aiohttp
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent

BASE_URL = "https://ru.sputnik.kg/news/"
HEADERS = {"User-Agent": UserAgent().random}


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, headers=HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = BS(r, "html.parser")
            items = soup.find_all("list_content", {"class": "list_title"})
            for item in items:
                title = item.find("a", {"class": "list_title"}).text.strip()
                link = title.get("href")


    if __name__ == '__main__':
        main()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
