def z91():
     from PIL import Image
     img = Image.open("вкусныхпраздников.jpg")
     a = img.crop((200, 150, 800, 800))
     a.save("ВКУСНЕЙШИЕпраздники.jpg")

def z92():
    from PIL import Image
    holiday_cards = {
         "День рождения": "с днем рождения.jpg",
         "Новый год": "с новым годом.jpg",
         "8 марта": "с 8 марта.jpg"
     }
    a = input("введите праздник ")
    if a in holiday_cards:
         b = holiday_cards[a]
         b = Image.open(b)
         b.show()

def z93():
    from PIL import Image, ImageDraw, ImageFont
    img = Image.open("вкусныхпраздников.jpg")
    a = img.crop((200, 150, 800, 800))
    a.save("ВКУСНЕЙШИЕпраздники.jpg")
    b = input ("ведите имя")
    draw = ImageDraw.Draw(a)
    C = ImageFont.truetype("D:\\UserFolders\\Downloads\\4-font.ttf", 30)
    color = (150, 170,187)
    color2 = (150, 170,187)
    draw.text((75, 550), b, font=C, fill=color, stroke_width=1, stroke_fill=color2)
    draw.text((200, 550), "поздравляем!", font=C, fill=color)
    a.show()
    a.save('tretyezadanie.png')

z92()