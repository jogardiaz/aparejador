##########################################################################################
import maya.cmds as cmds

##########################################################################################
names=[]
GUIDES_MSTR_GRP='guides_grp'
GUIDES_JOINTS_GRP='guides_joint_grp'

##########################################################################################
#GENERATE GUIDES TO PIVOT THE JOINTS OF THE RIG
def generate_guides(body_part='', name='', amount=0, thumb=None, color='8', side='l'):

    def spine(name, amount, color):
        for number_guide in range(amount):
            guide_spine = cmds.spaceLocator(name=f'Guide_{name}_{(number_guide + 1)}')[0]
            
            if number_guide == 0: 
                guides_grp = cmds.group(name=f'{name}_guides_grp', empty=True)
                cmds.parent(guide_spine,guides_grp)
                cmds.parent(guides_grp, GUIDES_MSTR_GRP)  

            else:
                cmds.parent(guide_spine, f'Guide_{name}_{number_guide}')
                moveAmount = 2.8 / amount
                cmds.xform(guide_spine, translation=(0,moveAmount,0), objectSpace=True)

            cmds.setAttr(f'{guide_spine}.overrideEnabled', True)
            cmds.setAttr(f'{guide_spine}.overrideColor', color)
        cmds.xform(f'Guide_{name}_1', translation=(0, 9, 0), objectSpace=True)
        
##########################################################################################
    def arm(name, color, side):
        if side == 'l': arm_pos = ((.1, 12, 0), (.85, .35, 0), (2.15, 0, 0),
                                   (2.5, 0, 0), (1, 0, 0))
        elif side == 'r': arm_pos = ((-.1, 12, 0), (-.85, .35, 0), (-2.15, 0, 0),
                                     (-2.5, 0, 0), (-1, 0, 0))

        ARM_GUIDES = ('Clavicle', 'Shoulder', 'Elbow', 'Wrist', 'HandTip')

        for number_guide in range(len(ARM_GUIDES)):
            guide_arm = cmds.spaceLocator(n='Guide_%s_%s' % (name, ARM_GUIDES[number_guide]))[0]
           
            if ARM_GUIDES[number_guide] == ARM_GUIDES[0]:
                guides_grp = cmds.group(n='%s_guides_grp'%(name), em=True)
                cmds.parent(guide_arm,guides_grp)
                cmds.parent(guides_grp, GUIDES_MSTR_GRP)                    
           
            else: cmds.parent(guide_arm, 'Guide_%s_%s' % (name, ARM_GUIDES[number_guide - 1]))
                
            cmds.setAttr(guide_arm + '.overrideEnabled', True)
            cmds.setAttr(guide_arm + '.overrideColor', color)
            cmds.xform('Guide_%s_%s' % (name, ARM_GUIDES[number_guide]), t=arm_pos[number_guide], os=True)
        
##########################################################################################
    def leg(name, color, side):
        if side == 'l': leg_pos = ((.34, 8.6, 0), (.14, -.8, 0), (0, -3.7, .1), 
                                   (0, -3.4, -.1), (0, -.52, .65), (0, 0, .9))
        elif side == 'r': leg_pos = ((-.34, 8.6, 0), (-.14, -.8, 0), (0, -3.7, .1),
                                     (0, -3.4, -.1), (0, -.52, .65), (0, 0, .9))

        LEG_GUIDES = ('Pelvis', 'Hip', 'Knee', 'Ankle', 'Ball', 'FootTip')
        
        
        for number_guide in range(len(LEG_GUIDES)):
            guide_leg = cmds.spaceLocator(n='Guide_%s_%s' % (name, LEG_GUIDES[number_guide]))[0]
            
            if LEG_GUIDES[number_guide] == LEG_GUIDES[0]: 
                guides_grp = cmds.group(n='%s_guides_grp'%(name), em=True)
                cmds.parent(guide_leg,guides_grp)
                cmds.parent(guides_grp, GUIDES_MSTR_GRP)
            
            else: cmds.parent(guide_leg, 'Guide_%s_%s' % (name, LEG_GUIDES[number_guide - 1]))

            cmds.setAttr(guide_leg + '.overrideEnabled', True)
            cmds.setAttr(guide_leg + '.overrideColor', color)
            cmds.xform('Guide_%s_%s' % (name, LEG_GUIDES[number_guide]), t=leg_pos[number_guide], os=True)

##########################################################################################
    def hand(name, thumb, amount, color, side):
        if side == 'l':
            thumb_pos = ((5.6, 12.3, .17), (.075, 0, .06), (.16, 0, .12), (.15, 0, .25), (.1, 0, .2))
            fingers_pos = (
                ((5.65, 12.3, .11), (.6, 0, .13), (.22, 0, 0), (.18, 0, 0), (.19, 0, 0)),
                ((5.65, 12.3, .07), (.6, 0, .01), (.29, 0, 0), (.19, 0, 0), (.2, 0, 0)),
                ((5.65, 12.3, -.037), (.59, 0, -.03), (.26, 0, 0), (.17, 0, 0), (.19, 0, 0)),
                ((5.65, 12.3, -.1), (.56, 0, -.1), (.18, 0, 0), (.15, 0, 0), (.15, 0, 0))
            )
            extra_finger_pos = ((5.65, 12.3, -.15), (.56, 0, -.1), (.18, 0, 0), (.15, 0, 0), (.15, 0, 0))
        elif side == 'r':
            thumb_pos = ((-5.6, 12.3, .17), (-.075, 0, .06), (-.16, 0, .12), (-.15, 0, .25), (-.1, 0, .2))
            fingers_pos = (
                ((-5.65, 12.3, .11), (-.6, 0, .13), (-.22, 0, 0), (-.18, 0, 0), (-.19, 0, 0)),
                ((-5.65, 12.3, .07), (-.6, 0, .01), (-.29, 0, 0), (-.19, 0, 0), (-.2, 0, 0)),
                ((-5.65, 12.3, -.037), (-.59, 0, -.03), (-.26, 0, 0), (-.17, 0, 0), (-.19, 0, 0)),
                ((-5.65, 12.3, -.1), (-.56, 0, -.1), (-.18, 0, 0), (-.15, 0, 0), (-.15, 0, 0))
            )
        extra_finger_pos = ((-5.65, 12.3, -.15), (-.56, 0, -.1), (-.18, 0, 0), (-.15, 0, 0), (-.15, 0, 0))
        guides_grp = cmds.group(n=f'{name}_guides_grp', empty=True)
        cmds.parent(guides_grp, GUIDES_MSTR_GRP)

        if thumb:
            for number_guide in range(5):
                guide_thumb = cmds.spaceLocator(n=f'Guide_{name}_Thumb{number_guide + 1}')[0]
                
                if number_guide == 0: cmds.parent(guide_thumb, guides_grp)
                else: cmds.parent(guide_thumb, f'Guide_{name}_Thumb{number_guide}')
                
                cmds.setAttr(f'{guide_thumb}.overrideEnabled', True)
                cmds.setAttr(f'{guide_thumb}.overrideColor', color)
                cmds.xform(f'Guide_{name}_Thumb{number_guide + 1}', translation=thumb_pos[number_guide], 
                           objectSpace=True)                


        fingers = ('Index', 'Middle', 'Ring', 'Pinky')
        if amount <= 4:
            for finger in range(amount):
                for number_guide in range(5):
                    guide_finger = cmds.spaceLocator(n=f'Guide_{name}_{fingers[finger]}{number_guide + 1}')[0]
                    
                    if number_guide == 0: cmds.parent(guide_finger, guides_grp)
                    else: cmds.parent(guide_finger, f'Guide_{name}_{fingers[finger]}{number_guide}')
                    
                    cmds.setAttr(f'{guide_finger}.overrideEnabled', True)
                    cmds.setAttr(f'{guide_finger}.overrideColor', color)
                    cmds.xform(f'Guide_{name}_{fingers[finger]}{number_guide + 1}',
                               translation=fingers_pos[finger][number_guide], objectSpace=True)

        else:
            for finger in range(len(fingers)):
                for number_guide in range(5):
                    guide_finger = cmds.spaceLocator(n=f'Guide_{name}_{fingers[finger]}{number_guide + 1}')[0]
                    
                    if number_guide == 0: cmds.parent(guide_finger, guides_grp)
                    else: cmds.parent(guide_finger, f'Guide_{name}_{fingers[finger]}{number_guide}')
                    
                    cmds.setAttr(f'{guide_finger}.overrideEnabled', True)
                    cmds.setAttr(f'{guide_finger}.overrideColor', color)
                    cmds.xform(f'Guide_{name}_{fingers[finger]}{number_guide + 1}',
                               translation=fingers_pos[finger][number_guide], objectSpace=True)

            for finger in range(amount - 4):
                for number_guide in range(5):
                    guide_finger = cmds.spaceLocator(n=f'Guide_{name}_extraFinger_{finger + 1}_{number_guide + 1}')[0]
                    
                    if number_guide == 0:
                        print(finger + 1.0) / 10
                        cmds.move(5.65, 12.3, extra_finger_pos[0][2] - ((finger + 1.0) / 10), guide_finger, localSpace=True)
                        cmds.parent(guide_finger, guides_grp)
                    
                    else:
                        cmds.parent(guide_finger, f'Guide_{name}_extraFinger_{finger + 1}_{number_guide}')
                    
                    cmds.setAttr(f'{guide_finger}.overrideEnabled', True)
                    cmds.setAttr(f'{guide_finger}.overrideColor', color)
                
                for number_guide in range(1, 5):
                    cmds.xform(f'Guide_{name}_extraFinger_{finger + 1}_{number_guide + 1}',
                               translation=extra_finger_pos[number_guide], objectSpace=1)
    
##########################################################################################
    def foot(name, color, side):
        if side == 'l': foot_pos = ((.47, 0, -.3), (0, 0, 1.8), (-.39, 0, -.5),
                                   (.77, 0, 0), (-.39, 0, 0), (-.39, 0, 0))
        elif side == 'r': foot_pos = ((-.47, 0, -.3), (0, 0, 1.8), (.39, 0, -.5),
                                     (-.77, 0, 0), (.39, 0, 0), (.39, 0, 0))

        FOOT_GUIDES = ['heel', 'tip', 'in', 'out', 'ball', 'toes']

        for number_guide in range(len(FOOT_GUIDES)):
            guide_foot = cmds.spaceLocator(n=f'Guide_{name}_{FOOT_GUIDES[number_guide]}')[0]
            
            if number_guide == 0: 
                guides_grp = cmds.group(n=f'{name}_guides_grp', empty=True)
                cmds.parent(guide_foot,guides_grp)
                cmds.parent(guides_grp, GUIDES_MSTR_GRP)
            
            elif number_guide == 5: cmds.parent(guide_foot, f'Guide_{name}_{FOOT_GUIDES[3]}')
            
            else: cmds.parent(guide_foot, f'Guide_{name}_{FOOT_GUIDES[number_guide-1]}')
            
            cmds.setAttr(guide_foot + '.overrideEnabled', True)
            cmds.setAttr(guide_foot + '.overrideColor', color)
            cmds.xform(guide_foot, t=foot_pos[number_guide], objectSpace=True)

##########################################################################################
    def neck(name, amount, color):
        for number_guide in range(amount):
            guide_neck = cmds.spaceLocator(n=f'Guide_{name}_{number_guide + 1}')[0]
            
            if number_guide == 0: 
                guides_grp = cmds.group(n=f'{name}_guides_grp', empty=True)
                cmds.parent(guide_neck,guides_grp)
                cmds.parent(guides_grp, GUIDES_MSTR_GRP)
            
            else:
                cmds.parent(guide_neck, f'Guide_{name}_{number_guide}')
                moveAmount = 1.6 / amount
                cmds.move(0, moveAmount, 0, localSpace=1)
            
            cmds.setAttr(guide_neck + '.overrideEnabled', 1)
            cmds.setAttr(guide_neck + '.overrideColor', color)
        
        cmds.xform(f'Guide_{name}_1', translation=(0, 12.5, 0), objectSpace=True)

##########################################################################################
    def guide_type(body_part, amount, color, side):
        if cmds.objExists(GUIDES_MSTR_GRP): pass                    
        else: cmds.group(n=GUIDES_MSTR_GRP, em=True)
                    
        type_guide = {
            "spine" : spine,
            "arm" : arm,
            "leg" : leg,
            "hand": hand,
            "foot": foot,
            "neck"  : neck,
        }

        color_ctl = {
            "yellow": 17,
            "green": 14,
            "red": 13,
            "blue": 6,
            "pink": 20,
            "littleBlue": 18,
            "white": 16,
            'littleGreen': 19
        }

        type = type_guide.get(body_part)
        color = color_ctl.get(color)
        if type == spine or type == neck: type(name, amount, color)   
        elif type == hand: type(name, thumb, amount, color, side)
        elif type == arm or type == leg or type == foot: type(name, color, side)
        else: type(name, color)
        
    if cmds.objExists(name):
        cmds.warning('Guide_%s_already_exist' % (name))
        pass
    else: guide_type(body_part, amount, color, side)

##########################################################################################
#FIX GUIDES SHAPES FOR BETTER VISUALIZATION
def guides_sizes(resize = .2):
    cmds.select('Guide*')
    sel = cmds.ls(sl=True)

    for guide in sel: 
        if 'Shape' in guide:
            for axis in ('X','Y','Z'):
                cmds.setAttr(f'{guide}.localScale{axis}', resize)

    cmds.select(cl=True)
    
##########################################################################################
def mirror_guides(correct_side='', mirror_to=''):      
    list_correct_guides = cmds.listRelatives(f'{correct_side}_guides_grp',
                                             allDescendents=True)
    list_correct_guides.reverse()
    list_mirror_to_guides = cmds.listRelatives(f'{mirror_to}_guides_grp',
                                               allDescendents=True)
    list_mirror_to_guides.reverse()
    
    if len(list_correct_guides) != len(list_mirror_to_guides): 
        cmds.warning('Choose similar modules')
    
    cmds.setAttr(f'{mirror_to}_guides_grp.scaleX', 1)

    for guide in range(len(list_correct_guides)):
        
        if 'Shape' in list_correct_guides[guide] : pass
        
        else:
            constraint = cmds.parentConstraint(list_correct_guides[guide], 
                                               list_mirror_to_guides[guide],mo=False)
            cmds.delete(constraint)

    cmds.setAttr(f'{mirror_to}_guides_grp.scaleX', -1)

##########################################################################################
#GENERATE JOINTS IN THE SAME POSITION THAN GUIDES FOR ORIENT PROPOURSES
def joints(vis = False):
    cmds.hide(GUIDES_MSTR_GRP)

    list_guides = cmds.listRelatives(GUIDES_MSTR_GRP, ad=True)

    if cmds.objExists(GUIDES_JOINTS_GRP): pass
    else: cmds.group(n=GUIDES_JOINTS_GRP, em=True)

    for guide in list_guides:
        if 'Shape' in guide: pass
        elif 'Guide_' in guide:
            cmds.select(cl=True)
            jnt = cmds.joint(n=guide + '_jnt')
            constraint = cmds.parentConstraint(guide, jnt, mo=False)
            cmds.delete(constraint)
    for guide in list_guides:
        if 'Shape' in guide: pass
        elif 'Guide_' in guide:
            father = cmds.listRelatives(guide, p=True)[0]
            if '_grp' in father: cmds.parent(guide + '_jnt', GUIDES_JOINTS_GRP)
            else: cmds.parent(guide + '_jnt', father + '_jnt')

    orientJnts(vis)

def orientJnts(vis):
    jnts = cmds.listRelatives(GUIDES_JOINTS_GRP, ad=1)
    for jnt in jnts:
        cmds.makeIdentity(jnt, apply=True, t=True, r=True, s=True)
    for jnt in jnts:
        cmds.joint(jnt, e=True, zso=True, oj='xzy', sao='yup')
    cmds.setAttr(GUIDES_JOINTS_GRP + '.visibility', vis)
    cmds.select(cl=True)

##########################################################################################
# THIS WAY YOU CAN GENERATE THE GUIDES
# generate_guides(body_part='arm',   name='L_Arm',  color='blue', side='l')
# generate_guides(body_part='arm',   name='R_Arm',  color='red',  side='r')
# generate_guides(body_part='leg',   name='L_Leg',  color='blue', side='l')
# generate_guides(body_part='leg',   name='R_Leg',  color='red',  side='r')
# generate_guides(body_part='foot',  name='L_Foot', color='littleBlue', side='l')
# generate_guides(body_part='foot',  name='R_Foot', color='pink', side='r')
# generate_guides(body_part='spine', name='Spine',  amount=5, color='yellow')
# generate_guides(body_part='neck',  name='Neck',   amount=3, color='yellow')
# generate_guides(body_part='hand',  name='L_Hand', thumb=True, amount=4, side='l', color='littleBlue')
# generate_guides(body_part='hand',  name='R_Hand', thumb=True, amount=4, side='r', color='pink')

# guides_sizes(resize=.2)

# ##########################################################################################
# #MIRROR IF NECESSARY AND CREATE JOINTS WITH VISIBILITY IF NECESSARY
# mirror_guides(correct_side='L_Arm', mirror_to='R_Arm')
# mirror_guides(correct_side='L_Leg', mirror_to='R_Leg')
# mirror_guides(correct_side='L_Foot', mirror_to='R_Foot')
# mirror_guides(correct_side='L_Hand', mirror_to='R_Hand')

#joints(vis=True)

