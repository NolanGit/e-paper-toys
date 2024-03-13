from libs.canvas import Canvas
from libs.layout import Column, Row
from libs.shapes import Point
from libs.text import Text
from libs.font import font24

canvas = Canvas(800, 480)

col = Column(
    canvas=canvas, x=10, y=10, width=canvas.width - 20, height=canvas.height - 20
)
col.gutter = 10
row1 = col.add_row()
row2 = col.add_row()
row3 = col.add_row()
row4 = col.add_row()
row5 = col.add_row()

row1.gutter = 10
row1_col1 = row1.add_col()
row1_col2 = row1.add_col()
row1_col1.rectangle_self()
row1_col2.rectangle_self()

row2.gutter = 30
row2_col1 = row2.add_col()
row2_col2 = row2.add_col()
row2_col3 = row2.add_col()
row2_col1.rectangle_self()
row2_col2.rectangle_self()
row2_col3.rectangle_self()

row3.rectangle_self()
row4.rectangle_self()
row5.rectangle_self()

text = Text("hello", font24, Point(row3.center_point.x, row3.center_point.y), canvas)
text.draw()

canvas.save("pil_test.bmp")
