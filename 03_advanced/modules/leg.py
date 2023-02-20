##########################################################################################
import maya.cmds as cmds
from modules import controls

from modules.controls import *

##########################################################################################
LEG_JOINTS=['Pelvis','Hip','Knee','Ankle','Ball','FootTip']
chains = ['Wjnt','Fkjnt','Ikjnt']
color = ''
DO_NOT_TOUCH = 'DO_NOT_TOUCH'


def rig_leg(side='l', name='L_Leg'):
    if   side == 'l': 
        side  = 'L'
        color = 'Blue'
    elif side == 'r': 
        side  = 'R'
        color = 'Red'

    ##########################################################################################
    #CREATE WJNT, FK AND IK CHAINS
    cmds.select(clear=True)
    
    for chain in chains:
        
        for joint in LEG_JOINTS:
            joint_leg = cmds.joint(n=f'{side}_{joint}_{chain}')
            
            for axis in ('X','Y','Z'):
                rotate_axis = cmds.getAttr(f'Guide_{name}_{joint}_jnt.jointOrient{axis}')
                cmds.setAttr(f'{joint_leg}.jointOrient{axis}', rotate_axis)
           
            constraint = cmds.pointConstraint(f'Guide_{name}_{joint}_jnt', joint_leg, maintainOffset=False)
            cmds.delete(constraint)      
        
        cmds.select(clear=True)            

    for chain in range(2):
        cmds.parent(f'{side}_{LEG_JOINTS[1]}_{chains[chain+1]}',f'{side}_{LEG_JOINTS[0]}_{chains[0]}')
        cmds.delete(f'{side}_{LEG_JOINTS[0]}_{chains[chain+1]}')
    
    ##########################################################################################
    #CREATE FK CONTROLS
    for control in range(len(LEG_JOINTS)):
        controls.generate_control('Circle', color, f'{side}_{LEG_JOINTS[control]}_fk_ctrl')
        
        if control == 0:
            constraint = cmds.pointConstraint(f'{side}_{LEG_JOINTS[control]}_{chains[0]}',
                                           f'{side}_{LEG_JOINTS[control]}_fk_ctrl_adj', maintainOffset=False)
            cmds.delete(constraint)
        
        else: 
            constraint = cmds.parentConstraint(f'{side}_{LEG_JOINTS[control]}_{chains[0]}',
                                           f'{side}_{LEG_JOINTS[control]}_fk_ctrl_adj', maintainOffset=False)
            cmds.delete(constraint)
        
        if LEG_JOINTS[control] == LEG_JOINTS[0]:
            cmds.parentConstraint(f'{side}_{LEG_JOINTS[control]}_fk_ctrl', 
                                  f'{side}_{LEG_JOINTS[control]}_{chains[0]}', maintainOffset=True)
        
        elif LEG_JOINTS[control] == LEG_JOINTS[-1]: cmds.delete(f'{side}_{LEG_JOINTS[control]}_fk_ctrl_adj')
        
        else:
            cmds.parentConstraint(f'{side}_{LEG_JOINTS[control]}_fk_ctrl', 
                                  f'{side}_{LEG_JOINTS[control]}_{chains[1]}', maintainOffset=True)
            cmds.parent(f'{side}_{LEG_JOINTS[control]}_fk_ctrl_adj', f'{side}_{LEG_JOINTS[control-1]}_fk_ctrl')
    
    ##########################################################################################
    #CREATE IK
    ik_arm  = cmds.ikHandle(name=f'{name}_IK', startJoint=f'{side}_{LEG_JOINTS[1]}_{chains[2]}', 
                           endEffector=f'{side}_{LEG_JOINTS[3]}_{chains[2]}', solver='ikRPsolver')[0]
    ik_ball = cmds.ikHandle(name=f'{name}_ball_IK', startJoint=f'{side}_{LEG_JOINTS[3]}_{chains[2]}', 
                           endEffector=f'{side}_{LEG_JOINTS[4]}_{chains[2]}', solver='ikRPsolver')[0]
    ik_toe  = cmds.ikHandle(name=f'{name}_toe_IK', startJoint=f'{side}_{LEG_JOINTS[4]}_{chains[2]}', 
                           endEffector=f'{side}_{LEG_JOINTS[5]}_{chains[2]}', solver='ikRPsolver')[0]
    
    controls.generate_control('Cube', color, f'{side}_Foot_ctrl')
    constraint = cmds.pointConstraint(f'{side}_{LEG_JOINTS[3]}_{chains[2]}', f'{side}_Foot_ctrl_adj',
                                      maintainOffset=False)
    cmds.delete(constraint)
    cmds.parent(ik_arm, ik_ball, ik_toe, f'{side}_Foot_ctrl')

    cmds.addAttr(f'{side}_Foot_ctrl', longName='sep', attributeType='enum', enumName='********', keyable=True)
    cmds.addAttr(f'{side}_Foot_ctrl', longName='strech', attributeType='float', dv=1, min=0, max=1, keyable=True, hidden=False)
    cmds.addAttr(f'{side}_Foot_ctrl', longName='volumPresservation', attributeType='float', dv=1, min=0, max=1, keyable=True)

    ##########################################################################################
    #CREATE POLE VECTOR
    pos_hip   = cmds.xform(f'{side}_{LEG_JOINTS[1]}_{chains[2]}', worldSpace=True, q=True, translation=True)
    pos_knee  = cmds.xform(f'{side}_{LEG_JOINTS[2]}_{chains[2]}', worldSpace=True, q=True, translation=True)
    pos_ankle = cmds.xform(f'{side}_{LEG_JOINTS[3]}_{chains[2]}', worldSpace=True, q=True, translation=True)

    distance_leg   = cmds.distanceDimension(startPoint=(.1,0,0), endPoint=(1.1,0,0))
    dist_leg_locs  = cmds.listConnections( distance_leg, destination=False, source=True )
    loc_dist_arm_1 = dist_leg_locs[0]
    loc_dist_arm_2 = dist_leg_locs[1]
    cmds.select(loc_dist_arm_1)
    cmds.xform(relative=False, translation=pos_hip)
    cmds.parent(loc_dist_arm_1, f'{side}_{LEG_JOINTS[0]}_fk_ctrl_adj')
    cmds.select(loc_dist_arm_2)
    cmds.xform(relative=False, translation=pos_ankle)
    cmds.parent(loc_dist_arm_2, f'{side}_Foot_ctrl')
    distance_leg_value = cmds.getAttr(f'{distance_leg}.distance') 
    
    controls.generate_control('Cone', color, f'{name}_pv_ctrl')
    constraint = cmds.pointConstraint(f'{side}_{LEG_JOINTS[2]}_{chains[2]}',
                                      f'{name}_pv_ctrl_adj', maintainOffset=False)
    cmds.delete(constraint)
    cmds.select(f'{name}_pv_ctrl_adj')
    cmds.move(distance_leg_value, z=True, relative=True)
    
    curve_pv = cmds.curve(name=f'{name}_cv_pv', degree=1, point=(pos_hip, pos_knee, pos_ankle)) 
    cmds.moveVertexAlongDirection (f'{curve_pv}.cv[1]', normalDirection=distance_leg_value)
    locator_pv = cmds.spaceLocator(name=f'{name}_pv_loc')[0]
    pos_pv= cmds.pointPosition(f'{curve_pv}.cv[1]')
    cmds.xform (locator_pv, worldSpace=True, translation=pos_pv)
    cmds.parent(locator_pv, f'{name}_pv_ctrl')
    cmds.poleVectorConstraint(locator_pv, ik_arm)

    cmds.delete(curve_pv)

    ##########################################################################################
    #STRECH AND VOLUMEN PRESSERVATION
    global_md = cmds.shadingNode('multiplyDivide', name=f'{name}_global_md', asUtility=True)
    cmds.setAttr(f'{global_md}.operation', 2)
    cmds.connectAttr(f'{distance_leg}.distance', f'{global_md}.input1.input1X')
    
    distance_leg1   = cmds.distanceDimension(startPoint=(pos_hip), endPoint=(pos_knee))
    dist_leg1_value = cmds.getAttr(f'{distance_leg1}.distance') 
    distance_leg1   = cmds.listRelatives(distance_leg1, parent=True)
    cmds.delete(distance_leg1)
    distance_leg2   = cmds.distanceDimension(startPoint=(pos_knee), endPoint=(pos_ankle))
    dist_leg2_value = cmds.getAttr(f'{distance_leg2}.distance') 
    distance_leg2   = cmds.listRelatives(distance_leg2, parent=True)
    cmds.delete(distance_leg2)
    dist_leg_strech = dist_leg1_value + dist_leg2_value
    
    strech_md = cmds.shadingNode('multiplyDivide', name=f'{name}_strech_md', asUtility=True)
    cmds.setAttr(f'{strech_md}.operation', 2)
    cmds.connectAttr(f'{global_md}.output.outputX', f'{strech_md}.input1.input1X')
    cmds.setAttr(f'{strech_md}.input2X', dist_leg_strech)

    condition_strech = cmds.shadingNode('condition', name=f'{name}_strech_con', asUtility=True)
    cmds.connectAttr(f'{strech_md}.outputX', f'{condition_strech}.firstTerm')
    cmds.connectAttr(f'{strech_md}.outputX', f'{condition_strech}.colorIfTrueR')
    cmds.setAttr(f'{condition_strech}.secondTerm', 1)
    cmds.setAttr(f'{condition_strech}.operation', 2)

    blendColor_strech = cmds.shadingNode('blendColors', name=f'{name}_strech_bc', asUtility=True)
    cmds.connectAttr(f'{condition_strech}.outColorR', f'{blendColor_strech}.color1R')
    cmds.connectAttr(f'{side}_Foot_ctrl.strech', f'{blendColor_strech}.blender')
    cmds.setAttr(f'{blendColor_strech}.color2R', 1)
    cmds.connectAttr(f'{blendColor_strech}.output.outputR', f'{side}_{LEG_JOINTS[1]}_{chains[2]}.scale.scaleX')
    cmds.connectAttr(f'{blendColor_strech}.output.outputR', f'{side}_{LEG_JOINTS[2]}_{chains[2]}.scale.scaleX')

    pow_volumen = cmds.shadingNode('multiplyDivide', name=f'{name}_volum_pow', asUtility=True)
    cmds.connectAttr(f'{condition_strech}.outColorR', f'{pow_volumen}.input1.input1X')
    cmds.setAttr(f'{pow_volumen}.input2.input2X', .5)
    cmds.setAttr(f'{pow_volumen}.operation', 3)

    volum_md = cmds.shadingNode('multiplyDivide', name=f'{name}_volum_md', asUtility=True)
    cmds.connectAttr(f'{pow_volumen}.output.outputX', f'{volum_md}.input2.input2X')
    cmds.setAttr(f'{volum_md}.input1.input1X', 1)
    cmds.setAttr(f'{volum_md}.operation', 2)
    cmds.connectAttr(f'{volum_md}.output.outputX', f'{side}_{LEG_JOINTS[1]}_{chains[2]}.scale.scaleY')
    cmds.connectAttr(f'{volum_md}.output.outputX', f'{side}_{LEG_JOINTS[2]}_{chains[2]}.scale.scaleY')
    cmds.connectAttr(f'{volum_md}.output.outputX', f'{side}_{LEG_JOINTS[1]}_{chains[2]}.scale.scaleZ')
    cmds.connectAttr(f'{volum_md}.output.outputX', f'{side}_{LEG_JOINTS[2]}_{chains[2]}.scale.scaleZ')
    ##########################################################################################
    #SWITCH IK/FK
    ctrls_grp    = cmds.group(n=f'{name}_ctrls_grp', empty=True)
    ctrls_ik_grp = cmds.group(n=f'{name}_ik_ctrls_grp', empty=True)

    if cmds.objExists(f'{name}_switch_ctrl'): pass
    else: controls.generate_control('Cube', color, f'{name}_switch_ctrl')

    attributes = ['tx','ty','tz','rx','ry','rz','sx','sy','sz','v']
    for attr in attributes:
        cmds.setAttr(f'{name}_switch_ctrl.{attr}', lock=True, keyable=False)
    cmds.addAttr(f'{name}_switch_ctrl', longName='IKFK', attributeType='float', defaultValue=1, 
                 min=0, max=1, keyable=True, hidden=False) 

    constraint = cmds.pointConstraint(f'{side}_{LEG_JOINTS[3]}_{chains[0]}',
                                      f'{name}_switch_ctrl_adj', maintainOffset=False)
    cmds.delete(constraint)
    movement = cmds.getAttr(f'{side}_{LEG_JOINTS[-1]}_{chains[0]}.tx')
    cmds.select(f'{name}_switch_ctrl_adj')
    cmds.move(-(movement*2), z=True, relative=True)

    control_vis_rev = cmds.shadingNode('reverse', n=f'{name}_vis_tev', asUtility=True)
    cmds.connectAttr(f'{name}_switch_ctrl.IKFK', f'{control_vis_rev}.input.inputX')
    cmds.connectAttr(f'{control_vis_rev}.outputX', f'{side}_{LEG_JOINTS[1]}_fk_ctrl_adj.visibility')
    cmds.connectAttr(f'{name}_switch_ctrl.IKFK', f'{name}_ik_ctrls_grp.visibility')

    for joint in LEG_JOINTS:

        if joint == LEG_JOINTS[0]:pass
        else:
            for movement in ('translate', 'rotate', 'scale'):
                blend_color = cmds.shadingNode('blendColors', 
                                               name=f'{side}_{joint}_switch_bc', asUtility=True)
                cmds.connectAttr(f'{name}_switch_ctrl.IKFK', f'{blend_color}.blender')
                cmds.connectAttr(f'{side}_{joint}_{chains[2]}.{movement}', f'{blend_color}.color1')
                cmds.connectAttr(f'{side}_{joint}_{chains[1]}.{movement}', f'{blend_color}.color2')
                cmds.connectAttr(f'{blend_color}.output', f'{side}_{joint}_{chains[0]}.{movement}')

    ##########################################################################################
    #CLEAN ARM SETUP
    module_grp   = cmds.group(name=f'{name}_mstr_grp', empty=True)

    if cmds.objExists(DO_NOT_TOUCH): pass
    else: cmds.group(n=DO_NOT_TOUCH, empty=True)

    cmds.parent(f'{side}_Foot_ctrl_adj', f'{name}_pv_ctrl_adj', ctrls_ik_grp)
    cmds.parent(ctrls_ik_grp, f'{side}_{LEG_JOINTS[0]}_fk_ctrl_adj', f'{name}_switch_ctrl_adj', ctrls_grp)
    cmds.parent(f'{side}_{LEG_JOINTS[0]}_{chains[0]}', ctrls_grp, module_grp)

    distance_leg = cmds.listRelatives(distance_leg, p=True)
    cmds.hide(locator_pv, ik_arm,distance_leg, f'{side}_{LEG_JOINTS[1]}_{chains[2]}', 
              f'{side}_{LEG_JOINTS[1]}_{chains[1]}', loc_dist_arm_1,loc_dist_arm_2)
    cmds.parent(distance_leg, DO_NOT_TOUCH)

    

# rig_leg(side='l', name='L_Leg')
# rig_leg(side='r', name='R_Leg')
