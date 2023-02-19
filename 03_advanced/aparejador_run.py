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

path_aparejador = 'J:\\python advance\\aparejador\\03_advanced'
sys.path.append(path_aparejador)

from modules import guides
from modules import arm
from modules import leg
from modules import reverse_foot
from modules import hand
from modules import spine
importlib.reload(arm)
importlib.reload(leg)
importlib.reload(guides)
importlib.reload(reverse_foot)
importlib.reload(hand)
importlib.reload(spine)

##########################################################################################
#GENERATE GUIDES
guides.generate_guides(body_part='arm',  name='L_Arm',  color='blue', side='l')
guides.generate_guides(body_part='arm',  name='R_Arm',  color='red',  side='r')
guides.generate_guides(body_part='leg',  name='L_Leg',  color='blue', side='l')
guides.generate_guides(body_part='leg',  name='R_Leg',  color='red',  side='r')
guides.generate_guides(body_part='foot', name='L_Foot', color='littleBlue', side='l')
guides.generate_guides(body_part='foot', name='R_Foot', color='pink', side='r')
guides.generate_guides(body_part='spine',name='Spine',  amount=5, color='yellow')
guides.generate_guides(body_part='neck', name='Neck',   amount=3, color='yellow')
guides.generate_guides(body_part='hand', name='L_Hand', thumb=True, amount=4, 
                       color='littleBlue', side='l')
guides.generate_guides(body_part='hand', name='R_Hand', thumb=True, amount=4,
                       color='pink', side='r')

guides.guides_sizes(resize = .2)

##########################################################################################
#MIRROR IF NECESSARY AND CREATE JOINTS WITH VISIBILITY IF NECESSARY
guides.mirror_guides(correct_side='L_Arm', mirror_to='R_Arm')
guides.mirror_guides(correct_side='L_Leg', mirror_to='R_Leg')
guides.mirror_guides(correct_side='L_Foot', mirror_to='R_Foot')
guides.mirror_guides(correct_side='L_Hand', mirror_to='R_Hand')

guides.joints(vis=True)

##########################################################################################
# #BUILD RIG
arm.rig_arm(side='l', name='L_Arm')
arm.rig_arm(side='r', name='R_Arm')
leg.rig_leg(side='l', name='L_Leg')
leg.rig_leg(side='r', name='R_Leg')
reverse_foot.create_reverse_foot(side='l', name='L_Foot',connect_to='L_Leg')
reverse_foot.create_reverse_foot(side='r', name='R_Foot',connect_to='R_Leg')
hand.rig_hand(side='l', name='L_Hand', thumb=True, amount=4)
hand.rig_hand(side='r', name='R_Hand', thumb=True, amount=4)
spine.rig_spine(name='Spine', amount=5)
