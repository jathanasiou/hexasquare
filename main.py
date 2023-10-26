from math import pi, cos
import drawsvg as draw

A4_X = 210
A4_Y = 297

HEXR_outer = 100 # also Length of each side
HEXR_inner = HEXR_outer * cos(pi/6)
HEX_THICC = 1
SQ_THICC = 2

diff_x = 2   * HEXR_inner
diff_y = 1.5 * HEXR_outer

canvas = draw.Drawing(A4_X*5, A4_Y*5, origin='top-left')

background = draw.Rectangle(-A4_X*5,-A4_Y*5, A4_X*5*2, A4_Y*5*2, fill='white')
canvas.append(background)

def draw_hex(x=0,y=0,color='black', trans='none'):
  shape = draw.Lines(
    x,            y-HEXR_outer,
    x+HEXR_inner, y-HEXR_outer/2,
    x+HEXR_inner, y+HEXR_outer/2,
    x,            y+HEXR_outer,
    x-HEXR_inner, y+HEXR_outer/2,
    x-HEXR_inner, y-HEXR_outer/2,
    x,            y-HEXR_outer,
    stroke=color,
    close=True,
    stroke_width=HEX_THICC,
    fill='none',
    transform=trans
  )
  canvas.append(shape)

# draw square with padding for hex shape
def draw_square(x=0,y=0,color='brown'):
  up_down = draw.Lines(
    x, y-HEXR_outer,
    x, y+HEXR_outer,
    stroke=color,
    stroke_width=SQ_THICC,
  )
  left_right = draw.Lines(
    x-HEXR_inner, y,
    x+HEXR_inner, y,
    stroke=color,
    stroke_width=SQ_THICC,
  )
  canvas.append(up_down)
  canvas.append(left_right)

def draw_grid(count_x, count_y):
  # +1 offset to avoid top left going off-bounds
  for y in range(1, count_y + 1):
    for x in range(1, count_x + 1 + y%2):
      target_x = diff_x*(x + 0.5*(abs((y%2)-1)))
      target_y = diff_y*(y)
      draw_square(target_x, target_y)
      draw_hex(target_x, target_y)

# draw_hex(0,0, 'black')
# draw_hex(diff_x,     0,      'green')

# draw_hex(0.5*diff_x, diff_y, 'blue')
# draw_hex(1.5*diff_x, diff_y, 'orange')

# draw_hex(0,          2*diff_y, 'pink')
# draw_hex(diff_x,     2*diff_y, 'brown')
# draw_hex(2*diff_x,   2*diff_y, 'red')

draw_grid(4,6)

canvas.set_pixel_scale(4)  # Set number of pixels per geometry unit
# canvas.set_render_size(A4_X*10, A4_Y*10)  # Alternative to set_pixel_scale
canvas.save_svg('example.svg')
canvas.save_png('example.png')



# Display in Jupyter notebook
# canvas.rasterize()  # Display as PNG
canvas  # Display as SVG