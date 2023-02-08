import maya.cmds as cmds

REVERSE_FOOT_LOCS = ['heel','tip','in','out','ball','toes']

#Create attributes in the control and connect to the rotation of the locators
def create_reverse_foot(type='', name='',connect_to=''):
    if   type == 'l_foot': side  = 'L'
    elif type == 'r_foot': side  = 'R'
    ##########################################################################################
    #CREATE FINAL LOCATORS AND HIERARCHY
    cmds.select(cl=True)
    for locator in range(len(REVERSE_FOOT_LOCS)):
        loc_reverse = cmds.spaceLocator(n='%s_%s_reverse_foot'%(name, REVERSE_FOOT_LOCS[locator]))[0]
        offset = cmds.group(n='%s_%s_reverse_foot_adj'%(name, REVERSE_FOOT_LOCS[locator]))
        constraint = cmds.parentConstraint('Guide_%s_%s'%(name, REVERSE_FOOT_LOCS[locator]), offset, mo=False)
        cmds.delete(constraint)      
        if locator == 0: pass
        else: cmds.parent(offset, '%s_%s_reverse_foot'%(name, REVERSE_FOOT_LOCS[locator-1]))
    cmds.parent(f'{name}_{REVERSE_FOOT_LOCS[5]}_reverse_foot_adj', f'{name}_{REVERSE_FOOT_LOCS[3]}_reverse_foot')
    cmds.select(cl=True)
    #########################################################################################
    #CONNECT LOCATORS TO CONTROL
    control = '%s_switch_ctrl'%(connect_to)
    cmds.select(control)
    cmds.addAttr(ln='Sep', at='enum', en='********', h=False, k=True, r=True, w=True)
    cmds.setAttr('%s.Sep'%(control),l=True)

    cmds.addAttr(ln='TipSwivel', at='float', h=False, k=True, r=True, w=True)
    cmds.connectAttr(control+'.TipSwivel','%s_%s_reverse_foot.rotateY'%(name, REVERSE_FOOT_LOCS[1]))

    cmds.addAttr(ln='BallSwivel', at='float', h=False, k=True, r=True, w=True)
    cmds.connectAttr('%s.BallSwivel'%(control),'%s_%s_reverse_foot.rotateY'%(name, REVERSE_FOOT_LOCS[4]))
    cmds.connectAttr('%s.BallSwivel'%(control),'%s_%s_reverse_foot.rotateY'%(name, REVERSE_FOOT_LOCS[5]))

    cmds.addAttr(ln='TipRotation', at='float', h=False, k=True, r=True, w=True)
    cmds.connectAttr('%s.TipRotation'%(control),'%s_%s_reverse_foot.rotateX'%(name, REVERSE_FOOT_LOCS[1]))

    cmds.addAttr(ln='HeelBall', at='float', min=-10, max=10, h=False, k=True, r=True, w=True)
    hell_ball_rev = cmds.shadingNode('remapValue',au=True, n='%s_heelBall_Heel_rv'%(control))
    cmds.connectAttr('%s.HeelBall'%(control),'%s.inputValue'%(hell_ball_rev))
    cmds.setAttr('%s.inputMax'%(hell_ball_rev), 10)
    cmds.setAttr('%s.outputMax'%(hell_ball_rev), -45)    
    cmds.connectAttr('%s.outColorR'%(hell_ball_rev), '%s_%s_reverse_foot.rotateX'%(name, REVERSE_FOOT_LOCS[0]))
    
    hell_ball_rev_neg = cmds.shadingNode('remapValue',au=True, n='%s_heelBall_Ball_rv'%(control))
    cmds.connectAttr('%s.HeelBall'%(control),'%s.inputValue'%(hell_ball_rev_neg))
    cmds.setAttr('%s.inputMax'%(hell_ball_rev_neg), 0)
    cmds.setAttr('%s.outputMax'%(hell_ball_rev_neg), 0)
    cmds.setAttr('%s.inputMin'%(hell_ball_rev_neg), -10)
    cmds.setAttr('%s.outputMin'%(hell_ball_rev_neg), 45)
    cmds.connectAttr('%s.outColorR'%(hell_ball_rev_neg), '%s_%s_reverse_foot.rotateX'%(name, REVERSE_FOOT_LOCS[4]))

    cmds.select(control)
    cmds.addAttr(ln='FootTilt', at='float', min=-10, max=10, h=False, k=True, r=True, w=True)
    foot_tilt_rv = cmds.shadingNode('remapValue',au=True, n=control + 'FootTilt_out_rv')
    cmds.connectAttr('%s.FootTilt'%(control),'%s.inputValue'%(foot_tilt_rv))
    cmds.setAttr('%s.inputMax'%(foot_tilt_rv), 10)
    cmds.setAttr('%s.outputMax'%(foot_tilt_rv), -45)    
    cmds.connectAttr('%s.outColorR'%(foot_tilt_rv), '%s_%s_reverse_foot.rotateZ'%(name, REVERSE_FOOT_LOCS[3]))

    foot_tilt_rv_2 = cmds.shadingNode('remapValue',au=True, n=control + 'FootTilt_in_rv')
    cmds.connectAttr(control+'.FootTilt','%s.inputValue'%(foot_tilt_rv_2))
    cmds.setAttr('%s.inputMin'%(foot_tilt_rv_2), -10)
    cmds.setAttr('%s.outputMin'%(foot_tilt_rv_2), 45)
    cmds.setAttr('%s.inputMax'%(foot_tilt_rv_2), 0)
    cmds.setAttr('%s.outputMax'%(foot_tilt_rv_2), 0)
    cmds.connectAttr('%s.outColorR'%(foot_tilt_rv_2), '%s_%s_reverse_foot.rotateZ'%(name, REVERSE_FOOT_LOCS[2]))

    cmds.select(control)
    cmds.addAttr(ln='Toes', at='float', h=False, k=True, r=True, w=True)
    cmds.connectAttr('%s.Toes'%(control),'%s_%s_reverse_foot.rotateX'%(name, REVERSE_FOOT_LOCS[5]))

    #CLEAN SETUP
    cmds.parent('%s_%s_reverse_foot_adj'%(name, REVERSE_FOOT_LOCS[0]), '%s_Foot_ctrl'%(side))
    cmds.parent(f'{connect_to}_ball_IK', f'{connect_to}_IK', f'{name}_ball_reverse_foot')
    cmds.parent(f'{connect_to}_toe_IK', f'{name}_toes_reverse_foot')
    cmds.hide(f'{name}_{REVERSE_FOOT_LOCS[0]}_reverse_foot_adj')
