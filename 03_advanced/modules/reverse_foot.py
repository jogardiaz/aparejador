##########################################################################################
import maya.cmds as cmds

##########################################################################################
REVERSE_FOOT_LOCS = ['heel','tip','in','out','ball','toes']

#Create attributes in the control and connect to the rotation of the locators
def create_reverse_foot(side='', name='',connect_to=''):
    if   side == 'l': side  = 'L'
    elif side == 'r': side  = 'R'

    ##########################################################################################
    #CREATE FINAL LOCATORS AND HIERARCHY
    cmds.select(clear=True)

    for locator in range(len(REVERSE_FOOT_LOCS)):

        loc_reverse = cmds.spaceLocator(name=f'{name}_{REVERSE_FOOT_LOCS[locator]}_reverse_foot')[0]
        offset = cmds.group(name=f'{name}_{REVERSE_FOOT_LOCS[locator]}_reverse_foot_adj')
        constraint = cmds.parentConstraint(f'Guide_{name}_{REVERSE_FOOT_LOCS[locator]}',
                                           offset, maintainOffset=False)
        cmds.delete(constraint)      
        
        if locator == 0: pass
        else: cmds.parent(offset, f'{name}_{REVERSE_FOOT_LOCS[locator-1]}_reverse_foot')
    
    cmds.parent(f'{name}_{REVERSE_FOOT_LOCS[5]}_reverse_foot_adj', f'{name}_{REVERSE_FOOT_LOCS[3]}_reverse_foot')
    cmds.select(clear=True)

    #########################################################################################
    #CONNECT LOCATORS TO CONTROL
    control = f'{connect_to}_switch_ctrl'
    cmds.select(control)
    cmds.addAttr(longName='Sep', attributeType='enum', enumName='********', hidden=False, 
                 keyable=True, readable=True, writable=True)
    cmds.setAttr(f'{control}.Sep', lock=True)

    cmds.addAttr(longName='TipSwivel', attributeType='float', hidden=False, keyable=True,
                 readable=True, writable=True)
    cmds.connectAttr(f'{control}.TipSwivel', f'{name}_{REVERSE_FOOT_LOCS[1]}_reverse_foot.rotateY')

    cmds.addAttr(longName='BallSwivel', attributeType='float', hidden=False, keyable=True,
                 readable=True, writable=True)
    cmds.connectAttr(f'{control}.BallSwivel', f'{name}_{REVERSE_FOOT_LOCS[4]}_reverse_foot.rotateY')
    cmds.connectAttr(f'{control}.BallSwivel', f'{name}_{REVERSE_FOOT_LOCS[5]}_reverse_foot.rotateY')

    cmds.addAttr(longName='TipRotation', attributeType='float', hidden=False, keyable=True,
                 readable=True, writable=True)
    cmds.connectAttr(f'{control}.TipRotation', f'{name}_{REVERSE_FOOT_LOCS[1]}_reverse_foot.rotateX')

    cmds.addAttr(longName='HeelBall', attributeType='float', min=-10, max=10, hidden=False,
                 keyable=True, readable=True, writable=True)
    hell_ball_rev = cmds.shadingNode('remapValue', asUtility=True, name=f'{control}_heelBall_Heel_rv')
    cmds.connectAttr(f'{control}.HeelBall', f'{hell_ball_rev}.inputValue')
    cmds.setAttr(f'{hell_ball_rev}.inputMax', 10)
    cmds.setAttr(f'{hell_ball_rev}.outputMax', -45)    
    cmds.connectAttr(f'{hell_ball_rev}.outColorR', f'{name}_{REVERSE_FOOT_LOCS[0]}_reverse_foot.rotateX')
    
    hell_ball_rev_neg = cmds.shadingNode('remapValue', asUtility=True, name=f'{control}_heelBall_Ball_rv')
    cmds.connectAttr(f'{control}.HeelBall',f'{hell_ball_rev_neg}.inputValue')
    cmds.setAttr(f'{hell_ball_rev_neg}.inputMax', 0)
    cmds.setAttr(f'{hell_ball_rev_neg}.outputMax', 0)
    cmds.setAttr(f'{hell_ball_rev_neg}.inputMin', -10)
    cmds.setAttr(f'{hell_ball_rev_neg}.outputMin', 45)
    cmds.connectAttr(f'{hell_ball_rev_neg}.outColorR', f'{name}_{REVERSE_FOOT_LOCS[4]}_reverse_foot.rotateX')

    cmds.select(control)
    cmds.addAttr(longName='FootTilt', attributeType='float', min=-10, max=10, hidden=False,
                 keyable=True, readable=True, writable=True)
    foot_tilt_rv = cmds.shadingNode('remapValue', asUtility=True, name=f'{control}FootTilt_out_rv')
    cmds.connectAttr(f'{control}.FootTilt',f'{foot_tilt_rv}.inputValue')
    cmds.setAttr(f'{foot_tilt_rv}.inputMax', 10)
    cmds.setAttr(f'{foot_tilt_rv}.outputMax', -45)    
    cmds.connectAttr(f'{foot_tilt_rv}.outColorR', f'{name}_{REVERSE_FOOT_LOCS[3]}_reverse_foot.rotateZ')

    foot_tilt_rv_2 = cmds.shadingNode('remapValue', asUtility=True, name=f'{control}FootTilt_in_rv')
    cmds.connectAttr(f'{control}.FootTilt',f'{foot_tilt_rv_2}.inputValue')
    cmds.setAttr(f'{foot_tilt_rv_2}.inputMin', -10)
    cmds.setAttr(f'{foot_tilt_rv_2}.outputMin', 45)
    cmds.setAttr(f'{foot_tilt_rv_2}.inputMax', 0)
    cmds.setAttr(f'{foot_tilt_rv_2}.outputMax', 0)
    cmds.connectAttr(f'{foot_tilt_rv_2}.outColorR', f'{name}_{REVERSE_FOOT_LOCS[2]}_reverse_foot.rotateZ')

    cmds.select(control)
    cmds.addAttr(longName='Toes', attributeType='float', hidden=False, keyable=True,
                 readable=True, writable=True)
    cmds.connectAttr(f'{control}.Toes',f'{name}_{REVERSE_FOOT_LOCS[5]}_reverse_foot.rotateX')

    #CLEAN SETUP
    cmds.parent(f'{name}_{REVERSE_FOOT_LOCS[0]}_reverse_foot_adj', f'{side}_Foot_ctrl')
    cmds.parent(f'{connect_to}_ball_IK', f'{connect_to}_IK', f'{name}_ball_reverse_foot')
    cmds.parent(f'{connect_to}_toe_IK', f'{name}_toes_reverse_foot')
    cmds.hide(f'{name}_{REVERSE_FOOT_LOCS[0]}_reverse_foot_adj')
