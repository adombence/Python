from PIL import Image
from pathlib import Path
import glob
import os.path

for count, filename in enumerate(glob.glob('input/**/*.*', recursive=True), start=1):
    if ".svg" not in filename:
        im = Image.open(filename)
        # Opacity
        # im.putalpha(128)
        # Rgba
        webp_im = im.convert('RGBA')
        # Rgb formátum a jpg-hez
        jpeg_im = im.convert('RGB')
        # Átméretezés
        # width, height = rgb_im.size
        # rgb_im = rgb_im.resize((width//6, height//6))
        # Mappa másolás
        path = filename.split('\\')
        path.pop(0)
        out_path = ''
        i = 0
        back_slash = '\\'
        while i < len(path):
            if i < (len(path) - 1):
                out_path = out_path + path[i] + back_slash
            i += 1
        # Ha nem létezik a mappa, akkor létrehozza
        Path('output/' + out_path).mkdir(parents=True, exist_ok=True)
        # Tényleges mentés
        webp_im.save(('output/' + out_path + 'img_webp_' + str(count) + '.webp'), quality=75)
        jpeg_im.save(('output/' + out_path + 'img_jpg_' + str(count) + '.jpg'), quality=100)
        # Sima mentés
        # webp_im.save(('output/img_webp_' + str(count) + '.webp'), quality=75)
        # jpeg_im.save(('output/img_jpg_' + str(count) + '.jpg'), quality=100)
        print(count, filename)
