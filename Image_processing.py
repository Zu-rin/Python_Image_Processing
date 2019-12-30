from PIL import Image
import PIL
import numpy as np
import sys
import pprint

def image_type_check(img):
    if not isinstance(img, (PIL.JpegImagePlugin.JpegImageFile, PIL.Image.Image)):
        raise TypeError("Type of [img] must be <class 'PIL.*'>")

def Enlarge(img, h, w):
    image_type_check(img)
    newimg = img.resize((int(img.width * w), int(img.height * h)), Image.LANCZOS)
    return newimg

def End_value_smooth(img):
    image_type_check(img)
    noise = 20
    width, height = img.size
    for y in range(height):
        for x in range(width):
            if max(img.getpixel((x, y))) < noise:
                img.putpixel((x, y), (0, 0, 0))
            elif min(img.getpixel((x, y))) > 255 - noise:
                img.putpixel((x, y), (255, 255, 255))
    return img

def main():
    filename = "K-ON_logo.jpg"
    img_data = Image.open(filename)
    width, height = img_data.size
    img = []
    for y in range(height):
        for x in range(width):
            img.append(img_data.getpixel((x,y)))
    img_meta = np.array(img)
    img2 = Enlarge(img_data, 2, 2)
    img2.show()
    print(type(img2))
    img3 = End_value_smooth(img2)
    img3.show()


if __name__ == "__main__":
    main()