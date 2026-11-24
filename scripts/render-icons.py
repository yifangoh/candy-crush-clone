"""Render the PNG app icons from icons/icon.svg and icons/icon-maskable.svg.

Usage:  pip install playwright && playwright install chromium
        python scripts/render-icons.py
"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

ICONS = Path(__file__).resolve().parent.parent / "icons"
JOBS = [
    ("icon.svg", "icon-512.png", 512),
    ("icon.svg", "icon-192.png", 192),
    ("icon.svg", "apple-touch-icon.png", 180),
    ("icon.svg", "favicon-32.png", 32),
    ("icon-maskable.svg", "icon-maskable-512.png", 512),
    ("icon-maskable.svg", "icon-maskable-192.png", 192),
]

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for src, out, size in JOBS:
            page = await browser.new_page(viewport={"width": size, "height": size})
            svg = (ICONS / src).read_text().replace('width="512" height="512"', f'width="{size}" height="{size}"', 1)
            await page.set_content(f'<html><body style="margin:0">{svg}</body></html>')
            await page.screenshot(path=str(ICONS / out), clip={"x": 0, "y": 0, "width": size, "height": size})
            await page.close()
            print("wrote", out)
        await browser.close()

asyncio.run(main())
