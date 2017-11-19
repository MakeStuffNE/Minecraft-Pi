import minecraft.minecraft as minecraft
mc = minecraft.minecraft.create()

sky_jail = [-56,40,116,-48,48,108,85]
mc.setBlocks (sky_jail)
Hollow = [-55,41,115,-49,47,109,00]
mc.setBlocks (hollow)

mc.player.setPos(-52,44,112)
mc.postToChat(“You’re in Jail now fool!!”)
