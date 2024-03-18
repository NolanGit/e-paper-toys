import os
from PIL import ImageFont

def get_font(font_size=24):
    return ImageFont.truetype(os.path.join(os.getcwd(), "resource/Font.ttc"), font_size)
