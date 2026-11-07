import os, math
from PIL import Image, ImageDraw

def bands_clown(d,W,H):
    for bx in (W*0.30, W*0.55):
        rect(d, int(bx), int(H*0.22), int(bx)+5, int(H*0.78), (255,255,255,255), (18,18,24,255), 1)
        rect(d, int(bx)+1, int(H*0.22), int(bx)+4, int(H*0.78), (230,230,230,255), None)
def stripes_vertical(d,W,H,color):
    for sx in (W*0.28, W*0.44, W*0.60):
        rect(d, int(sx), int(H*0.18), int(sx)+4, int(H*0.82), color, (18,18,24,255), 1)
def eye_spot(d,W,H):
    ell(d, int(W*0.22), int(H*0.4), int(W*0.34), int(H*0.6), (26,35,126,255), (18,18,24,255), 1)
    ell(d, int(W*0.26), int(H*0.44), int(W*0.30), int(H*0.56), (18,18,24,255), None)
def spots_puffer(d,W,H):
    import math
    cx,cy=W*0.52,H*0.5
    for i in range(10):
        a=math.radians(i*36)
        x=cx+math.cos(a)*10; y=cy+math.sin(a)*8
        ell(d,int(x-3),int(y-3),int(x+3),int(y+3),(244,143,177,255),None)
def spikes_puffer(d,W,H):
    import math
    cx,cy=W*0.52,H*0.5; r=W*0.34
    for i in range(16):
        a=math.radians(i*20)
        x1=cx+math.cos(a)*r; y1=cy+math.sin(a)*r
        x2=cx+math.cos(a)*(r+6); y2=cy+math.sin(a)*(r+6)
        line(d,int(x1),int(y1),int(x2),int(y2),(93,64,55,255),1)
def stripes_lion(d,W,H):
    for sx in (W*0.22,W*0.30,W*0.38,W*0.46,W*0.54,W*0.62):
        rect(d,int(sx),int(H*0.2),int(sx)+3,int(H*0.8),(255,255,255,255),(18,18,24,255),1)
def lion_fins(d,W,H):
    for fx in range(int(W*0.22), int(W*0.72), 7):
        poly(d,[(fx,H*0.12),(fx+3,0),(fx+7,H*0.12)],(255,202,40,255),(18,18,24,255),1)
    poly(d,[(W*0.4,H*0.6),(W*0.28,H*0.95),(W*0.52,H*0.95)],(255,112,67,255),(18,18,24,255),1)
def bands_moorish(d,W,H):
    rect(d,int(W*0.22),6,int(W*0.34),H-6,(20,20,20,255),(18,18,24,255),1)
    rect(d,int(W*0.46),6,int(W*0.58),H-6,(20,20,20,255),(18,18,24,255),1)
def moorish_dorsal(d,W,H):
    for x in (W*0.28,W*0.42,W*0.56):
        poly(d,[(x,H*0.12),(x+8,-2),(x+16,H*0.12)],(255,193,7,255),(18,18,24,255),1)
def yellow_rear(d,W,H):
    for x in range(int(W*0.55), int(W*0.88)):
        for y in range(6, H-6):
            if (x-W*0.72)**2/(W*0.18)**2 + (y-H*0.5)**2/(H*0.38)**2 <= 1:
                d.point((x,y),(255,213,79,255))
def white_patches(d,W,H):
    ell(d,int(W*0.30),int(H*0.25),int(W*0.46),int(H*0.55),(255,255,255,255),(18,18,24,255),1)
    ell(d,int(W*0.62),int(H*0.30),int(W*0.78),int(H*0.60),(255,255,255,255),(18,18,24,255),1)
def red_patch(d,W,H):
    ell(d,int(W*0.48),int(H*0.35),int(W*0.62),int(H*0.65),(191,54,12,255),(18,18,24,255),1)
def koi_dorsal(d,W,H):
    poly(d,[(W*0.32,H*0.12),(W*0.50,0),(W*0.68,H*0.12)],(191,54,12,255),(18,18,24,255),1)
def stripes_tropical(d,W,H):
    for sx in (W*0.22,W*0.32,W*0.42,W*0.52,W*0.62):
        rect(d,int(sx),int(H*0.18),int(sx)+4,int(H*0.82),(255,64,129,255),(18,18,24,255),1)
def cyan_spot(d,W,H):
    ell(d,int(W*0.30),int(H*0.30),int(W*0.46),int(H*0.62),(0,229,255,255),(18,18,24,255),1)
    ell(d,int(W*0.34),int(H*0.34),int(W*0.42),int(H*0.58),(224,64,251,255),None)
def dorsal_double(d,W,H):
    poly(d,[(W*0.26,H*0.12),(W*0.36,0),(W*0.46,H*0.12)],(0,229,255,255),(18,18,24,255),1)
    poly(d,[(W*0.46,H*0.12),(W*0.56,0),(W*0.66,H*0.12)],(0,229,255,255),(18,18,24,255),1)

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
def smooth(d,cx,cy,rx,ry,fill,outline=K,steps=36):
    pts=[]
    for i in range(steps):
        a=2*math.pi*i/steps
        pts.append((cx+math.cos(a)*rx*(1+0.03*math.sin(3*a)), cy+math.sin(a)*ry*(1+0.02*math.cos(2*a))))
    poly(d,pts,fill,outline,1)

# Template fish: body oval, forked tail left, dorsal fin top, eye right, shading.
# Each species passes colors + pattern function.
def base_fish(W,H, body, shadow, highlight, tail, tailShadow, fin, finHi, eyeWhite=(255,255,255,255),
              tail_up=False, pattern=None):
    img=new(W,H); d=ImageDraw.Draw(img)
    ty = H//2 + (-4 if tail_up else 0)
    bodyLeft = int(W*0.18)
    # tail (forked) filled solid, attached to body
    poly(d,[(bodyLeft,ty-2),(2,ty-10),(0,ty-6),(0,ty+6),(2,ty+10),(bodyLeft,ty+2)],tail,K,1)
    poly(d,[(bodyLeft,ty),(4,ty-6),(4,ty+6)],tailShadow,None)
    # dorsal fin behind body (drawn first, larger)
    poly(d,[(W*0.26, H*0.18),(W*0.50, -2),(W*0.74, H*0.18)],fin,K,1)
    poly(d,[(W*0.28, H*0.18),(W*0.50, 0),(W*0.72, H*0.18)],finHi,None)
    # anal fin behind body (larger)
    poly(d,[(W*0.26, H*0.82),(W*0.50, H+2),(W*0.74, H*0.82)],fin,K,1)
    poly(d,[(W*0.28, H*0.82),(W*0.50, H),(W*0.72, H*0.82)],finHi,None)
    # body oval on top
    smooth(d, W*0.52, H*0.5, W*0.34, H*0.38, body, K)
    smooth(d, W*0.52, H*0.62, W*0.30, H*0.22, shadow, None)
    smooth(d, W*0.42, H*0.38, W*0.22, H*0.18, highlight, None)
    # pectoral fin on top
    poly(d,[(W*0.46,H*0.55),(W*0.34,H*0.72),(W*0.56,H*0.72)],fin,K,1)
    # pattern
    if pattern: pattern(d, W, H)
    # eye (smaller, white sclera)
    ex, ey = int(W*0.78), int(H*0.38)
    ell(d, ex-2, ey-2, ex+2, ey+2, (255,255,255,255), K, 1)
    ell(d, ex-1, ey-1, ex+1, ey+1, (20,20,24,255), None)
    ell(d, ex-1, ey-2, ex+0, ey-1, (255,255,255,255), None)
    # mouth
    line(d, int(W*0.92), int(H*0.5), int(W*0.95), int(H*0.52), K, 1)
    return img

# Pattern helpers
def bands_clown(d,W,H):
    for bx in (W*0.30, W*0.55):
        rect(d, int(bx), int(H*0.22), int(bx)+5, int(H*0.78), (255,255,255,255), (18,18,24,255), 1)
        rect(d, int(bx)+1, int(H*0.22), int(bx)+4, int(H*0.78), (230,230,230,255), None)
def stripes_vertical(d,W,H,color):
    for sx in (W*0.28, W*0.44, W*0.60):
        rect(d, int(sx), int(H*0.18), int(sx)+4, int(H*0.82), color, (18,18,24,255), 1)
def eye_spot(d,W,H):
    ell(d, int(W*0.22), int(H*0.4), int(W*0.34), int(H*0.6), (26,35,126,255), (18,18,24,255), 1)
    ell(d, int(W*0.26), int(H*0.44), int(W*0.30), int(H*0.56), (18,18,24,255), None)
def spots_puffer(d,W,H):
    import math
    cx,cy=W*0.52,H*0.5
    for i in range(10):
        a=math.radians(i*36)
        x=cx+math.cos(a)*10; y=cy+math.sin(a)*8
        ell(d, int(x-3),int(y-3),int(x+3),int(y+3),(244,143,177,255),None)
def spikes_puffer(d,W,H):
    import math
    cx,cy=W*0.52,H*0.5; r=W*0.34
    for i in range(16):
        a=math.radians(i*20)
        x1=cx+math.cos(a)*r; y1=cy+math.sin(a)*r
        x2=cx+math.cos(a)*(r+6); y2=cy+math.sin(a)*(r+6)
        line(d,int(x1),int(y1),int(x2),int(y2),(93,64,55,255),1)
def stripes_lion(d,W,H):
    for sx in (W*0.22,W*0.30,W*0.38,W*0.46,W*0.54,W*0.62):
        rect(d,int(sx),int(H*0.2),int(sx)+3,int(H*0.8),(255,255,255,255),(18,18,24,255),1)
def lion_fins(d,W,H):
    for fx in range(int(W*0.22), int(W*0.72), 7):
        poly(d,[(fx,H*0.12),(fx+3,0),(fx+7,H*0.12)],(255,202,40,255),(18,18,24,255),1)
    poly(d,[(W*0.4,H*0.6),(W*0.28,H*0.95),(W*0.52,H*0.95)],(255,112,67,255),(18,18,24,255),1)
def bands_moorish(d,W,H):
    rect(d,int(W*0.22),6,int(W*0.34),H-6,(20,20,20,255),(18,18,24,255),1)
    rect(d,int(W*0.46),6,int(W*0.58),H-6,(20,20,20,255),(18,18,24,255),1)
def moorish_dorsal(d,W,H):
    for x in (W*0.28,W*0.42,W*0.56):
        poly(d,[(x,H*0.12),(x+8,-2),(x+16,H*0.12)],(255,193,7,255),(18,18,24,255),1)
def yellow_rear(d,W,H):
    # paint right half yellow
    for x in range(int(W*0.55), int(W*0.88)):
        for y in range(6, H-6):
            if (x-W*0.72)**2/(W*0.18)**2 + (y-H*0.5)**2/(H*0.38)**2 <= 1:
                d.point((x,y),(255,213,79,255))
def white_patches(d,W,H):
    ell(d,int(W*0.30),int(H*0.25),int(W*0.46),int(H*0.55),(255,255,255,255),(18,18,24,255),1)
    ell(d,int(W*0.62),int(H*0.30),int(W*0.78),int(H*0.60),(255,255,255,255),(18,18,24,255),1)
def red_patch(d,W,H):
    ell(d,int(W*0.48),int(H*0.35),int(W*0.62),int(H*0.65),(191,54,12,255),(18,18,24,255),1)
def koi_dorsal(d,W,H):
    poly(d,[(W*0.32,H*0.12),(W*0.50,0),(W*0.68,H*0.12)],(191,54,12,255),(18,18,24,255),1)
def stripes_tropical(d,W,H):
    for sx in (W*0.22,W*0.32,W*0.42,W*0.52,W*0.62):
        rect(d,int(sx),int(H*0.18),int(sx)+4,int(H*0.82),(255,64,129,255),(18,18,24,255),1)
def cyan_spot(d,W,H):
    ell(d,int(W*0.30),int(H*0.30),int(W*0.46),int(H*0.62),(0,229,255,255),(18,18,24,255),1)
    ell(d,int(W*0.34),int(H*0.34),int(W*0.42),int(H*0.58),(224,64,251,255),None)
def dorsal_double(d,W,H):
    poly(d,[(W*0.26,H*0.12),(W*0.36,0),(W*0.46,H*0.12)],(0,229,255,255),(18,18,24,255),1)
    poly(d,[(W*0.46,H*0.12),(W*0.56,0),(W*0.66,H*0.12)],(0,229,255,255),(18,18,24,255),1)

# Small reef fish (compact)
def small_body(d,W,H):
    pass

# Species definitions: (W,H, body,shadow,highlight,tail,tailShadow,fin,finHi, pattern_func, tail_up default)
SPECS = {
 'clownfish': (96,48, (255,109,50,255),(195,55,20,255),(255,165,120,255),(255,109,50,255),(195,55,20,255),(255,193,7,255),(255,224,130,255), bands_clown),
 'bluetang': (96,48, (30,120,220,255),(12,60,150,255),(110,175,245,255),(255,230,59,255),(200,200,50,255),(12,60,150,255),(30,120,220,255), None),
 'angelfish': (80,80, (240,130,175,255),(190,20,85,255),(248,180,205,255),(190,20,85,255),(120,10,50,255),(190,20,85,255),(240,130,175,255), None),
 'butterflyfish': (80,48, (255,230,59,255),(245,160,30,255),(255,245,190,255),(255,143,0,255),(200,100,0,255),(255,143,0,255),(255,230,59,255), None),
 'royalgramma': (80,40, (123,31,162,255),(74,20,140,255),(170,80,200,255),(255,213,79,255),(200,170,40,255),(74,20,140,255),(123,31,162,255), None),
 'pufferfish': (72,60, (255,245,157,255),(185,195,45,255),(255,255,225,255),(244,143,177,255),(200,100,140,255),(93,64,55,255),(140,100,90,255), None),
 'lionfish': (100,52, (229,57,53,255),(183,28,28,255),(255,138,128,255),(183,28,28,255),(120,15,10,255),(255,202,40,255),(255,236,179,255), None),
 'moorishidol': (96,44, (255,255,255,255),(225,225,225,255),(240,240,240,255),(255,193,7,255),(200,150,0,255),(255,193,7,255),(255,230,100,255), None),
 'koi': (100,44, (255,138,101,255),(216,67,21,255),(255,171,145,255),(191,54,12,255),(140,30,8,255),(191,54,12,255),(255,138,101,255), None),
 'goldfish': (80,44, (255,202,40,255),(249,168,37,255),(255,236,179,255),(229,57,53,255),(180,30,25,255),(249,168,37,255),(255,202,40,255), None),
 'tropical': (80,40, (0,230,118,255),(0,137,123,255),(100,255,180,255),(255,64,129,255),(200,40,90,255),(255,64,129,255),(0,230,118,255), None),
 'exotic': (88,44, (224,64,251,255),(123,31,162,255),(235,120,255,255),(0,229,255,255),(0,170,200,255),(0,229,255,255),(224,64,251,255), None),
 'smallreef': (56,32, (38,198,218,255),(0,131,143,255),(100,220,230,255),(0,131,143,255),(0,90,100,255),(255,238,88,255),(38,198,218,255), None),
 'turtle': (108,68, (46,125,50,255),(27,94,32,255),(102,187,106,255),(46,125,50,255),(27,94,32,255),(102,187,106,255),(46,125,50,255), None),
}

# Extra pattern functions per species
EXTRA = {
 'clownfish': [bands_clown],
 'angelfish': [lambda d,W,H: (stripes_vertical(d,W,H,(190,20,85,255)),)],
 'butterflyfish': [eye_spot, lambda d,W,H: stripes_vertical(d,W,H,(26,35,126,255))],
 'pufferfish': [spots_puffer, spikes_puffer],
 'lionfish': [stripes_lion, lion_fins],
 'moorishidol': [bands_moorish, moorish_dorsal],
 'royalgramma': [yellow_rear],
 'koi': [white_patches, red_patch, koi_dorsal],
 'goldfish': [white_patches],
 'tropical': [stripes_tropical],
 'exotic': [cyan_spot, dorsal_double],
}

def make_fish(name, tail_up=False):
    W,H,body,shadow,hi,tail,tailSh,fin,finHi,pat = SPECS[name]
    img = base_fish(W,H,body,shadow,hi,tail,tailSh,fin,finHi,None,tail_up)
    d = ImageDraw.Draw(img)
    # apply patterns
    for fn in EXTRA.get(name, []):
        try:
            fn(d, W, H)
        except Exception as e:
            pass
    # species-specific eye spot for butterfly already in pattern
    return img

# Run
for name in SPECS:
    for f in (0,1):
        save(make_fish(name, tail_up=(f==1)), f"{name}_{f}.png")

# Environment (keep previous PIL versions by re-running gen_assets env part? We'll regenerate env separately)
print("FISH DONE")
