from playwright.sync_api import sync_playwright
D="#0E4D5C"; A="#7CC6D3"; L="#F4F9FA"; M="#2C6E7C"
def iso(drop,leaf1,leaf2,size):
    return f'<svg width="{size}" height="{size*1.2}" viewBox="0 0 100 120" aria-hidden="true"><path d="M50 4 C50 4 14 50 14 78 A36 36 0 0 0 86 78 C86 50 50 4 50 4 Z" fill="{drop}"/><path d="M50 100 C47 82 51 66 68 56 C70 76 64 92 50 100 Z" fill="{leaf1}"/><path d="M50 100 C52 88 46 78 34 73 C32 86 39 96 50 100 Z" fill="{leaf2}"/></svg>'
def word(col,w):
    S=lambda cx:f"M{cx+20} 58 C{cx+12} 47 {cx-22} 47 {cx-21} 63 C{cx-19} 76 {cx+22} 72 {cx+21} 88 C{cx+20} 103 {cx-14} 104 {cx-22} 92"
    E=lambda cx:f"M{cx-25} 75 H{cx+25} A25 25 0 1 0 {cx+17.7} 92.7"
    R=lambda x:f"M{x} 50 V100 M{x} 72 C{x} 57 {x+12} 50 {x+26} 51"
    N=lambda x:f"M{x} 50 V100 M{x} 72 C{x} 58 {x+10} 50 {x+22} 50 C{x+36} 50 {x+44} 58 {x+44} 72 V100"
    V=lambda x:f"M{x} 50 L{x+22} 100 L{x+44} 50"
    T=lambda x:f"M{x} 32 V88 C{x} 98 {x+6} 101 {x+16} 99"
    Aa=lambda cx:f"M{cx+25} 75 A25 25 0 1 0 {cx-25} 75 A25 25 0 1 0 {cx+25} 75 M{cx+25} 50 V100"
    d=" ".join([S(22),E(87),R(130),E(195),N(238),V(298),"M360 50 V100",T(384),T(418),"M375 52 H434",Aa(473)])
    return f'<svg width="{w}" height="{w*82/512}" viewBox="-5 25 512 82" aria-hidden="true"><path d="{d}" fill="none" stroke="{col}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/><circle cx="360" cy="34" r="6.5" fill="{col}"/></svg>'
def foot(dark):
    if dark: return f'<div class="foot">{iso(L,A,D,34)}{word(L,170)}</div>'
    return f'<div class="foot">{iso(D,A,"#fff",34)}{word(D,170)}</div>'

import base64,os
def uri(p):
    ext="png" if p.endswith(".png") else "jpeg"
    return f"data:image/{ext};base64,"+base64.b64encode(open(p,"rb").read()).decode()
IMG={n:uri(f"assets/{n}.jpg") for n in ["k8-cocina","k8-grifo","k8-pantalla","vaso","mano-vaso"]}
SELLO=uri("assets/sello.png")
CSS=f"""*{{box-sizing:border-box;margin:0}}body{{width:1080px;height:1350px;font-family:Inter,sans-serif;overflow:hidden}}
.s{{width:1080px;height:1350px;position:relative;display:flex;flex-direction:column;overflow:hidden}}
.light{{background:{L};color:{D}}}.dark{{background:{D};color:#fff}}
.pad{{padding:120px 100px 0}}
.kick{{font-size:30px;font-weight:600;letter-spacing:6px;text-transform:uppercase}}
.light .kick{{color:{M}}}.dark .kick{{color:{A}}}
h1{{font-size:92px;line-height:1.05;font-weight:700;letter-spacing:-2px;margin-top:30px}}
.lead{{font-size:40px;line-height:1.42;margin-top:36px}}
.light .lead{{color:{M}}}.dark .lead{{color:#E3F1F4}}
.acc{{color:{A}}}
.big{{font-size:300px;font-weight:800;letter-spacing:-10px;line-height:.9}}
.light .big{{color:{D}}}.dark .big{{color:{A}}}
ul{{list-style:none;padding:0;margin-top:56px;display:flex;flex-direction:column;gap:34px}}
li{{display:flex;gap:30px;align-items:baseline;font-size:46px;font-weight:600;line-height:1.2}}
li b{{font-size:34px;font-weight:700;min-width:64px}}
.light li b{{color:{M}}}.dark li b{{color:{A}}}
li span{{display:block;font-size:33px;font-weight:400;margin-top:8px;line-height:1.35}}
.light li span{{color:{M}}}.dark li span{{color:#E3F1F4}}
.foot{{position:absolute;left:100px;bottom:76px;display:flex;align-items:center;gap:18px}}
.cnt{{position:absolute;right:100px;bottom:84px;font-size:28px;font-weight:600;letter-spacing:2px}}
.light .cnt{{color:{M}}}.dark .cnt{{color:{A}}}
.photo{{width:1080px;height:780px;object-fit:cover;display:block}}
.panel{{flex:1;background:{D};color:#fff;padding:64px 100px 0}}
.panel .kick{{color:{A}}}.panel h1{{font-size:84px;margin-top:22px}}
.sello{{position:absolute;width:150px;height:150px;border-radius:50%;background:#fff;padding:10px;display:flex;align-items:center;justify-content:center}}
.sello img{{width:100%;height:100%;object-fit:contain}}
.btn{{margin-top:60px;align-self:flex-start;padding:30px 54px;border-radius:999px;font-size:40px;font-weight:700}}
.dark .btn{{background:{A};color:{D}}}.light .btn{{background:{D};color:#fff}}
"""
def ft(dark,n,N,cover=False):
    c=f"Desliza  →" if cover else f"{n}/{N}"
    return foot(dark)+f'<div class="cnt">{c}</div>'
def cover_photo(img,kick,title,pos="center"):
    return lambda n,N:("dark",f'<img class="photo" src="{IMG[img]}" style="object-position:{pos}"><div class="sello" style="top:48px;right:48px">{"<img src=%s>"%SELLO}</div><div class="panel"><div class="kick">{kick}</div><h1>{title}</h1></div>'+ft(True,n,N,True))
def cover_text(theme,kick,title,lead="",extra=""):
    return lambda n,N:(theme,f'<div class="pad" style="flex:1;display:flex;flex-direction:column;justify-content:center;padding-bottom:160px"><div class="kick">{kick}</div><h1 style="font-size:110px">{title}</h1>{f"<div class=lead>{lead}</div>" if lead else ""}{extra}</div>'+ft(theme=="dark",n,N,True))
def big(theme,b,kick,title,text,bsize=300):
    return lambda n,N:(theme,f'<div class="pad" style="flex:1;display:flex;flex-direction:column;justify-content:center;padding-bottom:180px"><div class="kick">{kick}</div><div class="big" style="margin-top:70px;font-size:{bsize}px">{b}</div><h1 style="margin-top:50px;font-size:76px">{title}</h1><div class="lead">{text}</div></div>'+ft(theme=="dark",n,N))
def lst(theme,kick,title,items):
    li="".join(f"<li><b>{b}</b><div>{t}{f'<span>{s}</span>' if s else ''}</div></li>" for b,t,s in items)
    return lambda n,N:(theme,f'<div class="pad" style="flex:1;display:flex;flex-direction:column;justify-content:center;padding-bottom:180px"><div class="kick">{kick}</div><h1 style="font-size:84px">{title}</h1><ul>{li}</ul></div>'+ft(theme=="dark",n,N))
def photo_slide(img,kick,title,text,pos="center"):
    return lambda n,N:("light",f'<img class="photo" style="height:700px;object-position:{pos}" src="{IMG[img]}"><div class="pad" style="padding-top:64px"><div class="kick">{kick}</div><h1 style="font-size:76px;margin-top:20px">{title}</h1><div class="lead" style="margin-top:24px">{text}</div></div>'+ft(False,n,N))
def cta():
    return lambda n,N:("dark",f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 100px 120px">{iso(L,A,D,170)}<h1 style="font-size:88px;margin-top:50px">¿Hablamos?</h1><div class="lead">Precio, financiación e instalación de tu Leveluk K8, sin compromiso.</div><div class="btn" style="align-self:center">Escríbenos por WhatsApp</div><div style="display:flex;align-items:center;gap:22px;margin-top:70px"><div style="width:120px;height:120px;border-radius:50%;background:#fff;padding:8px"><img src="{SELLO}" style="width:100%;height:100%;object-fit:contain"></div><div style="font-size:30px;font-weight:600;text-align:left;line-height:1.3">Distribuidora<br>independiente Enagic®</div></div></div>'+f'<div class="cnt">{n}/{N}</div>')
C={}
C[1]=[cover_text("light","Serenvitta","Agua Kangen® en tu casa.","Directamente de tu grifo, con el equipo original de Enagic®.",f'<div style="display:flex;align-items:center;gap:24px;margin-top:60px"><div style="width:150px;height:150px"><img src="{SELLO}" style="width:100%;height:100%"></div><div style="font-size:32px;font-weight:600;line-height:1.3;color:{D}">Distribuidora<br>independiente Enagic®</div></div>'),
 lst("light","Quiénes somos","Te ayudamos a tener tu K8",[("01","Te asesoramos","Resolvemos tus dudas antes de comprar"),("02","Te acompañamos","En la instalación y la puesta en marcha"),("03","Seguimos contigo","Mantenimiento, filtros y consejos de uso")]),
 lst("light","En este perfil","Lo que vas a encontrar",[("01","El Leveluk K8 por dentro",""),("02","Usos del agua en casa",""),("03","Financiación a tu medida",""),("04","Respuestas a tus dudas","")]),
 cta()]
C[2]=[cover_photo("k8-cocina","Leveluk K8","Te presento el K8",pos="center 40%"),
 big("light","8","Electrólisis","Placas de titanio platinado","El corazón del equipo: son las que separan el agua en sus distintos tipos."),
 big("dark","7","Versatilidad","Niveles de pH","Desde agua para beber y cocinar hasta agua para la limpieza del hogar."),
 photo_slide("k8-pantalla","Fácil de usar","Pantalla táctil","Eliges el agua que necesitas con un solo toque.","center 30%"),
 big("dark","JP","Calidad","Fabricado en Japón","Por Enagic®, con su propia tecnología y control de calidad.",bsize=260),
 cta()]
C[3]=[cover_text("dark","Leveluk K8",'Un equipo, <span class="acc">5 tipos de agua.</span>',"Desliza y descubre para qué sirve cada una."),
 big("light","8,5–9,5","pH","Agua Kangen®","Para beber y cocinar cada día.",bsize=190),
 big("dark","7","pH","Agua neutra","Agua filtrada para el uso diario."),
 big("light","6","pH","Agua de belleza","Para el cuidado exterior de la piel y el cabello."),
 big("dark","11,5","pH","Alcalina fuerte","Para lavar fruta y verdura y desengrasar.",bsize=250),
 big("light","2,5","pH","Ácida fuerte","Para la limpieza del hogar.",bsize=250),
 cta()]
C[4]=[cover_photo("vaso","Garrafas vs. K8","¿Sigues cargando garrafas?",pos="center 55%"),
 lst("light","El problema","Lo que ya conoces",[("✕","Peso","Cargar garrafas del súper a casa"),("✕","Plástico","Envases que tiras cada semana"),("✕","Espacio","La despensa llena de agua")]),
 lst("dark","Con el K8","Lo que ganas",[("✓","Agua al instante","Directamente desde tu grifo"),("✓","Sin cargar nada","Ni viajes extra al súper"),("✓","4 tipos de agua más","Para cocina, limpieza y cuidado")]),
 lst("light","Hagamos cuentas","¿Cuánto gastas en agua?",[("01","Cuántas garrafas compras al mes",""),("02","Cuántos años llevas haciéndolo",""),("03","Te lo comparamos con tu K8","Escríbenos y lo calculamos contigo")]),
 cta()]
C[5]=[cover_text("light","Financiación",'Tu K8 en casa, <span style="color:#2C6E7C">en cómodas cuotas.</span>',"Un plan a tu medida, sin sorpresas."),
 lst("light","Así de fácil","Cómo funciona",[("01","Nos escribes","Por WhatsApp o mensaje directo"),("02","Calculamos tu cuota","Según lo que te encaje"),("03","Instalamos tu K8","Y empiezas a disfrutarlo")]),
 big("dark","€","Sin sorpresas","Precio cerrado","Te damos el precio completo y las condiciones antes de que decidas.",bsize=260),
 cta()]
C[6]=[cover_photo("k8-grifo","Instalación","Se conecta a tu grifo",pos="center 45%"),
 lst("light","Paso a paso","Instalarlo es sencillo",[("01","Adaptador en el grifo","El que ya tienes en tu cocina"),("02","Colocas el equipo","En la encimera, junto al grifo"),("03","Lo enciendes","Y eliges el agua en la pantalla")]),
 big("dark","0","Sin obras","Obras necesarias","No hace falta tocar la instalación de tu cocina.",bsize=300),
 lst("light","No estás solo","Te acompañamos",[("✓","Adaptadores para distintos grifos",""),("✓","Ayuda en la puesta en marcha",""),("✓","Consejos de uso y mantenimiento","")]),
 cta()]
C[7]=[lambda n,N:("dark",f'<div class="pad" style="flex:1;display:flex;flex-direction:column;justify-content:center;padding-bottom:160px"><div style="width:300px;height:300px;border-radius:50%;background:#fff;padding:18px"><img src="{SELLO}" style="width:100%;height:100%;object-fit:contain"></div><div class="kick" style="margin-top:60px">Enagic® · Japón</div><h1 style="font-size:100px">Distribuidora independiente Enagic®</h1></div>'+ft(True,n,N,True)),
 big("light","1974","Desde","Nace Enagic® en Japón","Más de 50 años dedicados a fabricar ionizadores de agua.",bsize=260),
 big("dark","JP","Origen","Fabricado en Japón","Cada Leveluk K8 sale de las fábricas de Enagic® en Japón.",bsize=260),
 lst("light","Con Serenvitta","Compras con garantía",[("✓","Equipo original Enagic®",""),("✓","Distribuidora independiente",""),("✓","Atención cercana y en español","")]),
 cta()]
C[8]=[cover_photo("k8-pantalla","Así funciona","Cómo funciona tu K8",pos="center 30%"),
 big("light","01","Paso 1","Filtra el agua","Antes de nada, el agua del grifo pasa por su filtro."),
 big("dark","02","Paso 2","Electrólisis","Sus 8 placas separan el agua en distintos tipos según su pH."),
 big("light","03","Paso 3","Eliges con un toque","En la pantalla táctil, el agua que necesitas en cada momento."),
 big("dark","04","Mantenimiento","Autolimpieza","Y solo un cambio de filtro periódico."),
 cta()]
C[9]=[cover_text("dark","Preguntas frecuentes",'Antes de comprar <span class="acc">tu K8</span>',"Las dudas que más nos llegan, respondidas."),
 lst("light","Pregunta 1","¿Cuánto cuesta?",[("→","Precio cerrado","Te lo damos completo, sin letra pequeña"),("→","Financiación","En cuotas adaptadas a ti","")][:2] if False else [("→","Precio cerrado","Te lo damos completo, sin letra pequeña"),("→","Financiación","En cuotas adaptadas a ti")]),
 lst("dark","Pregunta 2","¿Es difícil instalarlo?",[("→","Se conecta a tu grifo","Sin obras"),("→","Te acompañamos","En la puesta en marcha")]),
 lst("light","Pregunta 3","¿Qué mantenimiento necesita?",[("→","Autolimpieza","El equipo se limpia solo"),("→","Filtro","Un cambio periódico")]),
 lst("dark","Pregunta 4","¿Y si tengo más dudas?",[("→","Escríbenos","Por WhatsApp o mensaje directo"),("→","Te respondemos","Con calma y sin compromiso")]),
 cta()]
from playwright.sync_api import sync_playwright
os.makedirs("out",exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1350})
    for c,slides in C.items():
        N=len(slides)
        for i,f in enumerate(slides,1):
            theme,body=f(i,N)
            pg.set_content(f'<html lang="es"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="s {theme}">{body}</div></body></html>')
            pg.screenshot(path=f"out/carrusel-{c}-{i:02d}.png",clip={"x":0,"y":0,"width":1080,"height":1350})
    b.close()
from PIL import Image
g=Image.new("RGB",(3*360+8,3*450+8),"white")
for k,c in enumerate(range(9,0,-1)):
    g.paste(Image.open(f"out/carrusel-{c}-01.png").resize((360,450)),((k%3)*364,(k//3)*454))
g.save("out/cuadricula.png")
# contact sheet of all slides
import glob
fs=sorted(glob.glob("out/carrusel-*.png"),key=lambda f:(int(f.split('-')[1]),f))
cols=7; rows=9
s=Image.new("RGB",(cols*220,rows*275),"white")
for f in fs:
    c=int(f.split('-')[1]); i=int(f.split('-')[2][:2])
    s.paste(Image.open(f).resize((216,270)),((i-1)*220,(c-1)*275))
s.save("out/todas.png")
