import math, time

def circle(x: float, y: float, radius: float) -> float:
  return math.sqrt(x**2 + y**2) - radius

def sample(x: float, y: float, state: float) -> str:
  # return a '#' if we're inside the circle, and ' ' otherwise
  if circle(x, y, 1.0 - state) <= 0:
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
  time.sleep(1/30)