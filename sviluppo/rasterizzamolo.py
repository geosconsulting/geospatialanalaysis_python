__author__ = 'Fabio'
import shapefile
import fpdf
from PIL import Image,ImageDraw
r=shapefile.Reader("../dati/hancock.shp")
xdist = r.bbox[2] - r.bbox[0]
ydist = r.bbox[3] - r.bbox[1]
iwidth  = 400
iheight = 600
xratio = iwidth/xdist
yratio = iheight/ydist
pixels =[]
for x,y in r.shapes()[0].points:
    px = int(iwidth - ((r.bbox[2] -x)*xratio))
    py = int(iwidth - ((r.bbox[3] -y)*yratio))
    pixels.append((px,py))

img = Image.new("RGB",(iwidth,iheight),"white")
draw = ImageDraw.Draw(img)
draw.polygon(pixels,outline="rgb(203,196,190)",fill="rgb(198,204,189)")
img.save("../dati/hancock.png")
pdf = fpdf.FPDF("P","mm","A4")
pdf.add_page()
pdf.set_font("Arial","B",20)
pdf.cell(160,25,"Hancock County blab bla",border=0,align="C")
pdf.image("../dati/hancock.png",25,50,150,160)
pdf.output("../dati/mappa.pdf","F")