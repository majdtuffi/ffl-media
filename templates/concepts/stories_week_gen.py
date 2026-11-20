import random
HEAD='''<!doctype html><html lang="{lang}" dir="{dir}"><head><meta charset="utf-8"><style>
@import url(base.css);
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:#000}
body{font-family:"Inter","Noto Kufi Arabic",sans-serif;-webkit-font-smoothing:antialiased}
.sl{position:relative;width:1080px;height:1920px;overflow:hidden}
.abs{position:absolute}
.c{left:0;right:0;text-align:center}
.dom{font-family:Inter;direction:ltr;unicode-bidi:isolate;display:inline-block;white-space:nowrap;font-weight:800;letter-spacing:-.02em;line-height:1}
.dom small{font-size:.36em;font-weight:600;letter-spacing:0;opacity:.6;margin-right:.12em}
.lat{font-family:Inter;direction:ltr;unicode-bidi:isolate;display:inline-block}
{css}
</style></head><body><div class="sl">{body}</div></body></html>'''
DOM='<span class="dom"><small>www.</small>ffl.ae</span>'
def page(n,lang,css,body):
    open(n+'.html','w').write(HEAD.replace('{lang}',lang).replace('{dir}','rtl' if lang=='ar' else 'ltr').replace('{css}',css).replace('{body}',body.replace('{DOM}',DOM)))
random.seed(3)
def bars(n,h):
    return ''.join(f'<i style="width:{random.choice([2,3,3,5,7])}px;margin-right:{random.choice([3,4,5])}px;height:{h}px"></i>' for _ in range(n))

# 1 RECEIPT (EN)
rows=[('Security deposit','0.00'),('Delivery in Dubai','0.00'),('Pickup in Dubai','0.00'),('Hidden fees','0.00')]
page('s1','en','''
.sl{background:#0C0C0E;color:#F5F5F7}
.h{top:270px;font-size:92px;font-weight:800;letter-spacing:-2px;line-height:1.08}
.h b{color:#C99A20}
.rc{left:170px;top:560px;width:740px;background:#F3EFE6;color:#111;transform:rotate(2.5deg);padding:56px 54px 80px;box-shadow:0 40px 90px rgba(0,0,0,.6);
 -webkit-mask:conic-gradient(from -45deg at bottom,#0000,#000 1deg 89deg,#0000 90deg) bottom/40px 51% repeat-x,linear-gradient(#000 0 0) top/100% 50.5% no-repeat;}
.rc .t{text-align:center;font-weight:800;font-size:54px;letter-spacing:6px}
.rc .u{text-align:center;font-size:22px;font-weight:600;letter-spacing:5px;color:#6c675c;margin-top:8px}
.ds{border-top:3px dashed #9b9484;margin:34px 0}
.r{display:flex;align-items:baseline;font-size:36px;font-weight:600;margin:22px 0}
.r i{flex:1;border-bottom:3px dotted #b9b2a2;margin:0 14px;position:relative;top:-6px}
.r b{font-weight:800;font-variant-numeric:tabular-nums}
.tt{display:flex;justify-content:space-between;font-size:46px;font-weight:800}
.bc{display:flex;justify-content:center;align-items:flex-end;margin-top:40px}
.bc i{display:block;background:#111}
.th{text-align:center;font-size:24px;font-weight:600;letter-spacing:3px;color:#6c675c;margin-top:18px}
.s{top:1500px;font-size:42px;font-weight:600;color:rgba(245,245,247,.88)}
.d{top:1580px}.d .dom{font-size:96px;color:#E3B63F}.d .dom small{color:#F5F5F7}
''','''
<div class="abs c h">The extras,<br><b>itemised.</b></div>
<div class="abs rc"><div class="t">FAST FLEET</div><div class="u">LUXURY CAR RENTAL · DUBAI</div><div class="ds"></div>'''
+''.join(f'<div class="r"><span>{a}</span><i></i><b>AED {b}</b></div>' for a,b in rows)+
'''<div class="ds"></div><div class="tt"><span>EXTRAS</span><span>AED 0.00</span></div>
<div class="bc">'''+bars(48,84)+'''</div><div class="th">THANK YOU · SEE YOU IN DUBAI</div></div>
<div class="abs c s">Book your car online</div><div class="abs c d">{DOM}</div>
''')

# 2 KEY CARD + CAR KEY (AR) ivory
page('s2','ar','''
.sl{background:#F2EEE5;color:#111}
.h{top:265px;font-size:78px;font-weight:800;line-height:1.5}
.h b{color:#A67C12}
.card{left:150px;top:640px;width:470px;height:300px;border-radius:26px;background:#fff;border:2px solid #d9d3c5;transform:rotate(-9deg);box-shadow:0 30px 60px rgba(0,0,0,.18);padding:34px 38px;direction:rtl}
.card .a{font-size:26px;font-weight:600;color:#857f72}
.card .n{font-family:Inter;font-weight:800;font-size:92px;letter-spacing:-2px;margin-top:6px;direction:ltr;text-align:right}
.card .st{position:absolute;left:0;right:0;bottom:44px;height:44px;background:#111}
.key{left:500px;top:780px;width:440px;height:560px;transform:rotate(11deg)}
.lb{font-size:34px;font-weight:700;color:#3a3a3a}
.s{top:1440px;font-size:44px;font-weight:700;color:#111}
.d{top:1545px}.d .dom{font-size:100px;color:#111}
''','''
<div class="abs c h">مفتاح الغرفة من الفندق.<br><b>مفتاح السيارة منّا.</b></div>
<div class="abs card"><div class="a">بطاقة الغرفة</div><div class="n">1204</div><div class="st"></div></div>
<svg class="abs key" viewBox="0 0 440 560">
 <defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a2a2e"/><stop offset="1" stop-color="#0c0c0e"/></linearGradient>
 <filter id="sh" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="26" stdDeviation="22" flood-opacity=".3"/></filter></defs>
 <circle cx="220" cy="70" r="52" fill="none" stroke="#B9902A" stroke-width="12"/>
 <rect x="196" y="112" width="48" height="56" rx="10" fill="#B9902A"/>
 <g filter="url(#sh)"><rect x="90" y="150" width="260" height="380" rx="70" fill="url(#g)" stroke="#C99A20" stroke-width="5"/></g>
 <rect x="126" y="186" width="188" height="308" rx="46" fill="none" stroke="rgba(201,154,32,.35)" stroke-width="2"/>
 <g fill="none" stroke="#E3B63F" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="220" cy="250" r="34"/><rect x="207" y="246" width="26" height="20" rx="4"/><path d="M211 246v-8a9 9 0 0 1 18 0v8"/>
  <circle cx="220" cy="345" r="34"/><rect x="207" y="341" width="26" height="20" rx="4"/><path d="M211 341v-8a9 9 0 0 1 16-5"/>
  <circle cx="220" cy="440" r="34"/><path d="M203 446l5-13q2-5 7-5h10q5 0 7 5l5 13M200 446h40v9h-40z"/>
 </g>
</svg>
<div class="abs c s">نوصل سيارتك لباب فندقك في دبي</div>
<div class="abs c d">{DOM}</div>
''')

# 3 RESERVED PARKING SIGN (AR)
page('s3','ar','''
.sl{background:#101012;color:#F5F5F7}
.sky{inset:0 0 520px 0;background:linear-gradient(180deg,#17171b,#0d0d0f)}
.gnd{left:0;right:0;bottom:0;height:520px;background:#1a1a1d}
.ln{bottom:0;width:14px;height:560px;background:#E9E4D6;transform-origin:bottom}
.pole{left:526px;top:1010px;width:28px;height:400px;background:linear-gradient(90deg,#4a4a4f,#8b8b91 45%,#3a3a3f)}
.sign{left:230px;top:300px;width:620px;height:740px;border-radius:44px;background:#0C0C0E;border:10px solid #C99A20;box-shadow:0 30px 70px rgba(0,0,0,.6);text-align:center}
.sign:before{content:"";position:absolute;inset:14px;border:2px solid rgba(201,154,32,.45);border-radius:28px}
.P{font-family:Inter;font-weight:800;font-size:330px;line-height:1;color:#E3B63F;margin-top:36px}
.rv{font-size:112px;font-weight:800;line-height:1.25;margin-top:-6px}
.nm{font-size:44px;font-weight:600;color:rgba(245,245,247,.8);margin-top:10px}
.s{top:1490px;font-size:44px;font-weight:700;color:#F5F5F7;line-height:1.5}
.d{top:1640px}.d .dom{font-size:92px;color:#E3B63F}.d .dom small{color:#F5F5F7}
''','''
<div class="abs sky"></div><div class="abs gnd"></div>
<div class="abs ln" style="left:40px;transform:skewX(-17deg)"></div><div class="abs ln" style="right:40px;transform:skewX(17deg)"></div>
<div class="abs pole"></div>
<div class="abs sign"><div class="P">P</div><div class="rv">محجوز</div><div class="nm">لسيارتك في دبي</div></div>
<div class="abs c s">احجزها من الموقع، ونوصلها لك</div>
<div class="abs c d">{DOM}</div>
''')

# 4 MAP PIN (EN)
random.seed(11)
roads=''
for i in range(9):
    y=120+i*200+random.randint(-40,40); roads+=f'<path d="M-50 {y} Q 540 {y+random.randint(-140,140)} 1130 {y+random.randint(-80,80)}" stroke="#26262b" stroke-width="{random.choice([10,14,22])}" fill="none"/>'
for i in range(6):
    x=90+i*190+random.randint(-40,40); roads+=f'<path d="M{x} -50 Q {x+random.randint(-160,160)} 960 {x+random.randint(-90,90)} 1970" stroke="#232327" stroke-width="{random.choice([10,14,20])}" fill="none"/>'
page('s4','en','''
.sl{background:#141417;color:#F5F5F7}
.mp{inset:0}
.h{top:265px;font-size:104px;font-weight:800;letter-spacing:-2.5px;line-height:1.05;text-shadow:0 4px 30px #141417}
.h b{color:#E3B63F}
.you{left:672px;top:520px;background:#F5F5F7;color:#111;font-weight:800;font-size:34px;padding:14px 28px;border-radius:999px}
.sheet{left:60px;right:60px;top:1230px;border-radius:44px;background:#F3EFE6;color:#111;padding:44px 50px;box-shadow:0 30px 80px rgba(0,0,0,.55)}
.sheet .k{font-size:28px;font-weight:600;color:#857f72;letter-spacing:.5px}
.sheet .v{font-size:54px;font-weight:800;letter-spacing:-1px;margin-top:4px}
.sheet .row{display:flex;gap:16px;margin-top:30px}
.sheet .chip{flex:1;border:2px solid #d5cebd;border-radius:22px;padding:18px 22px}
.sheet .chip span{display:block;font-size:24px;font-weight:600;color:#857f72}
.sheet .chip b{font-size:34px;font-weight:800}
.d{top:1640px}.d .dom{font-size:84px;color:#E3B63F}.d .dom small{color:#F5F5F7}
''','''
<svg class="abs mp" viewBox="0 0 1080 1920">'''+roads+'''
<path d="M250 1130 C 300 950, 520 1010, 560 880 S 700 800, 770 790" stroke="#C99A20" stroke-width="10" stroke-dasharray="4 26" stroke-linecap="round" fill="none"/>
<circle cx="250" cy="1130" r="46" fill="#0C0C0E" stroke="#C99A20" stroke-width="6"/>
<g transform="translate(250 1130)" fill="none" stroke="#E3B63F" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><path d="M-22 6l6-16q2-6 9-6h14q7 0 9 6l6 16M-26 6h52v12h-52z"/></g>
<g transform="translate(770 790)"><path d="M0 0 C -52 -62 -62 -92 -62 -118 A 62 62 0 1 1 62 -118 C 62 -92 52 -62 0 0Z" fill="#E3B63F"/><circle cx="0" cy="-118" r="24" fill="#141417"/></g>
</svg>
<div class="abs c h">We come<br><b>to you.</b></div>
<div class="abs you">Your hotel</div>
<div class="abs sheet"><div class="k">FAST FLEET · DELIVERY</div><div class="v">Your car is on its way.</div>
<div class="row"><div class="chip"><span>Delivery in Dubai</span><b>Free</b></div><div class="chip"><span>Security deposit</span><b>None</b></div></div></div>
<div class="abs c d">{DOM}</div>
''')

# 5 SEARCH (AR) light
page('s5','ar','''
.sl{background:#F2EEE5;color:#111}
.h{top:300px;font-size:96px;font-weight:800;line-height:1.35}
.sb{left:70px;right:70px;top:640px;height:132px;border-radius:66px;background:#fff;border:3px solid #111;display:flex;align-items:center;padding:0 44px;gap:24px;direction:rtl;box-shadow:0 18px 40px rgba(0,0,0,.1)}
.sb svg{width:50px;height:50px;flex:none}
.sb .q{font-size:42px;font-weight:600;white-space:nowrap}
.sb .cur{width:4px;height:60px;background:#A67C12;margin-right:4px}
.res{left:70px;right:70px;top:810px;border-radius:40px;background:#0C0C0E;color:#F5F5F7;padding:46px 50px 50px;direction:rtl;box-shadow:0 30px 70px rgba(0,0,0,.3)}
.res .top{display:flex;align-items:center;justify-content:space-between}
.res .top img{width:150px}
.res .dom{font-size:100px;color:#E3B63F}
.res .dom small{color:#F5F5F7}
.res .t{font-size:46px;font-weight:800;margin-top:26px}
.res ul{list-style:none;margin-top:22px}
.res li{font-size:38px;font-weight:600;color:rgba(245,245,247,.88);margin-top:16px;display:flex;align-items:center;gap:18px}
.res li:before{content:"";width:14px;height:14px;border-radius:50%;background:#C99A20;flex:none}
.btn{margin-top:38px;display:inline-block;background:#C99A20;color:#151515;font-weight:800;font-size:40px;padding:20px 54px;border-radius:999px}
.s{top:1560px;font-size:64px;font-weight:800;color:#111}
.s b{color:#A67C12}
''','''
<div class="abs c h">تدوّر سيارة في دبي؟</div>
<div class="abs sb"><svg viewBox="0 0 24 24" fill="none" stroke="#111" stroke-width="2.4" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M16.5 16.5L21 21"/></svg><span class="q">تأجير سيارة في دبي بدون وديعة</span><span class="cur"></span></div>
<div class="abs res"><div class="top">{DOM}<img src="logo_t.png"></div>
<div class="t">احجز سيارتك أونلاين</div>
<ul><li>بدون وديعة تأمين</li><li>توصيل واستلام مجاني داخل دبي</li><li>مع سائق أو بدون</li></ul>
<span class="btn">احجز الآن</span></div>
<div class="abs c s">لقيتها. <b>لا تدوّر أكثر.</b></div>
''')
