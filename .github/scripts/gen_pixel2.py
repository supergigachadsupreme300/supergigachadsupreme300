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

# Palettes
P_CLOWN = {'.':None,'K':(18,18,24,255),'O':(255,109,50,255),'D':(195,55,20,255),'W':(255,255,255,255),'G':(225,225,225,255),'Y':(255,193,7,255),'L':(255,165,120,255)}
P_TANG  = {'.':None,'K':(18,18,24,255),'B':(30,120,220,255),'D':(12,60,150,255),'Y':(255,230,59,255),'L':(110,175,245,255),'W':(255,255,255,255)}
P_ANGEL = {'.':None,'K':(18,18,24,255),'P':(240,130,175,255),'D':(190,20,85,255),'Y':(255,230,59,255),'L':(248,180,205,255),'W':(255,255,255,255)}
P_BUTTER= {'.':None,'K':(18,18,24,255),'Y':(255,230,59,255),'D':(245,160,30,255),'B':(26,35,126,255),'O':(255,143,0,255),'W':(255,255,255,255),'L':(255,245,190,255)}
P_PUFFER= {'.':None,'K':(18,18,24,255),'Y':(255,245,157,255),'D':(185,195,45,255),'P':(244,143,177,255),'W':(255,255,255,255),'G':(93,64,55,255),'L':(255,255,225,255)}
P_LION  = {'.':None,'K':(18,18,24,255),'R':(225,50,45,255),'D':(175,25,20,255),'W':(255,255,255,255),'Y':(255,202,40,255),'O':(255,112,67,255),'L':(255,130,120,255)}
P_MOOR  = {'.':None,'K':(18,18,24,255),'B':(20,20,20,255),'W':(255,255,255,255),'Y':(255,193,7,255),'L':(235,235,235,255)}
P_ROYAL = {'.':None,'K':(18,18,24,255),'P':(123,31,162,255),'D':(74,20,140,255),'Y':(255,213,79,255),'L':(170,80,200,255),'W':(255,255,255,255)}
P_KOI   = {'.':None,'K':(18,18,24,255),'O':(255,138,101,255),'D':(216,67,21,255),'W':(255,255,255,255),'R':(191,54,12,255),'Y':(255,202,40,255),'L':(255,171,145,255)}
P_GOLD  = {'.':None,'K':(18,18,24,255),'Y':(255,202,40,255),'D':(249,168,37,255),'W':(255,255,255,255),'R':(229,57,53,255),'L':(255,236,179,255)}
P_TROP  = {'.':None,'K':(18,18,24,255),'G':(0,230,118,255),'D':(0,137,123,255),'P':(255,64,129,255),'W':(255,255,255,255),'L':(100,255,180,255)}
P_EXOTIC= {'.':None,'K':(18,18,24,255),'V':(224,64,251,255),'D':(123,31,162,255),'C':(0,229,255,255),'W':(255,255,255,255),'L':(235,120,255,255)}
P_SMALL = {'.':None,'K':(18,18,24,255),'C':(38,198,218,255),'D':(0,131,143,255),'Y':(255,238,88,255),'W':(255,255,255,255),'L':(100,220,230,255)}
P_TURTLE= {'.':None,'K':(18,18,24,255),'G':(46,125,50,255),'D':(27,94,32,255),'L':(102,187,106,255),'Y':(255,241,118,255)}

# ---- Clownfish (48x22) ----
clown_0 = [
"................................................",
"...................KKKKKK.......................",
".................KKOOOOOOK......................",
"................KOOOOOOOOOK.....................",
"...............KOOOOOOOOOOOK....................",
"..............KOOOOOOOOOOOOOK...................",
".............KOOOOOOOOOOOOOOOK..................",
"............KOOOOOOOOOOOOOOOOOK.................",
"...........KOOOOOOOOOOOOOOOOOOOK................",
"..........KOOOOOOOOOOOOOOOOOOOOOK...............",
"..........KWWWOOOOOOOOOOOOOOOOOOK...............",
".........KWWWOOOOOOOOOOOOOOOOOOOK..............",
".........KWWWOOOOOOOOOOOOOOOOOOOK..............",
"..........KOOOOOOOOOOOOOOOOOOOOOK...............",
"...........KOOOOOOOOOOOOOOOOOOOK................",
"............KOOOOOOOOOOOOOOOOOK.................",
".............KOOOOOOOOOOOOOOOK..................",
"..............KOOOOOOOOOOOOOK...................",
"...............KOOOOOOOOOOOK....................",
"................KKKKKKKKKKK.....................",
"................................................",
"................................................",
]
# Add tail (left) and dorsal fin by replacing rows 0-2 and leftmost cols
# We'll instead build final via post-processing not possible; include in grid:
# Tail: rows 8-12, cols 0-6 forked. Dorsal: rows 0-3, cols 20-30.
# Let's insert tail into rows 8-12 (prepend K/O) and dorsal into top rows.
# Simpler: keep grid body only and add tail/fin as extra in same grid by widening:
# We'll just save body grid; tail/fin drawn in environment? No, fish needs them.
# Instead, manually edit rows to include tail on left and fin on top.
clown_0 = [
".....................KKKKKK.....................",
"...................KKOOOOOOK....................",
".................KKOOOOOOOOOK...................",
"................KOOOOOOOOOOOOK..................",
"...............KOOOOOOOOOOOOOOK.................",
"..............KOOOOOOOOOOOOOOOOK................",
".............KOOOOOOOOOOOOOOOOOOK...............",
"............KOOOOOOOOOOOOOOOOOOOOK..............",
".....KK...KWWWOOOOOOOOOOOOOOOOOOOK.............",
"....KOOOK.KWWWOOOOOOOOOOOOOOOOOOOOK............",
"....KOOOK.KWWWOOOOOOOOOOOOOOOOOOOOK............",
".....KK...KOOOOOOOOOOOOOOOOOOOOOOK.............",
"............KOOOOOOOOOOOOOOOOOOOOK..............",
".............KOOOOOOOOOOOOOOOOOOK...............",
"..............KOOOOOOOOOOOOOOOOK................",
"...............KOOOOOOOOOOOOOOK.................",
"................KOOOOOOOOOOOOK..................",
".................KKOOOOOOOOK....................",
"...................KKKKKK.......................",
"................................................",
"................................................",
"................................................",
]
# dorsal fin: add to rows 0-2 above body (cols 18-28)
clown_0[0] = "...................YYYYY......................."
clown_0[1] = "..................YYYYYYY......................"
clown_0[2] = ".................YYYYYYYYY....................."
# pectoral fin rows 12-14
clown_0[12] = clown_0[12][:18] + "Y" + clown_0[12][19:]
# tail fork left rows 8-12 already have ".....KK" etc; ok

clown_1 = [row for row in clown_0]  # same shape, tail slightly up
clown_1[8]  = ".....KK...KWWWOOOOOOOOOOOOOOOOOOOK............."
clown_1[9]  = "....KOOOK.KWWWOOOOOOOOOOOOOOOOOOOOK............"
clown_1[10] = "....KOOOK.KWWWOOOOOOOOOOOOOOOOOOOOK............"
clown_1[11] = ".....KK...KOOOOOOOOOOOOOOOOOOOOOOK............."

save(render(clown_0, P_CLOWN, 2), "clownfish_0.png")
save(render(clown_1, P_CLOWN, 2), "clownfish_1.png")
print("clownfish done")
