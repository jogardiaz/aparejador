##########################################################################################
import importlib


import maya.cmds as cmds
import modules.controls as controls 

from controls import *

importlib.reload(controls)

##########################################################################################
ARM_JOINTS=['Clavicle','Shoulder','Elbow','Wrist','HandTip']
chains = ['Wjnt','Fkjnt','Ikjnt']
color = ''
DO_NOT_TOUCH = 'DO_NOT_TOUCH'

def rig_arm(side = 'l',name = 'L_Arm'):
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
        for joint in ARM_JOINTS:
            joint_arm = cmds.joint(name=f'{side}_{joint}_{chain}')
            for axis in ('X','Y','Z'):
                rotate_axis = cmds.getAttr(f'Guide_{name}_{joint}_jnt.jointOrient{axis}')
                cmds.setAttr(f'{joint_arm}.jointOrient{axis}', rotate_axis)
            constraint = cmds.pointConstraint(f'Guide_{name}_{joint}_jnt', 
                                              joint_arm, maintainOffset=False)
            cmds.delete(constraint)      
        cmds.select(clear=True)            

    for chain in range(2):
        cmds.parent(f'{side}_{ARM_JOINTS[1]}_{chains[chain+1]}',
                    f'{side}_{ARM_JOINTS[0]}_{chains[0]}')
        cmds.delete(f'{side}_{ARM_JOINTS[0]}_{chains[chain+1]}')
        
    ##########################################################################################
    #CREATE FK CONTROLS
    for control in range(len(ARM_JOINTS)):
        controls.Circle(name = color, color_name = f'{side}_{ARM_JOINTS[control]}_fk_ctrl')
        
        if control == 0:
            constraint = cmds.pointConstraint(f'{side}_{ARM_JOINTS[control]}_{chains[0]}',
                                           f'{side}_{ARM_JOINTS[control]}_fk_ctrl_adj', 
                                           maintainOffset=False)
            cmds.delete(constraint)
        
        else: 
            constraint = cmds.parentConstraint(f'{side}_{ARM_JOINTS[control]}_{chains[0]}',
                                           f'{side}_{ARM_JOINTS[control]}_fk_ctrl_adj', 
                                           maintainOffset=False)
            cmds.delete(constraint)

        if ARM_JOINTS[control] == ARM_JOINTS[0]:
            cmds.parentConstraint(f'{side}_{ARM_JOINTS[control]}_fk_ctrl', 
                                  f'{side}_{ARM_JOINTS[control]}_{chains[0]}', 
                                  maintainOffset=True)
        
        elif ARM_JOINTS[control] == ARM_JOINTS[-1]: 
            cmds.delete(f'{side}_{ARM_JOINTS[control]}_fk_ctrl_adj')
        
        else:
            cmds.parentConstraint(f'{side}_{ARM_JOINTS[control]}_fk_ctrl', 
                                  f'{side}_{ARM_JOINTS[control]}_{chains[1]}',
                                    maintainOffset=True)
            cmds.parent(f'{side}_{ARM_JOINTS[control]}_fk_ctrl_adj',
                        f'{side}_{ARM_JOINTS[control-1]}_fk_ctrl')
            
    ##########################################################################################
    #CREATE IK
    ik_arm = cmds.ikHandle(n=f'{name}_IK',sj=f'{side}_{ARM_JOINTS[1]}_{chains[2]}', 
                           ee=f'{side}_{ARM_JOINTS[3]}_{chains[2]}',solver='ikRPsolver')[0]
    controls.Cube(color_name = color, name = f'{side}_Hand_ctrl')
    constraint = cmds.parentConstraint(f'{side}_{ARM_JOINTS[3]}_{chains[2]}',
                                       f'{side}_Hand_ctrl_adj', maintainOffset=False)
    cmds.delete(constraint)
    cmds.parent(ik_arm, f'{side}_Hand_ctrl')
    cmds.orientConstraint(f'{side}_Hand_ctrl',f'{side}_{ARM_JOINTS[3]}_{chains[2]}')

    cmds.addAttr(f'{side}_Hand_ctrl', longName='Sep', attributeType='enum', 
                 enumName='********', keyable=True)
    cmds.setAttr(f'{side}_Hand_ctrl.Sep',l=True)
    cmds.addAttr(f'{side}_Hand_ctrl', longName='strech', attributeType='float', 
                 defaultValue=1, minValue=0, maxValue=1, keyable=True, hidden=False)
    cmds.addAttr(f'{side}_Hand_ctrl', longName='volumPresservation', attributeType='float', 
                 defaultValue=1, minValue=0, maxValue=1, k=True)
    
    ##########################################################################################
    #CREATE POLE VECTOR
    pos_shoulder = cmds.xform(f'{side}_{ARM_JOINTS[1]}_{chains[2]}', worldSpace=True,
                              q=True, translation=True)
    pos_elbow    = cmds.xform(f'{side}_{ARM_JOINTS[2]}_{chains[2]}', worldSpace=True,
                              q=True, translation=True)
    pos_wrist    = cmds.xform(f'{side}_{ARM_JOINTS[3]}_{chains[2]}', worldSpace=True,
                              q=True, translation=True)

    distance_arm = cmds.distanceDimension(startPoint=(.1,0,0), endPoint=(1.1,0,0))
    distance_arm_locs = cmds.listConnections( distance_arm, destination=False, source=True)
    loc_dist_arm_1 = distance_arm_locs[0]
    loc_dist_arm_2 = distance_arm_locs[1]
    cmds.select(loc_dist_arm_1)
    cmds.xform(relative=False, translation=pos_shoulder)
    cmds.parent(loc_dist_arm_1, f'{side}_{ARM_JOINTS[0]}_fk_ctrl')
    cmds.select(loc_dist_arm_2)
    cmds.xform(relative=False, translation=pos_wrist)
    cmds.parent(loc_dist_arm_2, f'{side}_Hand_ctrl')
    distance_arm_value = cmds.getAttr(f'{distance_arm}.distance') 
    
    controls.Cone(color_name = color, name = f'{name}_pv_ctrl')
    constraint = cmds.pointConstraint(f'{side}_{ARM_JOINTS[2]}_{chains[2]}',
                                      f'{name}_pv_ctrl_adj', maintainOffset=False)
    cmds.delete(constraint)
    cmds.select(f'{name}_pv_ctrl_adj')
    cmds.move(-(distance_arm_value), z=True,relative=True)
    
    curve_pv = cmds.curve(name=f'{name}_cv_pv',degree=1,
                          point=(pos_shoulder, pos_elbow, pos_wrist)) 
    cmds.moveVertexAlongDirection (f'{curve_pv}.cv[1]',normalDirection=distance_arm_value)
    locator_pv = cmds.spaceLocator(name=f'{name}_pv_loc')[0]
    pos_pv= cmds.pointPosition (f'{curve_pv}.cv[1]')
    cmds.xform (locator_pv, worldSpace=True, translation=pos_pv)
    cmds.parent(locator_pv, f'{name}_pv_ctrl')
    cmds.poleVectorConstraint(locator_pv, ik_arm)

    cmds.delete(curve_pv)

    ##########################################################################################
    #STRECH AND VOLUMEN PRESSERVATION
    global_md = cmds.shadingNode('multiplyDivide', name=f'{name}_global_md', asUtility=True)
    cmds.setAttr(f'{global_md}.operation', 2)
    cmds.connectAttr(f'{distance_arm}.distance',f'{global_md}.input1.input1X')
    
    distance_arm1 = cmds.distanceDimension(startPoint=(pos_shoulder), endPoint=(pos_elbow))
    distance_arm1_value = cmds.getAttr(f"{distance_arm1}.distance") 
    distance_arm1 = cmds.listRelatives(distance_arm1, parent=True)
    cmds.delete(distance_arm1)
    distance_arm2 = cmds.distanceDimension(startPoint=(pos_elbow), endPoint=(pos_wrist))
    distance_arm2_value = cmds.getAttr(f"{distance_arm2}.distance") 
    distance_arm2 = cmds.listRelatives(distance_arm2, parent=True)
    cmds.delete(distance_arm2)
    distance_arm_strech = distance_arm1_value + distance_arm2_value
    
    strech_md = cmds.shadingNode('multiplyDivide', name=f'{name}_strech_md', asUtility=True)
    cmds.setAttr(f'{strech_md}.operation', 2)
    cmds.connectAttr(f'{global_md}.output.outputX', f'{strech_md}.input1.input1X')
    cmds.setAttr(f'{strech_md}.input2X', distance_arm_strech)

    condition_strech = cmds.shadingNode('condition', name=f'{name}_strech_con', asUtility=True)
    cmds.connectAttr(f'{strech_md}.outputX', f'{condition_strech}.firstTerm')
    cmds.connectAttr(f'{strech_md}.outputX', f'{condition_strech}.colorIfTrueR')
    cmds.setAttr(f'{condition_strech}.secondTerm', 1)
    cmds.setAttr(f'{condition_strech}.operation', 2)

    blendColor_strech = cmds.shadingNode('blendColors', name=f'{name}_strech_bc', asUtility=True)
    cmds.connectAttr(f'{condition_strech}.outColorR', f'{blendColor_strech}.color1R')
    cmds.connectAttr(f'{side}_Hand_ctrl.strech', f'{blendColor_strech}.blender')
    cmds.setAttr(f'{blendColor_strech}.color2R', 1)
    cmds.connectAttr(f'{blendColor_strech}.output.outputR',
                     f'{side}_{ARM_JOINTS[1]}_{chains[2]}.scale.scaleX')
    cmds.connectAttr(f'{blendColor_strech}.output.outputR',
                     f'{side}_{ARM_JOINTS[2]}_{chains[2]}.scale.scaleX')

    pow_volumen = cmds.shadingNode('multiplyDivide', name=f'{name}_volum_pow', asUtility=True)
    cmds.connectAttr(f'{condition_strech}.outColorR',f'{pow_volumen}.input1.input1X')
    cmds.setAttr(f'{pow_volumen}.input2.input2X', .5)
    cmds.setAttr(f'{pow_volumen}.operation', 3)

    volum_md = cmds.shadingNode('multiplyDivide', name=f'{name}_volum_md', asUtility=True)
    cmds.connectAttr(f'{pow_volumen}.output.outputX', f'{volum_md}.input2.input2X')
    cmds.setAttr(f'{volum_md}.input1.input1X', 1)
    cmds.setAttr(f'{volum_md}.operation', 2)
    cmds.connectAttr(f'{volum_md}.output.outputX', f'{side}_{ARM_JOINTS[1]}_{chains[2]}.scale.scaleY')
    cmds.connectAttr(f'{volum_md}.output.outputX', f'{side}_{ARM_JOINTS[2]}_{chains[2]}.scale.scaleY')
    cmds.connectAttr(f'{volum_md}.output.outputX', f'{side}_{ARM_JOINTS[1]}_{chains[2]}.scale.scaleZ')
    cmds.connectAttr(f'{volum_md}.output.outputX', f'{side}_{ARM_JOINTS[2]}_{chains[2]}.scale.scaleZ')
    ##########################################################################################
    #SWITCH IK/FK
    ctrls_grp    = cmds.group(n=f'{name}_ctrls_grp', empty=True)
    ctrls_ik_grp = cmds.group(n=f'{name}_ik_ctrls_grp', empty=True)

    if cmds.objExists(f'{name}_switch_ctrl'): pass
    else: controls.Cube(color_name = color, name = f'{name}_switch_ctrl')

    attributes = ['tx','ty','tz','rx','ry','rz','sx','sy','sz','v']
    for attr in attributes:
        cmds.setAttr(f'{name}_switch_ctrl.{attr}', lock=True, keyable=False)
    cmds.addAttr(f'{name}_switch_ctrl', longName='IKFK', attributeType='float', 
                 defaultValue=1, minValue=0, maxValue=1, keyable=True, hidden=False) 

    constraint = cmds.pointConstraint(f'{side}_{ARM_JOINTS[-1]}_{chains[0]}', 
                                      f'{name}_switch_ctrl_adj', maintainOffset=False)
    cmds.delete(constraint)
    movement = cmds.getAttr(f'{side}_{ARM_JOINTS[-1]}_{chains[0]}.tx')
    cmds.select(f'{name}_switch_ctrl_adj')
    cmds.move(movement, y=True, relative=True)

    control_vis_rev = cmds.shadingNode('reverse', name=f'{name}_vis_tev', asUtility=True)
    cmds.connectAttr(f'{name}_switch_ctrl.IKFK', f'{control_vis_rev}.input.inputX')
    cmds.connectAttr(f'{control_vis_rev}.outputX', f'{side}_{ARM_JOINTS[1]}_fk_ctrl_adj.visibility')
    cmds.connectAttr(f'{name}_switch_ctrl.IKFK', f'{name}_ik_ctrls_grp.visibility')

    for joint in ARM_JOINTS:
        if joint == ARM_JOINTS[0]:pass
        else:
            for movement in ('translate', 'rotate', 'scale'):
                blend_color = cmds.shadingNode('blendColors',name=f'{side}_{joint}_switch_bc',asUtility=True)
                cmds.connectAttr(f'{name}_switch_ctrl.IKFK', f'{blend_color}.blender')
                cmds.connectAttr(f'{side}_{joint}_{chains[2]}.{movement}', f'{blend_color}.color1')
                cmds.connectAttr(f'{side}_{joint}_{chains[1]}.{movement}', f'{blend_color}.color2')
                cmds.connectAttr(f'{blend_color}.output', f'{side}_{joint}_{chains[0]}.{movement}')
    ##########################################################################################
    #CLEAN ARM SETUP
    module_grp   = cmds.group(name=f'{name}_mstr_grp', empty=True)

    if cmds.objExists(DO_NOT_TOUCH): pass
    else: cmds.group(name=DO_NOT_TOUCH, empty=True)

    cmds.parent(f'{side}_Hand_ctrl_adj', f'{name}_pv_ctrl_adj',ctrls_ik_grp)
    cmds.parent(ctrls_ik_grp, f'{side}_{ARM_JOINTS[0]}_fk_ctrl_adj', f'{name}_switch_ctrl_adj', ctrls_grp)
    cmds.parent(f'{side}_{ARM_JOINTS[0]}_{chains[0]}', ctrls_grp, module_grp)

    distance_arm = cmds.listRelatives(distance_arm, p=True)
    cmds.hide(locator_pv, ik_arm,distance_arm, f'{side}_{ARM_JOINTS[1]}_{chains[2]}', 
              f'{side}_{ARM_JOINTS[1]}_{chains[1]}', loc_dist_arm_1, loc_dist_arm_2)
    cmds.parent(distance_arm, DO_NOT_TOUCH)


# rig_arm(side='l', name='L_Arm')
# rig_arm(side='r', name='R_Arm')