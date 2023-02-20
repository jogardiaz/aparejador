##########################################################################################
import maya.cmds as cmds
from modules import controls

from modules.controls import *

##########################################################################################
color_main = 'Yellow'
color_sec  = 'Green'
DO_NOT_TOUCH = 'DO_NOT_TOUCH'
side = 'C'

def rig_spine(name='', amount=0):
    #CREATE WJNTS
    for guide in range(1,amount+1):
        joint = cmds.joint(name=f'{side}_{name}_{guide}_Wjnt')
        
        for axis in ('X','Y','Z'):
            rotate_axis = cmds.getAttr(f'Guide_{name}_{guide}_jnt.jointOrient{axis}')
            cmds.setAttr(f'{joint}.jointOrient{axis}', rotate_axis)
        
            constraint = cmds.pointConstraint(f'Guide_{name}_{guide}_jnt', joint, maintainOffset=False)
        cmds.delete(constraint)      

    cmds.select(clear=True)        

    ##########################################################################################
    #CREATE IK SPLINE
    ik = cmds.ikHandle(n=f'{name}_IK', startJoint=f'{side}_{name}_1_Wjnt',
                       endEffector=f'{side}_{name}_{amount}_Wjnt', solver='ikSplineSolver', createCurve=True)
    ik_spine = ik[0]
    cmds.rename(ik[-1], f'{name}_crv')
    ik_crv = f'{name}_crv'

    controls.Cube(name = f'{side}_Hip_ctrl', color_name = color_main)
    joint_hip = cmds.joint(name=f'{side}_Hip_jnt')
    cmds.parent(joint_hip, f'{side}_Hip_ctrl')
    constraint = cmds.pointConstraint(f'{side}_{name}_1_Wjnt', f'{side}_Hip_ctrl_adj')
    cmds.delete(constraint)
    
    controls.Circle(name = f'{side}_Chest_ctrl', color_name = color_main)
    joint_chest = cmds.joint(name=f'{side}_Chest_jnt')
    cmds.parent(joint_chest, f'{side}_Chest_ctrl')
    constraint = cmds.pointConstraint(f'{side}_{name}_{amount}_Wjnt', f'{side}_Chest_ctrl_adj')
    cmds.delete(constraint)
    
    cmds.select(joint_hip, joint_chest, ik_crv)
    cmds.skinCluster()

#rig_spine(name='Spine', amount=5)
