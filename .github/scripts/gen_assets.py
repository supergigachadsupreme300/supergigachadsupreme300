import os, math
from PIL import Image, ImageDraw

OUT = "D:/schools/supergigachadsupreme300/aquarium/assets/sprites"
os.makedirs(OUT, exist_ok=True)

def new(w, h):
    return Image.new("RGBA", (w, h), (0,0,0,0))

def save(img, name):
    img.save(os.path.join(OUT, name), "PNG")
    print("saved", name)

K = (20,20,20,255)
def ell(d, x0,y0,x1,y1, fill, outline=K, w=1):
    d.ellipse((x0,y0,x1,y1), fill=fill, outline=outline, width=w)
def rect(d, x0,y0,x1,y1, fill, outline=K, w=1):
    d.rectangle((x0,y0,x1,y1), fill=fill, outline=outline, width=w)
def poly(d, pts, fill, outline=K, w=1):
    d.polygon(pts, fill=fill, outline=outline, width=w)
def line(d, x0,y0,x1,y1, fill, w=1):
    d.line((x0,y0,x1,y1), fill=fill, width=w)

# ---------- Clownfish (80x40) ----------
def clownfish(tail_up=False):
    img = new(80, 40)
    d = ImageDraw.Draw(img)
    O=(255,112,67,255); D=(190,60,30,255); W=(255,255,255,255); Bk=(20,20,20,255)
    Y=(255,193,7,255); L=(255,171,145,255)
    ty = 18 if not tail_up else 12
    # tail (forked, left)
    poly(d, [(6,ty),(0,ty-8),(2,ty),(0,ty+8)], O, Bk, 1)
    poly(d, [(6,ty),(2,ty-4),(4,ty),(2,ty+4)], D, None)
    # body (oval)
    ell(d, 8,6,62,34, O, Bk, 1)
    # shadow lower half
    ell(d, 10,22,60,34, D, None)
    # highlight
    ell(d, 12,8,40,18, L, None)
    # white bands with black edges
    rect(d, 22,7,28,33, W, Bk, 1)
    rect(d, 40,7,46,33, W, Bk, 1)
    # dark separators inside bands
    rect(d, 24,7,26,33, (200,200,200,255), None)
    # dorsal fin
    poly(d, [(24,6),(36,0),(48,6)], Y, Bk, 1)
    poly(d, [(26,6),(36,2),(46,6)], (255,224,130,255), None)
    # pectoral fin
    poly(d, [(34,24),(28,32),(40,32)], Y, Bk, 1)
    # anal fin
    poly(d, [(34,34),(28,38),(40,38)], Y, Bk, 1)
    # eye
    ell(d, 52,12,58,18, (255,255,255,255), Bk, 1)
    ell(d, 53,13,57,17, (20,20,20,255), None)
    ell(d, 54,13,56,15, (255,255,255,255), None)
    # mouth
    line(d, 60,19,62,20, Bk, 1)
    # scales texture (subtle)
    for i in range(0,5):
        for j in range(0,3):
            d.point((18+i*6, 12+j*6), fill=(200,90,50,120))
    return img

# ---------- Blue Tang ----------
def bluetang(tail_up=False):
    img = new(80, 40)
    d = ImageDraw.Draw(img)
    B=(30,136,229,255); D=(13,71,161,255); Y=(255,235,59,255); Bk=(20,20,20,255)
    L=(100,181,246,255)
    ty = 19 if not tail_up else 13
    poly(d, [(6,ty),(0,ty-9),(2,ty),(0,ty+9)], Y, Bk, 1)
    ell(d, 8,5,64,35, B, Bk, 1)
    ell(d, 10,24,62,35, D, None)
    ell(d, 12,7,46,20, L, None)
    # yellow tail base patch
    ell(d, 8,14,16,26, Y, Bk, 1)
    # dorsal fin
    poly(d, [(20,5),(38,0),(56,5)], D, Bk, 1)
    # anal fin
    poly(d, [(20,35),(38,40),(56,35)], D, Bk, 1)
    # pectoral
    poly(d, [(36,26),(30,32),(42,32)], D, Bk, 1)
    # eye
    ell(d, 54,13,60,19, (255,255,255,255), Bk, 1)
    ell(d, 55,14,59,18, Bk, None)
    ell(d, 56,14,58,16, (255,255,255,255), None)
    line(d, 62,18,64,19, Bk, 1)
    return img

# ---------- Angelfish (tall) ----------
def angelfish(tail_up=False):
    img = new(70, 60)
    d = ImageDraw.Draw(img)
    P=(244,143,177,255); D=(194,24,91,255); Y=(255,235,59,255); Bk=(20,20,20,255)
    L=(248,187,208,255)
    ty = 28 if not tail_up else 22
    poly(d, [(4,ty),(0,ty-5),(0,ty+5)], D, Bk, 1)
    ell(d, 6,6,52,54, P, Bk, 1)
    ell(d, 8,36,50,54, D, None)
    ell(d, 10,8,36,26, L, None)
    # vertical stripes
    rect(d, 18,6,22,54, D, Bk, 1)
    rect(d, 32,6,36,54, D, Bk, 1)
    # long dorsal fin
    poly(d, [(10,6),(28,0),(46,6)], D, Bk, 1)
    poly(d, [(12,6),(28,2),(44,6)], P, None)
    # anal fin
    poly(d, [(10,54),(28,60),(46,54)], D, Bk, 1)
    # pectoral
    poly(d, [(30,30),(22,40),(38,40)], (255,200,220,255), Bk, 1)
    # eye
    ell(d, 40,18,46,24, (255,255,255,255), Bk, 1)
    ell(d, 41,19,45,23, Bk, None)
    ell(d, 42,19,44,21, (255,255,255,255), None)
    line(d, 48,24,50,25, Bk, 1)
    return img

# ---------- Butterflyfish (flat round) ----------
def butterflyfish(tail_up=False):
    img = new(70, 40)
    d = ImageDraw.Draw(img)
    Y=(255,235,59,255); D=(249,168,37,255); B=(26,35,126,255); Bk=(20,20,20,255)
    O=(255,143,0,255); L=(255,249,196,255)
    ty = 18 if not tail_up else 14
    poly(d, [(4,ty),(0,ty-4),(0,ty+4)], O, Bk, 1)
    ell(d, 6,6,52,34, Y, Bk, 1)
    ell(d, 8,20,50,34, D, None)
    ell(d, 10,8,36,22, L, None)
    # eye spot
    ell(d, 12,12,20,20, B, Bk, 1)
    ell(d, 14,14,18,18, Bk, None)
    ell(d, 15,14,17,16, (255,255,255,255), None)
    # vertical bar
    rect(d, 34,7,38,33, B, Bk, 1)
    # dorsal fin
    poly(d, [(14,6),(26,0),(38,6)], O, Bk, 1)
    poly(d, [(16,6),(26,2),(36,6)], Y, None)
    # eye
    ell(d, 42,12,48,18, (255,255,255,255), Bk, 1)
    ell(d, 43,13,47,17, Bk, None)
    ell(d, 44,13,46,15, (255,255,255,255), None)
    line(d, 50,17,52,18, Bk, 1)
    return img

# ---------- Pufferfish ----------
def pufferfish(tail_up=False):
    img = new(60, 48)
    d = ImageDraw.Draw(img)
    Y=(255,245,157,255); D=(192,202,51,255); P=(244,143,177,255)
    Bk=(20,20,20,255); W=(255,255,255,255); G=(93,64,55,255)
    r=18; cx,cy=28,24
    ell(d, cx-r, cy-r, cx+r, cy+r, Y, Bk, 1)
    ell(d, cx-r+3, cy+4, cx+r-3, cy+r, D, None)
    ell(d, cx-r+4, cy-r+4, cx-2, cy, (255,255,230,255), None)
    import math
    for i in range(10):
        a=math.radians(i*36)
        x=cx+int(math.cos(a)*7); y=cy+int(math.sin(a)*7)
        ell(d, x-3,y-3,x+3,y+3, P, None)
    # spikes
    for i in range(16):
        a=math.radians(i*22.5)
        x1=cx+int(math.cos(a)*r); y1=cy+int(math.sin(a)*r)
        x2=cx+int(math.cos(a)*(r+5)); y2=cy+int(math.sin(a)*(r+5))
        line(d, x1,y1,x2,y2, G, 1)
    # tail
    ty = cy if not tail_up else cy-4
    poly(d, [(cx-r,ty),(cx-r-8,ty-5),(cx-r-8,ty+5)], P, Bk, 1)
    # eye
    ell(d, cx+6, cy-6, cx+14, cy+2, W, Bk, 1)
    ell(d, cx+7, cy-5, cx+13, cy+1, Bk, None)
    ell(d, cx+8, cy-5, cx+10, cy-3, W, None)
    # mouth
    ell(d, cx+r-2, cy+1, cx+r+2, cy+4, G, None)
    return img

# ---------- Lionfish ----------
def lionfish(tail_up=False):
    img = new(90, 44)
    d = ImageDraw.Draw(img)
    R=(229,57,53,255); D=(183,28,28,255); W=(255,255,255,255); Bk=(20,20,20,255)
    Y=(255,202,40,255); O=(255,112,67,255); L=(255,138,128,255)
    ty = 20 if not tail_up else 15
    poly(d, [(6,ty),(0,ty-6),(2,ty),(0,ty+6)], D, Bk, 1)
    ell(d, 10,8,62,36, R, Bk, 1)
    ell(d, 12,24,60,36, D, None)
    ell(d, 14,10,40,24, L, None)
    # stripes
    for sx in [16,22,28,34,40,46,52]:
        rect(d, sx,9,sx+3,35, W, Bk, 1)
    # dramatic dorsal fins
    for fx in range(14,58,6):
        poly(d, [(fx,8),(fx+3,0),(fx+6,8)], Y, Bk, 1)
        poly(d, [(fx+1,8),(fx+3,2),(fx+5,8)], (255,236,179,255), None)
    # pectoral fan
    poly(d, [(30,26),(20,40),(40,40)], O, Bk, 1)
    poly(d, [(32,26),(24,38),(36,38)], Y, None)
    # anal fin
    poly(d, [(30,36),(24,44),(36,44)], O, Bk, 1)
    # eye
    ell(d, 52,12,58,18, (255,255,255,255), Bk, 1)
    ell(d, 53,13,57,17, Bk, None)
    ell(d, 54,13,56,15, (255,255,255,255), None)
    line(d, 60,17,62,18, Bk, 1)
    return img

# ---------- Moorish Idol ----------
def moorishidol(tail_up=False):
    img = new(88, 40)
    d = ImageDraw.Draw(img)
    B=(20,20,20,255); W=(255,255,255,255); Y=(255,193,7,255); Bk=(20,20,20,255)
    L=(240,240,240,255)
    ty = 18 if not tail_up else 14
    poly(d, [(4,ty),(0,ty-5),(0,ty+5)], Y, Bk, 1)
    ell(d, 8,6,52,32, W, Bk, 1)
    ell(d, 10,20,50,32, (220,220,220,255), None)
    # black bands
    rect(d, 14,6,20,32, B, Bk, 1)
    rect(d, 26,6,32,32, B, Bk, 1)
    # yellow dorsal (elongated)
    poly(d, [(16,6),(22,0),(28,6)], Y, Bk, 1)
    poly(d, [(28,6),(34,-4),(40,6)], Y, Bk, 1)
    poly(d, [(40,6),(46,-2),(52,6)], Y, Bk, 1)
    # snout
    rect(d, 52,13,68,17, W, Bk, 1)
    rect(d, 52,14,68,16, B, None)
    # eye
    ell(d, 40,10,46,16, (255,255,255,255), Bk, 1)
    ell(d, 41,11,45,15, Bk, None)
    ell(d, 42,11,44,13, (255,255,255,255), None)
    # tail
    poly(d, [(6,ty),(2,ty-3),(2,ty+3)], Y, Bk, 1)
    return img

# ---------- Royal Gramma ----------
def royalgramma(tail_up=False):
    img = new(70, 36)
    d = ImageDraw.Draw(img)
    P=(123,31,162,255); Y=(255,213,79,255); D=(74,20,140,255); Bk=(20,20,20,255)
    L=(170,80,200,255)
    ty = 16 if not tail_up else 12
    poly(d, [(4,ty),(0,ty-5),(0,ty+5)], Y, Bk, 1)
    ell(d, 6,4,56,32, P, Bk, 1)
    # yellow rear half
    for x in range(30,57):
        for y in range(5,32):
            if (x-42)**2/14**2 + (y-18)**2/13**2 <= 1:
                d.point((x,y), fill=Y)
    ell(d, 8,22,54,32, D, None)
    ell(d, 10,6,30,18, L, None)
    # dorsal fin
    poly(d, [(14,4),(28,0),(42,4)], D, Bk, 1)
    # pectoral
    poly(d, [(26,22),(20,28),(32,28)], (180,100,200,255), Bk, 1)
    # eye
    ell(d, 46,10,52,16, (255,255,255,255), Bk, 1)
    ell(d, 47,11,51,15, Bk, None)
    ell(d, 48,11,50,13, (255,255,255,255), None)
    line(d, 54,15,56,16, Bk, 1)
    return img

# ---------- Koi ----------
def koi(tail_up=False):
    img = new(90, 36)
    d = ImageDraw.Draw(img)
    O=(255,138,101,255); D=(216,67,21,255); W=(255,255,255,255); Bk=(20,20,20,255)
    R=(191,54,12,255); Y=(255,202,40,255); L=(255,171,145,255)
    ty = 16 if not tail_up else 11
    poly(d, [(6,ty),(0,ty-7),(3,ty),(0,ty+7)], R, Bk, 1)
    poly(d, [(6,ty),(2,ty-4),(4,ty),(2,ty+4)], D, None)
    ell(d, 10,4,72,32, O, Bk, 1)
    ell(d, 12,22,70,32, D, None)
    ell(d, 14,6,44,20, L, None)
    # white patches
    ell(d, 20,8,32,20, W, Bk, 1)
    ell(d, 50,10,62,22, W, Bk, 1)
    # red patches
    ell(d, 36,14,46,24, R, Bk, 1)
    # dorsal fin
    poly(d, [(22,4),(36,0),(50,4)], R, Bk, 1)
    # pectoral
    poly(d, [(40,24),(32,32),(48,32)], (255,180,160,255), Bk, 1)
    # eye
    ell(d, 60,10,66,16, (255,255,255,255), Bk, 1)
    ell(d, 61,11,65,15, Bk, None)
    ell(d, 62,11,64,13, (255,255,255,255), None)
    line(d, 68,15,70,16, Bk, 1)
    return img

# ---------- Goldfish ----------
def goldfish(tail_up=False):
    img = new(70, 36)
    d = ImageDraw.Draw(img)
    Y=(255,202,40,255); D=(249,168,37,255); W=(255,255,255,255); Bk=(20,20,20,255)
    R=(229,57,53,255); L=(255,236,179,255)
    ty = 16 if not tail_up else 12
    poly(d, [(4,ty),(0,ty-6),(2,ty),(0,ty+6)], R, Bk, 1)
    poly(d, [(4,ty),(1,ty-3),(3,ty),(1,ty+3)], D, None)
    ell(d, 8,4,58,32, Y, Bk, 1)
    ell(d, 10,22,56,32, D, None)
    ell(d, 12,6,38,20, L, None)
    ell(d, 20,8,30,18, W, Bk, 1)
    poly(d, [(18,4),(28,0),(38,4)], D, Bk, 1)
    poly(d, [(18,4),(28,2),(38,4)], Y, None)
    poly(d, [(26,24),(18,32),(34,32)], (255,224,130,255), Bk, 1)
    ell(d, 46,10,52,16, (255,255,255,255), Bk, 1)
    ell(d, 47,11,51,15, Bk, None)
    ell(d, 48,11,50,13, (255,255,255,255), None)
    line(d, 54,15,56,16, Bk, 1)
    return img

# ---------- Tropical (green/pink) ----------
def tropical(tail_up=False):
    img = new(72, 34)
    d = ImageDraw.Draw(img)
    G=(0,230,118,255); D=(0,137,123,255); P=(255,64,129,255); Bk=(20,20,20,255)
    W=(255,255,255,255); L=(100,255,180,255)
    ty = 15 if not tail_up else 11
    poly(d, [(4,ty),(0,ty-5),(0,ty+5)], P, Bk, 1)
    ell(d, 6,4,56,30, G, Bk, 1)
    ell(d, 8,20,54,30, D, None)
    ell(d, 10,6,36,18, L, None)
    for sx in [14,20,26,32,38,44]:
        rect(d, sx,5,sx+3,29, P, Bk, 1)
    poly(d, [(12,4),(18,0),(24,4)], P, Bk, 1)
    ell(d, 46,8,52,14, W, Bk, 1)
    ell(d, 47,9,51,13, Bk, None)
    ell(d, 48,9,50,11, W, None)
    line(d, 54,13,56,14, Bk, 1)
    return img

# ---------- Exotic (purple/cyan) ----------
def exotic(tail_up=False):
    img = new(80, 40)
    d = ImageDraw.Draw(img)
    V=(224,64,251,255); D=(123,31,162,255); C=(0,229,255,255); Bk=(20,20,20,255)
    W=(255,255,255,255); L=(235,120,255,255)
    ty = 18 if not tail_up else 13
    poly(d, [(5,ty),(0,ty-6),(2,ty),(0,ty+6)], C, Bk, 1)
    ell(d, 8,5,64,35, V, Bk, 1)
    ell(d, 10,24,62,35, D, None)
    ell(d, 12,7,40,22, L, None)
    ell(d, 24,10,40,26, C, Bk, 1)
    ell(d, 27,13,37,23, V, None)
    poly(d, [(16,5),(24,0),(32,5)], C, Bk, 1)
    poly(d, [(32,5),(40,-1),(48,5)], C, Bk, 1)
    ell(d, 54,12,60,18, W, Bk, 1)
    ell(d, 55,13,59,17, Bk, None)
    ell(d, 56,13,58,15, W, None)
    line(d, 62,17,64,18, Bk, 1)
    return img

# ---------- Small reef fish ----------
def smallreef(tail_up=False):
    img = new(48, 28)
    d = ImageDraw.Draw(img)
    C=(38,198,218,255); D=(0,131,143,255); Y=(255,238,88,255); Bk=(20,20,20,255)
    W=(255,255,255,255); L=(100,220,230,255)
    ty = 13 if not tail_up else 9
    poly(d, [(3,ty),(0,ty-4),(0,ty+4)], D, Bk, 1)
    ell(d, 5,4,34,24, C, Bk, 1)
    ell(d, 7,16,32,24, D, None)
    ell(d, 8,5,22,14, L, None)
    poly(d, [(10,4),(14,0),(18,4)], Y, Bk, 1)
    ell(d, 26,8,32,14, W, Bk, 1)
    ell(d, 27,9,31,13, Bk, None)
    ell(d, 28,9,30,11, W, None)
    line(d, 34,12,36,13, Bk, 1)
    return img

# ---------- Sea Turtle ----------
def turtle(tail_up=False):
    img = new(96, 60)
    d = ImageDraw.Draw(img)
    G=(46,125,50,255); D=(27,94,32,255); L=(102,187,106,255); Bk=(20,20,20,255)
    Y=(255,241,118,255); Br=(139,69,19,255)
    # shell
    ell(d, 10,10,86,50, G, Bk, 2)
    ell(d, 16,14,80,46, D, None)
    # scutes
    for i in range(-3,4):
        line(d, 48+i*8, 12, 48+i*8, 48, D, 1)
    line(d, 14, 30, 82, 30, D, 1)
    # highlight
    ell(d, 18,14,44,28, L, None)
    # head
    ell(d, 78,22,96,40, L, Bk, 1)
    ell(d, 86,26,92,32, Bk, None)
    ell(d, 87,26,91,30, (255,255,255,255), None)
    # flippers
    poly(d, [(14,10),(4,2),(10,16)], L, Bk, 1)
    poly(d, [(14,50),(4,58),(10,44)], L, Bk, 1)
    poly(d, [(74,10),(84,2),(78,16)], L, Bk, 1)
    poly(d, [(74,50),(84,58),(78,44)], L, Bk, 1)
    return img

# ---------- Environment sprites (keep existing) ----------
def branching_coral():
    img = new(80, 80)
    d = ImageDraw.Draw(img)
    R=(239,83,80,255); D=(183,28,28,255); K=(20,20,20,255); P=(255,138,101,255); L=(255,180,170,255)
    poly(d, [(40,78),(24,40),(30,36)], R, K, 1)
    poly(d, [(40,78),(56,40),(50,36)], R, K, 1)
    poly(d, [(30,44),(18,22),(24,18)], D, K, 1)
    poly(d, [(50,44),(62,22),(56,18)], D, K, 1)
    poly(d, [(40,36),(36,8),(44,8)], P, K, 1)
    poly(d, [(36,40),(32,28),(40,28)], L, None)
    ell(d, 28,70,52,78, D, K, 1)
    return img

def brain_coral():
    img = new(72, 56)
    d = ImageDraw.Draw(img)
    O=(255,138,101,255); D=(230,74,25,255); K=(20,20,20,255)
    ell(d, 4,8,68,52, O, K, 1)
    ell(d, 10,14,62,46, D, None)
    for i in range(6):
        d.arc((10+i*3, 14+i*3, 62-i*3, 46-i*3), 0, 360, fill=K, width=1)
    ell(d, 28,22,44,38, O, K, 1)
    return img

def sea_fan():
    img = new(80, 80)
    d = ImageDraw.Draw(img)
    P=(186,104,200,255); D=(123,31,162,255); K=(20,20,20,255); L=(206,147,216,255)
    rect(d, 36,60,44,80, D, K, 1)
    import math
    for i in range(9):
        a=(i-4)*0.3
        x2=40+int(math.cos(-1.57+a)*36); y2=60+int(math.sin(-1.57+a)*36)
        line(d, 40,60, x2,y2, P, 2)
        # sub
        for j in (0.4,-0.4):
            xs=x2+int(math.cos(-1.57+a+j)*12); ys=y2+int(math.sin(-1.57+a+j)*12)
            line(d, x2,y2,xs,ys, D, 1)
    return img

def anemone():
    img = new(72, 72)
    d = ImageDraw.Draw(img)
    P=(244,143,177,255); D=(194,24,91,255); K=(20,20,20,255); G=(129,199,132,255); L=(248,187,208,255)
    ell(d, 20,56,52,72, G, K, 1)
    import math
    for i in range(12):
        a=math.radians(i*30)
        x=36+int(math.cos(a)*10); y=48+int(math.sin(a)*8)
        line(d, 36,52, x, y-18, P, 2)
        ell(d, x-3,y-22,x+3,y-16, P, K, 1)
        ell(d, x-1,y-20,x+1,y-18, L, None)
    return img

def seaweed():
    img = new(32, 80)
    d = ImageDraw.Draw(img)
    G=(46,125,50,255); D=(27,94,32,255); K=(20,20,20,255); L=(102,187,106,255)
    import math
    for i in range(6):
        x=6+i*4
        pts=[]
        xx=x
        for y in range(80,0,-3):
            xx=x+int(math.sin(y*0.12+i)*4)
            pts.append((xx,y))
        for j in range(len(pts)-1):
            line(d, pts[j][0],pts[j][1],pts[j+1][0],pts[j+1][1], G, 2)
        # leaflets
        for y in range(70,10,-12):
            xx=x+int(math.sin(y*0.12+i)*4)
            line(d, xx,y,xx+6,y-4, D, 1)
            line(d, xx,y,xx-6,y-4, D, 1)
    return img

def kelp():
    img = new(40, 100)
    d = ImageDraw.Draw(img)
    G=(27,94,32,255); D=(13,60,18,255); K=(20,20,20,255); L=(102,187,106,255)
    import math
    pts=[]
    x=20
    for y in range(100,0,-2):
        x=20+int(math.sin(y*0.12)*5)
        pts.append((x,y))
    for j in range(len(pts)-1):
        line(d, pts[j][0],pts[j][1],pts[j+1][0],pts[j+1][1], G, 4)
    for y in range(90,10,-10):
        x=20+int(math.sin(y*0.12)*5)
        line(d, x,y,x+12,y-8, L, 2)
        line(d, x,y,x-12,y-8, L, 2)
    return img

def rock():
    img = new(80, 48)
    d = ImageDraw.Draw(img)
    G=(120,144,156,255); D=(84,110,122,255); L=(176,190,197,255); K=(20,20,20,255); S=(96,125,139,255)
    poly(d, [(8,44),(16,12),(40,4),(72,12),(76,44),(40,48)], G, K, 1)
    ell(d, 20,12,44,28, L, None)
    ell(d, 50,16,68,30, D, None)
    ell(d, 28,30,44,42, S, None)
    for i in range(12):
        d.point((12+i*5, 20+(i*3)%12), fill=D)
    return img

def shell():
    img = new(40, 32)
    d = ImageDraw.Draw(img)
    P=(255,204,188,255); D=(255,138,101,255); K=(20,20,20,255); L=(255,224,204,255)
    poly(d, [(4,28),(20,4),(36,28)], P, K, 1)
    for i in range(7):
        line(d, 20,4, 4+i*5, 28, D, 1)
        line(d, 20,4, 36-i*5, 28, D, 1)
    ell(d, 14,10,26,20, L, None)
    return img

def treasure():
    img = new(88, 72)
    d = ImageDraw.Draw(img)
    B=(141,110,99,255); D=(93,64,55,255); G=(255,213,79,255); K=(20,20,20,255)
    L=(180,140,120,255)
    rect(d, 12,28,76,68, B, K, 1)
    rect(d, 12,20,76,30, D, K, 1)
    poly(d, [(12,28),(44,8),(76,28)], D, K, 1)
    poly(d, [(14,28),(44,12),(74,28)], L, None)
    rect(d, 36,32,52,44, G, K, 1)
    for i in range(5):
        ell(d, 16+i*12, 4, 28+i*12, 16, G, K, 1)
    return img

def shipwreck():
    img = new(120, 80)
    d = ImageDraw.Draw(img)
    B=(93,64,55,255); D=(62,39,35,255); G=(121,85,72,255); K=(20,20,20,255)
    L=(140,100,80,255)
    poly(d, [(8,68),(16,48),(104,48),(112,68)], B, K, 1)
    rect(d, 16,40,104,50, D, K, 1)
    rect(d, 56,4,64,48, G, K, 1)
    poly(d, [(64,8),(88,16),(68,28)], (190,190,190,200), K, 1)
    rect(d, 24,56,40,60, K, None)
    rect(d, 80,56,96,60, K, None)
    # broken planks
    rect(d, 8,44,20,46, L, None)
    rect(d, 90,42,108,44, L, None)
    return img

# ---- Save all ----
def saveall():
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
    # environment
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

saveall()
print("ALL DONE")
