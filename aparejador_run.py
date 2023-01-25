##########################################################################################
#content = autorig
#
#version = 0.1.0
#date = 2023-01-24
#
#author = Jogar Diaz <jogartista@gmail.com>
##########################################################################################

import sys

path_aparejador = 'J:\python advance\\aparejador'
sys.path.append(path_aparejador)

import modules.guides as guides
##########################################################################################

guides.generate_guides(type='l_arm',  name='L_Arm',  color='blue')
guides.generate_guides(type='r_arm',  name='R_Arm',  color='red')
guides.generate_guides(type='l_leg',  name='L_Leg',  color='blue')
guides.generate_guides(type='r_leg',  name='R_Leg',  color='red')
guides.generate_guides(type='r_foot', name='R_foot', color='pink')
guides.generate_guides(type='l_foot', name='L_foot', color='littleBlue')
guides.generate_guides(type='spine',  name='Spine',  amount=5, color='yellow')
guides.generate_guides(type='neck',   name='Neck',   amount=3, color='yellow')
guides.generate_guides(type='l_hand', name='L_Hand', thumb=True,   amount=4,   color='littleBlue')
guides.generate_guides(type='r_hand', name='R_Hand', thumb = True, amount = 4, color = 'pink')

guides.joints(vis=True)