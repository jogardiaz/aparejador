import maya.cmds as cmds

names=[]
GUIDES_GRP='guides_grp'
GUIDES_JOINTS_GRP='guides_joint_grp'

#GENERATE GUIDES TO PIVOT THE JOINTS OF THE RIG
def generate_guides(type, name, amount=0, thumb=None, color='8'):
    def spine(name, amount, color):
        for number_guide in range(amount):
            guide_spine = cmds.spaceLocator(n='Guide_%s_%s' % (name, str(number_guide + 1)))[0]
            if number_guide == 0: cmds.parent(guide_spine, GUIDES_GRP)                
            else:
                cmds.parent(guide_spine, 'Guide_%s_%s' % (name, str(number_guide)))
                moveAmount = 2.8 / amount
                cmds.xform(guide_spine, t=(0, moveAmount, 0), os=True)
            cmds.setAttr(guide_spine + '.overrideEnabled', True)
            cmds.setAttr(guide_spine + '.overrideColor', color)
        cmds.xform('Guide_%s_1' % (name), t=(0, 9, 0), os=True)
    def l_arm(name, color):
        ARM_GUIDES = ('Clavicle', 'Shoulder', 'Elbow', 'Wrist', 'HandTip')
        arm_pos = ((.1, 12, 0), (.85, .35, 0), (2.15, 0, 0), (2.5, 0, 0), (1, 0, 0))
        for number_guide in range(len(ARM_GUIDES)):
            guide_arm = cmds.spaceLocator(n='Guide_%s_%s' % (name, ARM_GUIDES[number_guide]))[0]
            if ARM_GUIDES[number_guide] == 'Clavicle': cmds.parent(guide_arm, GUIDES_GRP)                    
            else: cmds.parent(guide_arm, 'Guide_%s_%s' % (name, ARM_GUIDES[number_guide - 1]))
                
            cmds.setAttr(guide_arm + '.overrideEnabled', True)
            cmds.setAttr(guide_arm + '.overrideColor', color)
            cmds.xform('Guide_%s_%s' % (name, ARM_GUIDES[number_guide]), t=arm_pos[number_guide], os=True)
    def r_arm(name, color):
        ARM_GUIDES = ('Clavicle', 'Shoulder', 'Elbow', 'Wrist', 'HandTip')
        arm_pos = ((-.1, 12, 0), (-.85, .35, 0), (-2.15, 0, 0), (-2.5, 0, 0), (-1, 0, 0))
        for number_guide in range(len(ARM_GUIDES)):
            guide_arm = cmds.spaceLocator(n='Guide_%s_%s' % (name, ARM_GUIDES[number_guide]))[0]
            if ARM_GUIDES[number_guide] == 'Clavicle': cmds.parent(guide_arm, GUIDES_GRP)                    
            else: cmds.parent(guide_arm, 'Guide_%s_%s' % (name, ARM_GUIDES[number_guide - 1]))
                
            cmds.setAttr(guide_arm + '.overrideEnabled', True)
            cmds.setAttr(guide_arm + '.overrideColor', color)
            cmds.xform('Guide_%s_%s' % (name, ARM_GUIDES[number_guide]), t=arm_pos[number_guide], os=True)
    def l_leg(name, color):
        LEG_GUIDES = ('Pelvis', 'Hip', 'Knee', 'Ankle', 'Ball', 'FootTip')
        leg_pos = ((.34, 8.6, 0), (.14, -.8, 0), (0, -3.7, .1), (0, -3.4, -.1), (0, -.52, .65), (0, 0, .9))
        for number_guide in range(len(LEG_GUIDES)):
            guide_leg = cmds.spaceLocator(n='Guide_%s_%s' % (name, LEG_GUIDES[number_guide]))[0]
            if LEG_GUIDES[number_guide] == 'Pelvis': cmds.parent(guide_leg, GUIDES_GRP)
            else: cmds.parent(guide_leg, 'Guide_%s_%s' % (name, LEG_GUIDES[number_guide - 1]))

            cmds.setAttr(guide_leg + '.overrideEnabled', True)
            cmds.setAttr(guide_leg + '.overrideColor', color)
            cmds.xform('Guide_%s_%s' % (name, LEG_GUIDES[number_guide]), t=leg_pos[number_guide], os=True)
    def r_leg(name, color):
        LEG_GUIDES = ('Pelvis', 'Hip', 'Knee', 'Ankle', 'Ball', 'FootTip')
        leg_pos = ((-.34, 8.6, 0), (-.14, -.8, 0), (0, -3.7, .1), (0, -3.4, -.1), (0, -.52, .65), (0, 0, .9))
        for number_guide in range(len(LEG_GUIDES)):
            guide_leg = cmds.spaceLocator(n='Guide_%s_%s' % (name, LEG_GUIDES[number_guide]))[0]
            if LEG_GUIDES[number_guide] == 'Pelvis': cmds.parent(guide_leg, GUIDES_GRP)
            else: cmds.parent(guide_leg, 'Guide_%s_%s' % (name, LEG_GUIDES[number_guide - 1]))

            cmds.setAttr(guide_leg + '.overrideEnabled', True)
            cmds.setAttr(guide_leg + '.overrideColor', color)
            cmds.xform('Guide_%s_%s' % (name, LEG_GUIDES[number_guide]), t=leg_pos[number_guide], os=True)
    def l_hand(name, thumb, amount, color):
        thumbPos = ((5.6, 12.3, .17), (.075, 0, .06), (.16, 0, .12), (.15, 0, .25), (.1, 0, .2))
        fingersPos = (
            ((5.65, 12.3, .11), (.6, 0, .13), (.22, 0, 0), (.18, 0, 0), (.19, 0, 0)),
            ((5.65, 12.3, .07), (.6, 0, .01), (.29, 0, 0), (.19, 0, 0), (.2, 0, 0)),
            ((5.65, 12.3, -.037), (.59, 0, -.03), (.26, 0, 0), (.17, 0, 0), (.19, 0, 0)),
            ((5.65, 12.3, -.1), (.56, 0, -.1), (.18, 0, 0), (.15, 0, 0), (.15, 0, 0))
        )
        extraFingerPos = ((5.65, 12.3, -.15), (.56, 0, -.1), (.18, 0, 0), (.15, 0, 0), (.15, 0, 0))
        if thumb == True:
            for number_guide in range(5):
                guide_thumb = cmds.spaceLocator(n='Guide_%s_thumb%s' % (name, number_guide + 1))[0]
                if number_guide == 0: cmds.parent(guide_thumb, GUIDES_GRP)
                else: cmds.parent(guide_thumb, 'Guide_%s_thumb%s' % (name, number_guide))
                cmds.setAttr(guide_thumb + '.overrideEnabled', True)
                cmds.setAttr(guide_thumb + '.overrideColor', color)
                cmds.xform('Guide_%s_thumb%s' % (name, number_guide + 1), t=thumbPos[number_guide], os=True)                

        fingers = ('index', 'middle', 'ring', 'pinky')
        if amount <= 4:
            for finger in range(amount):
                for number_guide in range(5):
                    guide_finger = cmds.spaceLocator(n='Guide_%s_%s%s' % (name, fingers[finger], number_guide + 1))[0]
                    if number_guide == 0: cmds.parent(guide_finger, GUIDES_GRP)
                    else: cmds.parent(guide_finger, 'Guide_%s_%s%s' % (name, fingers[finger], number_guide))                        
                    cmds.setAttr(guide_finger + '.overrideEnabled', True)
                    cmds.setAttr(guide_finger + '.overrideColor', color)
                    cmds.xform('Guide_%s_%s%s' % (name, fingers[finger], number_guide + 1), t=fingersPos[finger][number_guide], os=True)
        else:
            for finger in range(len(fingers)):
                for number_guide in range(5):
                    guide_finger = cmds.spaceLocator(n='Guide_%s_%s%s' % (name, fingers[finger], number_guide + 1))[0]
                    if number_guide == 0: cmds.parent(guide_finger, GUIDES_GRP)
                    else: cmds.parent(guide_finger, 'Guide_%s_%s%s' % (name, fingers[finger], number_guide))
                    cmds.setAttr(guide_finger + '.overrideEnabled', True)
                    cmds.setAttr(guide_finger + '.overrideColor', color)
                    cmds.xform('Guide_%s_%s%s' % (name, fingers[finger], number_guide + 1), t=fingersPos[finger][number_guide], os=True)

            for finger in range(amount - 4):
                for number_guide in range(5):
                    guide_finger = cmds.spaceLocator(n='Guide_%s_extraFinger_%s_%s' % (name, finger + 1, number_guide + 1))[0]
                    if number_guide == 0:
                        print(finger + 1.0) / 10
                        cmds.move(5.65, 12.3, extraFingerPos[0][2] - ((finger + 1.0) / 10), guide_finger, ls=True)
                        cmds.parent(guide_finger, GUIDES_GRP)
                    else:
                        cmds.parent(guide_finger, 'Guide_%s_extraFinger_%s_%s' % (name, finger + 1, number_guide))
                    cmds.setAttr(guide_finger + '.overrideEnabled', True)
                    cmds.setAttr(guide_finger + '.overrideColor', color)
                for number_guide in range(1, 5):
                    cmds.xform('Guide_%s_extraFinger_%s_%s' % (name, finger + 1, number_guide + 1), t=extraFingerPos[number_guide], os=1)
    def r_hand(name, thumb, amount, color):
        thumbPos = ((-5.6, 12.3, .17), (-.075, 0, .06), (-.16, 0, .12), (-.15, 0, .25), (-.1, 0, .2))
        fingersPos = (
            ((-5.65, 12.3, .11), (-.6, 0, .13), (-.22, 0, 0), (-.18, 0, 0), (-.19, 0, 0)),
            ((-5.65, 12.3, .07), (-.6, 0, .01), (-.29, 0, 0), (-.19, 0, 0), (-.2, 0, 0)),
            ((-5.65, 12.3, -.037), (-.59, 0, -.03), (-.26, 0, 0), (-.17, 0, 0), (-.19, 0, 0)),
            ((-5.65, 12.3, -.1), (-.56, 0, -.1), (-.18, 0, 0), (-.15, 0, 0), (-.15, 0, 0))
        )
        extraFingerPos = ((-5.65, 12.3, -.15), (-.56, 0, -.1), (-.18, 0, 0), (-.15, 0, 0), (-.15, 0, 0))
        if thumb == True:
            for number_guide in range(5):
                guide_thumb = cmds.spaceLocator(n='Guide_%s_thumb%s' % (name, number_guide + 1))[0]
                if number_guide == 0: cmds.parent(guide_thumb, GUIDES_GRP)
                else: cmds.parent(guide_thumb, 'Guide_%s_thumb%s' % (name, number_guide))
                cmds.setAttr(guide_thumb + '.overrideEnabled', True)
                cmds.setAttr(guide_thumb + '.overrideColor', color)
                cmds.xform('Guide_%s_thumb%s' % (name, number_guide + 1), t=thumbPos[number_guide], os=True)                

        fingers = ('index', 'middle', 'ring', 'pinky')
        if amount <= 4:
            for finger in range(amount):
                for number_guide in range(5):
                    guide_finger = cmds.spaceLocator(n='Guide_%s_%s%s' % (name, fingers[finger], number_guide + 1))[0]
                    if number_guide == 0: cmds.parent(guide_finger, GUIDES_GRP)
                    else: cmds.parent(guide_finger, 'Guide_%s_%s%s' % (name, fingers[finger], number_guide))                        
                    cmds.setAttr(guide_finger + '.overrideEnabled', True)
                    cmds.setAttr(guide_finger + '.overrideColor', color)
                    cmds.xform('Guide_%s_%s%s' % (name, fingers[finger], number_guide + 1), t=fingersPos[finger][number_guide], os=True)
        else:
            for finger in range(len(fingers)):
                for number_guide in range(5):
                    guide_finger = cmds.spaceLocator(n='Guide_%s_%s%s' % (name, fingers[finger], number_guide + 1))[0]
                    if number_guide == 0: cmds.parent(guide_finger, GUIDES_GRP)
                    else: cmds.parent(guide_finger, 'Guide_%s_%s%s' % (name, fingers[finger], number_guide))
                    cmds.setAttr(guide_finger + '.overrideEnabled', True)
                    cmds.setAttr(guide_finger + '.overrideColor', color)
                    cmds.xform('Guide_%s_%s%s' % (name, fingers[finger], number_guide + 1), t=fingersPos[finger][number_guide], os=True)

            for finger in range(amount - 4):
                for number_guide in range(5):
                    guide_finger = cmds.spaceLocator(n='Guide_%s_extraFinger_%s_%s' % (name, finger + 1, number_guide + 1))[0]
                    if number_guide == 0:
                        print(finger + 1.0) / 10
                        cmds.move(5.65, 12.3, extraFingerPos[0][2] - ((finger + 1.0) / 10), guide_finger, ls=True)
                        cmds.parent(guide_finger, GUIDES_GRP)
                    else:
                        cmds.parent(guide_finger, 'Guide_%s_extraFinger_%s_%s' % (name, finger + 1, number_guide))
                    cmds.setAttr(guide_finger + '.overrideEnabled', True)
                    cmds.setAttr(guide_finger + '.overrideColor', color)
                for number_guide in range(1, 5):
                    cmds.xform('Guide_%s_extraFinger_%s_%s' % (name, finger + 1, number_guide + 1), t=extraFingerPos[number_guide], os=1)
    def l_foot(name, color):
        FOOT_GUIDES = ['heel', 'tip', 'in', 'out', 'ball', 'toes']
        foot_pos = [[.47, 0, -.3], [0, 0, 1.8], [-.39, 0, -.5], [.77, 0, 0], [-.39, 0, 0], [-.39, 0, 0]]
        for number_guide in range(len(FOOT_GUIDES)):
            guide_foot = cmds.spaceLocator(n='Guide_%s_%s' % (name, FOOT_GUIDES[number_guide]))[0]
            if number_guide == 0: cmds.parent(guide_foot, GUIDES_GRP)
            elif number_guide == 5: cmds.parent(guide_foot, 'Guide_%s_%s' % (name, FOOT_GUIDES[3]))
            else: cmds.parent(guide_foot, 'Guide_%s_%s' % (name, FOOT_GUIDES[number_guide - 1]))
            cmds.setAttr(guide_foot + '.overrideEnabled', True)
            cmds.setAttr(guide_foot + '.overrideColor', color)
            cmds.xform(guide_foot, t=foot_pos[number_guide], os=True)
    def r_foot(name, color):
        FOOT_GUIDES = ['heel', 'tip', 'in', 'out', 'ball', 'toes']
        foot_pos = [[-.47, 0, -.3], [0, 0, 1.8], [.39, 0, -.5], [-.77, 0, 0], [.39, 0, 0], [.39, 0, 0]]
        for number_guide in range(len(FOOT_GUIDES)):
            guide_foot = cmds.spaceLocator(n='Guide_%s_%s' % (name, FOOT_GUIDES[number_guide]))[0]
            if number_guide == 0: cmds.parent(guide_foot, GUIDES_GRP)
            elif number_guide == 5: cmds.parent(guide_foot, 'Guide_%s_%s' % (name, FOOT_GUIDES[3]))
            else: cmds.parent(guide_foot, 'Guide_%s_%s' % (name, FOOT_GUIDES[number_guide - 1]))
            cmds.setAttr(guide_foot + '.overrideEnabled', True)
            cmds.setAttr(guide_foot + '.overrideColor', color)
            cmds.xform(guide_foot, t=foot_pos[number_guide], os=True)
    def neck(name, amount, color):
        for number_guide in range(amount):
            guide_neck = cmds.spaceLocator(n='Guide_%s_%s' % (name, str(number_guide + 1)))[0]
            if number_guide == 0: cmds.parent(guide_neck, GUIDES_GRP)
            else:
                cmds.parent(guide_neck, 'Guide_%s_%s' % (name, str(number_guide)))
                moveAmount = 1.6 / amount
                cmds.move(0, moveAmount, 0, ls=1)
            cmds.setAttr(guide_neck + '.overrideEnabled', 1)
            cmds.setAttr(guide_neck + '.overrideColor', color)
        cmds.xform('Guide_%s_1' % (name), t=(0, 12.5, 0), os=True)
    def guideType(type, amount, color):
        if cmds.objExists(GUIDES_GRP): pass                    
        else: cmds.group(n=GUIDES_GRP, em=True)
                    
        typeGuide = {
            "spine": spine,
            "l_arm": l_arm,
            "r_arm": r_arm,
            "l_leg": l_leg,
            "r_leg": r_leg,
            "l_hand": l_hand,
            "r_hand": r_hand,
            "l_foot": l_foot,
            "r_foot": r_foot,
            "neck": neck,
        }

        colorCtl = {
            "yellow": 17,
            "green": 14,
            "red": 13,
            "blue": 6,
            "pink": 20,
            "littleBlue": 18,
            "white": 16,
            'littleGreen': 19
        }

        type = typeGuide.get(type)
        color = colorCtl.get(color)
        if type == spine or type == neck: type(name, amount, color)   
        elif type == l_hand or type == r_hand: type(name, thumb, amount, color)
        else: type(name, color)

    if cmds.objExists(name):
        cmds.warning('Guide_%s_already_exist' % (name))
        pass
    else: guideType(type, amount, color)

##########################################################################################
#GENERATE JOINTS IN THE SAME POSITION THAN GUIDES FOR ORIENT PROPOURSES
def joints(vis = False):
    cmds.hide(GUIDES_GRP)

    list_guides = cmds.listRelatives(GUIDES_GRP, ad=True)
    guides_positions = []

    if cmds.objExists(GUIDES_JOINTS_GRP): pass
    else: cmds.group(n=GUIDES_JOINTS_GRP, em=True)

    for guide in list_guides:
        if 'Shape' in guide: pass
        else: guides_positions.append(guide)

    for guide in guides_positions:
        cmds.select(cl=True)
        jnt = cmds.joint(n=guide + '_jnt')
        constraint = cmds.parentConstraint(guide, jnt, mo=False)
        cmds.delete(constraint)

    for guide in guides_positions:
        father = cmds.listRelatives(guide, p=True)[0]
        if father == GUIDES_GRP: cmds.parent(guide + '_jnt', GUIDES_JOINTS_GRP)
        else: cmds.parent(guide + '_jnt', father + '_jnt')

    orientJnts(vis)

def orientJnts(vis):
    jnts = cmds.listRelatives(GUIDES_JOINTS_GRP, ad=1)
    for i in jnts: cmds.joint(i, e=True, zso=True, oj='xzy', sao='yup')
    cmds.setAttr(GUIDES_JOINTS_GRP + '.visibility', vis)

##########################################################################################
# THIS WAY YOU CAN GENERATE THE GUIDES

# generate_guides(type='l_hand', name='L_Hand', thumb=True, amount=7, color='littleBlue')
# generate_guides(type = 'r_hand', name = 'R_Hand', thumb = True, amount = 4, color = 'pink')
# generate_guides(type='spine', name='Spine', amount=5, color='yellow')
# generate_guides(type = 'l_arm', name = 'L_Arm', color='blue')
# generate_guides(type = 'r_arm', name = 'R_Arm', color='red')
# generate_guides(type='neck', name='Neck', amount=3, color='yellow')
# generate_guides(type = 'l_leg', name = 'L_Leg', color='blue')
# generate_guides(type = 'r_leg', name = 'R_Leg', color='red')
# generate_guides(type = 'l_foot', name = 'L_foot', color='littleBlue')
# generate_guides(type = 'r_foot', name = 'R_foot', color='pink')
#
# joints(vis = False)

