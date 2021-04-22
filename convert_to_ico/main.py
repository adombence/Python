from PIL import Image
import glob

for count, filename in enumerate(glob.glob('input/*.*'), start=1):
    img = Image.open(filename)
    # icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]
    # img.save('logo.ico', sizes=icon_sizes)
    img.save('output/logo.ico')
