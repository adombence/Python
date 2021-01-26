from PIL import Image
import glob

for count, filename in enumerate(glob.glob('input/*.*'), start=1):
    im = Image.open(filename)
    rgb_im = im.convert('RGBA')
    rgb_im.save(('output/img' + str(count) + '.webp'), quality=75)
    print(count, filename)
