##########################################################################################
import maya.cmds as cmds
import modules.controls as controls 
##########################################################################################
ARM_JOINTS=['Clavicle','Shoulder','Elbow','Wrist','HandTip']
chains = ['Wjnt','Fkjnt','Ikjnt']
color = ''
DO_NOT_TOUCH = 'DO_NOT_TOUCH'

def rig_arm(type='l_arm', name='L_Arm'):
    if   type == 'l_arm': 
        side  = 'L'
        color = 'Blue'
    elif type == 'r_arm': 
        side  = 'R'
        color = 'Red'
    ##########################################################################################
    #CREATE WJNT, FK AND IK CHAINS
    cmds.select(cl=True)
    for chain in chains:
        for joint in ARM_JOINTS:
            joint_arm = cmds.joint(n='%s_%s_%s'%(side, joint, chain))
            for axis in ('X','Y','Z'):
                rotate_axis = cmds.getAttr('Guide_%s_%s_jnt.jointOrient%s'%(name, joint,axis))
                cmds.setAttr('%s.jointOrient%s'%(joint_arm, axis), rotate_axis)
            constraint = cmds.pointConstraint('Guide_%s_%s_jnt'%(name, joint), joint_arm, mo=False)
            cmds.delete(constraint)      
        cmds.select(cl=True)            

    for chain in range(2):
        cmds.parent('%s_%s_%s'%(side, ARM_JOINTS[1], chains[chain+1]),'%s_%s_%s'%(side, ARM_JOINTS[0], chains[0]))
        cmds.delete('%s_%s_%s'%(side, ARM_JOINTS[0], chains[chain+1]))
    ##########################################################################################
    #CREATE FK CONTROLS
    for control in range(len(ARM_JOINTS)):
        controls.generate_control('Circle', color, '%s_%s_fk_ctrl'%(side, ARM_JOINTS[control]))
        if control == 0:
            constraint = cmds.pointConstraint('%s_%s_%s'%(side, ARM_JOINTS[control], chains[0]),
                                           '%s_%s_fk_ctrl_adj'%(side, ARM_JOINTS[control]), mo=False)
            cmds.delete(constraint)
        else: 
            constraint = cmds.parentConstraint('%s_%s_%s'%(side, ARM_JOINTS[control], chains[0]),
                                           '%s_%s_fk_ctrl_adj'%(side, ARM_JOINTS[control]), mo=False)
            cmds.delete(constraint)
        if ARM_JOINTS[control] == ARM_JOINTS[0]:
            cmds.parentConstraint('%s_%s_fk_ctrl'%(side, ARM_JOINTS[control]), 
                                  '%s_%s_%s'%(side, ARM_JOINTS[control], chains[0]), mo=True)
        elif ARM_JOINTS[control] == ARM_JOINTS[-1]: cmds.delete('%s_%s_fk_ctrl_adj'%(side, ARM_JOINTS[control]))
        else:
            cmds.parentConstraint('%s_%s_fk_ctrl'%(side, ARM_JOINTS[control]), 
                                  '%s_%s_%s'%(side, ARM_JOINTS[control], chains[1]), mo=True)
            cmds.parent('%s_%s_fk_ctrl_adj'%(side, ARM_JOINTS[control]), '%s_%s_fk_ctrl'%(side, ARM_JOINTS[control-1]))
    ##########################################################################################
    #CREATE IK
    ik_arm = cmds.ikHandle(n='%s_IK'%(name),sj='%s_%s_%s'%(side, ARM_JOINTS[1], chains[2]), 
                           ee='%s_%s_%s'%(side, ARM_JOINTS[3], chains[2]), solver='ikRPsolver' )[0]
    controls.generate_control('Cube', color, '%s_Hand_ctrl'%(side))
    constraint = cmds.parentConstraint('%s_%s_%s'%(side, ARM_JOINTS[3], chains[2]), '%s_Hand_ctrl_adj'%(side), mo=False)
    cmds.delete(constraint)
    cmds.parent(ik_arm, '%s_Hand_ctrl'%(side))
    cmds.orientConstraint('%s_Hand_ctrl'%(side), '%s_%s_%s'%(side, ARM_JOINTS[3], chains[2]))

    cmds.addAttr('%s_Hand_ctrl'%(side), ln='Sep', at='enum', en='********', k=True)
    cmds.setAttr('%s_Hand_ctrl.Sep'%(side),l=True)
    cmds.addAttr('%s_Hand_ctrl'%(side), ln='strech', at='float', dv=1, min=0, max=1, k=True, h=False)
    cmds.addAttr('%s_Hand_ctrl'%(side), ln='volumPresservation', at='float', dv=1, min=0, max=1, k=True)
    ##########################################################################################
    #CREATE POLE VECTOR
    pos_shoulder = cmds.xform('%s_%s_%s'%(side, ARM_JOINTS[1], chains[2]), ws=True, q=True, t=True)
    pos_elbow    = cmds.xform('%s_%s_%s'%(side, ARM_JOINTS[2], chains[2]), ws=True, q=True, t=True)
    pos_wrist    = cmds.xform('%s_%s_%s'%(side, ARM_JOINTS[3], chains[2]), ws=True, q=True, t=True)

    # distance_arm = cmds.distanceDimension(sp=(pos_shoulder), ep=(pos_wrist))
    distance_arm = cmds.distanceDimension(sp=(.1,0,0), ep=(1.1,0,0))
    distance_arm_locs = cmds.listConnections( distance_arm, d=False, s=True )
    loc_dist_arm_1 = distance_arm_locs[0]
    loc_dist_arm_2 = distance_arm_locs[1]
    cmds.select(loc_dist_arm_1)
    cmds.xform(r=False, t=pos_shoulder)
    cmds.parent(loc_dist_arm_1, '%s_%s_fk_ctrl'%(side, ARM_JOINTS[0]))
    cmds.select(loc_dist_arm_2)
    cmds.xform(r=False, t=pos_wrist)
    cmds.parent(loc_dist_arm_2, '%s_Hand_ctrl'%(side))
    distance_arm_value = cmds.getAttr("%s.distance"%(distance_arm)) 
    
    controls.generate_control('Cone', color, '%s_pv_ctrl'%(name))
    constraint = cmds.pointConstraint('%s_%s_%s'%(side, ARM_JOINTS[2], chains[2]), '%s_pv_ctrl_adj'%(name), mo=False)
    cmds.delete(constraint)
    cmds.select('%s_pv_ctrl_adj'%(name))
    cmds.move(-(distance_arm_value), z=True,r=True)
    
    curve_pv = cmds.curve(n='%s_cv_pv'%(name),d=1, p=(pos_shoulder, pos_elbow, pos_wrist)) 
    cmds.moveVertexAlongDirection ('%s.cv[1]'%(curve_pv), n= distance_arm_value)
    locator_pv = cmds.spaceLocator(n='%s_pv_loc'%(name))[0]
    pos_pv= cmds.pointPosition ('%s.cv[1]'%(curve_pv))
    cmds.xform (locator_pv, ws=True, t=pos_pv)
    cmds.parent(locator_pv, '%s_pv_ctrl'%(name))
    cmds.poleVectorConstraint(locator_pv, ik_arm)

    cmds.delete(curve_pv)
    ##########################################################################################
    #STRECH AND VOLUMEN PRESSERVATION
    global_md = cmds.shadingNode('multiplyDivide', n='%s_global_md'%(name), au=True)
    cmds.setAttr('%s.operation'%(global_md), 2)
    cmds.connectAttr('%s.distance'%(distance_arm), '%s.input1.input1X'%(global_md))
    
    distance_arm1 = cmds.distanceDimension(sp=(pos_shoulder), ep=(pos_elbow))
    distance_arm1_value = cmds.getAttr("%s.distance"%(distance_arm1)) 
    distance_arm1 = cmds.listRelatives(distance_arm1, p=True)
    cmds.delete(distance_arm1)
    distance_arm2 = cmds.distanceDimension(sp=(pos_elbow), ep=(pos_wrist))
    distance_arm2_value = cmds.getAttr("%s.distance"%(distance_arm2)) 
    distance_arm2 = cmds.listRelatives(distance_arm2, p=True)
    cmds.delete(distance_arm2)
    distance_arm_strech = distance_arm1_value + distance_arm2_value
    
    strech_md = cmds.shadingNode('multiplyDivide', n='%s_strech_md'%(name), au=True)
    cmds.setAttr('%s.operation'%(strech_md), 2)
    cmds.connectAttr('%s.output.outputX'%(global_md), '%s.input1.input1X'%(strech_md))
    cmds.setAttr('%s.input2X'%(strech_md), distance_arm_strech)

    condition_strech = cmds.shadingNode('condition', n='%s_strech_con'%(name), au=True)
    cmds.connectAttr('%s.outputX'%(strech_md), '%s.firstTerm'%(condition_strech))
    cmds.connectAttr('%s.outputX'%(strech_md), '%s.colorIfTrueR'%(condition_strech))
    cmds.setAttr('%s.secondTerm'%(condition_strech), 1)
    cmds.setAttr('%s.operation'%(condition_strech), 2)

    blendColor_strech = cmds.shadingNode('blendColors', n='%s_strech_bc'%(name), au=True)
    cmds.connectAttr('%s.outColorR'%(condition_strech), '%s.color1R'%(blendColor_strech))
    cmds.connectAttr('%s_Hand_ctrl.strech'%(side), '%s.blender'%(blendColor_strech))
    cmds.setAttr('%s.color2R'%(blendColor_strech), 1)
    cmds.connectAttr('%s.output.outputR'%(blendColor_strech), '%s_%s_%s.scale.scaleX'%(side,ARM_JOINTS[1], chains[2]))
    cmds.connectAttr('%s.output.outputR'%(blendColor_strech), '%s_%s_%s.scale.scaleX'%(side,ARM_JOINTS[2], chains[2]))

    pow_volumen = cmds.shadingNode('multiplyDivide', n='%s_volum_pow'%(name), au=True)
    cmds.connectAttr('%s.outColorR'%(condition_strech), '%s.input1.input1X'%(pow_volumen))
    cmds.setAttr('%s.input2.input2X'%(pow_volumen), .5)
    cmds.setAttr('%s.operation'%(pow_volumen), 3)

    volum_md = cmds.shadingNode('multiplyDivide', n='%s_volum_md'%(name), au=True)
    cmds.connectAttr('%s.output.outputX'%(pow_volumen), '%s.input2.input2X'%(volum_md))
    cmds.setAttr('%s.input1.input1X'%(volum_md), 1)
    cmds.setAttr('%s.operation'%(volum_md), 2)
    cmds.connectAttr('%s.output.outputX'%(volum_md), '%s_%s_%s.scale.scaleY'%(side,ARM_JOINTS[1], chains[2]))
    cmds.connectAttr('%s.output.outputX'%(volum_md), '%s_%s_%s.scale.scaleY'%(side,ARM_JOINTS[2], chains[2]))
    cmds.connectAttr('%s.output.outputX'%(volum_md), '%s_%s_%s.scale.scaleZ'%(side,ARM_JOINTS[1], chains[2]))
    cmds.connectAttr('%s.output.outputX'%(volum_md), '%s_%s_%s.scale.scaleZ'%(side,ARM_JOINTS[2], chains[2]))
    ##########################################################################################
    #SWITCH IK/FK
    ctrls_grp    = cmds.group(n='%s_ctrls_grp'%(name), em=True)
    ctrls_ik_grp = cmds.group(n='%s_ik_ctrls_grp'%(name), em=True)

    if cmds.objExists('%s_switch_ctrl'%(name)): pass
    else: controls.generate_control('Cube', color, '%s_switch_ctrl'%(name))

    attributes = ['tx','ty','tz','rx','ry','rz','sx','sy','sz','v']
    for attr in attributes:
        cmds.setAttr('%s_switch_ctrl.%s'%(name,attr), lock=True, k=False)
    cmds.addAttr('%s_switch_ctrl'%(name), ln='IKFK', at='float', dv=1, min=0, max=1, k=True, h=False) 

    constraint = cmds.pointConstraint('%s_%s_%s'%(side,ARM_JOINTS[-1],chains[0]), '%s_switch_ctrl_adj'%(name), mo=False)
    cmds.delete(constraint)
    movement = cmds.getAttr('%s_%s_%s.tx'%(side,ARM_JOINTS[-1],chains[0]))
    cmds.select('%s_switch_ctrl_adj'%(name))
    cmds.move(movement, y=True,r=True)

    control_vis_rev = cmds.shadingNode('reverse', n='%s_vis_tev'%(name), au=True)
    cmds.connectAttr('%s_switch_ctrl.IKFK'%(name), '%s.input.inputX'%(control_vis_rev))
    cmds.connectAttr('%s.outputX'%(control_vis_rev), '%s_%s_fk_ctrl_adj.visibility'%(side, ARM_JOINTS[1]))
    cmds.connectAttr('%s_switch_ctrl.IKFK'%(name), '%s_ik_ctrls_grp.visibility'%(name))

    for joint in ARM_JOINTS:
        if joint == ARM_JOINTS[0]:pass
        else:
            for movement in ('translate', 'rotate', 'scale'):
                blend_color = cmds.shadingNode('blendColors',n='%s_%s_switch_bc'%(side,joint),au=True)
                cmds.connectAttr('%s_switch_ctrl.IKFK'%(name), '%s.blender'%(blend_color))
                cmds.connectAttr('%s_%s_%s.%s'%(side,joint,chains[2],movement), '%s.color1'%(blend_color))
                cmds.connectAttr('%s_%s_%s.%s'%(side,joint,chains[1],movement), '%s.color2'%(blend_color))
                cmds.connectAttr('%s.output'%(blend_color), '%s_%s_%s.%s'%(side,joint,chains[0],movement))
    ##########################################################################################
    #CLEAN ARM SETUP
    module_grp   = cmds.group(n='%s_mstr_grp'%(name), em=True)

    if cmds.objExists(DO_NOT_TOUCH): pass
    else: cmds.group(n=DO_NOT_TOUCH, em=True)

    cmds.parent('%s_Hand_ctrl_adj'%(side), '%s_pv_ctrl_adj'%(name),ctrls_ik_grp)
    cmds.parent(ctrls_ik_grp, '%s_%s_fk_ctrl_adj'%(side, ARM_JOINTS[0]), '%s_switch_ctrl_adj'%(name), ctrls_grp)
    cmds.parent('%s_%s_%s'%(side, ARM_JOINTS[0], chains[0]), ctrls_grp, module_grp)

    distance_arm = cmds.listRelatives(distance_arm, p=True)
    cmds.hide(locator_pv, ik_arm,distance_arm, '%s_%s_%s'%(side, ARM_JOINTS[1], chains[2]), 
              '%s_%s_%s'%(side, ARM_JOINTS[1], chains[1]),loc_dist_arm_1,loc_dist_arm_2)
    cmds.parent(distance_arm, DO_NOT_TOUCH)


# rig_arm(type='l_arm', name='L_Arm')
# rig_arm(type='r_arm', name='R_Arm')