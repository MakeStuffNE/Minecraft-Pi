import minecraft.minecraft as minecraft
mc = minecraft.Minecraft.create()
x1 = -54
y1 = 31
z1 = 100
x2 = -60
y2 = y1
z2 = 94
block = 01

for i in range (7):
      level = [x1,y1,z1,x2,y2,z2,block]
      mc.setBlocks(level)
      x1 = x1 - 1
      y1 = y1 + 1
      z1 = z1 - 1
      x2 = x2 + 1
      y2 = y1
      z2 = z2 + 1
