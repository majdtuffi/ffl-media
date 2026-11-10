# formal, flat design (v2) for How-to-Book highlight, 1080x1920
CSS='''
@import url(base.css);
body{background:#0C0C0E}
.slide{position:relative;width:1080px;height:1920px;overflow:hidden;background:#0C0C0E;direction:rtl;text-align:center}
.slide.en{direction:ltr}
.frame{position:absolute;inset:44px;border:1px solid rgba(201,154,32,.45);border-radius:0}
.logo{position:absolute;left:50%;transform:translateX(-50%);top:175px;width:310px;mix-blend-mode:normal}
.t{position:absolute;left:90px;right:90px;text-align:center}
.h1{top:470px;font-size:96px;font-weight:800;color:#F5F5F7;line-height:1.3}
.slide.en .h1{font-size:84px;white-space:nowrap}
.rule{position:absolute;left:50%;transform:translateX(-50%);top:640px;width:110px;height:3px;background:#C99A20}
.sub{top:672px;font-size:42px;font-weight:500;color:rgba(245,245,247,.68);line-height:1.5}
.card{position:absolute;left:100px;right:100px;border:1px solid rgba(255,255,255,.14);background:#151517;border-radius:6px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 40px}
.c-n{width:60px;height:60px;border:2px solid #C99A20;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:Inter;font-weight:700;font-size:32px;color:#C99A20;margin-bottom:12px}
.c-t{font-size:48px;font-weight:700;color:#F5F5F7;line-height:1.35}
.c-s{font-size:32px;font-weight:500;color:rgba(245,245,247,.62);line-height:1.5;margin-top:4px}
.c-h{font-size:36px;font-weight:700;color:#C99A20;line-height:1.3;padding-bottom:16px;margin-bottom:18px;border-bottom:1px solid rgba(201,154,32,.4);width:100%}
.c-i{font-size:44px;font-weight:600;color:#F5F5F7;line-height:1.75}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;width:100%}
.slide:not(.en) .grid span{font-family:'Noto Kufi Arabic',sans-serif !important}
.grid span{display:flex;align-items:center;justify-content:center;height:92px;line-height:1;border:1px solid rgba(201,154,32,.55);border-radius:4px;padding:0;font-size:38px;font-weight:700;color:#F5F5F7;text-align:center;font-family:Inter,"Noto Kufi Arabic"}
.contact{direction:ltr;position:absolute;left:100px;right:100px;text-align:center;border-top:1px solid rgba(255,255,255,.14);padding-top:30px}
.contact .num{font-size:42px;font-weight:600;color:#F5F5F7;letter-spacing:.5px;white-space:nowrap}
.contact i{display:inline-block;width:2px;height:34px;background:#C99A20;margin:0 26px;vertical-align:-6px}
'''
def head(t,s=None):
    h=f'<div class="t h1 chk">{t}</div><div class="rule"></div>'
    if s: h+=f'<div class="t sub chk">{s}</div>'
    return h
def step(top,n,t,s):
    return f'<div class="card chk" style="top:{top}px;height:230px"><div class="c-n"><span class="num">{n}</span></div><div class="c-t">{t}</div><div class="c-s">{s}</div></div>'
def lst(top,h,head_,items):
    return f'<div class="card chk" style="top:{top}px;height:{h}px"><div class="c-h">{head_}</div>'+''.join(f'<div class="c-i">{i}</div>' for i in items)+'</div>'
def one(top,h,head_,item):
    return lst(top,h,head_,[item])
def contact(top): return f'<div class="contact chk" style="top:{top}px"><span class="num">+971 50 501 3635</span><i></i><span class="num">www.ffl.ae</span></div>'
def build(name,body,en=False):
    open(name+'.html','w').write(f'<!doctype html><html lang="{"en" if en else "ar"}" dir="{"ltr" if en else "rtl"}"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="slide{" en" if en else ""}"><div class="frame"></div><img class="logo" src="logo_t.png">{body}</div></body></html>')
build('h0', head('احجز في دقائق','ثلاث خطوات وسيارتك جاهزة')+
  step(800,1,'اختر سيارتك وتواريخك','من الموقع أو عبر واتساب')+
  step(1060,2,'أرسل أوراقك','نراجعها ونتواصل معك')+
  step(1320,3,'نوصّل لك السيارة','توصيل واستلام مجاني داخل دبي')+contact(1620))
build('h1', head('الأوراق المطلوبة')+
  lst(800,360,'للمقيمين ومواطني الخليج',['صورة الهوية','رخصة القيادة','جواز السفر'])+
  lst(1190,360,'للزوار والسياح',['صورة جواز السفر','رخصة قيادة دولية','تأشيرة الدخول'])+contact(1620))
build('h2', head('الدفع والتوصيل')+
  f'<div class="card chk" style="top:800px;height:260px"><div class="c-h">طرق الدفع</div><div class="grid"><span>كاش</span><span>بطاقة</span><span>Tabby</span><span>Tamara</span></div></div>'+
  one(1090,230,'التوصيل والاستلام','مجاني داخل دبي')+
  one(1350,230,'الكيلومترات','<span class="num">250</span> كم باليوم')+contact(1620))
build('h3', head('Book in minutes','Three steps and your car is ready')+
  step(800,1,'Pick your car &amp; dates','On our website or on WhatsApp')+
  step(1060,2,'Send your documents','We review them and reply')+
  step(1320,3,'We deliver to you','Free delivery &amp; pickup in Dubai')+contact(1620),True)
build('h4', head('Required documents')+
  lst(800,360,'UAE &amp; GCC residents',['ID copy','Driving licence','Passport'])+
  lst(1190,360,'Tourists &amp; visitors',['Passport copy','International driving licence','Entry visa'])+contact(1620),True)
build('h5', head('Payment &amp; delivery')+
  f'<div class="card chk" style="top:800px;height:260px"><div class="c-h">Payment options</div><div class="grid"><span>Cash</span><span>Card</span><span>Tabby</span><span>Tamara</span></div></div>'+
  one(1090,230,'Delivery &amp; pickup','Free within Dubai')+
  one(1350,230,'Mileage','250 km per day')+contact(1620),True)
