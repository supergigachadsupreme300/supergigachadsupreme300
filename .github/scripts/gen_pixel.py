import os
from PIL import Image

OUT = "D:/schools/supergigachadsupreme300/aquarium/assets/sprites"
os.makedirs(OUT, exist_ok=True)

def render_grid(grid, palette, scale=1):
    """grid: list of strings; palette: dict char->(r,g,b,a) or None for transparent."""
    h = len(grid)
    w = max(len(row) for row in grid)
    img = Image.new("RGBA", (w*scale, h*scale), (0,0,0,0))
    px = img.load()
    for y, row in enumerate(grid):
        for x, ch in enumerate(row):
            col = palette.get(ch)
            if col is None:
                continue
            for sy in range(scale):
                for sx in range(scale):
                    px[x*scale+sx, y*scale+sy] = col
    return img

def save(img, name):
    img.save(os.path.join(OUT, name), "PNG")
    print("saved", name)

# ---- Clownfish: compact oval, orange body, 3 white bands ----
CLOWN_PALETTE = {
    '.': None,
    'K': (20,20,24,255),
    'O': (255,109,50,255),
    'D': (200,60,20,255),
    'W': (255,255,255,255),
    'G': (230,230,230,255),
    'Y': (255,193,7,255),
    'L': (255,160,120,255),
}
clownfish_0 = [
"................................................",
"................KKKKKK..........................",
"..............KKOOOOOOK.........................",
".............KOOOOOOOOOK........................",
"............KOOOOOOOOOOOK.......................",
"...........KOOOOOOOOOOOOOK......................",
"..........KOOOOOOOOOOOOOOOK.....................",
".........KOOOOOOOOOOOOOOOOOK....................",
".........KWWWOOOOOOOOOOOOOOOK...................",
"........KWWWOOOOOOOOOOOOOOOOOK..................",
"........KWWWOOOOOOOOOOOOOOOOOK..................",
"........KOOOOOOOOOOOOOOOOOOOOK..................",
".........KOOOOOOOOOOOOOOOOOOOK..................",
"..........KOOOOOOOOOOOOOOOOOK...................",
"...........KOOOOOOOOOOOOOOOK....................",
"............KOOOOOOOOOOOOOK.....................",
".............KOOOOOOOOOOOK......................",
"..............KOOOOOOOOK........................",
"...............KKKKKK...........................",
"................................................",
]
clownfish_1 = [
"................................................",
"................KKKKKK..........................",
"..............KKOOOOOOK.........................",
".............KOOOOOOOOOK........................",
"............KOOOOOOOOOOOK.......................",
"...........KOOOOOOOOOOOOOK......................",
"..........KOOOOOOOOOOOOOOOK.....................",
".........KOOOOOOOOOOOOOOOOOK....................",
".........KWWWOOOOOOOOOOOOOOOK...................",
"........KWWWOOOOOOOOOOOOOOOOOK..................",
"........KWWWOOOOOOOOOOOOOOOOOK..................",
"........KOOOOOOOOOOOOOOOOOOOOK..................",
".........KOOOOOOOOOOOOOOOOOOOK..................",
"..........KOOOOOOOOOOOOOOOOOK...................",
"...........KOOOOOOOOOOOOOOOK....................",
"............KOOOOOOOOOOOOOK.....................",
".............KOOOOOOOOOOOK......................",
"..............KOOOOOOOOK........................",
"...............KKKKKK...........................",
"................................................",
]
# add dorsal fin + tail via overlay not in grid; we'll draw fins separately? 
# Instead include them in grid by extending. Let's instead add tail to left and fin on top by editing rows:
# We'll post-process: add tail columns 0-4 and dorsal fin rows 0-2.
def add_tail_fin(grid, tail_up=False):
    # grid is list of strings; we prepend a tail fork on the left and a dorsal fin on top
    h = len(grid)
    w = max(len(r) for r in grid)
    # build new grid with 6 extra cols left and 4 extra rows top
    new = []
    # top fin rows
    fin_rows = [
        "......" + "."*w,
        ".....Y" + "."*w,
        "....YY" + "."*w,
    ]
    # Actually we'll just return grid unchanged to keep alignment; tail already in body outline left
    return grid

# Save clownfish (scale 3x for crispness)
img0 = render_grid(clownfish_0, CLOWN_PALETTE, 3)
img1 = render_grid(clownfish_1, CLOWN_PALETTE, 3)
# Add tail + dorsal fin manually via draw on larger canvas
from PIL import ImageDraw
def add_fins(img, tail_up=False):
    d = ImageDraw.Draw(img)
    # tail fork on left
    # find body leftmost non-transparent
    # draw a small fork
    w,h = img.size
    # tail: dark orange fork at left center
    import math
    cy = h//2
    for off in (-6,0,6):
        d.line([(2,cy+off),(10,cy)], fill=(200,60,20,255), width=2)
    # dorsal fin on top
    d.polygon([(w//2-10, 8),(w//2, 0),(w//2+10, 8)], fill=(255,193,7,255), outline=(20,20,24,255))
    return img
img0 = add_fins(img0, False)
img1 = add_fins(img1, True)
save(img0, "clownfish_0.png")
save(img1, "clownfish_1.png")
print("clownfish done")
