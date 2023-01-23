import maya.cmds as mc

names = []
guides_grp = 'Guides_grp'
guides_jnts_grp = 'Guides_jnts_grp'


def guides(type, name, amount=0, thumb=None, color='8'):
    def spine(name, amount, color):
        for number_guide in range(amount):
            loc = mc.spaceLocator(n='Guide_%s_%s' % (name, str(number_guide + 1)))[0]
            if number_guide == 0:
                if mc.objExists(guides_grp):
                    mc.parent(loc, guides_grp)
                else:
                    mc.group(n=guides_grp, em=1)
                    mc.parent(loc, guides_grp)
            else:
                mc.parent(loc, 'Guide_%s_%s' % (name, str(number_guide)))
                moveAmount = 2.8 / amount
                mc.xform(loc, t=(0, moveAmount, 0), os=True)
            mc.setAttr(loc + '.overrideEnabled', 1)
            mc.setAttr(loc + '.overrideColor', color)
        mc.xform('Guide_%s_1' % (name), t=(0, 9, 0), os=True)

    def l_arm(name, color):
        arm = ('Clavicle', 'Shoulder', 'Elbow', 'Wrist', 'HandTip')
        armPos = ((.1, 12, 0), (.85, .35, 0), (2.15, 0, 0), (2.5, 0, 0), (1, 0, 0))
        for i in range(len(arm)):
            loc = mc.spaceLocator(n='Guide_%s_%s' % (name, arm[i]))[0]
            if arm[i] == 'Clavicle':
                if mc.objExists(guides_grp):
                    mc.parent(loc, guides_grp)
                else:
                    mc.group(n=guides_grp, em=1)
                    mc.parent(loc, guides_grp)
            else:
                mc.parent(loc, 'Guide_%s_%s' % (name, arm[i - 1]))
            mc.setAttr(loc + '.overrideEnabled', 1)
            mc.setAttr(loc + '.overrideColor', color)
            mc.xform('Guide_%s_%s' % (name, arm[i]), t=armPos[i], os=True)

    def r_arm(name, color):
        arm = ('Clavicle', 'Shoulder', 'Elbow', 'Wrist', 'HandTip')
        armPos = ((-.1, 12, 0), (-.85, .35, 0), (-2.15, 0, 0), (-2.5, 0, 0), (-1, 0, 0))
        for i in range(len(arm)):
            loc = mc.spaceLocator(n='Guide_%s_%s' % (name, arm[i]))[0]
            if arm[i] == 'Clavicle':
                if mc.objExists(guides_grp):
                    mc.parent(loc, guides_grp)
                else:
                    mc.group(n=guides_grp, em=1)
                    mc.parent(loc, guides_grp)
            else:
                mc.parent(loc, 'Guide_%s_%s' % (name, arm[i - 1]))
            mc.setAttr(loc + '.overrideEnabled', 1)
            mc.setAttr(loc + '.overrideColor', color)
            mc.xform('Guide_%s_%s' % (name, arm[i]), t=armPos[i], os=True)

    def l_leg(name, color):
        leg = ('Pelvis', 'Hip', 'Knee', 'Ankle', 'Ball', 'FootTip')
        legPos = ((.34, 8.6, 0), (.14, -.8, 0), (0, -3.7, .1), (0, -3.4, -.1), (0, -.52, .65), (0, 0, .9))
        for i in range(len(leg)):
            loc = mc.spaceLocator(n='Guide_%s_%s' % (name, leg[i]))[0]
            if leg[i] == 'Pelvis':
                if mc.objExists(guides_grp):
                    mc.parent(loc, guides_grp)
                else:
                    mc.group(n=guides_grp, em=1)
                    mc.parent(loc, guides_grp)
            else:
                mc.parent(loc, 'Guide_%s_%s' % (name, leg[i - 1]))
            mc.setAttr(loc + '.overrideEnabled', 1)
            mc.setAttr(loc + '.overrideColor', color)
            mc.xform('Guide_%s_%s' % (name, leg[i]), t=legPos[i], os=True)

    def r_leg(name, color):
        leg = ('Pelvis', 'Hip', 'Knee', 'Ankle', 'Ball', 'FootTip')
        legPos = ((-.34, 8.6, 0), (-.14, -.8, 0), (0, -3.7, .1), (0, -3.4, -.1), (0, -.52, .65), (0, 0, .9))
        for i in range(len(leg)):
            loc = mc.spaceLocator(n='Guide_%s_%s' % (name, leg[i]))[0]
            if leg[i] == 'Pelvis':
                if mc.objExists(guides_grp):
                    mc.parent(loc, guides_grp)
                else:
                    mc.group(n=guides_grp, em=1)
                    mc.parent(loc, guides_grp)
            else:
                mc.parent(loc, 'Guide_%s_%s' % (name, leg[i - 1]))
            mc.setAttr(loc + '.overrideEnabled', 1)
            mc.setAttr(loc + '.overrideColor', color)
            mc.xform('Guide_%s_%s' % (name, leg[i]), t=legPos[i], os=True)

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
            for i in range(5):
                loc = mc.spaceLocator(n='Guide_%s_thumb%s' % (name, i + 1))[0]
                if i == 0:
                    if mc.objExists(guides_grp):
                        mc.parent(loc, guides_grp)
                    else:
                        mc.group(n=guides_grp, em=1)
                        mc.parent(loc, guides_grp)
                else:
                    mc.parent(loc, 'Guide_%s_thumb%s' % (name, i))
                mc.setAttr(loc + '.overrideEnabled', 1)
                mc.setAttr(loc + '.overrideColor', color)
            for i in range(5):
                mc.xform('Guide_%s_thumb%s' % (name, i + 1), t=thumbPos[i], os=True)

        fingers = ('index', 'middle', 'ring', 'pinky')
        if amount <= 4:
            for n in range(amount):
                for i in range(5):
                    loc = mc.spaceLocator(n='Guide_%s_%s%s' % (name, fingers[n], i + 1))[0]
                    if i == 0:
                        if mc.objExists(guides_grp):
                            mc.parent(loc, guides_grp)
                        else:
                            mc.group(n=guides_grp, em=1)
                            mc.parent(loc, guides_grp)
                    else:
                        mc.parent(loc, 'Guide_%s_%s%s' % (name, fingers[n], i))
                    mc.setAttr(loc + '.overrideEnabled', 1)
                    mc.setAttr(loc + '.overrideColor', color)
                for i in range(5):
                    mc.xform('Guide_%s_%s%s' % (name, fingers[n], i + 1), t=fingersPos[n][i], os=1)

        else:
            for n in range(len(fingers)):
                for i in range(5):
                    loc = mc.spaceLocator(n='Guide_%s_%s%s' % (name, fingers[n], i + 1))[0]
                    if i == 0:
                        if mc.objExists(guides_grp):
                            mc.parent(loc, guides_grp)
                        else:
                            mc.group(n=guides_grp, em=1)
                            mc.parent(loc, guides_grp)
                    else:
                        mc.parent(loc, 'Guide_%s_%s%s' % (name, fingers[n], i))
                    mc.setAttr(loc + '.overrideEnabled', 1)
                    mc.setAttr(loc + '.overrideColor', color)
                for i in range(5):
                    mc.xform('Guide_%s_%s%s' % (name, fingers[n], i + 1), t=fingersPos[n][i], os=1)
            for n in range(amount - 4):
                for i in range(5):
                    loc = mc.spaceLocator(n='Guide_%s_extraFinger_%s_%s' % (name, n + 1, i + 1))[0]
                    if i == 0:
                        print(n + 1.0) / 10
                        mc.move(5.65, 12.3, extraFingerPos[0][2] - ((n + 1.0) / 10), loc, ls=True)
                        if mc.objExists(guides_grp):
                            mc.parent(loc, guides_grp)
                        else:
                            mc.group(n=guides_grp, em=1)
                            mc.parent(loc, guides_grp)
                    else:
                        mc.parent(loc, 'Guide_%s_extraFinger_%s_%s' % (name, n + 1, i))
                    mc.setAttr(loc + '.overrideEnabled', 1)
                    mc.setAttr(loc + '.overrideColor', color)
                for i in range(1, 5):
                    mc.xform('Guide_%s_extraFinger_%s_%s' % (name, n + 1, i + 1), t=extraFingerPos[i], os=1)

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
            for i in range(5):
                loc = mc.spaceLocator(n='Guide_%s_thumb%s' % (name, i + 1))[0]
                if i == 0:
                    if mc.objExists(guides_grp):
                        mc.parent(loc, guides_grp)
                    else:
                        mc.group(n=guides_grp, em=1)
                        mc.parent(loc, guides_grp)
                else:
                    mc.parent(loc, 'Guide_%s_thumb%s' % (name, i))
                mc.setAttr(loc + '.overrideEnabled', 1)
                mc.setAttr(loc + '.overrideColor', color)
            for i in range(5):
                mc.xform('Guide_%s_thumb%s' % (name, i + 1), t=thumbPos[i], os=True)

        fingers = ('index', 'middle', 'ring', 'pinky')
        if amount <= 4:
            for n in range(amount):
                for i in range(5):
                    loc = mc.spaceLocator(n='Guide_%s_%s%s' % (name, fingers[n], i + 1))[0]
                    if i == 0:
                        if mc.objExists(guides_grp):
                            mc.parent(loc, guides_grp)
                        else:
                            mc.group(n=guides_grp, em=1)
                            mc.parent(loc, guides_grp)
                    else:
                        mc.parent(loc, 'Guide_%s_%s%s' % (name, fingers[n], i))
                    mc.setAttr(loc + '.overrideEnabled', 1)
                    mc.setAttr(loc + '.overrideColor', color)
                for i in range(5):
                    mc.xform('Guide_%s_%s%s' % (name, fingers[n], i + 1), t=fingersPos[n][i], os=1)

        else:
            for n in range(len(fingers)):
                for i in range(5):
                    loc = mc.spaceLocator(n='Guide_%s_%s%s' % (name, fingers[n], i + 1))[0]
                    if i == 0:
                        if mc.objExists(guides_grp):
                            mc.parent(loc, guides_grp)
                        else:
                            mc.group(n=guides_grp, em=1)
                            mc.parent(loc, guides_grp)
                    else:
                        mc.parent(loc, 'Guide_%s_%s%s' % (name, fingers[n], i))
                    mc.setAttr(loc + '.overrideEnabled', 1)
                    mc.setAttr(loc + '.overrideColor', color)
                for i in range(5):
                    mc.xform('Guide_%s_%s%s' % (name, fingers[n], i + 1), t=fingersPos[n][i], os=1)
            for n in range(amount - 4):
                for i in range(5):
                    loc = mc.spaceLocator(n='Guide_%s_extraFinger_%s_%s' % (name, n + 1, i + 1))[0]
                    if i == 0:
                        print
                        'n'
                        print
                        n + 1
                        print(n + 1.0) / 10
                        mc.move(-5.65, 12.3, extraFingerPos[0][2] - ((n + 1.0) / 10), loc, ls=True)
                        if mc.objExists(guides_grp):
                            mc.parent(loc, guides_grp)
                        else:
                            mc.group(n=guides_grp, em=1)
                            mc.parent(loc, guides_grp)
                    else:
                        mc.parent(loc, 'Guide_%s_extraFinger_%s_%s' % (name, n + 1, i))
                    mc.setAttr(loc + '.overrideEnabled', 1)
                    mc.setAttr(loc + '.overrideColor', color)
                for i in range(1, 5):
                    mc.xform('Guide_%s_extraFinger_%s_%s' % (name, n + 1, i + 1), t=extraFingerPos[i], os=1)

    def l_foot(name, color):
        listaLocs = ['heel', 'tip', 'in', 'out', 'ball', 'toes']
        locsPos = [[.47, 0, -.3], [0, 0, 1.8], [-.39, 0, -.5], [.77, 0, 0], [-.39, 0, 0], [-.39, 0, 0]]
        for i in range(len(listaLocs)):
            loc = mc.spaceLocator(n='Guide_%s_%s' % (name, listaLocs[i]))[0]
            if i == 0:
                if mc.objExists(guides_grp):
                    mc.parent(loc, guides_grp)
                else:
                    mc.group(n=guides_grp, em=1)
                    mc.parent(loc, guides_grp)
            elif i == 5:
                mc.parent(loc, 'Guide_%s_%s' % (name, listaLocs[3]))
            else:
                mc.parent(loc, 'Guide_%s_%s' % (name, listaLocs[i - 1]))
            mc.setAttr(loc + '.overrideEnabled', 1)
            mc.setAttr(loc + '.overrideColor', color)
            mc.xform(loc, t=locsPos[i], os=True)

    def r_foot(name, color):
        listaLocs = ['heel', 'tip', 'in', 'out', 'ball', 'toes']
        locsPos = [[-.47, 0, -.3], [0, 0, 1.8], [.39, 0, -.5], [-.77, 0, 0], [.39, 0, 0], [.39, 0, 0]]
        for i in range(len(listaLocs)):
            loc = mc.spaceLocator(n='Guide_%s_%s' % (name, listaLocs[i]))[0]
            if i == 0:
                if mc.objExists(guides_grp):
                    mc.parent(loc, guides_grp)
                else:
                    mc.group(n=guides_grp, em=1)
                    mc.parent(loc, guides_grp)
            elif i == 5:
                mc.parent(loc, 'Guide_%s_%s' % (name, listaLocs[3]))
            else:
                mc.parent(loc, 'Guide_%s_%s' % (name, listaLocs[i - 1]))
            mc.setAttr(loc + '.overrideEnabled', 1)
            mc.setAttr(loc + '.overrideColor', color)
            mc.xform(loc, t=locsPos[i], os=True)

    def neck(name, amount, color):
        for i in range(amount):
            loc = mc.spaceLocator(n='Guide_%s_%s' % (name, str(i + 1)))[0]
            if i == 0:
                if mc.objExists(guides_grp):
                    mc.parent(loc, guides_grp)
                else:
                    mc.group(n=guides_grp, em=1)
                    mc.parent(loc, guides_grp)
            else:
                mc.parent(loc, 'Guide_%s_%s' % (name, str(i)))
                moveAmount = 1.6 / amount
                mc.move(0, moveAmount, 0, ls=1)
            mc.setAttr(loc + '.overrideEnabled', 1)
            mc.setAttr(loc + '.overrideColor', color)
        mc.xform('Guide_%s_1' % (name), t=(0, 12.5, 0), os=True)

    def guideType(type, amount, color):
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
        if type == spine or type == neck:
            type(name, amount, color)
        elif type == l_hand or type == r_hand:
            type(name, thumb, amount, color)
        else:
            type(name, color)

    if name in names:
        mc.warning('Guide_%s_already_exist' % (name))
        pass
    else:
        names.append(name)
        guideType(type, amount, color)


def joints(vis = False):
    mc.hide(guides_grp)

    list = mc.listRelatives(guides_grp, ad=True)
    locs = []

    if mc.objExists(guides_jnts_grp):
        pass
    else:
        mc.group(n=guides_jnts_grp, em=1)

    for i in list:
        if 'Shape' in i:
            pass
        else:
            locs.append(i)

    for i in locs:
        mc.select(cl=1)
        jnt = mc.joint(n=i + '_jnt')
        cons = mc.parentConstraint(i, jnt, mo=0)
        mc.delete(cons)

    for i in locs:
        father = mc.listRelatives(i, p=True)[0]
        if father == guides_grp:
            mc.parent(i + '_jnt', guides_jnts_grp)
        else:
            mc.parent(i + '_jnt', father + '_jnt')

    orientJnts(vis)

def orientJnts(vis):
    jnts = mc.listRelatives(guides_jnts_grp, ad=1)
    for i in jnts:
        mc.joint(i, e=True, zso=True, oj='xzy', sao='yup')
    if vis == False:
        mc.hide(guides_jnts_grp)
    else:
        pass

# guides(type='l_hand', name='L_Hand', thumb=True, amount=7, color='littleBlue')
# guides(type = 'r_hand', name = 'R_Hand', thumb = True, amount = 4, color = 'pink')
# guides(type='spine', name='Spine', amount=5, color='yellow')
# guides(type = 'l_arm', name = 'L_Arm', color='blue')
# guides(type = 'r_arm', name = 'R_Arm', color='red')
# guides(type='neck', name='Neck', amount=3, color='yellow')
# guides(type = 'l_leg', name = 'L_Leg', color='blue')
# guides(type = 'r_leg', name = 'R_Leg', color='red')
# guides(type = 'l_foot', name = 'L_foot', color='littleBlue')
# guides(type = 'r_foot', name = 'R_foot', color='pink')
#
#
# joints(vis = False)

