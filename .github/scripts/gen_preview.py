import os
from PIL import Image

SPR = "D:/schools/supergigachadsupreme300/aquarium/assets/sprites"
OUT = "D:/schools/supergigachadsupreme300/aquarium/assets/ui"
os.makedirs(OUT, exist_ok=True)

species = ['clownfish','bluetang','angelfish','butterflyfish','pufferfish','lionfish',
           'moorishidol','royalgramma','koi','goldfish','tropical','exotic','smallreef','turtle']

imgs = []
for s in species:
    for f in (0,1):
        p = os.path.join(SPR, f"{s}_{f}.png")
        if os.path.exists(p):
            imgs.append((s, f, Image.open(p).convert("RGBA")))

# Build grid: 7 per row
cols = 7
rows = (len(imgs)+cols-1)//cols
# cell size
cell_w = max(im.width for _,_,im in imgs) + 20
cell_h = max(im.height for _,_,im in imgs) + 20
sheet = Image.new("RGBA", (cols*cell_w, rows*cell_h), (30,40,60,255))
for i,(s,f,im) in enumerate(imgs):
    r,c = divmod(i, cols)
    x = c*cell_w + (cell_w-im.width)//2
    y = r*cell_h + (cell_h-im.height)//2
    sheet.paste(im, (x,y), im)
sheet.save(os.path.join(OUT, "fish_preview_sheet.png"))
print("saved fish_preview_sheet.png", sheet.size)
