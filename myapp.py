import pyqrcode
text=pyqrcode.create('https://www.bdu.ac.in/')
text.svg('D:\\buniv.svg',scale=5)
text.png('D:\\buniv2.png',scale=8)