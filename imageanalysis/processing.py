from PIL import Image

im = Image.open("_7521705.jpg")
print im.format, im.size, im.mode
l = im.getcolors(im.size[0]*im.size[1])
n = len(l)
for index, item in enumerate(l):
  print index, item

#f = open('_7521705_swatch_colors.txt', 'w')
#f.write(str(s))