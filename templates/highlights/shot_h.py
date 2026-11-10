import os
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch()
    for i in range(6):
        n=f'h{i}'
        pg=b.new_page(viewport={'width':1080,'height':1920})
        pg.goto(f'file://{os.getcwd()}/{n}.html'); pg.wait_for_timeout(1200)
        pg.evaluate("document.fonts.ready")
        pg.screenshot(path=f'out7/{n}.png')
        boxes=pg.evaluate("""()=>[...document.querySelectorAll('.chk')].map(e=>{const r=e.getBoundingClientRect();const t=(e.innerText||'').replace(/\\s+/g,' ').slice(0,26);return [t,Math.round(r.left),Math.round(r.top),Math.round(r.right),Math.round(r.bottom),e.scrollWidth>e.clientWidth+1]})""")
        # text overflow inside elements: check any element whose text exceeds its container
        over=pg.evaluate("""()=>{const out=[];document.querySelectorAll('.srow,.card').forEach(c=>{const cr=c.getBoundingClientRect();c.querySelectorAll('*').forEach(e=>{const r=e.getBoundingClientRect();if(r.width&&(r.right>cr.right-20||r.left<cr.left+20||r.bottom>cr.bottom-8))out.push([e.className||e.tagName,Math.round(r.left),Math.round(r.right),Math.round(r.bottom),Math.round(cr.bottom)])})});return out}""")
        print('==',n)
        bs=sorted(boxes,key=lambda b:b[2])
        for a in bs: print('  ',a)
        print('  OVERFLOW:',over[:6])
        pg.close()
    b.close()
