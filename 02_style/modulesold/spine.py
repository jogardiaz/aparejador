##########################################################################################
import maya.cmds as cmds
from modules import controls
##########################################################################################
color_main = 'Yellow'
color_sec  = 'Green'
DO_NOT_TOUCH = 'DO_NOT_TOUCH'
side = 'C'

def rig_spine(name='', amount=0):
    #CREATE WJNTS
    for guide in range(1,amount+1):
        joint = cmds.joint(n=f'{side}_{name}_{guide}_Wjnt')
        for axis in ('X','Y','Z'):
            rotate_axis = cmds.getAttr(f'Guide_{name}_{guide}_jnt.jointOrient{axis}')
            cmds.setAttr(f'{joint}.jointOrient{axis}', rotate_axis)
        constraint = cmds.pointConstraint(f'Guide_{name}_{guide}_jnt', joint, mo=False)
        cmds.delete(constraint)      

    cmds.select(cl=True)            
    ##########################################################################################
    #CREATE IK SPLINE
    ik = cmds.ikHandle(n=f'{name}_IK', sj=f'{side}_{name}_1_Wjnt', ee=f'{side}_{name}_{amount}_Wjnt',
                  sol='ikSplineSolver',ccv=True)
    ik_spine = ik[0]
    cmds.rename(ik[-1], f'{name}_crv')
    ik_crv = f'{name}_crv'

    controls.generate_control(control_shape='Cube',shape_color=color_main, name=f'{side}_Hip_ctrl')
    joint_hip = cmds.joint(n=f'{side}_Hip_jnt')
    cmds.parent(joint_hip, f'{side}_Hip_ctrl')
    constraint = cmds.pointConstraint(f'{side}_{name}_1_Wjnt', f'{side}_Hip_ctrl_adj')
    cmds.delete(constraint)
    controls.generate_control(control_shape='Circle',shape_color=color_main, name=f'{side}_Chest_ctrl')
    joint_chest = cmds.joint(n=f'{side}_Chest_jnt')
    cmds.parent(joint_chest, f'{side}_Chest_ctrl')
    constraint = cmds.pointConstraint(f'{side}_{name}_{amount}_Wjnt', f'{side}_Chest_ctrl_adj')
    cmds.delete(constraint)
    cmds.select(joint_hip, joint_chest, ik_crv)
    cmds.skinCluster()

rig_spine(name='Spine', amount=5)
