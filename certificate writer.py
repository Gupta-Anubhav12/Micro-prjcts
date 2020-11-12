from PIL import Image, ImageDraw, ImageFont
img = Image.open('certificate.jpg')
d1 = ImageDraw.Draw(img)
# d1.textsize(50)
font = ImageFont.truetype("arial.ttf", 80)
d1.text((760, 450), "Sanuj Sood", fill=( 0,0,0,100),font = font)


img.show()
img.save("image_text.jpg")