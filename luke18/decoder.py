from PIL import Image
from datetime import date
import math

PADDING = 1
PAINT_COLOR = (0,250,0)

def to_date(stamp):
    return date.fromtimestamp(int(stamp))

def image_size(stamps):
    start = to_date(stamps[0])
    end = to_date(stamps[len(stamps)-1])
    days = (end - start).days
    return (math.ceil(days/7)+2*PADDING, 7+2*PADDING) 

timestamps = []
with open('./groenne-firkanter/.git/logs/refs/heads/master', 'r') as f:
    for line in f:
        timestamps.append(line.split(' ')[4])

startdate = to_date(timestamps[0]);
img = Image.new("RGB", image_size(timestamps))

for timestamp in timestamps:
    delta = (to_date(timestamp) - startdate).days
    x, y = math.floor(delta/7) + PADDING, (delta % 7) + PADDING
    img.putpixel((x,y),PAINT_COLOR)

img.save('output.png')
print('image painted. opening image')
img.show()