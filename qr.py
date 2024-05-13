import qrcode


kod = qrcode.make("https://github.com/ozkayamert")
kod.save("gitcode.png")