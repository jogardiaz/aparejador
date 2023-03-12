##########################################################################################
#content = autorig
#
#version = 0.1.0
#date = 2023-01-24
#
#author = Jogar Diaz <jogartista@gmail.com>
##########################################################################################
import os
import sys

# PATH = 'J:\\python advance\\aparejador\\04_ui'
# TITLE = 'aparejador'
TITLE = os.path.splitext(os.path.basename(__file__))[0]
PATH = os.path.dirname(__file__)
sys.path.append(PATH)

from lib.Qt import QtWidgets, QtGui, QtCore, QtCompat

# from modules import guides
# from modules import arm
# from modules import leg
# from modules import hand
# from modules import spine

##########################################################################################
# CLASS
class Aparejador:
    
    def __init__(self):
        path_ui = PATH + '/' + TITLE + '.ui'
        print(path_ui)
        self.wgAparejador = QtCompat.loadUi(path_ui)

        ##########################################################################################
        # SIGNALS
        self.wgAparejador.btnNewModule.clicked.connect(self.new_module)
        self.wgAparejador.btnCreate.clicked.connect(self.create_guides)
        self.wgAparejador.btnMirror.clicked.connect(self.mirror_guides)
        self.wgAparejador.btnJnts.clicked.connect(self.jnts_guides)
        self.wgAparejador.btnBuild.clicked.connect(self.build_rig)


        self.wgAparejador.show()

    ##########################################################################################
    # PRESS
    def new_module(self):
        print('This feature will be added soon')

    def create_guides(self):
        print('create')

        #TODO: CREATE A FOR READING TYPES
        # type = str(self.wgAparejador.BoxType1.currentText())

        #SPINE
        name = str(self.wgAparejador.name1.text())
        amount = self.wgAparejador.BoxNumbers1.value()
        print(('body_part=spine, name=' + name + ',amount=' + str(amount) + ',color=yellow'))
        #guides.generate_guides(body_part='spine', name=name, amount=amount, color='yellow')

        # ARM1
        name = str(self.wgAparejador.name2.text())
        side_box = str(self.wgAparejador.side2.currentText())
        final_name = side_box + '_'+ name
        if 'L' == side_box:
            color = 'blue'
            side = 'l'
        elif 'R' == side_box:
            color = 'red'
            side = 'r'
        print(('body_part=Arm, name=' + name + ',side=' + side_box + ',color=' + color))
        # guides.generate_guides(body_part='arm', name=final_name, color=color, side=side)

        # ARM2
        name = str(self.wgAparejador.name3.text())
        side_box = str(self.wgAparejador.side3.currentText())
        final_name = side_box + '_' + name
        if 'L' == side_box:
            color = 'blue'
            side = 'l'
        elif 'R' == side_box:
            color = 'red'
            side = 'r'
        print(('body_part=Arm, name=' + name + ',side=' + side_box + ',color=' + color))
        # guides.generate_guides(body_part='arm', name=final_name, color=color, side=side)

        # LEG1
        name = str(self.wgAparejador.name4.text())
        side_box = str(self.wgAparejador.side4.currentText())
        final_name = side_box + '_' + name
        if 'L' == side_box:
            color = 'blue'
            side = 'l'
        elif 'R' == side_box:
            color = 'red'
            side = 'r'
        print(('body_part=Leg, name=' + name + ',side=' + side_box + ',color=' + color))
        # guides.generate_guides(body_part='leg', name=final_name, color=color, side=side)

        # LEG2
        name = str(self.wgAparejador.name5.text())
        side_box = str(self.wgAparejador.side5.currentText())
        final_name = side_box + '_' + name
        if 'L' == side_box:
            color = 'blue'
            side = 'l'
        elif 'R' == side_box:
            color = 'red'
            side = 'r'
        print(('body_part=Leg, name=' + name + ',side=' + side_box + ',color=' + color))
        # guides.generate_guides(body_part='leg', name=final_name, color=color, side=side)

        # NECK
        name = str(self.wgAparejador.name6.text())
        amount = self.wgAparejador.BoxNumbers6.value()
        print(('body_part=neck, name=' + name + ',amount=' + str(amount) + ',color=yellow'))
        # guides.generate_guides(body_part='neck', name=name, amount=amount, color='yellow')

        # HAND1
        name = str(self.wgAparejador.name7.text())
        side_box = str(self.wgAparejador.side7.currentText())
        final_name = side_box + '_' + name
        amount = self.wgAparejador.BoxNumbers7.value()
        thumb = self.wgAparejador.thumb7.checkState()
        if 'L' == side_box:
            color = 'littleBlue'
            side = 'l'
        elif 'R' == side_box:
            color = 'pink'
            side = 'r'

        if self.wgAparejador.thumb7.isChecked():
            thumb = True
        else:
            thumb = False
        print('body_part=hand, name=' + name + ',side=' + side_box + ',color=' + color + ',amount=' + str(amount) + ',Thumb=' + str(thumb))
        # guides.generate_guides(body_part='hand', name=final_name, thumb=thumb, amount=amount,
        #                        color='littleBlue', side='l')

        # HAND1
        name = str(self.wgAparejador.name8.text())
        side_box = str(self.wgAparejador.side8.currentText())
        final_name = side_box + '_' + name
        amount = self.wgAparejador.BoxNumbers8.value()
        if 'L' == side_box:
            color = 'littleBlue'
            side = 'l'
        elif 'R' == side_box:
            color = 'pink'
            side = 'r'

        if self.wgAparejador.thumb8.isChecked():
            thumb = True
        else:
            thumb = False

        print('body_part=hand, name=' + name + ',side=' + side_box + ',color=' + color + ',amount=' + str(
            amount) + ',Thumb=' + str(thumb))
        # guides.generate_guides(body_part='hand', name=final_name, thumb=thumb, amount=amount,
        #                        color='littleBlue', side='l')



        # guides.generate_guides(body_part='hand', name='R_Hand', thumb=True, amount=4,
        #                        color='pink', side='r')
        #
        # guides.guides_sizes(resize=.2)

    def mirror_guides(self):
        print('mirror')
        print('correct_side=L_Arm, mirror_to=R_Arm')
        print('correct_side=L_Leg, mirror_to=R_Leg')
        print('correct_side=L_Hand, mirror_to=R_Hand')
        # guides.mirror_guides(correct_side='L_Arm', mirror_to='R_Arm')
        # guides.mirror_guides(correct_side='L_Leg', mirror_to='R_Leg')
        # guides.mirror_guides(correct_side='L_Hand', mirror_to='R_Hand')

    def jnts_guides(self):
        print('joints')
        print('This allows you to control the orientation of every joint in your rig, but its an optional step')
        # guides.joints(vis=True)

    def build_rig(self):
        print('build')
        # guides.joints(vis=True)
        # arm.rig_arm(side='l', name='L_Arm')
        # arm.rig_arm(side='r', name='R_Arm')
        # leg.rig_leg(side='l', name='L_Leg')
        # leg.rig_leg(side='r', name='R_Leg')
        # hand.rig_hand(side='l', name='L_Hand', thumb=True, amount=4)
        # hand.rig_hand(side='r', name='R_Hand', thumb=True, amount=4)
        # spine.rig_spine(name='Spine', amount=5)

##########################################################################################
# START UI
# app = QtWidgets.QApplication(sys.argv)
# aparejador = Aparejador()
# app.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    aparejador = Aparejador()
    app.exec_()
    