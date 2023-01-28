##########################################################################################
import maya.cmds as cmds
import modules.controls as controls 
##########################################################################################
ARM_JOINTS=['Clavicle','Shoulder','Elbow','Wrist','HandTip']
chains = ['Wjnt','Fkjnt','Ikjnt']
color = ''

def arm(name='L_Arm' ,side='l_arm'):
    if   side == 'l_arm': 
        side = 'L'
        color = 'Blue'
    elif side == 'r_arm': 
        side = 'R'
        color = 'Red'
    
    #CREATE WJNT, FK AND IK CHAINS
    cmds.select(cl=True)
    for chain in chains:
        for joint in ARM_JOINTS:
            joint_arm = cmds.joint(n='%s_%s_%s'%(side, joint, chain))
            constraint = cmds.parentConstraint('Guide_%s_%s_jnt'%(name, joint), joint_arm, mo=False)
            cmds.delete(constraint)      
        cmds.select(cl=True)            

    for chain in range(2):
        cmds.parent('%s_%s_%s'%(side, ARM_JOINTS[1], chains[chain+1]),'%s_%s_%s'%(side, ARM_JOINTS[0], chains[0]))
        cmds.delete('%s_%s_%s'%(side, ARM_JOINTS[0], chains[chain+1]))
        
    #CREATE FK CONTROLS
    for control in range(len(ARM_JOINTS)):
        controls.generate_control('Circle', color, '%s_%s_fk_ctrl'%(side, ARM_JOINTS[control]))
        constraint = cmds.parentConstraint('%s_%s_%s'%(side, ARM_JOINTS[control], chains[0]),
                                           '%s_%s_fk_ctrl_adj'%(side, ARM_JOINTS[control]), mo=False)
        cmds.delete(constraint)
        if ARM_JOINTS[control] == ARM_JOINTS[0]:
            cmds.parentConstraint('%s_%s_fk_ctrl_adj'%(side, ARM_JOINTS[control]), '%s_%s_%s'%(side, ARM_JOINTS[control], chains[0]))
        elif ARM_JOINTS[control] == ARM_JOINTS[-1]: cmds.delete('%s_%s_fk_ctrl_adj'%(side, ARM_JOINTS[control]))
        else:
            cmds.parentConstraint('%s_%s_fk_ctrl_adj'%(side, ARM_JOINTS[control]), '%s_%s_%s'%(side, ARM_JOINTS[control], chains[1]))
            cmds.parent('%s_%s_fk_ctrl_adj'%(side, ARM_JOINTS[control]), '%s_%s_fk_ctrl'%(side, ARM_JOINTS[control-1]))
        
        
arm(name='L_Arm',side='l_arm')
arm(name='R_Arm',side='r_arm')


