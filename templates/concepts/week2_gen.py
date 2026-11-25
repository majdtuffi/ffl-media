import math
HEAD='''<!doctype html><html lang="{lang}" dir="{dir}"><head><meta charset="utf-8"><style>
@import url(base.css);
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:#000}
body{font-family:"Inter","Noto Kufi Arabic",sans-serif;-webkit-font-smoothing:antialiased}
.sl{position:relative;width:1080px;height:{H}px;overflow:hidden}
.abs{position:absolute}
.c{left:0;right:0;text-align:center}
.dom{font-family:Inter;direction:ltr;unicode-bidi:isolate;display:inline-block;white-space:nowrap;font-weight:800;letter-spacing:-.02em;line-height:1}
.dom small{font-size:.36em;font-weight:600;letter-spacing:0;opacity:.6;margin-right:.12em}
.lat{font-family:Inter;direction:ltr;unicode-bidi:isolate;display:inline-block}
{css}
</style></head><body><div class="sl">{body}</div></body></html>'''
DOM='<span class="dom"><small>www.</small>ffl.ae</span>'
def page(n,lang,css,body,H=1920):
    open(n+'.html','w').write(HEAD.replace('{lang}',lang).replace('{dir}','rtl' if lang=='ar' else 'ltr').replace('{H}',str(H)).replace('{css}',css).replace('{body}',body.replace('{DOM}',DOM)))
def sun(s=90):
    rays=''.join(f'<line x1="50" y1="8" x2="50" y2="20" transform="rotate({a} 50 50)"/>' for a in range(0,360,45))
    return f'<svg width="{s}" height="{s}" viewBox="0 0 100 100" fill="none" stroke="#E3B63F" stroke-width="7" stroke-linecap="round"><circle cx="50" cy="50" r="19" fill="#E3B63F"/>{rays}</svg>'

# 1 WEATHER (EN)
rows=''.join(f'<div class="r"><span class="dy">{d}</span>{sun(84)}<span class="tx">Great day for a drive</span></div>' for d in ('Fri','Sat','Sun'))
page('w1','en','''
.sl{background:#F2EEE5;color:#111}
.h{top:270px;font-size:92px;font-weight:800;letter-spacing:-2px;line-height:1.08}
.cd{left:80px;right:80px;top:540px;border-radius:56px;background:#0C0C0E;color:#F5F5F7;padding:54px 60px 40px;box-shadow:0 40px 80px rgba(0,0,0,.28)}
.cd .t{display:flex;justify-content:space-between;align-items:center}
.cd .ci{font-size:76px;font-weight:800;letter-spacing:-1.5px}
.cd .su{font-size:34px;font-weight:600;color:rgba(245,245,247,.65);margin-top:2px}
.r{display:flex;align-items:center;gap:34px;border-top:2px solid rgba(245,245,247,.14);padding:26px 0;margin-top:0}
.r:first-of-type{margin-top:36px}
.r .dy{width:110px;font-size:44px;font-weight:800}
.r .tx{font-size:40px;font-weight:600;color:rgba(245,245,247,.9)}
.s{top:1345px;font-size:58px;font-weight:800;letter-spacing:-1px}
.s b{color:#A67C12}
.s2{top:1470px;font-size:40px;font-weight:600;color:#3a3a3a}
.d{top:1550px}.d .dom{font-size:96px;color:#111}
''','''
<div class="abs c h">Weekend forecast</div>
<div class="abs cd"><div class="t"><div><div class="ci">Dubai</div><div class="su">This weekend</div></div>'''+sun(170)+'''</div>'''+rows+'''</div>
<div class="abs c s"><b>100%</b> chance of a good drive.</div>
<div class="abs c s2">Book your car online</div>
<div class="abs c d">{DOM}</div>
''')

# 2 DOOR HANGER (AR)
page('w2','ar','''
.sl{background:#17130f;color:#F5F5F7}
.wd{inset:0;background:repeating-linear-gradient(90deg,#2b2118 0 178px,#231a12 178px 182px,#2e2319 182px 360px,#211811 360px 364px)}
.vg{inset:0;background:radial-gradient(ellipse at 50% 40%,rgba(0,0,0,0) 30%,rgba(0,0,0,.55) 100%)}
.kn{left:440px;top:250px;width:200px;height:200px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#f3d98a,#b8891f 55%,#6e4f0c);box-shadow:0 30px 50px rgba(0,0,0,.6)}
.hg{left:260px;top:300px;width:560px;height:1090px;border-radius:60px;background:#F3EFE6;color:#111;transform:rotate(-4deg);transform-origin:50% 100px;box-shadow:0 50px 90px rgba(0,0,0,.6);text-align:center}
.hole{position:absolute;left:50%;top:44px;width:210px;height:210px;margin-left:-105px;border-radius:50%;background:#241b13;box-shadow:inset 0 10px 20px rgba(0,0,0,.6)}
.hg .a{margin-top:330px;font-size:40px;font-weight:700;color:#857f72;letter-spacing:1px}
.hg .b{font-size:104px;font-weight:800;line-height:1.3;margin-top:14px}
.hg .ln{width:120px;height:5px;background:#C99A20;margin:34px auto}
.hg .cc{font-size:60px;font-weight:800;line-height:1.5;color:#A67C12}
.hg svg{width:150px;height:110px;margin-top:26px}
.s{top:1455px;font-size:46px;font-weight:700}
.d{top:1545px}.d .dom{font-size:92px;color:#E3B63F}.d .dom small{color:#F5F5F7}
''','''
<div class="abs wd"></div><div class="abs vg"></div>
<div class="abs hg"><div class="hole"></div><div class="a">الرجاء عدم الإزعاج</div><div class="b">مو في<br>الغرفة</div><div class="ln"></div><div class="cc">طلعنا نلف دبي</div>
<svg viewBox="0 0 150 110" fill="none" stroke="#111" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"><path d="M22 62l12-30q4-10 15-10h52q11 0 15 10l12 30"/><rect x="14" y="62" width="122" height="28" rx="10"/><circle cx="40" cy="92" r="11" fill="#F3EFE6"/><circle cx="110" cy="92" r="11" fill="#F3EFE6"/></svg></div>
<div class="abs kn"></div>
<div class="abs c s">سيارتك توصل لباب فندقك في دبي</div>
<div class="abs c d">{DOM}</div>
''')

# 3 GAUGE (AR)
ticks=''
for i in range(0,11):
    a=math.radians(180-i*18); x1=400+300*math.cos(a); y1=420-300*math.sin(a); x2=400+(250 if i%5==0 else 268)*math.cos(a); y2=420-(250 if i%5==0 else 268)*math.sin(a)
    ticks+=f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{"#E3B63F" if i==0 else "rgba(245,245,247,.55)"}" stroke-width="{10 if i%5==0 else 5}" stroke-linecap="round"/>'
page('w3','ar','''
.sl{background:#0C0C0E;color:#F5F5F7}
.h{top:270px;font-size:88px;font-weight:800;line-height:1.4}
.h b{color:#E3B63F}
.g{left:140px;top:560px;width:800px;height:520px}
.z{top:1040px;font-family:Inter;font-weight:800;font-size:240px;line-height:1;color:#E3B63F}
.lb{top:1300px;font-size:56px;font-weight:800}
.s{top:1445px;font-size:42px;font-weight:600;color:rgba(245,245,247,.85)}
.d{top:1545px}.d .dom{font-size:96px;color:#E3B63F}.d .dom small{color:#F5F5F7}
''','''
<div class="abs c h">العدّاد واقف<br><b>على صفر</b></div>
<svg class="abs g" viewBox="0 0 800 520"><path d="M100 420 A300 300 0 0 1 700 420" fill="none" stroke="rgba(245,245,247,.16)" stroke-width="26" stroke-linecap="round"/>'''+ticks+'''
<line x1="400" y1="420" x2="150" y2="420" stroke="#E3B63F" stroke-width="14" stroke-linecap="round"/><circle cx="400" cy="420" r="34" fill="#0C0C0E" stroke="#E3B63F" stroke-width="10"/></svg>
<div class="abs c z">0</div>
<div class="abs c lb">وديعة التأمين</div>
<div class="abs c s">بدون وديعة تأمين. احجز من الموقع</div>
<div class="abs c d">{DOM}</div>
''')

# 4 CHAT (AR)
page('w4','ar','''
.sl{background:#F2EEE5;color:#111}
.b{max-width:760px;padding:34px 46px;font-size:54px;font-weight:700;line-height:1.4;border-radius:52px;box-shadow:0 14px 30px rgba(0,0,0,.1)}
.me{right:80px;background:#0C0C0E;color:#F5F5F7;border-bottom-right-radius:12px}
.us{left:80px;background:#E3B63F;color:#111;border-bottom-left-radius:12px}
.nm{left:96px;font-size:28px;font-weight:700;color:#857f72;direction:ltr}
.s{top:1410px;font-size:44px;font-weight:700;color:#111}
.d{top:1500px}.d .dom{font-size:100px;color:#111}
''','''
<div class="abs b me" style="top:300px">وصلنا الفندق. والسيارة؟</div>
<div class="abs nm" style="top:468px">Fast Fleet</div>
<div class="abs b us" style="top:512px">عند الباب تنتظرك.</div>
<div class="abs b me" style="top:730px">والوديعة؟</div>
<div class="abs nm" style="top:898px">Fast Fleet</div>
<div class="abs b us" style="top:942px">بدون وديعة تأمين.</div>
<div class="abs b me" style="top:1160px">أجل مشينا.</div>
<div class="abs c s">احجز سيارتك من الموقع</div>
<div class="abs c d">{DOM}</div>
''')

# 5 POLAROID (EN)
page('w5','en','''
.sl{background:#0C0C0E;color:#F5F5F7}
.h{top:265px;font-size:92px;font-weight:800;letter-spacing:-2px;line-height:1.08}
.h b{color:#E3B63F}
.p{background:#F7F5EF;padding:34px 34px 0;box-shadow:0 40px 80px rgba(0,0,0,.6)}
.p img{display:block;width:100%;object-fit:cover}
.p .cp{height:130px;display:flex;align-items:center;justify-content:center;color:#222;font-size:44px;font-weight:600;font-style:italic;letter-spacing:-.5px}
.p1{left:330px;top:560px;width:600px;transform:rotate(7deg)}
.p1 img{height:520px;object-position:50% 50%}
.p2{left:120px;top:690px;width:680px;transform:rotate(-5deg)}
.p2 img{height:600px;object-position:38% 65%}
.s{top:1500px;font-size:42px;font-weight:600;color:rgba(245,245,247,.88)}
.d{top:1580px}.d .dom{font-size:92px;color:#E3B63F}.d .dom small{color:#F5F5F7}
''','''
<div class="abs c h">A trip worth<br><b>framing.</b></div>
<div class="abs p p1"><img src="rr.jpg"><div class="cp">Dubai, day two</div></div>
<div class="abs p p2"><img src="urus.jpg"><div class="cp">Dubai, day one</div></div>
<div class="abs c s">Book your car online</div>
<div class="abs c d">{DOM}</div>
''')

# FEED: ROAD SIGN (AR) 1080x1350
AR_UP='<svg viewBox="0 0 100 100" fill="none" stroke="#F5F5F7" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"><path d="M50 88V14M20 44L50 14l30 30"/></svg>'
AR_L='<svg viewBox="0 0 100 100" fill="none" stroke="#0C0C0E" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"><path d="M88 50H14M44 20L14 50l30 30"/></svg>'
page('f1','ar','''
.sl{background:#101012;color:#F5F5F7}
.sk{inset:0;background:linear-gradient(180deg,#1a1a1f 0%,#0d0d0f 70%)}
.gt{left:60px;right:60px;top:150px;height:26px;background:linear-gradient(180deg,#77777d,#3d3d42)}
.pl{top:150px;width:30px;height:1200px;background:linear-gradient(90deg,#4a4a4f,#8b8b91 45%,#3a3a3f)}
.sg{left:120px;right:120px;border-radius:28px;padding:40px 54px;display:flex;align-items:center;justify-content:space-between;direction:rtl;box-shadow:0 30px 60px rgba(0,0,0,.55)}
.sg svg{width:150px;height:150px;flex:none}
.s1{top:210px;height:340px;padding-bottom:86px;background:#1D3F8F;border:8px solid #F5F5F7}
.s1 .k{font-size:40px;font-weight:700;opacity:.85}
.s1 .v{font-size:136px;font-weight:800;line-height:1.05}
.s2{top:590px;height:390px;background:#E3B63F;border:8px solid #0C0C0E;color:#0C0C0E}
.s2 .k{font-size:40px;font-weight:800}
.s2 .v{font-size:104px;font-weight:800;line-height:1.25}
.s2 .dom{font-size:84px;color:#0C0C0E;margin-top:6px}
.s{top:1060px;font-size:76px;font-weight:800}
.s b{color:#E3B63F}
.s3{top:1195px;font-size:40px;font-weight:600;color:rgba(245,245,247,.8)}
''','''
<div class="abs sk"></div>
<div class="abs pl" style="left:90px"></div><div class="abs pl" style="right:90px"></div><div class="abs gt"></div>
<div class="abs sg s1"><div><div class="k">الوجهة</div><div class="v">دبي</div></div>'''+AR_UP+'''</div>
<div class="abs sg s2"><div><div class="k">المخرج القادم</div><div class="v">سيارتك</div>{DOM}</div>'''+AR_L+'''</div>
<div class="abs c s">خذ <b>المخرج الصح</b></div>
<div class="abs c s3">احجز سيارتك من الموقع قبل لا توصل</div>
''',1350)
