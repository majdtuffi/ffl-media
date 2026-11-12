import asyncio
from playwright.async_api import async_playwright
G="#DDB967"
S=f'fill="none" stroke="{G}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"'
S2=S.replace('stroke-width="7"','stroke-width="6"')
icons={
"howto":f'<rect x="18" y="26" width="84" height="76" rx="6" {S}/><path d="M18 48h84M40 16v20M80 16v20M44 76l12 12 22-24" {S}/>',
"reviews":f'<path d="M60 14l14.1 28.6 31.6 4.6-22.9 22.3 5.4 31.4L60 86.1 31.8 100.9l5.4-31.4L14.3 47.2l31.6-4.6z" {S}/>',
"delivery":f'<path d="M60 108S24 74 24 48a36 36 0 0 1 72 0c0 26-36 60-36 60z" {S}/><circle cx="60" cy="48" r="13" {S}/>',
"faq":f'<circle cx="60" cy="60" r="46" {S}/><path d="M45 47a15 15 0 1 1 22 13c-5 3-7 6-7 12" {S}/><circle cx="60" cy="87" r="4" fill="{G}" stroke="{G}"/>',
"fleet":f'<path d="M14 78V62l10-6 10-22a8 8 0 0 1 7-5h38a8 8 0 0 1 7 5l10 22 10 6v16a4 4 0 0 1-4 4H18a4 4 0 0 1-4-4z" {S}/><path d="M26 56h68M24 82v10M96 82v10" {S}/><circle cx="34" cy="68" r="4" {S}/><circle cx="86" cy="68" r="4" {S}/>',
"brands":f'<g transform="rotate(-45 60 60) translate(-9 -9) scale(1.15)"><path d="M26 36h18c8 0 14 6 14 14v20c0 8-6 14-14 14H26c-9 0-16-7-16-16V52c0-9 7-16 16-16z" {S2}/><rect x="19" y="52" width="9" height="16" rx="4.5" {S2}/><path d="M58 52h44l9 8-9 8H58" {S2}/><path d="M66 60h30" {S2}/></g>',
}
names={"howto":"How to Book","reviews":"Reviews","delivery":"Delivery","faq":"FAQ","fleet":"Fleet","brands":"Brands"}
def page(k):
    return f'''<html><body style="margin:0"><div style="width:1080px;height:1920px;background:#0C0C0E;position:relative">
<svg viewBox="0 0 120 120" style="position:absolute;left:290px;top:710px;width:500px;height:500px">{icons[k]}</svg></div></body></html>'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1080,"height":1920})
        for k in icons:
            await pg.set_content(page(k)); await pg.screenshot(path=f"out8/{k}.png")
        await b.close()
asyncio.run(main())
from PIL import Image
for k in icons:
    im=Image.open(f"out8/{k}.png").convert("RGB"); assert im.size==(1080,1920); im.save(f"out8/final/cover_{k}.jpg",quality=95,subsampling=0)
