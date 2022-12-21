import time


def sample(x: int, y: int) -> str:
  # draw an alternating checkboard pattern
  if (x + y + int(time.time())) % 2:
    return str(int(time.time() % 10))
  else:
    return ' '

while True:
  # loop over each position and sample a character
  frame_chars = []
  for y in range(20):
    for x in range(80):
      frame_chars.append(sample(x, y))
    frame_chars.append('\n')
  # print out a control sequence to clear the terminal, then the frame
  # (I haven't tested this on windows, but I believe it should work there,
  # please get in touch if it doesn't)
  print('\033[2J' + ''.join(frame_chars))
  # cap at 30fps
  time.sleep(1/30)