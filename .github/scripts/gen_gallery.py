import os
from PIL import Image

SPR = "D:/schools/supergigachadsupreme300/aquarium/assets/sprites"
OUT = "D:/schools/supergigachadsupreme300/aquarium/assets/ui"
os.makedirs(OUT, exist_ok=True)

species = ['smallreef', 'clownfish', 'bluetang']
# Build gallery: each species 2 frames, native + 4x enlarged
cell_w = 260
cell_h = 120
cols = 3
rows = len(species)
sheet = Image.new("RGBA", (cols*cell_w, rows*cell_h), (24,32,48,255))
for i, s in enumerate(species):
    for f in (0,1):
        p = os.path.join(SPR, f"{s}_{f}.png")
        im = Image.open(p).convert("RGBA")
        # native at left
        x0 = 0*cell_w + 10
        # enlarged 3x
        big = im.resize((im.width*3, im.height*3), Image.NEAREST)
        x1 = 1*cell_w + (cell_w - big.width)//2
        x2 = 2*cell_w + (cell_w - big.width)//2
        y = i*cell_h + (cell_h - im.height)//2
        yb = i*cell_h + (cell_h - big.height)//2
        sheet.paste(im, (x0, y), im)
        sheet.paste(big, (x1, yb), big)
        sheet.paste(big, (x2, yb), big) if f==1 else None
# Actually simpler: col0 native frame0, col1 3x frame0, col2 3x frame1
# redo cleanly
sheet = Image.new("RGBA", (cols*cell_w, rows*cell_h), (24,32,48,255))
for i, s in enumerate(species):
    im0 = Image.open(os.path.join(SPR, f"{s}_0.png")).convert("RGBA")
    im1 = Image.open(os.path.join(SPR, f"{s}_1.png")).convert("RGBA")
    big0 = im0.resize((im0.width*3, im0.height*3), Image.NEAREST)
    big1 = im1.resize((im1.width*3, im1.height*3), Image.NEAREST)
    y = i*cell_h
    sheet.paste(im0, (10, y + (cell_h-im0.height)//2), im0)
    sheet.paste(big0, (cell_w + (cell_w-big0.width)//2, y + (cell_h-big0.height)//2), big0)
    sheet.paste(big1, (2*cell_w + (cell_w-big1.width)//2, y + (cell_h-big1.height)//2), big1)
sheet.save(os.path.join(OUT, "fish_gallery_3.png"))
print("saved fish_gallery_3.png", sheet.size)
