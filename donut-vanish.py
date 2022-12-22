import math, time

def donut_2d(x: float, y: float, radius: float, thickness: float) -> float:
  # same radius as before, though the donut will appear larger as
  # half the thickness is outside this radius

  # how thick the donut will be

  # take the abs of the circle calculation from before, subtracting
  # `thickness / 2`. `abs(...)` will be 0 on the edge of the circle, and
  # increase as you move away. therefore, `abs(...) - thickness / 2` will
  # be ≤ 0 only `thickness / 2` units away from the circle's edge on either
  # side, giving a donut with a total width of `thickness`
  return abs(math.sqrt(x**2 + y**2) - radius) - thickness / 2


def circle(x: float, y: float, radius: float) -> float:
  return math.sqrt(x**2 + y**2) - radius

def sample(x: float, y: float, state: float) -> str:
  # return a '#' if we're inside the shape, and ' ' otherwise
  if donut_2d(x, y, 1.0 - state, 0.99 - state) <= 0:
    return str(int(state*10))
  else:
    return ' '

def frame_state():
  return (time.time() % 10)/10

while True:
  frame_chars = []
  state = frame_state()
  for y in range(20):
    for x in range(80):
      # remap to -1..1 range (for x)...
      remapped_x = x / 80 * 2 - 1
      # ...and corrected for aspect ratio range (for y)
      remapped_y = (y / 20 * 2 - 1) * (2 * 20/80)
      frame_chars.append(sample(remapped_x, remapped_y, state))
    frame_chars.append('\n')
  print('\033[2J' + ''.join(frame_chars))
  time.sleep(1/60)