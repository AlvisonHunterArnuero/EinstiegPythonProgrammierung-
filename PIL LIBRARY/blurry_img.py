from PIL import Image as img, ImageFilter

before = img.open("bridge.bmp")
after = before.filter(ImageFilter.BLUR)
after.save("out.bmp")
