def whitespace():
  return "    "

def bar():
  return "+---"


def run():
  for i in range(1,5):
    line = ""
    for j in range(i, 4):
      line += whitespace()
    for k in range(4-i, 4):
      line += bar()
    print(line + "+")
    line = ""
    for j in range(i, 4):
      line += whitespace()
    for k in range(4-i, 4):
      line += "|   "
    print(line + "|")
  line = ""
  for z in range(1,5):
    line += bar()
  print(line + "+")
  





