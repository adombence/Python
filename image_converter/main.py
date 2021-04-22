from PIL import Image
import glob
import os.path

for count, filename in enumerate(glob.glob('input/**/*.*', recursive=True), start=1):
    if ".svg" not in filename:
        path = os.path.dirname(filename)
        # os.path.relpath(path, 'input')
        # print(path)
        im = Image.open(filename)
        # opacity
        # im.putalpha(128)
        # rgba
        # webp_im = im.convert('RGBA')
        # rgb formátum a jpg-hez
        jpeg_im = im.convert('RGB')
        # átméretezés
        # width, height = rgb_im.size
        # rgb_im = rgb_im.resize((width//6, height//6))
        # webp_im.save(('output/img_webp_' + str(count) + '.webp'), quality=75)
        jpeg_im.save(('output/img_jpg_' + str(count) + '.jpg'), quality=100)
        print(count, filename)
