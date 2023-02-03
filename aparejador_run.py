##########################################################################################
#content = autorig
#
#version = 0.1.0
#date = 2023-01-24
#
#author = Jogar Diaz <jogartista@gmail.com>
##########################################################################################
import sys
import importlib

path_aparejador = 'J:\python advance\\aparejador'
sys.path.append(path_aparejador)

from modules import guides
from modules import arm, leg, reverse_foot
importlib.reload(arm)
importlib.reload(leg)
importlib.reload(guides)
importlib.reload(reverse_foot)
##########################################################################################
#GENERATE GUIDES
guides.generate_guides(type='l_arm',  name='L_Arm',  color='blue')
guides.generate_guides(type='r_arm',  name='R_Arm',  color='red')
guides.generate_guides(type='l_leg',  name='L_Leg',  color='blue')
guides.generate_guides(type='r_leg',  name='R_Leg',  color='red')
guides.generate_guides(type='r_foot', name='R_Foot', color='pink')
guides.generate_guides(type='l_foot', name='L_Foot', color='littleBlue')
guides.generate_guides(type='spine',  name='Spine',  amount=5, color='yellow')
guides.generate_guides(type='neck',   name='Neck',   amount=3, color='yellow')
guides.generate_guides(type='l_hand', name='L_Hand', thumb=True,   amount=4,   color='littleBlue')
guides.generate_guides(type='r_hand', name='R_Hand', thumb = True, amount = 4, color = 'pink')

guides.guides_sizes(resize = .2)

##########################################################################################
#MIRROR IF NECESSARY AND CREATE JOINTS WITH VISIBILITY IF NECESSARY
guides.mirror_guides(correct_side='L_Arm', mirror_to='R_Arm')
guides.mirror_guides(correct_side='L_Leg', mirror_to='R_Leg')
guides.mirror_guides(correct_side='L_Foot', mirror_to='R_Foot')
guides.mirror_guides(correct_side='L_Hand', mirror_to='R_Hand')

guides.joints(vis=True)
##########################################################################################
#BUILD RIG
arm.rig_arm(type='l_arm', name='L_Arm')
arm.rig_arm(type='r_arm', name='R_Arm')
leg.rig_leg(type='l_leg', name='L_Leg')
leg.rig_leg(type='r_leg', name='R_Leg')
reverse_foot.create_reverse_foot(type='l_foot', name='L_Foot',connect_to='L_Leg')
reverse_foot.create_reverse_foot(type='r_foot', name='R_Foot',connect_to='R_Leg')

