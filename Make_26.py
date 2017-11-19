
import minecraft.minecraft as minecraft
mc = minecraft.Minecraft.create()

ground = [-128,-128,-128,128,0,128,02]
mc.setBlocks (ground)

sky = [-128,0,-128,128,128,128,00]
mc.setBlocks (sky)
