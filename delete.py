import os

cwd = os.getcwd()
test = os.listdir(cwd)

for item in test:
    if item.endswith(".png"):
      os.remove(os.path.join(cwd, item))
