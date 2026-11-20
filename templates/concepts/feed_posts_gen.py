HEAD='''<!doctype html><html lang="{lang}" dir="{dir}"><head><meta charset="utf-8"><style>
@import url(base.css);
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:#000}
body{font-family:"Inter","Noto Kufi Arabic",sans-serif;-webkit-font-smoothing:antialiased}
.sl{position:relative;width:1080px;height:1350px;overflow:hidden}
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
CHK='<svg viewBox="0 0 64 64"><rect x="5" y="5" width="54" height="54" rx="12" fill="none" stroke="#111" stroke-width="5"/><path d="M16 33l11 11 22-26" fill="none" stroke="#A67C12" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
BOX='<svg viewBox="0 0 64 64"><rect x="5" y="5" width="54" height="54" rx="12" fill="none" stroke="#111" stroke-width="5"/></svg>'
# 1 CHECKLIST (AR)
page('f1','ar','''
.sl{background:#0C0C0E;color:#F5F5F7}
.h{top:84px;font-size:112px;font-weight:800;line-height:1.3}
.h b{color:#C99A20}
.pp{left:150px;top:296px;width:780px;height:740px;background:#F3EFE6;color:#111;border-radius:18px;transform:rotate(-3deg);box-shadow:0 40px 90px rgba(0,0,0,.6);padding:50px 60px;direction:rtl;
 background-image:repeating-linear-gradient(180deg,transparent 0 118px,#d9d3c5 118px 120px);background-position:0 150px}
.pp .tt{font-size:44px;font-weight:800;color:#6c675c;height:100px}
.it{display:flex;align-items:center;gap:30px;height:120px;font-size:64px;font-weight:800}
.it svg{width:70px;height:70px;flex:none}
.it.done span{color:#8f897b;text-decoration:line-through;text-decoration-thickness:5px;text-decoration-color:#A67C12}
.ring{position:absolute;left:150px;right:36px;top:498px;height:136px;border:7px solid #C99A20;border-radius:50%;transform:rotate(-2deg)}
.s{top:1062px;font-size:44px;font-weight:700}
.d{top:1190px}.d .dom{font-size:96px;color:#E3B63F}.d .dom small{color:#F5F5F7}
''','''
<div class="abs c h">ناسي <b>شي؟</b></div>
<div class="abs pp"><div class="tt">قائمة السفر إلى دبي</div>
<div class="it done">'''+CHK+'''<span>الجواز</span></div>
<div class="it done">'''+CHK+'''<span>التذكرة</span></div>
<div class="it done">'''+CHK+'''<span>الفندق</span></div>
<div class="it">'''+BOX+'''<span>السيارة</span></div>
<div class="ring"></div></div>
<div class="abs c s">احجز سيارتك من الموقع قبل لا توصل</div>
<div class="abs c d">{DOM}</div>
''')
# 2 NOW PLAYING (EN)
IC='fill="#F5F5F7"'
page('f2','en','''
.sl{background:#0C0C0E;color:#F5F5F7}
.bg{left:-400px;top:-80px;width:1900px;height:1510px;object-fit:cover;filter:blur(40px) brightness(.38) saturate(1.2)}
.np{top:78px;font-size:28px;font-weight:700;letter-spacing:8px;color:rgba(245,245,247,.75)}
.art{left:170px;top:150px;width:740px;height:620px;border-radius:36px;object-fit:cover;object-position:38% 70%;box-shadow:0 40px 90px rgba(0,0,0,.6)}
.t{left:170px;top:810px;font-size:68px;font-weight:800;letter-spacing:-1.5px}
.a{left:170px;top:898px;font-size:38px;font-weight:500;color:rgba(245,245,247,.72)}
.bar{left:170px;right:170px;top:985px;height:8px;border-radius:4px;background:rgba(245,245,247,.25)}
.bar i{position:absolute;left:0;top:0;height:8px;width:38%;border-radius:4px;background:#E3B63F}
.bar b{position:absolute;left:38%;top:-10px;width:28px;height:28px;margin-left:-14px;border-radius:50%;background:#F5F5F7}
.tm{left:170px;right:170px;top:1008px;display:flex;justify-content:space-between;font-size:24px;font-weight:600;color:rgba(245,245,247,.6)}
.ct{left:0;right:0;top:1040px;display:flex;justify-content:center;align-items:center;gap:90px}
.ct svg{width:64px;height:64px}.ct .pl{width:112px;height:112px}
.s{top:1172px;font-size:36px;font-weight:600;color:rgba(245,245,247,.9)}
.d{top:1256px}.d .dom{font-size:62px;color:#E3B63F}.d .dom small{color:#F5F5F7}
''','''
<img class="abs bg" src="urus.jpg">
<div class="abs c np">NOW PLAYING</div>
<img class="abs art" src="urus.jpg">
<div class="abs t">Weekend in Dubai</div>
<div class="abs a">Lamborghini Urus · Fast Fleet</div>
<div class="abs bar"><i></i><b></b></div>
<div class="abs tm"><span>Fri</span><span>Sun</span></div>
<div class="abs ct">
<svg viewBox="0 0 24 24" '''+IC+'''><path d="M6 5h2.4v14H6zM20 5v14L9.5 12z"/></svg>
<svg class="pl" viewBox="0 0 24 24"><circle cx="12" cy="12" r="12" fill="#F5F5F7"/><path d="M9.5 7.2v9.6L17 12z" fill="#0C0C0E"/></svg>
<svg viewBox="0 0 24 24" '''+IC+'''><path d="M15.6 5H18v14h-2.4zM4 5v14l10.5-7z"/></svg>
</div>
<div class="abs c s">Press play on your weekend. Book online</div>
<div class="abs c d">{DOM}</div>
''')
# 3 NATIONAL DAY PLATE (AR)
page('f3','ar','''
.sl{background:#0C0C0E;color:#F5F5F7}
.h{top:150px;font-size:128px;font-weight:800;line-height:1.25}
.pl{left:120px;top:470px;width:840px;height:380px;border-radius:34px;background:#F7F5EF;border:10px solid #111;outline:6px solid #C9C4B6;display:flex;overflow:hidden;direction:ltr;box-shadow:0 40px 90px rgba(0,0,0,.65)}
.fl{width:230px;height:100%;display:flex;flex:none}
.fl .r{width:62px;background:#CE1126}
.fl .st{flex:1;display:flex;flex-direction:column}
.fl .st i{flex:1}
.nm{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#111}
.nm b{font-family:Inter;font-weight:800;font-size:250px;line-height:.95;letter-spacing:-6px}
.nm span{font-size:38px;font-weight:800;letter-spacing:1px;margin-top:2px}
.s{top:930px;font-size:60px;font-weight:700;line-height:1.5}
.s b{color:#E3B63F;font-weight:800}
.dt{top:1060px;font-size:38px;font-weight:600;color:rgba(245,245,247,.7)}
.lg{left:50%;transform:translateX(-50%);top:1160px;width:200px}
''','''
<div class="abs c h">عيد الاتحاد</div>
<div class="abs pl"><div class="fl"><div class="r"></div><div class="st"><i style="background:#00732F"></i><i style="background:#fff"></i><i style="background:#000"></i></div></div>
<div class="nm"><b>55</b><span>الإمارات العربية المتحدة</span></div></div>
<div class="abs c s">كل عام <b>والإمارات</b> وأهلها بخير</div>
<div class="abs c dt"><span class="lat">2</span> ديسمبر</div>
<img class="abs lg" src="logo_t.png">
''')

digs=''.join(f'<div class="dg{" on" if ch!="0" else ""}"><span>{ch}</span></div>' for ch in '000055')
page('f3','ar','''
.sl{background:#0C0C0E;color:#F5F5F7}
.h{top:150px;font-size:128px;font-weight:800;line-height:1.25}
.od{left:90px;right:90px;top:470px;height:330px;border-radius:40px;background:#17171A;border:3px solid rgba(201,154,32,.55);display:flex;align-items:center;justify-content:center;gap:16px;direction:ltr;box-shadow:inset 0 0 60px rgba(0,0,0,.8),0 40px 90px rgba(0,0,0,.6)}
.dg{width:128px;height:230px;border-radius:16px;background:linear-gradient(180deg,#050506 0%,#232327 48%,#232327 52%,#050506 100%);border:1px solid #333;display:flex;align-items:center;justify-content:center;position:relative}
.dg:after{content:"";position:absolute;left:0;right:0;top:50%;height:2px;background:rgba(0,0,0,.6)}
.dg span{font-family:Inter;font-weight:800;font-size:170px;line-height:1;color:rgba(245,245,247,.22)}
.dg.on{background:linear-gradient(180deg,#8f6c12 0%,#E3B63F 48%,#E3B63F 52%,#8f6c12 100%);border-color:#E3B63F}
.dg.on span{color:#0C0C0E}
.un{top:830px;font-size:40px;font-weight:700;letter-spacing:1px;color:rgba(245,245,247,.7)}
.s{top:930px;font-size:60px;font-weight:700;line-height:1.5}
.s b{color:#E3B63F;font-weight:800}
.dt{top:1060px;font-size:38px;font-weight:600;color:rgba(245,245,247,.7)}
.lg{left:50%;transform:translateX(-50%);top:1160px;width:200px}
''','''
<div class="abs c h">عيد الاتحاد</div>
<div class="abs od">'''+digs+'''</div>
<div class="abs c un">سنة والمسيرة مستمرة</div>
<div class="abs c s">كل عام <b>والإمارات</b> وأهلها بخير</div>
<div class="abs c dt"><span class="lat">2</span> ديسمبر</div>
<img class="abs lg" src="logo_t.png">
''')

page('f3','ar','''
.sl{background:#EFEBE2;color:#111}
.h{top:120px;font-size:124px;font-weight:800;line-height:1.25}
.h .lat{font-weight:800;color:#A67C12}
.fg{left:140px;top:400px;width:800px;height:400px;display:flex;direction:ltr;box-shadow:0 30px 70px rgba(0,0,0,.28)}
.fg .r{width:200px;background:#C8102E}
.fg .st{flex:1;display:flex;flex-direction:column}
.fg .st i{flex:1;display:block}
.s{top:890px;font-size:62px;font-weight:800;line-height:1.5}
.dt{top:1010px;font-size:40px;font-weight:600;color:#5c574d}
.lg{left:50%;transform:translateX(-50%);top:1130px;width:150px;height:150px;border-radius:50%;background:#0C0C0E;display:flex;align-items:center;justify-content:center}
.lg img{width:112px}
''','''
<div class="abs c h">عيد الاتحاد <span class="lat">55</span></div>
<div class="abs fg"><div class="r"></div><div class="st"><i style="background:#00843D"></i><i style="background:#FFFFFF"></i><i style="background:#000000"></i></div></div>
<div class="abs c s">كل عام والإمارات وأهلها بخير</div>
<div class="abs c dt"><span class="lat">2</span> ديسمبر <span class="lat">2026</span></div>
<div class="abs lg"><img src="logo_t.png"></div>
''')

page('f3','ar','''
.sl{background:#0C0C0E;color:#F5F5F7}
.h{top:84px;font-size:124px;font-weight:800;line-height:1.25}
.fg{left:330px;top:300px;width:420px;height:210px;display:flex;direction:ltr;outline:2px solid rgba(255,255,255,.22);box-shadow:0 20px 60px rgba(0,0,0,.6)}
.fg .r{width:105px;background:#C8102E}
.fg .st{flex:1;display:flex;flex-direction:column}
.fg .st i{flex:1;display:block}
.pl{left:120px;top:590px;width:840px;height:340px;border-radius:34px;background:#F7F5EF;border:10px solid #111;outline:6px solid #C9C4B6;box-shadow:0 40px 90px rgba(0,0,0,.65);display:flex;flex-direction:column;align-items:center;justify-content:center;color:#111}
.pl b{font-family:Inter;font-weight:800;font-size:230px;line-height:.95;letter-spacing:-6px}
.pl span{font-size:38px;font-weight:800;letter-spacing:1px;margin-top:2px}
.pl:before,.pl:after{content:"";position:absolute;top:50%;width:18px;height:18px;margin-top:-9px;border-radius:50%;background:#b9b3a4;box-shadow:inset 0 2px 3px rgba(0,0,0,.4)}
.pl:before{left:34px}.pl:after{right:34px}
.s{top:985px;font-size:60px;font-weight:700;line-height:1.5}
.s b{color:#E3B63F;font-weight:800}
.dt{top:1100px;font-size:38px;font-weight:600;color:rgba(245,245,247,.7)}
.lg{left:50%;transform:translateX(-50%);top:1185px;width:180px}
''','''
<div class="abs c h">عيد الاتحاد</div>
<div class="abs fg"><div class="r"></div><div class="st"><i style="background:#00843D"></i><i style="background:#FFFFFF"></i><i style="background:#000000"></i></div></div>
<div class="abs pl"><b>55</b><span>الإمارات العربية المتحدة</span></div>
<div class="abs c s">كل عام <b>والإمارات</b> وأهلها بخير</div>
<div class="abs c dt"><span class="lat">2</span> ديسمبر</div>
<img class="abs lg" src="logo_t.png">
''')
