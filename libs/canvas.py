from PIL import Image, ImageDraw


class Canvas:
    """
    Basic canvas
    """

    width = 0
    height = 0
    image_draw = None

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.Limage = Image.new("1", (width, height), 255)  # 255: clear the frame
        self.image_draw = ImageDraw.Draw(self.Limage)
        self.line = []
        self.rectangle = []

    def save(self, file_name):
        self.Limage.save(file_name)
