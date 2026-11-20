import asyncio
from playwright.async_api import async_playwright
fg=open('design/fg.svg').read()
inner=fg.split('>',1)[1].rsplit('</svg>',1)[0]
def page(w,h,body): return f'<html><body style="margin:0;width:{w}px;height:{h}px;overflow:hidden">{body}</body></html>'
icon=f'<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024"><rect width="1024" height="1024" fill="#0f1418"/><g transform="translate(512 512) scale(1.12) translate(-512 -540)">{inner}</g></svg>'
icon512=icon.replace('width="1024" height="1024" viewBox','width="512" height="512" viewBox')
# adaptive foreground: content within central 66% safe zone
fgad=f'<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024"><g transform="translate(512 512) scale(0.78) translate(-512 -540)">{inner}</g></svg>'
bg='<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024"><rect width="1024" height="1024" fill="#0f1418"/></svg>'
splash=f'<svg xmlns="http://www.w3.org/2000/svg" width="2732" height="2732"><rect width="2732" height="2732" fill="#0f1418"/><g transform="translate(1366 1300) scale(0.7) translate(-512 -540)">{inner}</g><text x="1366" y="1820" fill="#eef2f4" font-family="Roboto,Arial,sans-serif" font-size="120" font-weight="700" text-anchor="middle">HV Network Driver</text></svg>'
feature=f'''<div style="width:1024px;height:500px;background:linear-gradient(135deg,#0f1418,#1c2830);display:flex;align-items:center;font-family:Roboto,Arial,sans-serif;color:#eef2f4">
<svg width="360" height="360" viewBox="0 0 1024 1024" style="margin:0 30px 0 50px"><g transform="translate(512 512) scale(1.12) translate(-512 -540)">{inner}</g></svg>
<div><div style="font-size:62px;font-weight:800;line-height:1.05">HV Network<br>Driver</div>
<div style="font-size:28px;color:#ffb000;font-weight:700;margin-top:18px">Know you're on an approved network</div>
<div style="font-size:22px;color:#93a3ae;margin-top:10px">Heavy vehicle maps · Route alerts · Break timer</div></div></div>'''
jobs=[('assets/icon-only.png',1024,1024,icon),('assets/icon-foreground.png',1024,1024,fgad),('assets/icon-background.png',1024,1024,bg),
      ('assets/splash.png',2732,2732,splash),('assets/splash-dark.png',2732,2732,splash),
      ('store/icon-512.png',512,512,icon512),('store/feature-graphic-1024x500.png',1024,500,feature)]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for path,w,h,body in jobs:
            pg=await b.new_page(viewport={'width':w,'height':h})
            await pg.set_content(page(w,h,body)); await pg.wait_for_timeout(150)
            await pg.screenshot(path=path,omit_background=('foreground' in path))
            await pg.close()
        await b.close()
import os; os.makedirs('store',exist_ok=True)
asyncio.run(main())
