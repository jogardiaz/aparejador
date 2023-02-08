##########################################################################################
import maya.cmds as cmds
from modules import controls
##########################################################################################
color = ''
DO_NOT_TOUCH = 'DO_NOT_TOUCH'
side = ''
fingers=[]

def rig_hand(type='', name='', thumb=True, amount=4):
    if   type == 'l_hand':
        side  = 'L'
        color = 'Blue'
    elif type == 'r_hand':
        side  = 'R'
        color = 'Red'
        
    if thumb == True: fingers = ['Index','Middle','Ring','Pinky', 'Thumb']
    elif thumb == False: fingers = ['Index','Middle','Ring','Pinky']

    hand_grp = cmds.group(n=f'{name}_mstr_grp', em=True)
    ##########################################################################################
    #CREATE FINGERS CHAIN
    cmds.select(cl=True)
    for finger in fingers:
        cmds.select(cl=True)
        for number in range(5):
            joint_finger = cmds.joint(n=f'{side}_{finger}_{number+1}_Wjnt')
            constraint = cmds.pointConstraint(f'Guide_{name}_{finger}{number+1}_jnt', 
                                              joint_finger, mo=False)
            cmds.delete(constraint)      
            for axis in ('X','Y','Z'):
                rotate_axis = cmds.getAttr(f'Guide_{name}_{finger}{number+1}_jnt.jointOrient{axis}')
                cmds.setAttr(f'{joint_finger}.jointOrient{axis}', rotate_axis)
            if number < 4:
                controls.generate_control(control_shape='Circle', shape_color=color, 
                                          name=f'{side}_{finger}_{number+1}_ctrl')
                constraint = cmds.parentConstraint(joint_finger, 
                                                f'{side}_{finger}_{number+1}_ctrl_adj', mo=False)
                cmds.delete(constraint)
                cmds.parent(joint_finger, f'{side}_{finger}_{number+1}_ctrl')
                print('entra')
            elif number == 4: cmds.parent(joint_finger, f'{side}_{finger}_{number}_Wjnt')

            if number == 0: cmds.parent(f'{side}_{finger}_{number+1}_ctrl_adj', hand_grp)
            elif number > 0 and number < 4: cmds.parent(f'{side}_{finger}_{number+1}_ctrl_adj',
                                                        f'{side}_{finger}_{number}_ctrl')
    cmds.select(cl=True)            
    ##########################################################################################
    #CONNECT TO ARM
    cmds.parentConstraint(f'{side}_Wrist_Wjnt', hand_grp, mo=True)

# rig_hand(type='l_hand', name='L_Hand', thumb=True, amount=4)