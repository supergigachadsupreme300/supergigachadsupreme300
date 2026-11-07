import os
from PIL import Image

OUT = "D:/schools/supergigachadsupreme300/aquarium/assets/sprites"
os.makedirs(OUT, exist_ok=True)

def render(grid, palette, scale=2):
    h = len(grid)
    w = max(len(r) for r in grid)
    img = Image.new("RGBA", (w*scale, h*scale), (0,0,0,0))
    px = img.load()
    for y, row in enumerate(grid):
        for x in range(w):
            ch = row[x] if x < len(row) else '.'
            col = palette.get(ch)
            if col is None: continue
            for sy in range(scale):
                for sx in range(scale):
                    px[x*scale+sx, y*scale+sy] = col
    return img

def save(img, name):
    img.save(os.path.join(OUT, name), "PNG")
    print("saved", name)

K=(18,18,24,255)
def P(**kw): return kw  # not used

# ===================== CLOWNFISH (48x22) =====================
CP = {'.':None,'K':K,'O':(255,109,50,255),'D':(195,55,20,255),'W':(255,255,255,255),'G':(225,225,225,255),'Y':(255,193,7,255),'L':(255,165,120,255)}
clown_0 = [
"................................................",
"........................KKKKKK..................",
"......................KKOOOOOOK.................",
".....................KOOOOOOOOOK................",
"....................KOOOOOOOOOOOK...............",
"...................KOOOOOOOOOOOOOK..............",
"..................KOOOOOOOOOOOOOOOK.............",
".................KOOOOOOOOOOOOOOOOOK............",
"................KOOOOOOOOOOOOOOOOOOOK...........",
"...............KOOOOOOOOOOOOOOOOOOOOOK..........",
"..............KOOOOOOOOOOOOOOOOOOOOOOOK.........",
".............KOOOOOOOOOOOOOOOOOOOOOOOOOK........",
"............KWWWOOOOOOOOOOOOOOOOOOOOOOOOK.......",
"...........KWWWOOOOOOOOOOOOOOOOOOOOOOOOOOK......",
"...........KWWWOOOOOOOOOOOOOOOOOOOOOOOOOOK......",
"............KOOOOOOOOOOOOOOOOOOOOOOOOOOOK.......",
".............KOOOOOOOOOOOOOOOOOOOOOOOOOK........",
"..............KOOOOOOOOOOOOOOOOOOOOOOOK.........",
"...............KOOOOOOOOOOOOOOOOOOOOOK..........",
"................KOOOOOOOOOOOOOOOOOOOK...........",
".................KKOOOOOOOOOOOOOOOOK............",
"...................KKKKKKKKKKKKKKK..............",
]
# Add tail (left fork) by prepending columns 0-5 to rows 9-13
for i in range(9,14):
    clown_0[i] = "KK...." + clown_0[i][6:]
# dorsal fin on top rows 1-3
clown_0[1] = ".....................YYYYY......................"
clown_0[2] = "....................YYYYYYY....................."
clown_0[3] = "...................YYYYYYYYY...................."
clown_1 = [r for r in clown_0]
clown_1[9]  = "KK....KWWWOOOOOOOOOOOOOOOOOOOOOOK............."
clown_1[10] = "KK....KWWWOOOOOOOOOOOOOOOOOOOOOOK............."
clown_1[11] = "KK....KOOOOOOOOOOOOOOOOOOOOOOOOK.............."
clown_1[12] = "KK....KOOOOOOOOOOOOOOOOOOOOOOOK..............."
save(render(clown_0, CP, 2), "clownfish_0.png")
save(render(clown_1, CP, 2), "clownfish_1.png")

# ===================== BLUE TANG (48x22) =====================
TP = {'.':None,'K':K,'B':(30,120,220,255),'D':(12,60,150,255),'Y':(255,230,59,255),'L':(110,175,245,255),'W':(255,255,255,255)}
tang_0 = [
"................................................",
"........................KKKKKK..................",
"......................KKBBBBBK..................",
".....................KBBBBBBBBK.................",
"....................KBBBBBBBBBBK................",
"...................KBBBBBBBBBBBBK...............",
"..................KBBBBBBBBBBBBBBK..............",
".................KBBBBBBBBBBBBBBBBK.............",
"................KBBBBBBBBBBBBBBBBBBK............",
"...............KBBBBBBBBBBBBBBBBBBBBK...........",
"..............KBBBBBBBBBBBBBBBBBBBBBBK..........",
".............KBBBBBBBBBBBBBBBBBBBBBBBBK.........",
"............KBBBBBBBBBBBBBBBBBBBBBBBBBBK........",
"...........KBBBBBBBBBBBBBBBBBBBBBBBBBBBBK.......",
"............KBBBBBBBBBBBBBBBBBBBBBBBBBBK........",
".............KBBBBBBBBBBBBBBBBBBBBBBBBK.........",
"..............KBBBBBBBBBBBBBBBBBBBBBBK..........",
"...............KBBBBBBBBBBBBBBBBBBBBK...........",
"................KBBBBBBBBBBBBBBBBBBK............",
".................KKBBBBBBBBBBBBBBBK.............",
"...................KKKKKKKKKKKKKKK..............",
"................................................",
]
# tail yellow fork left rows 9-13
for i in range(9,14):
    tang_0[i] = "KK...." + tang_0[i][6:]
# dorsal fin top
tang_0[1] = ".....................DDDD......................"
tang_0[2] = "....................DDDDDD....................."
tang_0[3] = "...................DDDDDDDD...................."
# yellow tail base rows 10-12 cols 6-9
for i in range(10,13):
    tang_0[i] = tang_0[i][:6] + "YYY" + tang_0[i][9:]
tang_1 = [r for r in tang_0]
save(render(tang_0, TP, 2), "bluetang_0.png")
save(render(tang_1, TP, 2), "bluetang_1.png")

# ===================== ANGELFISH (40x40) =====================
AP = {'.':None,'K':K,'P':(240,130,175,255),'D':(190,20,85,255),'Y':(255,230,59,255),'L':(248,180,205,255),'W':(255,255,255,255)}
angel_0 = [
"........................................",
"..................KKKK..................",
"................KPPPPPK.................",
"...............KPPPPPPPK................",
"..............KPPPPPPPPPK...............",
".............KPPPPPPPPPPPK..............",
"............KPPPPPPPPPPPPPK.............",
"...........KPPPPPPPPPPPPPPPK............",
"..........KPPPPPPPPPPPPPPPPPK...........",
".........KPPPPPPPPPPPPPPPPPPPK..........",
"........KPPPPPPPPPPPPPPPPPPPPPK.........",
".......KPPPPPPPPPPPPPPPPPPPPPPPK........",
"......KPPPPPPPPPPPPPPPPPPPPPPPPPK.......",
".....KPPPPPPPPPPPPPPPPPPPPPPPPPPPK......",
"....KPPPPPPPPPPPPPPPPPPPPPPPPPPPPPK.....",
"...KPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPK....",
"..KPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPK...",
".KPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPK..",
"KPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPK.",
"KDDDDPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPK.",
"KDDDDPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPK.",
"KPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPK.",
".KPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPK..",
"..KPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPK...",
"...KKKKPPPPPPPPPPPPPPPPPPPPPPPPPPPK.....",
"......KPPPPPPPPPPPPPPPPPPPPPPPPPK.......",
".......KPPPPPPPPPPPPPPPPPPPPPPPK........",
"........KPPPPPPPPPPPPPPPPPPPPPK.........",
".........KKKKPPPPPPPPPPPPPPPK...........",
"............KPPPPPPPPPPPPPK.............",
".............KKKKKKKKKKKKK..............",
"........................................",
"........................................",
"........................................",
"........................................",
"........................................",
"........................................",
"........................................",
"........................................",
]
# stripes + fins
for i in range(4,36):
    angel_0[i] = angel_0[i][:10] + "D" + angel_0[i][11:]
    angel_0[i] = angel_0[i][:20] + "D" + angel_0[i][21:]
# dorsal fin top rows 0-3
angel_0[0] = "..........DDDDDDDDDDDDDDDDDD............"
angel_0[1] = ".........DDDDDDDDDDDDDDDDDDDD..........."
angel_0[2] = "........DDDDDDDDDDDDDDDDDDDDDD.........."
# anal fin bottom
angel_0[33] = "........DDDDDDDDDDDDDDDDDDDDDD.........."
angel_0[34] = ".........DDDDDDDDDDDDDDDDDDDD..........."
angel_0[35] = "..........DDDDDDDDDDDDDDDDDD............"
# eye
angel_0[12] = angel_0[12][:28] + "WWW" + angel_0[12][31:]
angel_0[13] = angel_0[13][:28] + "WKW" + angel_0[13][31:]
angel_0[14] = angel_0[14][:28] + "WWW" + angel_0[14][31:]
angel_1 = [r for r in angel_0]
save(render(angel_0, AP, 2), "angelfish_0.png")
save(render(angel_1, AP, 2), "angelfish_1.png")

# ===================== BUTTERFLYFISH (44x24) =====================
BP = {'.':None,'K':K,'Y':(255,230,59,255),'D':(245,160,30,255),'B':(26,35,126,255),'O':(255,143,0,255),'W':(255,255,255,255),'L':(255,245,190,255)}
butter_0 = [
"............................................",
"..................KKKKKK....................",
"................KYYYYYYK....................",
"...............KYYYYYYYYK...................",
"..............KYYYYYYYYYYK..................",
".............KYYYYYYYYYYYYK.................",
"............KYYYYYYYYYYYYYYK................",
"...........KYYYYYYYYYYYYYYYYK...............",
"..........KYYYYYYYYYYYYYYYYYYK..............",
".........KYYYYYYYYYYYYYYYYYYYYK.............",
"........KYYYYYYYYYYYYYYYYYYYYYYK............",
".......KYYYYYYYYYYYYYYYYYYYYYYYYK...........",
"......KYYYYYYYYYYYYYYYYYYYYYYYYYYK..........",
".....KYYYYYYYYYYYYYYYYYYYYYYYYYYYYK.........",
"....KYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYK........",
"...KYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYK.......",
"..KYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYK......",
".KYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYK.....",
"KYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYK....",
"KDDDDYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYK....",
"KDDDDYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYK....",
"KYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYK....",
".KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK.....",
"............................................",
]
# eye spot
for i in range(4,8):
    butter_0[i] = butter_0[i][:8] + "BBBB" + butter_0[i][12:]
    butter_0[i] = butter_0[i][:9] + "BB" + butter_0[i][11:]
# vertical bar
for i in range(3,20):
    butter_0[i] = butter_0[i][:22] + "BB" + butter_0[i][24:]
# dorsal fin top
butter_0[0] = ".........OOOOOOOOOOOOOOOOO.................."
butter_0[1] = "........OOOOOOOOOOOOOOOOOOO................."
butter_0[2] = ".......OOOOOOOOOOOOOOOOOOOOO................"
# eye
butter_0[9]  = butter_0[9][:30] + "WWW" + butter_0[9][33:]
butter_0[10] = butter_0[10][:30] + "WKW" + butter_0[10][33:]
butter_0[11] = butter_0[11][:30] + "WWW" + butter_0[11][33:]
butter_1 = [r for r in butter_0]
save(render(butter_0, BP, 2), "butterflyfish_0.png")
save(render(butter_1, BP, 2), "butterflyfish_1.png")

# ===================== PUFFERFISH (40x36) =====================
PP = {'.':None,'K':K,'Y':(255,245,157,255),'D':(185,195,45,255),'P':(244,143,177,255),'W':(255,255,255,255),'G':(93,64,55,255),'L':(255,255,225,255)}
puff_0 = [
"........................................",
"..................KKKK..................",
"................KYYYYYK.................",
"...............KYYYYYYYK................",
"..............KYYYYYYYYYK...............",
".............KYYYYYYYYYYYK..............",
"............KYYYYYYYYYYYYYK.............",
"...........KYYYYYYYYYYYYYYYK............",
"..........KYYYYYYYYYYYYYYYYYK...........",
".........KYYYYYYYYYYYYYYYYYYYK..........",
"........KYYYYYYYYYYYYYYYYYYYYYK.........",
".......KYYYYYYYYYYYYYYYYYYYYYYYK........",
"......KYYYYYYYYYYYYYYYYYYYYYYYYYK.......",
".....KYYYYYYYYYYYYYYYYYYYYYYYYYYYK......",
"....KYYYYYYYYYYYYYYYYYYYYYYYYYYYYYK.....",
"...KYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYK....",
"..KYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYK...",
".KYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYK..",
"KYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYK.",
"KDDDDYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYK.",
"KDDDDYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYK.",
"KYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYK.",
"KYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYK.",
".KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK..",
]
# spots
for i in range(6):
    puff_0[8+i] = puff_0[8+i][:10+i] + "PPP" + puff_0[8+i][13+i:]
# spikes on outline (add dots around)
# eye
puff_0[9]  = puff_0[9][:24] + "WWW" + puff_0[9][27:]
puff_0[10] = puff_0[10][:24] + "WKW" + puff_0[10][27:]
puff_0[11] = puff_0[11][:24] + "WWW" + puff_0[11][27:]
# tail left
for i in range(10,16):
    puff_0[i] = "KK.." + puff_0[i][4:]
puff_1 = [r for r in puff_0]
save(render(puff_0, PP, 2), "pufferfish_0.png")
save(render(puff_1, PP, 2), "pufferfish_1.png")

# ===================== LIONFISH (50x26) =====================
LP = {'.':None,'K':K,'R':(225,50,45,255),'D':(175,25,20,255),'W':(255,255,255,255),'Y':(255,202,40,255),'O':(255,112,67,255),'L':(255,130,120,255)}
lion_0 = [
"..................................................",
".......................KKKKKKKK..................",
".....................KKRRRRRRRRK.................",
"....................KRRRRRRRRRRRK................",
"...................KRRRRRRRRRRRRRK...............",
"..................KRRRRRRRRRRRRRRRK..............",
".................KRRRRRRRRRRRRRRRRRK.............",
"................KRRRRRRRRRRRRRRRRRRRK............",
"...............KRRRRRRRRRRRRRRRRRRRRRK...........",
"..............KRRRRRRRRRRRRRRRRRRRRRRRK..........",
".............KRRRRRRRRRRRRRRRRRRRRRRRRRK.........",
"............KRRRRRRRRRRRRRRRRRRRRRRRRRRRK........",
"...........KRRRRRRRRRRRRRRRRRRRRRRRRRRRRRK.......",
"..........KRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRK......",
".........KRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRK.....",
"........KRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRK....",
".......KRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRK...",
"......KRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRK..",
".....KRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRK.",
"....KRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRK",
"....KDDDDRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRK.",
"....KDDDDRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRK.",
"....KRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRK",
".....KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK.",
"..................................................",
"..................................................",
]
# stripes
for i in range(4,22):
    lion_0[i] = lion_0[i][:12] + "WWW" + lion_0[i][15:]
    lion_0[i] = lion_0[i][:20] + "WWW" + lion_0[i][23:]
    lion_0[i] = lion_0[i][:28] + "WWW" + lion_0[i][31:]
    lion_0[i] = lion_0[i][:36] + "WWW" + lion_0[i][39:]
# dorsal fins top
lion_0[0] = "..............YYYYYYYYYYYYYYYYYYYY.............."
lion_0[1] = ".............YYYYYYYYYYYYYYYYYYYYYY............."
lion_0[2] = "............YYYYYYYYYYYYYYYYYYYYYYYY............"
# pectoral fan
for i in range(14,20):
    lion_0[i] = lion_0[i][:10] + "OOO" + lion_0[i][13:]
# eye
lion_0[9]  = lion_0[9][:38] + "WWW" + lion_0[9][41:]
lion_0[10] = lion_0[10][:38] + "WKW" + lion_0[10][41:]
lion_0[11] = lion_0[11][:38] + "WWW" + lion_0[11][41:]
# tail left
for i in range(10,16):
    lion_0[i] = "KK..." + lion_0[i][5:]
lion_1 = [r for r in lion_0]
save(render(lion_0, LP, 2), "lionfish_0.png")
save(render(lion_1, LP, 2), "lionfish_1.png")

# ===================== MOORISH IDOL (48x22) =====================
MP = {'.':None,'K':K,'B':(20,20,20,255),'W':(255,255,255,255),'Y':(255,193,7,255),'L':(235,235,235,255)}
moor_0 = [
"................................................",
"...................KKKKKK.......................",
".................KKWWWWWWK......................",
"................KWWWWWWWWWK.....................",
"...............KWWWWWWWWWWWK....................",
"..............KWWWWWWWWWWWWWK...................",
".............KWWWWWWWWWWWWWWWK..................",
"............KWWWWWWWWWWWWWWWWWK.................",
"...........KWWWWWWWWWWWWWWWWWWWK................",
"..........KWWWWWWWWWWWWWWWWWWWWWK...............",
".........KWWWWWWWWWWWWWWWWWWWWWWWK..............",
"........KWWWWWWWWWWWWWWWWWWWWWWWWWK.............",
".......KWWWWWWWWWWWWWWWWWWWWWWWWWWWK............",
"......KWWWWWWWWWWWWWWWWWWWWWWWWWWWWWK...........",
".....KWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWK..........",
"....KWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWK.........",
"...KWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWK........",
"..KWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWK.......",
".KWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWK......",
"KWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWK.....",
"KBBBBWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWK....",
"KBBBBWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWK....",
]
# black bands
for i in range(4,22):
    moor_0[i] = moor_0[i][:10] + "BBBB" + moor_0[i][14:]
    moor_0[i] = moor_0[i][:20] + "BBBB" + moor_0[i][24:]
# yellow dorsal (elongated)
moor_0[0] = "..........YYYYYYYYYYYYYYYYYYYY.................."
moor_0[1] = ".........YYYYYYYYYYYYYYYYYYYYYY................."
moor_0[2] = "........YYYYYYYYYYYYYYYYYYYYYYYY................"
# snout
for i in range(10,14):
    moor_0[i] = moor_0[i][:38] + "WWWWWWWWWW" + moor_0[i][48:]
    moor_0[i] = moor_0[i][:38] + "BBBBBBBBBB" + moor_0[i][48:] if False else moor_0[i]
# eye
moor_0[8]  = moor_0[8][:30] + "WWW" + moor_0[8][33:]
moor_0[9]  = moor_0[9][:30] + "WKW" + moor_0[9][33:]
moor_0[10] = moor_0[10][:30] + "WWW" + moor_0[10][33:]
# tail left
for i in range(9,15):
    moor_0[i] = "KK...." + moor_0[i][6:]
moor_1 = [r for r in moor_0]
save(render(moor_0, MP, 2), "moorishidol_0.png")
save(render(moor_1, MP, 2), "moorishidol_1.png")

# ===================== ROYAL GRAMMA (40x20) =====================
RP = {'.':None,'K':K,'P':(123,31,162,255),'D':(74,20,140,255),'Y':(255,213,79,255),'L':(170,80,200,255),'W':(255,255,255,255)}
royal_0 = [
"........................................",
".................KKKKKK.................",
"...............KKPPPPPK.................",
"..............KPPPPPPPPK................",
".............KPPPPPPPPPPK...............",
"............KPPPPPPPPPPPPK..............",
"...........KPPPPPPPPPPPPPPK.............",
"..........KPPPPPPPPPPPPPPPPK............",
".........KPPPPPPPPPPPPPPPPPPK...........",
"........KPPPPPPPPPPPPPPPPPPPPK..........",
".......KPPPPPPPPPPPPPPPPPPPPPK..........",
"......KPPPPPPPPPPPPPPPPPPPPPPPK.........",
".....KPPPPPPPPPPPPPPPPPPPPPPPPPK........",
"....KPPPPPPPPPPPPPPPPPPPPPPPPPPPK.......",
"...KPPPPPPPPPPPPPPPPPPPPPPPPPPPPPK......",
"..KPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPK.....",
".KPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPK....",
"KPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPK...",
"KDDDDPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPK...",
"KDDDDPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPK...",
]
# yellow rear half
for i in range(6,20):
    for j in range(len(royal_0[i])):
        if j > 22 and royal_0[i][j] in 'PKD':
            pass
# simpler: replace cols 24-36 with Y in rows 6-18
for i in range(6,19):
    royal_0[i] = royal_0[i][:24] + "YYYYYYYYYYYY" + royal_0[i][36:]
# dorsal fin
royal_0[0] = "...........DDDDDDDDDDDDDDD.............."
royal_0[1] = "..........DDDDDDDDDDDDDDDDD............."
royal_0[2] = ".........DDDDDDDDDDDDDDDDDDD............"
# eye
royal_0[8]  = royal_0[8][:28] + "WWW" + royal_0[8][31:]
royal_0[9]  = royal_0[9][:28] + "WKW" + royal_0[9][31:]
royal_0[10] = royal_0[10][:28] + "WWW" + royal_0[10][31:]
# tail left
for i in range(8,14):
    royal_0[i] = "KK...." + royal_0[i][6:]
royal_1 = [r for r in royal_0]
save(render(royal_0, RP, 2), "royalgramma_0.png")
save(render(royal_1, RP, 2), "royalgramma_1.png")

# ===================== KOI (50x22) =====================
KP = {'.':None,'K':K,'O':(255,138,101,255),'D':(216,67,21,255),'W':(255,255,255,255),'R':(191,54,12,255),'Y':(255,202,40,255),'L':(255,171,145,255)}
koi_0 = [
"..................................................",
".....................KKKKKK.......................",
"...................KKOOOOOOK......................",
"..................KOOOOOOOOOK.....................",
".................KOOOOOOOOOOOK....................",
"................KOOOOOOOOOOOOOK...................",
"...............KOOOOOOOOOOOOOOOK..................",
"..............KOOOOOOOOOOOOOOOOOK.................",
".............KOOOOOOOOOOOOOOOOOOOK................",
"............KOOOOOOOOOOOOOOOOOOOOOK...............",
"...........KOOOOOOOOOOOOOOOOOOOOOOOK..............",
"..........KOOOOOOOOOOOOOOOOOOOOOOOOOK.............",
".........KOOOOOOOOOOOOOOOOOOOOOOOOOOOK............",
"........KOOOOOOOOOOOOOOOOOOOOOOOOOOOOOK...........",
".......KOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOK..........",
"......KOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOK.........",
".....KOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOK.........",
"....KOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOK..........",
"...KOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOK..........",
"..KOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOK...........",
".KOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOK............",
"KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK............",
]
# white patches
for i in range(6,16):
    koi_0[i] = koi_0[i][:16] + "WWWWWW" + koi_0[i][22:]
for i in range(8,18):
    koi_0[i] = koi_0[i][:34] + "WWWWWW" + koi_0[i][40:]
# red patch
for i in range(10,18):
    koi_0[i] = koi_0[i][:24] + "RRRRRR" + koi_0[i][30:]
# dorsal fin
koi_0[0] = "......................RRRRRR......................"
koi_0[1] = ".....................RRRRRRRR....................."
koi_0[2] = "....................RRRRRRRRRR...................."
# tail left
for i in range(9,15):
    koi_0[i] = "KK...." + koi_0[i][6:]
# eye
koi_0[8]  = koi_0[8][:38] + "WWW" + koi_0[8][41:]
koi_0[9]  = koi_0[9][:38] + "WKW" + koi_0[9][41:]
koi_0[10] = koi_0[10][:38] + "WWW" + koi_0[10][41:]
koi_1 = [r for r in koi_0]
save(render(koi_0, KP, 2), "koi_0.png")
save(render(koi_1, KP, 2), "koi_1.png")

# ===================== GOLDFISH (40x22) =====================
GP = {'.':None,'K':K,'Y':(255,202,40,255),'D':(249,168,37,255),'W':(255,255,255,255),'R':(229,57,53,255),'L':(255,236,179,255)}
gold_0 = [
"........................................",
"...................KKKKKK...............",
".................KKYYYYYK...............",
"................KYYYYYYYYK..............",
"...............KYYYYYYYYYYK.............",
"..............KYYYYYYYYYYYYK............",
".............KYYYYYYYYYYYYYYK...........",
"............KYYYYYYYYYYYYYYYYK..........",
"...........KYYYYYYYYYYYYYYYYYYK.........",
"..........KYYYYYYYYYYYYYYYYYYYYK........",
".........KYYYYYYYYYYYYYYYYYYYYYK.......",
"........KYYYYYYYYYYYYYYYYYYYYYYYK.......",
".......KYYYYYYYYYYYYYYYYYYYYYYYYK......",
"......KYYYYYYYYYYYYYYYYYYYYYYYYYK......",
".....KYYYYYYYYYYYYYYYYYYYYYYYYYYK......",
"....KYYYYYYYYYYYYYYYYYYYYYYYYYYYK......",
"...KYYYYYYYYYYYYYYYYYYYYYYYYYYYYK......",
"..KYYYYYYYYYYYYYYYYYYYYYYYYYYYYYK......",
".KYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYK......",
"KYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYK......",
"KDDDDYYYYYYYYYYYYYYYYYYYYYYYYYYYK......",
"KDDDDYYYYYYYYYYYYYYYYYYYYYYYYYYYK......",
]
for i in range(6,16):
    gold_0[i] = gold_0[i][:14] + "WWWW" + gold_0[i][18:]
poly_rows = [0,1,2]
for r in poly_rows:
    gold_0[r] = "...................DDDDDD..............."
gold_0[0] = "...................DDDDDD..............."
gold_0[1] = "..................DDDDDDDD.............."
gold_0[2] = ".................DDDDDDDDDD............."
# tail left
for i in range(8,14):
    gold_0[i] = "KK...." + gold_0[i][6:]
# eye
gold_0[8]  = gold_0[8][:26] + "WWW" + gold_0[8][29:]
gold_0[9]  = gold_0[9][:26] + "WKW" + gold_0[9][29:]
gold_0[10] = gold_0[10][:26] + "WWW" + gold_0[10][29:]
gold_1 = [r for r in gold_0]
save(render(gold_0, GP, 2), "goldfish_0.png")
save(render(gold_1, GP, 2), "goldfish_1.png")

# ===================== TROPICAL (40x20) =====================
TrP = {'.':None,'K':K,'G':(0,230,118,255),'D':(0,137,123,255),'P':(255,64,129,255),'W':(255,255,255,255),'L':(100,255,180,255)}
trop_0 = [
"........................................",
"...................KKKKKK...............",
".................KGGGGGGK...............",
"................KGGGGGGGGK..............",
"...............KGGGGGGGGGGK.............",
"..............KGGGGGGGGGGGGK............",
".............KGGGGGGGGGGGGGGK...........",
"............KGGGGGGGGGGGGGGGGK..........",
"...........KGGGGGGGGGGGGGGGGGGK.........",
"..........KGGGGGGGGGGGGGGGGGGGGK........",
".........KGGGGGGGGGGGGGGGGGGGGGGK.......",
"........KGGGGGGGGGGGGGGGGGGGGGGGGK......",
".......KGGGGGGGGGGGGGGGGGGGGGGGGGK.....",
"......KGGGGGGGGGGGGGGGGGGGGGGGGGGK.....",
".....KGGGGGGGGGGGGGGGGGGGGGGGGGGGK.....",
"....KGGGGGGGGGGGGGGGGGGGGGGGGGGGGK.....",
"...KGGGGGGGGGGGGGGGGGGGGGGGGGGGGGK.....",
"..KGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGK.....",
".KGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGK.....",
"KGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGK.....",
"KDDDDGGGGGGGGGGGGGGGGGGGGGGGGGGGGK.....",
"KDDDDGGGGGGGGGGGGGGGGGGGGGGGGGGGGK.....",
]
for i in range(6,20):
    trop_0[i] = trop_0[i][:12] + "PPP" + trop_0[i][15:]
    trop_0[i] = trop_0[i][:18] + "PPP" + trop_0[i][21:]
    trop_0[i] = trop_0[i][:24] + "PPP" + trop_0[i][27:]
# dorsal fin
trop_0[0] = ".............PPPPPPPPPP................."
trop_0[1] = "............PPPPPPPPPPPP................"
trop_0[2] = "...........PPPPPPPPPPPPPP..............."
# tail left
for i in range(8,14):
    trop_0[i] = "KK...." + trop_0[i][6:]
# eye
trop_0[8]  = trop_0[8][:24] + "WWW" + trop_0[8][27:]
trop_0[9]  = trop_0[9][:24] + "WKW" + trop_0[9][27:]
trop_0[10] = trop_0[10][:24] + "WWW" + trop_0[10][27:]
trop_1 = [r for r in trop_0]
save(render(trop_0, TrP, 2), "tropical_0.png")
save(render(trop_1, TrP, 2), "tropical_1.png")

# ===================== EXOTIC (44x22) =====================
EP = {'.':None,'K':K,'V':(224,64,251,255),'D':(123,31,162,255),'C':(0,229,255,255),'W':(255,255,255,255),'L':(235,120,255,255)}
exo_0 = [
"............................................",
"...................KKKKKK...................",
".................KVVVVVVK...................",
"................KVVVVVVVVK..................",
"...............KVVVVVVVVVVK.................",
"..............KVVVVVVVVVVVVK................",
".............KVVVVVVVVVVVVVVK...............",
"............KVVVVVVVVVVVVVVVVK..............",
"...........KVVVVVVVVVVVVVVVVVVK.............",
"..........KVVVVVVVVVVVVVVVVVVVVK............",
".........KVVVVVVVVVVVVVVVVVVVVVVK...........",
"........KVVVVVVVVVVVVVVVVVVVVVVVVK..........",
".......KVVVVVVVVVVVVVVVVVVVVVVVVVVK.........",
"......KVVVVVVVVVVVVVVVVVVVVVVVVVVVVK........",
".....KVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVK.......",
"....KVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVK......",
"...KVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVK.....",
"..KVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVK....",
".KVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVK...",
"KVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVK..",
"KDDDDVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVK..",
"KDDDDVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVK..",
]
# cyan spot
for i in range(8,16):
    exo_0[i] = exo_0[i][:16] + "CCCCCC" + exo_0[i][22:]
# dorsal fins
exo_0[0] = ".............CCCCCCCCCCCC...................."
exo_0[1] = "............CCCCCCCCCCCCCCC.................."
exo_0[2] = "...........CCCCCCCCCCCCCCCCC................."
# tail left
for i in range(9,15):
    exo_0[i] = "KK...." + exo_0[i][6:]
# eye
exo_0[8]  = exo_0[8][:32] + "WWW" + exo_0[8][35:]
exo_0[9]  = exo_0[9][:32] + "WKW" + exo_0[9][35:]
exo_0[10] = exo_0[10][:32] + "WWW" + exo_0[10][35:]
exo_1 = [r for r in exo_0]
save(render(exo_0, EP, 2), "exotic_0.png")
save(render(exo_1, EP, 2), "exotic_1.png")

# ===================== SMALL REEF (28x16) =====================
SP = {'.':None,'K':K,'C':(38,198,218,255),'D':(0,131,143,255),'Y':(255,238,88,255),'W':(255,255,255,255),'L':(100,220,230,255)}
small_0 = [
"............................",
"...........KKKKKK...........",
".........KKCCCCCCCK.........",
"........KCCCCCCCCCCCK.......",
".......KCCCCCCCCCCCCCK......",
"......KCCCCCCCCCCCCCCCK.....",
".....KCCCCCCCCCCCCCCCCCK....",
"....KCCCCCCCCCCCCCCCCCCCK...",
"....KCCCCCCCCCCCCCCCCCCCK...",
"....KCCCCCCCCCCCCCCCCCCCK...",
".....KCCCCCCCCCCCCCCCCCK....",
"......KCCCCCCCCCCCCCCCK.....",
".......KCCCCCCCCCCCCCK......",
"........KCCCCCCCCCCCCCK.....",
".........KCCCCCCCCCCCCCK....",
"..........KKKKKKKKKKKK......",
]
for i in range(4,12):
    small_0[i] = small_0[i][:14] + "YYY" + small_0[i][17:]
# dorsal fin
small_0[0] = "...........YYYY............."
small_0[1] = "..........YYYYY............"
small_0[2] = ".........YYYYYYY..........."
# tail left
for i in range(6,10):
    small_0[i] = "KK.." + small_0[i][4:]
# eye
small_0[6] = small_0[6][:18] + "WWW" + small_0[6][21:]
small_0[7] = small_0[7][:18] + "WKW" + small_0[7][21:]
small_0[8] = small_0[8][:18] + "WWW" + small_0[8][21:]
small_1 = [r for r in small_0]
save(render(small_0, SP, 2), "smallreef_0.png")
save(render(small_1, SP, 2), "smallreef_1.png")

# ===================== TURTLE (54x34) =====================
TuP = {'.':None,'K':K,'G':(46,125,50,255),'D':(27,94,32,255),'L':(102,187,106,255),'Y':(255,241,118,255)}
turtle_0 = [
"......................................................",
".....................KKKKKKKKKK.......................",
"...................KGGGGGGGGGGGK......................",
"..................KGGGGGGGGGGGGGK.....................",
".................KGGGGGGGGGGGGGGGGK....................",
"................KGGGGGGGGGGGGGGGGGGK...................",
"...............KGGGGGGGGGGGGGGGGGGGGK..................",
"..............KGGGGGGGGGGGGGGGGGGGGGGK.................",
".............KGGGGGGGGGGGGGGGGGGGGGGGGK................",
"............KGGGGGGGGGGGGGGGGGGGGGGGGGGK...............",
"...........KGGGGGGGGGGGGGGGGGGGGGGGGGGGGK..............",
"..........KGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGK.............",
".........KGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGK............",
"........KGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGK...........",
".......KGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGK..........",
"......KGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGK.........",
".....KGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGK........",
"....KGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGK.......",
"...KGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGK......",
"..KGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGK.....",
".KGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGK....",
"KGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGK...",
"KDDDDGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGK...",
"KDDDDGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGK...",
"KGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGK...",
".KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK....",
"......................................................",
"......................................................",
"......................................................",
"......................................................",
"......................................................",
"......................................................",
"......................................................",
]
# scute lines
for i in range(6,24):
    turtle_0[i] = turtle_0[i][:27] + "D" + turtle_0[i][28:]
    turtle_0[i] = turtle_0[i][:18] + "D" + turtle_0[i][19:]
    turtle_0[i] = turtle_0[i][:36] + "D" + turtle_0[i][37:]
turtle_0[15] = "K" + "G"*12 + "D" + "G"*12 + "D" + "G"*12 + "D" + "G"*12 + "K" + "."*8
# head
for i in range(14,22):
    turtle_0[i] = turtle_0[i][:46] + "LLLL" + turtle_0[i][50:]
# eye
turtle_0[16] = turtle_0[16][:49] + "KK" + turtle_0[16][51:]
turtle_0[17] = turtle_0[17][:49] + "KK" + turtle_0[17][51:]
# flippers (left)
turtle_0[8]  = "LLLL" + turtle_0[8][4:]
turtle_0[9]  = "LLLL" + turtle_0[9][4:]
turtle_0[10] = "LLLL" + turtle_0[10][4:]
turtle_0[20] = "LLLL" + turtle_0[20][4:]
turtle_0[21] = "LLLL" + turtle_0[21][4:]
turtle_0[22] = "LLLL" + turtle_0[22][4:]
# right flippers
for i in range(8,13):
    turtle_0[i] = turtle_0[i][:50] + "LLLL"
for i in range(20,23):
    turtle_0[i] = turtle_0[i][:50] + "LLLL"
turtle_1 = [r for r in turtle_0]
save(render(turtle_0, TuP, 2), "turtle_0.png")
save(render(turtle_1, TuP, 2), "turtle_1.png")

# Environment sprites (reuse previous good ones by regenerating via PIL is separate; skip here)
print("FISH DONE")
