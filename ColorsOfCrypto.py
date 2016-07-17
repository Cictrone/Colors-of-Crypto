from PIL import Image
from Crypto.Cipher import AES
from Crypto.Random import random
from Crypto.Util import Counter
import os

if __name__ == '__main__':
    for j in range(1, 101):
        key = os.urandom(32)
        ctr = Counter.new(128)
        cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
        data = []
        num_pixels = 32
        length_width = num_pixels*3
        for i in range(0, length_width*length_width):
            data.append(random.randint(0,255))
        data = cipher.encrypt(bytes(data))
        im = Image.frombytes('RGB', (num_pixels, num_pixels), data)
        path = 'AES/CTR/%s.png' % str(j)
        im.save(path)
        print("%s Files made." % str(j))
