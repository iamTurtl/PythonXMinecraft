# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 11:34:30 2021

@author: User
"""
#連接minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

"""
#傳送玩家
position = mc.player.getTilePos()
#print(position)
x=-2
y=110
z=240
mc.player.setTilePos(x,y,z)
"""

"""
#說第t次
import time
t=0
while t<20:
    time.sleep(1)
    t=t+1
    mc.postToChat("第"+ str(t)+"次")
"""

"""
#蓋塔
t=0
while t<7:
    mc.setBlock(x-1,y,z,98)
    t=t+1
    y=y+1
#mc.setBlocks(x-1,y,z,x-1,y,z,98)
"""

"""
#蓋保護牆
x,y,z=mc.player.getTilePos()
#print(x,y,z)
mc.setBlocks(x+1,y+1,z+1,x-1,y-1,z-1,98)
mc.setBlocks(x,y,z,x,y+1,z,0)
#mc.setBlock(x,y-1,z,166)
#mc.setBlocks(x+1,y+1,z+1,x-1,y-1,z-1,0)
"""
"""
#蓋家
x,y,z=mc.player.getTilePos()
print(x,y,z)
mc.setBlocks(x+2,y-1,z,x-15,y+4,z+9,5)
mc.setBlocks(x+1,y,z+1,x-14,y+3,z+8,0)
"""
