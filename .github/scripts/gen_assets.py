import os, math
from PIL import Image, ImageDraw

OUT = "D:/schools/supergigachadsupreme300/aquarium/assets/sprites"
os.makedirs(OUT, exist_ok=True)

def new(w, h):
    return Image.new("RGBA", (w, h), (0,0,0,0))
def save(img, name):
    img.save(os.path.join(OUT, name), "PNG")
    print("saved", name)

K = (18,18,24,255)
def ell(d,x0,y0,x1,y1,fill,outline=K,w=1): d.ellipse((x0,y0,x1,y1),fill=fill,outline=outline,width=w)
def rect(d,x0,y0,x1,y1,fill,outline=K,w=1): d.rectangle((x0,y0,x1,y1),fill=fill,outline=outline,width=w)
def poly(d,pts,fill,outline=K,w=1): d.polygon(pts,fill=fill,outline=outline,width=w)
def line(d,x0,y0,x1,y1,fill,w=1): d.line((x0,y0,x1,y1),fill=fill,width=w)
def smooth_body(d, cx, cy, rx, ry, fill, outline=K, steps=24):
    # organic body via polygon with slight waviness
    pts=[]
    for i in range(steps):
        a=2*math.pi*i/steps
        rrx=rx*(1+0.04*math.sin(3*a))
        rry=ry*(1+0.03*math.cos(2*a))
        pts.append((cx+math.cos(a)*rrx, cy+math.sin(a)*rry))
    poly(d, pts, fill, outline, 1)

# ---------- Clownfish ----------
def clownfish(tail_up=False):
    img=new(96,48); d=ImageDraw.Draw(img)
    O=(255,112,67,255); D=(185,55,25,255); W=(255,255,255,255); Bk=(18,18,24,255)
    Y=(255,193,7,255); L=(255,175,145,255); S=(210,80,40,255)
    ty=22 if not tail_up else 16
    # tail
    poly(d,[(8,ty),(0,ty-9),(3,ty),(0,ty+9)],O,Bk,1)
    poly(d,[(8,ty),(3,ty-5),(5,ty),(3,ty+5)],D,None)
    # body
    smooth_body(d,46,24,34,15,O,Bk,32)
    # shadow lower
    smooth_body(d,46,28,30,10,D,None,32)
    # highlight
    smooth_body(d,40,16,22,8,L,None,24)
    # white bands with dark edges
    for bx in (26,46):
        rect(d,bx,8,bx+7,40,W,Bk,1)
        rect(d,bx+2,8,bx+5,40,(230,230,230,255),None)
    # dorsal fin
    poly(d,[(28,7),(42,0),(56,7)],Y,Bk,1)
    poly(d,[(30,7),(42,2),(54,7)],(255,224,130,255),None)
    # pectoral
    poly(d,[(40,26),(32,36),(48,36)],Y,Bk,1)
    # anal
    poly(d,[(40,40),(32,46),(48,46)],Y,Bk,1)
    # eye
    ell(d,64,14,72,22,(255,255,255,255),Bk,1)
    ell(d,65,15,71,21,(20,20,20,255),None)
    ell(d,66,15,69,18,(255,255,255,255),None)
    # mouth
    line(d,74,22,76,23,Bk,1)
    # scales
    for i in range(6):
        for j in range(3):
            d.point((22+i*6,14+j*7),fill=S)
    return img

# ---------- Blue Tang ----------
def bluetang(tail_up=False):
    img=new(96,48); d=ImageDraw.Draw(img)
    B=(30,136,229,255); D=(13,71,161,255); Y=(255,235,59,255); Bk=(18,18,24,255)
    L=(100,181,246,255); S=(20,90,180,255)
    ty=23 if not tail_up else 17
    poly(d,[(8,ty),(0,ty-10),(3,ty),(0,ty+10)],Y,Bk,1)
    poly(d,[(8,ty),(3,ty-6),(5,ty),(3,ty+6)],(200,200,50,255),None)
    smooth_body(d,48,24,36,16,B,Bk,36)
    smooth_body(d,48,28,32,11,D,None,36)
    smooth_body(d,40,16,24,9,L,None,28)
    # yellow tail base
    ell(d,8,16,18,30,Y,Bk,1)
    # dorsal fin
    poly(d,[(22,6),(42,0),(60,6)],D,Bk,1)
    poly(d,[(24,6),(42,2),(58,6)],B,None)
    # anal fin
    poly(d,[(22,42),(42,48),(60,42)],D,Bk,1)
    # pectoral
    poly(d,[(42,28),(34,36),(50,36)],D,Bk,1)
    # eye
    ell(d,66,14,74,22,(255,255,255,255),Bk,1)
    ell(d,67,15,73,21,Bk,None)
    ell(d,68,15,71,18,(255,255,255,255),None)
    line(d,76,20,78,21,Bk,1)
    for i in range(5):
        d.point((24+i*7,16+(i%2)*4),fill=S)
    return img

# ---------- Angelfish ----------
def angelfish(tail_up=False):
    img=new(80,80); d=ImageDraw.Draw(img)
    P=(244,143,177,255); D=(194,24,91,255); Y=(255,235,59,255); Bk=(18,18,24,255)
    L=(248,187,208,255)
    ty=36 if not tail_up else 28
    poly(d,[(6,ty),(0,ty-6),(0,ty+6)],D,Bk,1)
    smooth_body(d,40,40,26,30,P,Bk,40)
    smooth_body(d,40,52,24,14,D,None,40)
    smooth_body(d,34,24,16,12,L,None,32)
    # stripes
    poly(d,[(18,10),(22,10),(22,70),(18,70)],D,Bk,1)
    poly(d,[(34,10),(38,10),(38,70),(34,70)],D,Bk,1)
    # long dorsal
    poly(d,[(12,10),(32,0),(52,10)],D,Bk,1)
    poly(d,[(14,10),(32,3),(50,10)],P,None)
    # anal fin
    poly(d,[(12,70),(32,80),(52,70)],D,Bk,1)
    # pectoral
    poly(d,[(30,44),(20,56),(40,56)],(255,200,220,255),Bk,1)
    # eye
    ell(d,52,24,60,32,(255,255,255,255),Bk,1)
    ell(d,53,25,59,31,Bk,None)
    ell(d,54,25,57,28,(255,255,255,255),None)
    line(d,58,30,60,31,Bk,1)
    return img

# ---------- Butterflyfish ----------
def butterflyfish(tail_up=False):
    img=new(80,48); d=ImageDraw.Draw(img)
    Y=(255,235,59,255); D=(249,168,37,255); B=(26,35,126,255); Bk=(18,18,24,255)
    O=(255,143,0,255); L=(255,249,196,255)
    ty=22 if not tail_up else 17
    poly(d,[(6,ty),(0,ty-5),(0,ty+5)],O,Bk,1)
    smooth_body(d,40,24,30,16,Y,Bk,36)
    smooth_body(d,40,28,28,10,D,None,36)
    smooth_body(d,32,16,20,9,L,None,28)
    # eye spot
    ell(d,14,14,24,24,B,Bk,1)
    ell(d,16,16,22,22,Bk,None)
    ell(d,17,16,21,20,(255,255,255,255),None)
    # vertical bar
    poly(d,[(40,8),(46,8),(46,40),(40,40)],B,Bk,1)
    # dorsal fin
    poly(d,[(18,7),(32,0),(46,7)],O,Bk,1)
    poly(d,[(20,7),(32,2),(44,7)],Y,None)
    # eye
    ell(d,52,14,60,22,(255,255,255,255),Bk,1)
    ell(d,53,15,59,21,Bk,None)
    ell(d,54,15,57,18,(255,255,255,255),None)
    line(d,62,20,64,21,Bk,1)
    return img

# ---------- Pufferfish ----------
def pufferfish(tail_up=False):
    img=new(72,60); d=ImageDraw.Draw(img)
    Y=(255,245,157,255); D=(192,202,51,255); P=(244,143,177,255); Bk=(18,18,24,255)
    W=(255,255,255,255); G=(93,64,55,255); L=(255,255,230,255)
    cx,cy=34,30; r=22
    # body (slightly oval)
    smooth_body(d,cx,cy,r,r*0.9,Y,Bk,40)
    smooth_body(d,cx,cy+4,r-3,r*0.7,D,None,40)
    smooth_body(d,cx-4,cy-6,r*0.5,r*0.4,L,None,32)
    import math
    for i in range(12):
        a=math.radians(i*30)
        x=cx+int(math.cos(a)*8); y=cy+int(math.sin(a)*8)
        ell(d,x-3,y-3,x+3,y+3,P,None)
    # spikes
    for i in range(18):
        a=math.radians(i*20)
        x1=cx+int(math.cos(a)*r); y1=cy+int(math.sin(a)*r)
        x2=cx+int(math.cos(a)*(r+6)); y2=cy+int(math.sin(a)*(r+6))
        line(d,x1,y1,x2,y2,G,1)
    # tail
    ty=cy if not tail_up else cy-5
    poly(d,[(cx-r,ty),(cx-r-9,ty-6),(cx-r-9,ty+6)],P,Bk,1)
    # eye
    ell(d,cx+8,cy-8,cx+18,cy+2,W,Bk,1)
    ell(d,cx+9,cy-7,cx+17,cy+1,Bk,None)
    ell(d,cx+10,cy-7,cx+13,cy-4,W,None)
    # mouth
    ell(d,cx+r-3,cy+2,cx+r+2,cy+6,G,None)
    return img

# ---------- Lionfish ----------
def lionfish(tail_up=False):
    img=new(100,52); d=ImageDraw.Draw(img)
    R=(229,57,53,255); D=(183,28,28,255); W=(255,255,255,255); Bk=(18,18,24,255)
    Y=(255,202,40,255); O=(255,112,67,255); L=(255,138,128,255)
    ty=24 if not tail_up else 18
    poly(d,[(8,ty),(0,ty-7),(3,ty),(0,ty+7)],D,Bk,1)
    poly(d,[(8,ty),(3,ty-4),(5,ty),(3,ty+4)],R,None)
    smooth_body(d,52,26,40,16,R,Bk,40)
    smooth_body(d,52,32,36,11,D,None,40)
    smooth_body(d,42,18,26,9,L,None,32)
    # stripes
    for sx in [18,25,32,39,46,53,60]:
        poly(d,[(sx,10),(sx+4,10),(sx+4,40),(sx,40)],W,Bk,1)
    # dorsal fins (dramatic)
    for fx in range(16,72,7):
        poly(d,[(fx,10),(fx+3,0),(fx+7,10)],Y,Bk,1)
        poly(d,[(fx+1,10),(fx+3,2),(fx+6,10)],(255,236,179,255),None)
    # pectoral fan
    poly(d,[(36,30),(22,48),(50,48)],O,Bk,1)
    poly(d,[(38,30),(26,46),(48,46)],Y,None)
    # anal fin
    poly(d,[(36,42),(28,52),(44,52)],O,Bk,1)
    # eye
    ell(d,74,16,82,24,(255,255,255,255),Bk,1)
    ell(d,75,17,81,23,Bk,None)
    ell(d,76,17,79,20,(255,255,255,255),None)
    line(d,84,22,86,23,Bk,1)
    return img

# ---------- Moorish Idol ----------
def moorishidol(tail_up=False):
    img=new(96,44); d=ImageDraw.Draw(img)
    B=(20,20,20,255); W=(255,255,255,255); Y=(255,193,7,255); Bk=(18,18,24,255)
    L=(240,240,240,255)
    ty=20 if not tail_up else 15
    poly(d,[(6,ty),(0,ty-6),(0,ty+6)],Y,Bk,1)
    smooth_body(d,44,22,34,16,W,Bk,40)
    smooth_body(d,44,28,32,10,(225,225,225,255),None,40)
    # black bands
    poly(d,[(18,6),(26,6),(26,38),(18,38)],B,Bk,1)
    poly(d,[(34,6),(42,6),(42,38),(34,38)],B,Bk,1)
    # yellow dorsal (elongated)
    poly(d,[(20,6),(28,0),(36,6)],Y,Bk,1)
    poly(d,[(36,6),(44,-5),(52,6)],Y,Bk,1)
    poly(d,[(52,6),(60,-2),(68,6)],Y,Bk,1)
    # snout
    rect(d,68,16,88,20,W,Bk,1)
    rect(d,68,17,88,19,B,None)
    # eye
    ell(d,56,12,64,20,(255,255,255,255),Bk,1)
    ell(d,57,13,63,19,Bk,None)
    ell(d,58,13,61,16,(255,255,255,255),None)
    return img

# ---------- Royal Gramma ----------
def royalgramma(tail_up=False):
    img=new(80,40); d=ImageDraw.Draw(img)
    P=(123,31,162,255); Y=(255,213,79,255); D=(74,20,140,255); Bk=(18,18,24,255)
    L=(170,80,200,255)
    ty=18 if not tail_up else 13
    poly(d,[(6,ty),(0,ty-6),(0,ty+6)],Y,Bk,1)
    smooth_body(d,42,20,32,14,P,Bk,36)
    smooth_body(d,42,26,28,8,D,None,36)
    smooth_body(d,32,14,20,7,L,None,28)
    # yellow rear half
    for x in range(46,70):
        for y in range(6,34):
            if (x-56)**2/12**2+(y-20)**2/13**2<=1:
                d.point((x,y),fill=Y)
    # dorsal fin
    poly(d,[(18,6),(34,0),(50,6)],D,Bk,1)
    poly(d,[(20,6),(34,2),(48,6)],P,None)
    # pectoral
    poly(d,[(34,24),(26,32),(42,32)],(180,100,200,255),Bk,1)
    # eye
    ell(d,58,10,66,18,(255,255,255,255),Bk,1)
    ell(d,59,11,65,17,Bk,None)
    ell(d,60,11,63,14,(255,255,255,255),None)
    line(d,68,16,70,17,Bk,1)
    return img

# ---------- Koi ----------
def koi(tail_up=False):
    img=new(100,44); d=ImageDraw.Draw(img)
    O=(255,138,101,255); D=(216,67,21,255); W=(255,255,255,255); Bk=(18,18,24,255)
    R=(191,54,12,255); Y=(255,202,40,255); L=(255,171,145,255)
    ty=20 if not tail_up else 14
    poly(d,[(8,ty),(0,ty-8),(4,ty),(0,ty+8)],R,Bk,1)
    poly(d,[(8,ty),(4,ty-5),(6,ty),(4,ty+5)],D,None)
    smooth_body(d,50,22,42,16,O,Bk,44)
    smooth_body(d,50,28,38,10,D,None,44)
    smooth_body(d,40,14,26,9,L,None,32)
    # white patches
    smooth_body(d,26,14,10,7,W,Bk,24)
    smooth_body(d,60,16,9,7,W,Bk,24)
    # red patch
    smooth_body(d,44,20,8,6,R,Bk,24)
    # dorsal fin
    poly(d,[(26,6),(42,0),(58,6)],R,Bk,1)
    poly(d,[(28,6),(42,2),(56,6)],O,None)
    # pectoral
    poly(d,[(46,26),(36,36),(56,36)],(255,180,160,255),Bk,1)
    # eye
    ell(d,72,12,80,20,(255,255,255,255),Bk,1)
    ell(d,73,13,79,19,Bk,None)
    ell(d,74,13,77,16,(255,255,255,255),None)
    line(d,82,18,84,19,Bk,1)
    return img

# ---------- Goldfish ----------
def goldfish(tail_up=False):
    img=new(80,44); d=ImageDraw.Draw(img)
    Y=(255,202,40,255); D=(249,168,37,255); W=(255,255,255,255); Bk=(18,18,24,255)
    R=(229,57,53,255); L=(255,236,179,255)
    ty=20 if not tail_up else 14
    poly(d,[(6,ty),(0,ty-7),(3,ty),(0,ty+7)],R,Bk,1)
    poly(d,[(6,ty),(3,ty-4),(4,ty),(3,ty+4)],D,None)
    smooth_body(d,42,22,32,16,Y,Bk,40)
    smooth_body(d,42,28,28,10,D,None,40)
    smooth_body(d,34,14,22,9,L,None,32)
    smooth_body(d,26,14,8,6,W,Bk,24)
    poly(d,[(20,6),(32,0),(44,6)],D,Bk,1)
    poly(d,[(22,6),(32,2),(42,6)],Y,None)
    poly(d,[(30,26),(20,36),(40,36)],(255,224,130,255),Bk,1)
    ell(d,56,12,64,20,(255,255,255,255),Bk,1)
    ell(d,57,13,63,19,Bk,None)
    ell(d,58,13,61,16,(255,255,255,255),None)
    line(d,66,18,68,19,Bk,1)
    return img

# ---------- Tropical ----------
def tropical(tail_up=False):
    img=new(80,40); d=ImageDraw.Draw(img)
    G=(0,230,118,255); D=(0,137,123,255); P=(255,64,129,255); Bk=(18,18,24,255)
    W=(255,255,255,255); L=(100,255,180,255)
    ty=18 if not tail_up else 13
    poly(d,[(6,ty),(0,ty-6),(0,ty+6)],P,Bk,1)
    smooth_body(d,40,20,32,14,G,Bk,36)
    smooth_body(d,40,26,28,9,D,None,36)
    smooth_body(d,32,13,22,8,L,None,28)
    for sx in [16,22,28,34,40,46]:
        poly(d,[(sx,6),(sx+4,6),(sx+4,34),(sx,34)],P,Bk,1)
    poly(d,[(14,6),(20,0),(26,6)],P,Bk,1)
    ell(d,52,8,60,16,W,Bk,1)
    ell(d,53,9,59,15,Bk,None)
    ell(d,54,9,57,12,W,None)
    line(d,62,14,64,15,Bk,1)
    return img

# ---------- Exotic ----------
def exotic(tail_up=False):
    img=new(88,44); d=ImageDraw.Draw(img)
    V=(224,64,251,255); D=(123,31,162,255); C=(0,229,255,255); Bk=(18,18,24,255)
    W=(255,255,255,255); L=(235,120,255,255)
    ty=20 if not tail_up else 15
    poly(d,[(7,ty),(0,ty-7),(3,ty),(0,ty+7)],C,Bk,1)
    smooth_body(d,46,22,36,16,V,Bk,40)
    smooth_body(d,46,28,32,10,D,None,40)
    smooth_body(d,36,14,24,9,L,None,32)
    smooth_body(d,26,16,10,7,C,Bk,24)
    smooth_body(d,29,18,7,5,V,None,24)
    poly(d,[(18,6),(26,0),(34,6)],C,Bk,1)
    poly(d,[(34,6),(42,0),(50,6)],C,Bk,1)
    ell(d,62,12,70,20,W,Bk,1)
    ell(d,63,13,69,19,Bk,None)
    ell(d,64,13,67,16,W,None)
    line(d,72,18,74,19,Bk,1)
    return img

# ---------- Small reef fish ----------
def smallreef(tail_up=False):
    img=new(56,32); d=ImageDraw.Draw(img)
    C=(38,198,218,255); D=(0,131,143,255); Y=(255,238,88,255); Bk=(18,18,24,255)
    W=(255,255,255,255); L=(100,220,230,255)
    ty=14 if not tail_up else 10
    poly(d,[(4,ty),(0,ty-5),(0,ty+5)],D,Bk,1)
    smooth_body(d,28,16,22,11,C,Bk,32)
    smooth_body(d,28,21,18,6,D,None,32)
    smooth_body(d,22,11,14,6,L,None,24)
    poly(d,[(12,5),(17,0),(22,5)],Y,Bk,1)
    ell(d,36,8,44,16,W,Bk,1)
    ell(d,37,9,43,15,Bk,None)
    ell(d,38,9,41,12,W,None)
    line(d,46,13,48,14,Bk,1)
    return img

# ---------- Sea Turtle ----------
def turtle(tail_up=False):
    img=new(108,68); d=ImageDraw.Draw(img)
    G=(46,125,50,255); D=(27,94,32,255); L=(102,187,106,255); Bk=(18,18,24,255)
    Y=(255,241,118,255)
    smooth_body(d,54,34,46,26,G,Bk,48)
    smooth_body(d,54,38,40,20,D,None,48)
    smooth_body(d,40,22,24,14,L,None,36)
    # scutes
    for i in range(-3,4):
        line(d,54+i*9,12,54+i*9,56,D,1)
    line(d,14,34,94,34,D,1)
    # head
    smooth_body(d,92,34,14,10,L,Bk,24)
    ell(d,96,30,104,38,Bk,None)
    ell(d,97,30,101,34,(255,255,255,255),None)
    # flippers
    poly(d,[(18,12),(6,4),(14,20)],L,Bk,1)
    poly(d,[(18,56),(6,64),(14,48)],L,Bk,1)
    poly(d,[(82,12),(92,4),(86,20)],L,Bk,1)
    poly(d,[(82,56),(92,64),(86,48)],L,Bk,1)
    return img

# ---------- Environment (keep existing, slightly refined) ----------
def branching_coral():
    img=new(96,96); d=ImageDraw.Draw(img)
    R=(239,83,80,255); D=(183,28,28,255); K=(18,18,24,255); P=(255,138,101,255); L=(255,180,170,255)
    poly(d,[(48,94),(28,46),(36,42)],R,K,1); poly(d,[(48,94),(68,46),(60,42)],R,K,1)
    poly(d,[(36,52),(20,26),(28,22)],D,K,1); poly(d,[(60,52),(76,26),(68,22)],D,K,1)
    poly(d,[(48,42),(42,10),(54,10)],P,K,1)
    poly(d,[(42,48),(36,32),(46,32)],L,None)
    smooth_body(d,48,88,22,10,D,K,24)
    return img
def brain_coral():
    img=new(84,64); d=ImageDraw.Draw(img)
    O=(255,138,101,255); D=(230,74,25,255); K=(18,18,24,255)
    smooth_body(d,42,32,38,26,O,K,40)
    smooth_body(d,42,32,30,19,D,None,40)
    for i in range(6):
        d.arc((10+i*3,10+i*3,74-i*3,54-i*3),0,360,fill=K,width=1)
    smooth_body(d,42,32,12,9,O,K,24)
    return img
def sea_fan():
    img=new(96,96); d=ImageDraw.Draw(img)
    P=(186,104,200,255); D=(123,31,162,255); K=(18,18,24,255); L=(206,147,216,255)
    rect(d,44,74,52,96,D,K,1)
    import math
    for i in range(11):
        a=(i-5)*0.28
        x2=48+int(math.cos(-1.57+a)*44); y2=74+int(math.sin(-1.57+a)*44)
        line(d,48,74,x2,y2,P,2)
        for j in (0.35,-0.35):
            xs=x2+int(math.cos(-1.57+a+j)*14); ys=y2+int(math.sin(-1.57+a+j)*14)
            line(d,x2,y2,xs,ys,D,1)
    return img
def anemone():
    img=new(84,84); d=ImageDraw.Draw(img)
    P=(244,143,177,255); D=(194,24,91,255); K=(18,18,24,255); G=(129,199,132,255); L=(248,187,208,255)
    smooth_body(d,42,70,20,10,G,K,24)
    import math
    for i in range(14):
        a=math.radians(i*25.7)
        x=42+int(math.cos(a)*12); y=56+int(math.sin(a)*8)
        line(d,42,62,x,y-20,P,2)
        smooth_body(d,x,y-18,4,6,P,K,12)
        smooth_body(d,x-1,y-17,2,3,L,None,8)
    return img
def seaweed():
    img=new(40,96); d=ImageDraw.Draw(img)
    G=(46,125,50,255); D=(27,94,32,255); K=(18,18,24,255); L=(102,187,106,255)
    import math
    for i in range(7):
        x=6+i*5
        pts=[]
        xx=x
        for y in range(96,0,-3):
            xx=x+int(math.sin(y*0.1+i)*5)
            pts.append((xx,y))
        for j in range(len(pts)-1):
            line(d,pts[j][0],pts[j][1],pts[j+1][0],pts[j+1][1],G,2)
        for y in range(84,12,-14):
            xx=x+int(math.sin(y*0.1+i)*5)
            line(d,xx,y,xx+7,y-5,D,1)
            line(d,xx,y,xx-7,y-5,D,1)
    return img
def kelp():
    img=new(48,120); d=ImageDraw.Draw(img)
    G=(27,94,32,255); D=(13,60,18,255); K=(18,18,24,255); L=(102,187,106,255)
    import math
    pts=[]
    x=24
    for y in range(120,0,-2):
        x=24+int(math.sin(y*0.1)*6)
        pts.append((x,y))
    for j in range(len(pts)-1):
        line(d,pts[j][0],pts[j][1],pts[j+1][0],pts[j+1][1],G,5)
    for y in range(110,10,-12):
        x=24+int(math.sin(y*0.1)*6)
        line(d,x,y,x+14,y-10,L,2)
        line(d,x,y,x-14,y-10,L,2)
    return img
def rock():
    img=new(96,56); d=ImageDraw.Draw(img)
    G=(120,144,156,255); D=(84,110,122,255); L=(176,190,197,255); K=(18,18,24,255); S=(96,125,139,255)
    poly(d,[(10,50),(20,14),(44,6),(80,14),(88,50),(44,54)],G,K,1)
    smooth_body(d,30,24,16,12,L,None,24)
    smooth_body(d,62,26,14,10,D,None,24)
    smooth_body(d,44,40,12,8,S,None,20)
    for i in range(15):
        d.point((14+i*5,20+(i*7)%16),fill=D)
    return img
def shell():
    img=new(48,36); d=ImageDraw.Draw(img)
    P=(255,204,188,255); D=(255,138,101,255); K=(18,18,24,255); L=(255,224,204,255)
    poly(d,[(6,32),(24,4),(42,32)],P,K,1)
    for i in range(8):
        line(d,24,4,6+i*5,32,D,1)
        line(d,24,4,42-i*5,32,D,1)
    smooth_body(d,24,20,8,7,L,None,16)
    return img
def treasure():
    img=new(104,84); d=ImageDraw.Draw(img)
    B=(141,110,99,255); D=(93,64,55,255); G=(255,213,79,255); K=(18,18,24,255); L=(180,140,120,255)
    rect(d,14,34,90,78,B,K,1)
    rect(d,14,26,90,36,D,K,1)
    poly(d,[(14,34),(52,10),(90,34)],D,K,1)
    poly(d,[(16,34),(52,14),(88,34)],L,None)
    rect(d,42,38,62,52,G,K,1)
    for i in range(5):
        smooth_body(d,20+i*16,8,8,6,G,K,16)
    return img
def shipwreck():
    img=new(144,96); d=ImageDraw.Draw(img)
    B=(93,64,55,255); D=(62,39,35,255); G=(121,85,72,255); K=(18,18,24,255); L=(140,100,80,255)
    poly(d,[(10,82),(20,58),(124,58),(134,82)],B,K,1)
    rect(d,20,48,124,60,D,K,1)
    rect(d,68,6,78,58,G,K,1)
    poly(d,[(78,10),(104,20),(80,34)],(190,190,190,200),K,1)
    rect(d,30,68,46,72,K,None)
    rect(d,94,66,112,70,K,None)
    rect(d,10,54,24,56,L,None)
    rect(d,110,52,130,54,L,None)
    return img

# ---------- Save all ----------
species = {
    'clownfish': clownfish, 'bluetang': bluetang, 'angelfish': angelfish,
    'butterflyfish': butterflyfish, 'pufferfish': pufferfish, 'lionfish': lionfish,
    'moorishidol': moorishidol, 'royalgramma': royalgramma, 'koi': koi,
    'goldfish': goldfish, 'tropical': tropical, 'exotic': exotic,
    'smallreef': smallreef, 'turtle': turtle,
}
for name, fn in species.items():
    save(fn(False), f"{name}_0.png")
    save(fn(True), f"{name}_1.png")
save(branching_coral(), "coral_branching.png")
save(brain_coral(), "coral_brain.png")
save(sea_fan(), "coral_seafan.png")
save(anemone(), "anemone.png")
save(seaweed(), "seaweed.png")
save(kelp(), "kelp.png")
save(rock(), "rock.png")
save(shell(), "shell.png")
save(treasure(), "treasure.png")
save(shipwreck(), "shipwreck.png")
print("ALL DONE")
