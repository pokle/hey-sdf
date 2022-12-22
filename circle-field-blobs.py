import math, time

def firstdecimal(v: float) -> str:
  return int(v*10)%10

def circle(x: float, y: float, origin_x: float, origin_y: float, radius: float) -> float:
  return math.sqrt((origin_x - x)**2 + (origin_y-y)**2) - radius

def sample(x: float, y: float) -> str:
  Δ = circle(x, y, -1.0, -0.5, (time.monotonic() % 3)/2) * \
      circle(x, y, 1.0, -0.5, (time.monotonic() % 50)/40) * \
      circle(x, y, -1.0, 0.5, (time.monotonic() % 6)/5) * \
      circle(x, y, 1.0, 0.5, (time.monotonic() % 7)/6)

  return str(firstdecimal(Δ))


while True:
  frame_chars = []
  for y in range(20):
    for x in range(80):
      # remap to -1..1 range (for x)...
      remapped_x = x / 80 * 2 - 1
      # ...and corrected for aspect ratio range (for y)
      remapped_y = (y / 20 * 2 - 1) * (2.0 * 20/80)
      frame_chars.append(sample(remapped_x, remapped_y))
    frame_chars.append('\n')
  print('\033[2J' + ''.join(frame_chars))
  time.sleep(1/60)