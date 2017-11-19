import minecraft.minecraft as minecraft
mc = minecraft.minecraft.create()

Tower = [-55,1,99,-59,30,95,103]
mc.setBlocks(tower)

hollow = [-56,2,98,-58,30,96,00]
mc.setBlocks(hollow)

mc.setBlock(-57,1,94,67,2)

mc.setBlock(-57,2,95,71,2)
mc.setBlock(-57,3,95,71,11)

X = -56
Y = 6
Z = 95

For floors in range (5):
    For full in range (3):
        For window in range (3):
            mc.setBlock(x,y,z,20)
            y=y+1
        y=y-3
        x=x-1
    x=x+3
    y=y+5
