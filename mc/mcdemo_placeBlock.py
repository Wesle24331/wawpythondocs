#Wesley Welch
#Place Blocks
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    pos = mc.player.getTilePos()
    mc.setBlock(pos.x, pos.y - 1, pos.z, 41)
    mc.postToChat(pos)

