from PIL import Image


im = Image.open("C:/Users/Олег/Desktop/png-clipart-person-computer-icons-stick-figure-free-content-free-animated-s-website-stockxchng.png")
rgb_im = im.convert('RGB')
rgb_im.save("C:/Users/Олег/Desktop/file.jpg", "JPEG")