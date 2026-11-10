# FAQ highlight, flat formal template (reuses k_gen.py CSS/helpers)
import os
src=open('k_gen.py').read(); exec(src[:src.index("build('h0'")])
CSS+='.slide .qn{margin-left:18px}.slide.en .qn{margin-left:0;margin-right:18px}'
def qa(top,h,q,a,s=None):
    return f'<div class="card chk" style="top:{top}px;height:{h}px"><div class="c-h">{q}</div><div class="c-i" style="line-height:1.5">{a}</div>'+(f'<div class="c-s">{s}</div>' if s else '')+'</div>'
N='<span class="num">'
build('q0', head('أسئلة شائعة','<span class="num qn" style="display:inline-flex;align-items:center;justify-content:center;width:56px;height:56px;border:2px solid #C99A20;border-radius:50%;color:#C99A20;font-weight:700;font-size:32px;line-height:1;vertical-align:middle;position:relative;top:-3px">1</span>كل اللي تبي تعرفه قبل الحجز')+
  qa(800,250,'كم كيلو مسموح باليوم؟',f'{N}250</span>&nbsp;كم باليوم')+
  qa(1070,250,'كيف ينحسب سالك؟','حسب البوابات اللي تمرّ منها','ونعطيك الكشف عند تسليم السيارة')+
  qa(1340,250,'التوصيل مجاني؟','نعم، توصيل واستلام مجاني','داخل دبي')+contact(1620))
build('q1', head('أسئلة شائعة','<span class="num qn" style="display:inline-flex;align-items:center;justify-content:center;width:56px;height:56px;border:2px solid #C99A20;border-radius:50%;color:#C99A20;font-weight:700;font-size:32px;line-height:1;vertical-align:middle;position:relative;top:-3px">2</span>الدفع والحجز')+
  qa(800,250,'فيه وديعة تأمين؟','لا، بدون وديعة تأمين')+
  qa(1070,250,'شنو طرق الدفع؟',f'كاش، بطاقة، {N}Tabby</span> أو {N}Tamara</span>')+
  qa(1340,250,'كيف أحجز؟','عبر واتساب أو من الموقع',f'{N}www.ffl.ae</span>')+contact(1620))
build('q2', head('أسئلة شائعة','<span class="num qn" style="display:inline-flex;align-items:center;justify-content:center;width:56px;height:56px;border:2px solid #C99A20;border-radius:50%;color:#C99A20;font-weight:700;font-size:32px;line-height:1;vertical-align:middle;position:relative;top:-3px">3</span>الأوراق المطلوبة')+
  lst(800,360,'للمقيمين ومواطني الخليج',['صورة الهوية','رخصة القيادة','جواز السفر'])+
  lst(1190,360,'للزوار والسياح',['صورة جواز السفر','رخصة قيادة دولية','تأشيرة الدخول'])+contact(1620))
build('q3', head('FAQ','<span class="num qn" style="display:inline-flex;align-items:center;justify-content:center;width:56px;height:56px;border:2px solid #C99A20;border-radius:50%;color:#C99A20;font-weight:700;font-size:32px;line-height:1;vertical-align:middle;position:relative;top:-3px">1</span>Good to know before you book')+
  qa(800,250,'How many km are included?','250 km per day')+
  qa(1070,250,'How is Salik charged?','Per toll gate you pass','Statement provided at return')+
  qa(1340,250,'Is delivery free?','Yes, free delivery &amp; pickup','Within Dubai')+contact(1620),True)
build('q4', head('FAQ','<span class="num qn" style="display:inline-flex;align-items:center;justify-content:center;width:56px;height:56px;border:2px solid #C99A20;border-radius:50%;color:#C99A20;font-weight:700;font-size:32px;line-height:1;vertical-align:middle;position:relative;top:-3px">2</span>Payment &amp; booking')+
  qa(800,250,'Is there a security deposit?','No deposit required')+
  qa(1070,250,'How can I pay?','Cash, card, Tabby or Tamara')+
  qa(1340,250,'How do I book?','On WhatsApp or on our website','www.ffl.ae')+contact(1620),True)
build('q5', head('FAQ','<span class="num qn" style="display:inline-flex;align-items:center;justify-content:center;width:56px;height:56px;border:2px solid #C99A20;border-radius:50%;color:#C99A20;font-weight:700;font-size:32px;line-height:1;vertical-align:middle;position:relative;top:-3px">3</span>Required documents')+
  lst(800,360,'UAE &amp; GCC residents',['ID copy','Driving licence','Passport'])+
  lst(1190,360,'Tourists &amp; visitors',['Passport copy','International driving licence','Entry visa'])+contact(1620),True)
from playwright.sync_api import sync_playwright
from PIL import Image
with sync_playwright() as p:
    b=p.chromium.launch()
    for i in range(6):
        n=f'q{i}'; pg=b.new_page(viewport={'width':1080,'height':1920})
        pg.goto(f'file://{os.getcwd()}/{n}.html'); pg.wait_for_timeout(1200); pg.evaluate("document.fonts.ready")
        pg.screenshot(path=f'out9/{n}.png')
        over=pg.evaluate("""()=>{const out=[];document.querySelectorAll('.card').forEach(c=>{const cr=c.getBoundingClientRect();c.querySelectorAll('*').forEach(e=>{const r=e.getBoundingClientRect();if(r.width&&(r.right>cr.right-20||r.left<cr.left+20||r.bottom>cr.bottom-8||r.top<cr.top+8))out.push([e.className||e.tagName,Math.round(r.left),Math.round(r.right),Math.round(r.bottom),Math.round(cr.bottom)])})});document.querySelectorAll('.t').forEach(e=>{if(e.scrollWidth>e.clientWidth+1)out.push(['T-OVER',e.innerText])});const s=document.querySelector('.sub'),c=document.querySelector('.card');if(s&&s.getBoundingClientRect().bottom>c.getBoundingClientRect().top-20)out.push(['SUB-COLLIDE']);return out}""")
        lines=pg.evaluate("""()=>[...document.querySelectorAll('.c-i,.c-s,.c-h,.h1,.sub')].filter(e=>e.getBoundingClientRect().height>parseFloat(getComputedStyle(e).lineHeight)*1.5+ (e.classList.contains('c-h')?20:0)).map(e=>e.innerText)""")
        print(n,'OVER:',over,'WRAPPED:',lines); pg.close()
        im=Image.open(f'out9/{n}.png').convert('RGB'); assert im.size==(1080,1920); im.save(f'out9/final/faq_{i+1}.jpg',quality=95,subsampling=0)
    b.close()
