from PIL import Image, ImageDraw, ImageFont
font = ImageFont.truetype("Lexend-Medium.ttf", 24)

times = [(h, m) for h in range(1, 13) for m in range(0, 60)]
txt = [f'{h}:{m:02d}' for h, m in times]
files = [f'bikebus_times/{h}{m:02d}.png' for h, m in times]

def write_png(x, f):
    img = Image.new('RGB', (60, 30), (255, 255, 255))
    d = ImageDraw.Draw(img)
    bb = d.textbbox((0, 0), x, font=font)
    offset = (60 - bb[2])/2
    d.text((offset, 0), x, fill=(0, 0, 0), font=font)
    img.save(f, 'png')

[write_png(x, f) for x, f in zip(txt, files)]

