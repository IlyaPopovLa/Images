from PIL import Image

image = Image.open ("monro.jpg")
red, green, blue = image.split()

red_cropleft = red.crop ((50, 0, 696, 522))
red_cropcentre = red.crop ((25, 0, 671, 522))
red_offset = Image.blend(red_cropleft, red_cropcentre, 0.5)

blue_cropleft = blue.crop ((0, 0, 646, 522))
blue_cropcentre = blue.crop ((25, 0, 671, 522))
blue_offset = Image.blend (blue_cropleft, blue_cropcentre, 0.5)

green_cropcentre = green.crop ((25, 0, 671, 522))

new_image = Image.merge ("RGB", (red_offset, green_cropcentre, blue_offset))
new_image.thumbnail((80, 80))
new_image.save ("new_monro.jpg")
