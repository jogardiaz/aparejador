#********************************************************************
#content = autorig
#
#version = 0.1.0
#date = 2023-01-22
#
#author = Jogar Diaz <jogartista@gmail.com>
#********************************************************************
import sys
import os

import maya.cmds as mc


path_aparejador = 'J:\python advance\\aparejador'
sys.path.append(path_aparejador)

import modules.guides as guides

guides.guides(type ='spine', name='Spine', amount=5, color='yellow')
guides.guides(type ='neck', name='Neck', amount=3, color='yellow')
guides.guides(type = 'l_arm', name = 'L_Arm', color='blue')
guides.guides(type = 'r_arm', name = 'R_Arm', color='red')
guides.guides(type = 'l_hand', name='L_Hand', thumb=True, amount=4, color='littleBlue')
guides.guides(type = 'r_hand', name = 'R_Hand', thumb = True, amount = 4, color = 'pink')
guides.guides(type = 'l_leg', name = 'L_Leg', color='blue')
guides.guides(type = 'r_leg', name = 'R_Leg', color='red')
guides.guides(type = 'l_foot', name = 'L_foot', color='littleBlue')
guides.guides(type = 'r_foot', name = 'R_foot', color='pink')

guides.joints(vis = False)




