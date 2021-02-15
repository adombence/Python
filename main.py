from PIL import Image
from PIL import ImageFilter
import glob

for count, filename in enumerate(glob.glob('input/*.*'), start=1):
    im = Image.open(filename)
    blurred_image = im.filter(ImageFilter.BoxBlur(10))
    # blurred_image.show()
    rgb_im = blurred_image.convert('RGBA')
    rgb_im.save(('output/img' + str(count) + '.webp'), quality=75)
    print(count, filename)
