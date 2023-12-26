import pandas as pd
from PIL import Image, ImageDraw, ImageFont

data = pd.read_excel (r'gen.xlsx')

# print(data['name1'])
name1_list = data["name1"].tolist()
name2_list = data["name2"].tolist()
kvant_list = data["kvantum"].tolist()


im = Image.open(r'img.jpg')
width, height = im.size



for i in range(len(name1_list)):
    d = ImageDraw.Draw(im)
    text_color = (0, 137, 209)
    font = ImageFont.truetype("fonts/RussoOne-Regular.ttf", 50)

    name = f'{name1_list[i]} {name2_list[i]}'

    # d.text((360, 530)  # Позиция на картинке
    #        , name2_list[i], fill=text_color, font=font)

    _, _, w, h = d.textbbox((0, 0), name, font=font)
    d.text(((width - w) / 2, (500)), name, font=font, fill=text_color)

    _, _, w, h = d.textbbox((0, 0), kvant_list[i], font=font)
    d.text(((width - w) / 2, (800)), kvant_list[i], font=ImageFont.truetype('fonts/Roboto-Light.ttf',60), fill=(0, 0, 0))



    im.save("fifochka/certificate_" + name1_list[i] + ".pdf")

