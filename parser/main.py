import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        print("Navigating to jett.uz...")
        await page.goto("https://jett.uz")
        
        # Ожидание загрузки основного контента (можно настроить под селекторы сайта)
        await page.wait_for_load_state("networkidle")
        
        content = await page.content()
        print(f"Page title: {await page.title()}")
        print(f"Content length: {len(content)} characters")
        
        # Здесь будет логика извлечения данных
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
