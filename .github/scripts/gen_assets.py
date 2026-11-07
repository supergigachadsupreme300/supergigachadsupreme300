import os
from PIL import Image, ImageDraw

OUT = "D:/schools/supergigachadsupreme300/aquarium/assets/sprites"
os.makedirs(OUT, exist_ok=True)

def new(w, h):
    return Image.new("RGBA", (w, h), (0,0,0,0))

def outline(draw, shape_func, color=(20,20,20,255)):
    # draw outline by drawing shape slightly larger then fill
    pass

def save(img, name):
    img.save(os.path.join(OUT, name), "PNG")
    print("saved", name)

def ell(draw, x0,y0,x1,y1, fill, outline_color=(26,26,26,255)):
    draw.ellipse((x0,y0,x1,y1), fill=fill, outline=outline_color, width=1)

def rect(draw, x0,y0,x1,y1, fill, outline_color=(26,26,26,255)):
    draw.rectangle((x0,y0,x1,y1), fill=fill, outline=outline_color, width=1)

def poly(draw, pts, fill, outline_color=(26,26,26,255)):
    draw.polygon(pts, fill=fill, outline=outline_color, width=1)

# ---- Fish: clownfish (orange, white bands) ----
def clownfish(tail_up=False):
    img = new(40, 20)
    d = ImageDraw.Draw(img)
    O=(255,112,67,255); D=(180,60,30,255); W=(255,255,255,255); K=(26,26,26,255); Y=(255,193,7,255)
    # tail (left)
    tail_y = 8 if not tail_up else 5
    poly(d, [(2,tail_y),(0,tail_y-4),(0,tail_y+4)], O, K)
    # body
    ell(d, 6,4,30,16, O, K)
    # shadow lower
    ell(d, 8,10,28,16, D, None)
    # white bands
    rect(d, 12,5,15,15, W, K)
    rect(d, 20,5,23,15, W, K)
    # dorsal fin
    poly(d, [(14,4),(18,0),(22,4)], Y, K)
    # pectoral fin
    poly(d, [(16,12),(13,16),(19,16)], Y, K)
    # eye
    ell(d, 24,7,28,11, (255,255,255,255), K)
    ell(d, 25,8,27,10, K, None)
    # mouth
    rect(d, 29,9,31,10, K, None)
    return img
save(clownfish(False), "clownfish_0.png")
save(clownfish(True), "clownfish_1.png")

# ---- Blue tang ----
def bluetang(tail_up=False):
    img = new(40, 20)
    d = ImageDraw.Draw(img)
    B=(30,136,229,255); D=(13,71,161,255); Y=(255,235,59,255); K=(26,26,26,255); W=(255,255,255,255)
    tail_y = 9 if not tail_up else 6
    poly(d, [(2,tail_y),(0,tail_y-5),(0,tail_y+5)], Y, K)
    ell(d, 6,3,32,17, B, K)
    ell(d, 8,11,30,17, D, None)
    # yellow tail base
    rect(d, 6,7,9,13, Y, K)
    # dorsal
    poly(d, [(14,3),(20,-1),(26,3)], D, K)
    # eye
    ell(d, 25,7,29,11, W, K)
    ell(d, 26,8,28,10, K, None)
    rect(d, 31,9,33,10, K, None)
    return img
save(bluetang(False), "bluetang_0.png")
save(bluetang(True), "bluetang_1.png")

# ---- Angelfish (tall) ----
def angelfish(tail_up=False):
    img = new(36, 32)
    d = ImageDraw.Draw(img)
    P=(244,143,177,255); D=(194,24,91,255); Y=(255,235,59,255); K=(26,26,26,255); W=(255,255,255,255)
    tail_y = 14 if not tail_up else 10
    poly(d, [(2,tail_y),(0,tail_y-4),(0,tail_y+4)], D, K)
    ell(d, 6,4,28,28, P, K)
    ell(d, 8,18,26,28, D, None)
    # stripes
    rect(d, 13,4,15,28, D, K)
    rect(d, 20,4,22,28, D, K)
    # long dorsal
    poly(d, [(8,4),(16,-2),(24,4)], D, K)
    # anal fin
    poly(d, [(8,28),(16,34),(24,28)], D, K)
    # eye
    ell(d, 20,10,24,14, W, K)
    ell(d, 21,11,23,13, K, None)
    rect(d, 27,13,29,14, K, None)
    return img
save(angelfish(False), "angelfish_0.png")
save(angelfish(True), "angelfish_1.png")

# ---- Butterflyfish (flat round) ----
def butterflyfish(tail_up=False):
    img = new(36, 24)
    d = ImageDraw.Draw(img)
    Y=(255,235,59,255); D=(249,168,37,255); B=(26,35,126,255); K=(26,26,26,255); W=(255,255,255,255); O=(255,143,0,255)
    tail_y = 10 if not tail_up else 7
    poly(d, [(2,tail_y),(0,tail_y-3),(0,tail_y+3)], O, K)
    ell(d, 5,4,28,20, Y, K)
    ell(d, 7,12,26,20, D, None)
    # eye spot
    ell(d, 9,8,14,13, B, K)
    ell(d, 10,9,13,12, K, None)
    ell(d, 11,9,12,10, W, None)
    # vertical bar
    rect(d, 21,5,23,19, B, K)
    # dorsal
    poly(d, [(10,4),(16,0),(22,4)], O, K)
    # eye
    ell(d, 23,8,27,12, W, K)
    ell(d, 24,9,26,11, K, None)
    rect(d, 29,10,31,11, K, None)
    return img
save(butterflyfish(False), "butterflyfish_0.png")
save(butterflyfish(True), "butterflyfish_1.png")

# ---- Pufferfish (round) ----
def pufferfish(tail_up=False):
    img = new(32, 24)
    d = ImageDraw.Draw(img)
    Y=(255,245,157,255); D=(192,202,51,255); P=(244,143,177,255); K=(26,26,26,255); W=(255,255,255,255); G=(93,64,55,255)
    r=9
    cx,cy=15,12
    ell(d, cx-r, cy-r, cx+r, cy+r, Y, K)
    ell(d, cx-r+2, cy+2, cx+r-2, cy+r, D, None)
    # spots
    for (a,rr) in [(0,0),(60,0),(-60,0),(30,5),(-30,5)]:
        import math
        x=cx+int(math.cos(math.radians(a))*4); y=cy+int(math.sin(math.radians(a))*4)
        ell(d, x-2,y-2,x+2,y+2, P, None)
    # spikes
    for i in range(12):
        import math
        a=i/12*360
        x1=cx+int(math.cos(math.radians(a))*r); y1=cy+int(math.sin(math.radians(a))*r)
        x2=cx+int(math.cos(math.radians(a))*(r+3)); y2=cy+int(math.sin(math.radians(a))*(r+3))
        d.line((x1,y1,x2,y2), fill=G, width=1)
    # tail
    ty = 12 if not tail_up else 9
    poly(d, [(cx-r, ty),(cx-r-6, ty-3),(cx-r-6, ty+3)], P, K)
    # eye
    ell(d, cx+3, cy-4, cx+8, cy+0, W, K)
    ell(d, cx+4, cy-3, cx+7, cy-1, K, None)
    ell(d, cx+5, cy-3, cx+6, cy-2, W, None)
    # mouth
    ell(d, cx+r-2, cy, cx+r+1, cy+2, G, None)
    return img
save(pufferfish(False), "pufferfish_0.png")
save(pufferfish(True), "pufferfish_1.png")

# ---- Lionfish ----
def lionfish(tail_up=False):
    img = new(48, 24)
    d = ImageDraw.Draw(img)
    R=(229,57,53,255); D=(183,28,28,255); W=(255,255,255,255); K=(26,26,26,255); Y=(255,202,40,255); O=(255,112,67,255)
    tail_y = 11 if not tail_up else 8
    # tail
    poly(d, [(4,tail_y),(0,tail_y-4),(0,tail_y+4)], D, K)
    # body
    ell(d, 8,6,34,18, R, K)
    ell(d, 10,12,32,18, D, None)
    # stripes
    for sx in [12,16,20,24,28]:
        rect(d, sx,6,sx+2,18, W, K)
    # fan fins (dorsal)
    for fx in range(10,30,4):
        poly(d, [(fx,6),(fx+2,0),(fx+4,6)], Y, K)
    # pectoral (side fins)
    poly(d, [(16,14),(12,20),(20,20)], O, K)
    # eye
    ell(d, 28,8,32,12, W, K)
    ell(d, 29,9,31,11, K, None)
    rect(d, 34,10,36,11, K, None)
    return img
save(lionfish(False), "lionfish_0.png")
save(lionfish(True), "lionfish_1.png")

# ---- Koi ----
def koi(tail_up=False):
    img = new(48, 20)
    d = ImageDraw.Draw(img)
    O=(255,138,101,255); D=(216,67,21,255); W=(255,255,255,255); K=(26,26,26,255); R=(191,54,12,255); Y=(255,202,40,255)
    tail_y = 9 if not tail_up else 6
    # long flowing tail
    poly(d, [(4,tail_y),(0,tail_y-6),(2,tail_y),(0,tail_y+6)], R, K)
    ell(d, 8,4,36,16, O, K)
    ell(d, 10,10,34,16, D, None)
    # white patches
    ell(d, 14,6,20,12, W, K)
    ell(d, 26,7,32,13, W, K)
    # dorsal
    poly(d, [(14,4),(20,0),(26,4)], R, K)
    # eye
    ell(d, 30,7,34,11, W, K)
    ell(d, 31,8,33,10, K, None)
    rect(d, 35,9,37,10, K, None)
    return img
save(koi(False), "koi_0.png")
save(koi(True), "koi_1.png")

# ---- Small reef fish ----
def smallreef(tail_up=False):
    img = new(24, 14)
    d = ImageDraw.Draw(img)
    C=(38,198,218,255); D=(0,131,143,255); Y=(255,238,88,255); K=(26,26,26,255); W=(255,255,255,255)
    tail_y = 6 if not tail_up else 4
    poly(d, [(2,tail_y),(0,tail_y-3),(0,tail_y+3)], D, K)
    ell(d, 4,3,18,11, C, K)
    ell(d, 6,8,16,11, D, None)
    poly(d, [(8,3),(11,0),(14,3)], Y, K)
    ell(d, 14,5,18,9, W, K)
    ell(d, 15,6,17,8, K, None)
    rect(d, 19,6,21,7, K, None)
    return img
save(smallreef(False), "smallreef_0.png")
save(smallreef(True), "smallreef_1.png")

# ---- Coral & environment assets ----
def branching_coral():
    img = new(40, 40)
    d = ImageDraw.Draw(img)
    R=(239,83,80,255); D=(183,28,28,255); K=(26,26,26,255); P=(255,138,101,255)
    # branches
    poly(d, [(20,38),(12,20),(16,18)], R, K)
    poly(d, [(20,38),(28,20),(24,18)], R, K)
    poly(d, [(16,22),(10,10),(14,8)], D, K)
    poly(d, [(24,22),(30,10),(26,8)], D, K)
    poly(d, [(20,18),(18,4),(22,4)], P, K)
    # base
    ell(d, 14,34,26,40, D, K)
    return img
save(branching_coral(), "coral_branching.png")

def brain_coral():
    img = new(36, 28)
    d = ImageDraw.Draw(img)
    O=(255,138,101,255); D=(230,74,25,255); K=(26,26,26,255)
    ell(d, 2,4,34,26, O, K)
    ell(d, 6,8,30,22, D, None)
    # grooves
    for i in range(4):
        d.arc((6+i*2, 8+i, 30-i*2, 22-i), 0, 360, fill=K, width=1)
    ell(d, 14,12,22,18, O, K)
    return img
save(brain_coral(), "coral_brain.png")

def sea_fan():
    img = new(40, 40)
    d = ImageDraw.Draw(img)
    P=(186,104,200,255); D=(123,31,162,255); K=(26,26,26,255)
    # stem
    rect(d, 18,30,22,40, D, K)
    # fan branches
    for i in range(7):
        a = (i-3)*0.35
        import math
        x1=20; y1=30
        x2=20+int(math.cos(-1.57+a)*22); y2=30+int(math.sin(-1.57+a)*22)
        d.line((x1,y1,x2,y2), fill=P, width=2)
    # sub branches
    for i in range(7):
        import math
        a=(i-3)*0.35
        x=20+int(math.cos(-1.57+a)*12); y=30+int(math.sin(-1.57+a)*12)
        d.line((x,y,x+int(math.cos(-1.57+a+0.5)*8), y+int(math.sin(-1.57+a+0.5)*8)), fill=D, width=1)
        d.line((x,y,x+int(math.cos(-1.57+a-0.5)*8), y+int(math.sin(-1.57+a-0.5)*8)), fill=D, width=1)
    return img
save(sea_fan(), "coral_seafan.png")

def anemone():
    img = new(36, 36)
    d = ImageDraw.Draw(img)
    P=(244,143,177,255); D=(194,24,91,255); K=(26,26,26,255); G=(129,199,132,255)
    # base
    ell(d, 10,28,26,36, G, K)
    # tentacles
    import math
    for i in range(10):
        a=i/10*360
        x=18+int(math.cos(math.radians(a))*6); y=22+int(math.sin(math.radians(a))*4)
        d.line((18,24,x,y-10), fill=P, width=2)
        ell(d, x-2,y-12,x+2,y-8, P, K)
    return img
save(anemone(), "anemone.png")

def seaweed():
    img = new(16, 40)
    d = ImageDraw.Draw(img)
    G=(46,125,50,255); D=(27,94,32,255); K=(26,26,26,255)
    # narrow leaves
    import math
    for i in range(5):
        x=4+i*2
        d.line((x,40,x+int(math.sin(i)*3),0), fill=G, width=2)
        # leaflets
        for j in range(3):
            yy=35-j*10
            xx=x+int(math.sin(i)*3)* (1-j/3.0)*0.5
            d.line((xx,yy,xx+4,yy-3), fill=D, width=1)
            d.line((xx,yy,xx-4,yy-3), fill=D, width=1)
    return img
save(seaweed(), "seaweed.png")

def kelp():
    img = new(20, 50)
    d = ImageDraw.Draw(img)
    G=(27,94,32,255); D=(13,60,18,255); K=(26,26,26,255); L=(102,187,106,255)
    import math
    # stem
    pts=[]
    x=10
    for y in range(50,0,-2):
        x=10+int(math.sin(y*0.15)*3)
        pts.append((x,y))
    for i in range(len(pts)-1):
        d.line((pts[i][0],pts[i][1],pts[i+1][0],pts[i+1][1]), fill=G, width=3)
    # leaves
    for y in range(45,5,-8):
        x=10+int(math.sin(y*0.15)*3)
        d.line((x,y,x+8,y-6), fill=L, width=2)
        d.line((x,y,x-8,y-6), fill=L, width=2)
    return img
save(kelp(), "kelp.png")

def rock():
    img = new(40, 24)
    d = ImageDraw.Draw(img)
    G=(120,144,156,255); D=(84,110,122,255); L=(176,190,197,255); K=(26,26,26,255)
    poly(d, [(4,20),(8,6),(20,2),(32,6),(36,20),(20,23)], G, K)
    ell(d, 10,8,22,16, L, None)
    ell(d, 24,10,32,16, D, None)
    # texture
    for i in range(8):
        d.point((8+i*4, 12+i%3), fill=D)
    return img
save(rock(), "rock.png")

def shell():
    img = new(20, 16)
    d = ImageDraw.Draw(img)
    P=(255,204,188,255); D=(255,138,101,255); K=(26,26,26,255)
    poly(d, [(2,14),(10,2),(18,14)], P, K)
    for i in range(5):
        d.line((10,2,2+i*3,14), fill=D, width=1)
        d.line((10,2,18-i*3,14), fill=D, width=1)
    return img
save(shell(), "shell.png")

def treasure():
    img = new(44, 36)
    d = ImageDraw.Draw(img)
    B=(141,110,99,255); D=(93,64,55,255); G=(255,213,79,255); K=(26,26,26,255)
    # chest body
    rect(d, 6,14,38,34, B, K)
    rect(d, 6,10,38,16, D, K)
    # lid
    poly(d, [(6,14),(22,4),(38,14)], D, K)
    # lock
    rect(d, 18,16,26,22, G, K)
    # coins
    for i in range(4):
        ell(d, 10+i*8, 2, 16+i*8, 8, G, K)
    return img
save(treasure(), "treasure.png")

def shipwreck():
    img = new(60, 40)
    d = ImageDraw.Draw(img)
    B=(93,64,55,255); D=(62,39,35,255); G=(121,85,72,255); K=(26,26,26,255)
    # hull
    poly(d, [(4,34),(8,24),(52,24),(56,34)], B, K)
    rect(d, 8,20,52,26, D, K)
    # mast
    rect(d, 28,2,32,24, G, K)
    # broken sail
    poly(d, [(32,4),(44,8),(36,14)], (200,200,200,180), K)
    # details
    rect(d, 12,28,20,30, K, None)
    rect(d, 40,28,48,30, K, None)
    return img
save(shipwreck(), "shipwreck.png")

# ---- Goldfish ----
def goldfish(tail_up=False):
    img = new(40, 20)
    d = ImageDraw.Draw(img)
    Y=(255,202,40,255); D=(249,168,37,255); W=(255,255,255,255); K=(26,26,26,255); R=(229,57,53,255)
    tail_y = 9 if not tail_up else 6
    poly(d, [(4,tail_y),(0,tail_y-5),(2,tail_y),(0,tail_y+5)], R, K)
    ell(d, 8,4,32,16, Y, K)
    ell(d, 10,10,30,16, D, None)
    ell(d, 14,6,20,12, W, K)
    poly(d, [(14,4),(20,0),(26,4)], D, K)
    ell(d, 26,7,30,11, W, K)
    ell(d, 27,8,29,10, K, None)
    rect(d, 31,9,33,10, K, None)
    return img
save(goldfish(False), "goldfish_0.png")
save(goldfish(True), "goldfish_1.png")

# ---- Tropical (green/pink striped) ----
def tropical(tail_up=False):
    img = new(36, 18)
    d = ImageDraw.Draw(img)
    G=(0,230,118,255); D=(0,137,123,255); P=(255,64,129,255); W=(255,255,255,255); K=(26,26,26,255)
    tail_y = 8 if not tail_up else 5
    poly(d, [(2,tail_y),(0,tail_y-4),(0,tail_y+4)], P, K)
    ell(d, 5,3,28,15, G, K)
    ell(d, 7,10,26,15, D, None)
    for sx in [10,15,20]:
        rect(d, sx,4,sx+2,15, P, K)
    poly(d, [(10,3),(14,0),(18,3)], P, K)
    ell(d, 22,6,26,10, W, K)
    ell(d, 23,7,25,9, K, None)
    rect(d, 28,8,30,9, K, None)
    return img
save(tropical(False), "tropical_0.png")
save(tropical(True), "tropical_1.png")

# ---- Exotic (purple) ----
def exotic(tail_up=False):
    img = new(40, 22)
    d = ImageDraw.Draw(img)
    V=(224,64,251,255); D=(123,31,162,255); C=(0,229,255,255); W=(255,255,255,255); K=(26,26,26,255)
    tail_y = 10 if not tail_up else 7
    poly(d, [(3,tail_y),(0,tail_y-5),(0,tail_y+5)], C, K)
    ell(d, 6,4,32,18, V, K)
    ell(d, 8,12,30,18, D, None)
    ell(d, 14,7,22,15, C, K)
    ell(d, 16,9,20,13, V, K)
    poly(d, [(12,4),(18,0),(24,4)], C, K)
    ell(d, 26,7,30,11, W, K)
    ell(d, 27,8,29,10, K, None)
    rect(d, 32,9,34,10, K, None)
    return img
save(exotic(False), "exotic_0.png")
save(exotic(True), "exotic_1.png")

# ---- Sea Turtle ----
def turtle(tail_up=False):
    img = new(48, 30)
    d = ImageDraw.Draw(img)
    G=(46,125,50,255); D=(27,94,32,255); L=(102,187,106,255); K=(26,26,26,255); Y=(255,241,118,255)
    # shell
    ell(d, 6,6,42,24, G, K)
    ell(d, 10,9,38,21, D, None)
    # scutes
    for i in range(-2,3):
        d.line((24+i*6,8,24+i*6,22), fill=D, width=1)
    d.line((8,15,40,15), fill=D, width=1)
    # head
    ell(d, 38,10,48,20, L, K)
    ell(d, 42,12,46,16, K, None)
    ell(d, 43,12,45,14, (255,255,255,255), None)
    # flippers
    poly(d, [(10,6),(4,0),(8,10)], L, K)
    poly(d, [(10,24),(4,30),(8,20)], L, K)
    poly(d, [(34,6),(40,0),(36,10)], L, K)
    poly(d, [(34,24),(40,30),(36,20)], L, K)
    return img
save(turtle(False), "turtle_0.png")
save(turtle(True), "turtle_1.png")

# ---- Royal Gramma (purple front, yellow rear) ----
def royal_gramma(tail_up=False):
    img = new(36, 18)
    d = ImageDraw.Draw(img)
    P=(123,31,162,255); Y=(255,213,79,255); D=(74,20,140,255); K=(26,26,26,255); W=(255,255,255,255)
    tail_y = 8 if not tail_up else 5
    poly(d, [(2,tail_y),(0,tail_y-3),(0,tail_y+3)], Y, K)
    ell(d, 4,3,30,15, P, K)
    for x in range(18,31):
        for y in range(4,16):
            if (x-20)**2/8**2 + (y-10)**2/6**2 <= 1:
                d.point((x,y), fill=Y)
    ell(d, 6,9,28,15, D, None)
    poly(d, [(8,3),(12,0),(16,3)], P, K)
    ell(d, 24,6,28,10, W, K)
    ell(d, 25,7,27,9, K, None)
    rect(d, 29,8,31,9, K, None)
    return img
save(royal_gramma(False), "royalgramma_0.png")
save(royal_gramma(True), "royalgramma_1.png")

# ---- Moorish Idol (black/white/yellow, long snout) ----
def moorish_idol(tail_up=False):
    img = new(44, 20)
    d = ImageDraw.Draw(img)
    B=(26,26,26,255); W=(255,255,255,255); Y=(255,193,7,255); K=(26,26,26,255)
    tail_y = 9 if not tail_up else 6
    poly(d, [(2,tail_y),(0,tail_y-4),(0,tail_y+4)], Y, K)
    ell(d, 6,4,30,16, W, K)
    rect(d, 10,4,13,16, B, K)
    rect(d, 18,4,21,16, B, K)
    poly(d, [(12,4),(16,0),(20,4)], Y, K)
    poly(d, [(20,4),(24,-2),(28,4)], Y, K)
    rect(d, 30,8,40,11, W, K)
    rect(d, 30,9,40,10, B, None)
    ell(d, 24,6,28,10, (255,255,255,255), K)
    ell(d, 25,7,27,9, K, None)
    return img
save(moorish_idol(False), "moorishidol_0.png")
save(moorish_idol(True), "moorishidol_1.png")

print("DONE")
