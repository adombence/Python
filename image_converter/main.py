from PIL import Image
import glob

for count, filename in enumerate(glob.glob('input/*.*'), start=1):
    im = Image.open(filename)
    #opacity
    #im.putalpha(128)
    #rgba
    rgb_im = im.convert('RGBA')
    #átméretezés
    #width, height = rgb_im.size
    #rgb_im = rgb_im.resize((width//6, height//6))
    rgb_im.save(('output/img' + str(count) + '.webp'), quality=75)
    print(count, filename)
