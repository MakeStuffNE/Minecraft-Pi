from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

while True:
    mc.setBlock(47,3,-97,103)
    time.sleep (0.1)
    mc.setBlock(47,3,-97,00)
    time.sleep (0.1)
