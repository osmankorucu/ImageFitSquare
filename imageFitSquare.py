from PIL import Image
import sys
from pathlib import Path
if len(sys.argv) < 2:
    print("Lutfen parametre olarak resim veriniz")
else:
    file_path = " "
    file_path = file_path.join(sys.argv[1:])
    file_path = str.strip(file_path)
    paths = Path(file_path).glob('**/*')
    i=0
    for im in paths:
        print(im)
        image = Image.open(im)
        #print(im+"/n")
        min_size=1000
        fill_color=(256, 256, 256, 255)
        x, y = image.size
        size = max(min_size, x, y)
        new_image = Image.new('RGBA', (size, size), fill_color)
        new_image.paste(image, (int((size - x) / 2), int((size - y) / 2)))
        new_size = (1000, 1000)
        new_image.resize(new_size, Image.ANTIALIAS)
        new_image.save(str(i)+".png")
        i+=1
