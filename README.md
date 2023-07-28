url = "https://heroku.com/deploy?template=https://github.com/SS7SS/base64"

# قم بإنشاء زر "اضغط هنا"
button_markup = InlineKeyboardMarkup()
button = InlineKeyboardButton("اضغط هنا للتنصيب", url=url)
button_markup.add(button)
