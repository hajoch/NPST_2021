import numpy
import sys
from PIL import Image
from PIL import GifImagePlugin
CROP_SIZE = 30

images = []
cropped = []

print('⏳ Analysing frames.. [', end='', flush=True)
gif = Image.open('./opptak.gif')
for frame in range(0, gif.n_frames):
    gif.seek(frame)
    img = gif.copy().convert('RGB')
    img = numpy.array(img)
    img[:,:,1] *=0
    img[:,:,2] *=0
    img = Image.fromarray(img)
    images.append(img)
    cropped.append(img.copy().crop((0,0,CROP_SIZE,CROP_SIZE)))
    print('#',end = '', flush=True)
print('] ✔️')

print('⏳ Extracting red channel to gif... ', end = '', flush=True)
images[0].save('red_channel.gif', save_all=True, append_images=images, optimize=False, duration=100, loop=0)
print('✔️')

print('⏳ Creating mosaic... ', end = '', flush=True)
mosaic = Image.new('RGB', (CROP_SIZE*len(cropped)+1, CROP_SIZE))
for i in range(0, len(cropped)):
    piece = cropped[i]
    mosaic.paste(piece, (i*CROP_SIZE, 0))

mosaic.save('mosaic.jpg')
print('✔️')