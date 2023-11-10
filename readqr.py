from pyzbar.pyzbar import decode
from PIL import Image
content=decode(Image.open('D:\\buniv2.png'))
print(content[0].data.decode('ascii'))

