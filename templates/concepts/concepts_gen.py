import random
random.seed(7)
def bars(n,h):
    s=''
    for i in range(n):
        w=random.choice([2,2,3,4,6]); g=random.choice([2,3,4])
        s+=f'<i style="width:{w}px;margin-right:{g}px;height:{h}px"></i>'
    return s
HEAD='''<!doctype html><html lang="{lang}" dir="{dir}"><head><meta charset="utf-8"><style>
@import url(base.css);
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:#000}
body{font-family:"Inter","Noto Kufi Arabic",sans-serif;-webkit-font-smoothing:antialiased}
.sl{position:relative;width:1080px;height:1350px;overflow:hidden}
.abs{position:absolute}
.dom{font-family:Inter;direction:ltr;unicode-bidi:isolate;display:inline-block;white-space:nowrap;font-weight:800;letter-spacing:-.02em}
.dom small{font-size:.36em;font-weight:600;letter-spacing:0;opacity:.6;margin-right:.12em}
.lat{font-family:Inter;direction:ltr;unicode-bidi:isolate;display:inline-block}
{css}
</style></head><body><div class="sl">{body}</div></body></html>'''
DOM='<span class="dom"><small>www.</small>ffl.ae</span>'
def page(n,lang,css,body):
    open(n+'.html','w').write(HEAD.replace('{lang}',lang).replace('{dir}','rtl' if lang=='ar' else 'ltr').replace('{css}',css).replace('{body}',body.replace('{DOM}',DOM)))

# ---------- BOARDING PASS (AR) ----------
page('pass','ar','''
.sl{background:#0C0C0E;color:#F5F5F7}
.h{right:80px;top:84px;font-size:104px;font-weight:800;line-height:1.3;text-align:right;white-space:nowrap}
.h b{color:#C99A20}
.tk{left:84px;top:440px;width:912px;height:570px;transform:rotate(-4deg);background:#F3EFE6;color:#111;border-radius:26px;box-shadow:0 40px 80px rgba(0,0,0,.6)}
.top{position:absolute;left:0;right:0;top:0;height:92px;background:#151517;border-radius:26px 26px 0 0;display:flex;align-items:center;justify-content:space-between;padding:0 36px;direction:rtl}
.top span{color:#E3B63F;font-weight:700;font-size:32px}
.top img{height:64px}
.stub{position:absolute;left:0;top:92px;bottom:0;width:230px;border-right:3px dashed #b9b2a2;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px}
.stub .l{font-size:24px;font-weight:600;color:#6c675c}
.stub .d{font-family:Inter;font-weight:800;font-size:64px;letter-spacing:-1px;direction:ltr}
.bc{display:flex;align-items:flex-end;direction:ltr}
.bc i{display:block;background:#111}
.nt{position:absolute;left:214px;width:34px;height:34px;border-radius:50%;background:#0C0C0E}
.main{position:absolute;left:230px;right:0;top:92px;bottom:0;padding:24px 44px 0 36px;direction:rtl}
.rt{display:flex;align-items:center;justify-content:space-between}
.ap{text-align:center}
.ap .c{font-family:Inter;font-weight:800;font-size:86px;letter-spacing:-2px;line-height:1}
.ap .n{font-size:26px;font-weight:600;color:#6c675c;margin-top:6px}
.ln{flex:1;margin:0 26px;height:0;border-top:3px dashed #A67C12;position:relative;top:-18px}
.ln svg{position:absolute;left:50%;top:-27px;margin-left:-32px;width:64px;height:54px;background:#F3EFE6}
.gr{display:grid;grid-template-columns:1fr 1fr;gap:14px 24px;margin-top:22px;border-top:2px solid #d9d3c5;padding-top:22px}
.gr .k{font-size:22px;font-weight:600;color:#857f72}
.gr .v{font-size:30px;font-weight:800;color:#111;margin-top:2px;white-space:nowrap}
.s{left:0;right:0;top:1085px;text-align:center;font-size:44px;font-weight:600;color:rgba(245,245,247,.9)}
.d{left:0;right:0;top:1180px;text-align:center}
.d .dom{font-size:96px;color:#E3B63F}
.d .dom small{color:#F5F5F7}
''','''
<div class="abs h">حجزت الطيارة؟<br><b>باقي السيارة.</b></div>
<div class="abs tk">
 <div class="top"><span>بطاقة استلام السيارة</span><img src="logo_t.png"></div>
 <div class="nt" style="top:75px"></div><div class="nt" style="bottom:-17px"></div>
 <div class="stub"><div class="l">احجز من</div><div class="d">ffl.ae</div><div class="bc">'''+bars(26,70)+'''</div></div>
 <div class="main">
  <div class="rt">
   <div class="ap"><div class="c">DOH</div><div class="n">الدوحة</div></div>
   <div class="ln"><svg viewBox="0 0 64 54" fill="none" stroke="#A67C12" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 34 L14 22 Q16 16 22 16 L42 16 Q48 16 50 22 L54 34"/><rect x="7" y="34" width="50" height="12" rx="4"/><circle cx="18" cy="46" r="4.5" fill="#F3EFE6"/><circle cx="46" cy="46" r="4.5" fill="#F3EFE6"/></svg></div>
   <div class="ap"><div class="c">DXB</div><div class="n">دبي</div></div>
  </div>
  <div class="gr">
   <div><div class="k">الاستلام</div><div class="v">المطار أو الفندق</div></div>
   <div><div class="k">التوصيل</div><div class="v">مجاني داخل دبي</div></div>
   <div><div class="k">الوديعة</div><div class="v">بدون وديعة تأمين</div></div>
   <div><div class="k">السيارة</div><div class="v">على اختيارك</div></div>
  </div>
 </div>
</div>
<div class="abs s">احجز سيارتك من الموقع قبل لا توصل</div>
<div class="abs d">{DOM}</div>
''')

# ---------- LOCK SCREEN (EN) ----------
page('lock','en','''
.sl{background:#000;color:#fff}
.bg{left:-140px;top:-60px;width:1360px;height:1470px;object-fit:cover;object-position:50% 45%;filter:blur(3px) brightness(.62) saturate(1.05)}
.v{inset:0;background:linear-gradient(180deg,rgba(0,0,0,.35) 0%,rgba(0,0,0,0) 30%,rgba(0,0,0,.25) 60%,rgba(0,0,0,.8) 100%)}
.day{left:0;right:0;top:110px;text-align:center;font-size:40px;font-weight:600;opacity:.9}
.tm{left:0;right:0;top:150px;text-align:center;font-size:250px;font-weight:700;letter-spacing:-8px;line-height:1.1}
.n{left:56px;right:56px;border-radius:44px;background:rgba(245,245,247,.86);color:#111;padding:30px 34px;display:flex;gap:26px;align-items:center;box-shadow:0 20px 50px rgba(0,0,0,.35)}
.ic{flex:none;width:104px;height:104px;border-radius:24px;background:#0C0C0E;display:flex;align-items:center;justify-content:center}
.ic img{width:84px}
.tx{flex:1}
.r1{display:flex;justify-content:space-between;font-size:27px;font-weight:600;color:#55555a;letter-spacing:.3px}
.t{font-size:42px;font-weight:800;margin-top:4px;letter-spacing:-.5px}
.b{font-size:33px;font-weight:500;color:#2b2b2e;margin-top:4px;line-height:1.3}
.cta{left:0;right:0;top:1150px;text-align:center;font-size:40px;font-weight:600}
.d{left:0;right:0;top:1205px;text-align:center}
.d .dom{font-size:92px;color:#E3B63F}
.d .dom small{color:#fff}
''','''
<img class="abs bg" src="rr.jpg"><div class="abs v"></div>
<div class="abs day">Welcome to Dubai</div>
<div class="abs tm">9:41</div>
<div class="abs n" style="top:520px"><div class="ic"><img src="logo_t.png"></div><div class="tx"><div class="r1"><span>FAST FLEET</span><span>now</span></div><div class="t">Your Range Rover is here.</div><div class="b">Waiting at your hotel entrance.</div></div></div>
<div class="abs n" style="top:740px;transform:scale(.94);opacity:.92"><div class="ic"><img src="logo_t.png"></div><div class="tx"><div class="r1"><span>FAST FLEET</span><span>2m ago</span></div><div class="t">Delivery: free.</div><div class="b">Free delivery &amp; pickup within Dubai.</div></div></div>
<div class="abs n" style="top:945px;transform:scale(.88);opacity:.8"><div class="ic"><img src="logo_t.png"></div><div class="tx"><div class="r1"><span>FAST FLEET</span><span>5m ago</span></div><div class="t">Security deposit: none.</div><div class="b">Just pick it up and drive.</div></div></div>
<div class="abs cta">Book yours online</div>
<div class="abs d">{DOM}</div>
''')
