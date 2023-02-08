import maya.cmds as mc
import maya.mel as mel


def generate_control(control_shape, shape_color, name):
    type_ctrl = {
        "Sphere": Sphere,
        "Pin": Pin,
        "RectangleSide": RectangleSide,
        "rectangleFront": rectangleFront,
        "Orient": Orient,
        "Cube": Cube,
        "Arrow": Arrow,
        "Circle Cross": CircleCross,
        "Circle Orient": CircleOrient,
        "Cone": Cone,
        "Cross": Cross,
        "Square": Square,
        "Circle": Circle,
        "Double Arrow": doubleArrow
    }

    color_control = {
        "Yellow": 17,
        "Green": 14,
        "Red": 13,
        "Blue": 6,
        "Pink": 20,
        "Little Blue": 18,
        "White": 16,
        'Little Green' : 19
    }

    type_ctrl.get(control_shape)(name, color_control.get(shape_color))

def Sphere(name, color_control):
    sdk_grp = mc.group(n=name + '_sdk', empty=True)
    adj_grp = mc.group(n=name + '_adj', empty=True)
    mc.circle(n=name)
    mc.circle(n=name + '1')
    mc.circle(n=name + '2')
    mc.select(name + '1.cv[0:7]',r=True)
    mc.rotate(90,0,0)
    mc.select(name + '2.cv[0:7]')
    mc.rotate(0,90,0)
    mc.select(name + '1Shape',name + '2Shape')
    mc.select(name, add = 1)
    mc.parent(r=True, s=True)
    mc.delete(name + '1',name + '2')
    mc.setAttr(name + '.overrideEnabled', True)
    mc.setAttr(name + '.overrideColor', color_control)  

    mc.parent(name,sdk_grp)   
    mc.parent(sdk_grp,adj_grp) 

def Pin(name, color_control):
    ctl = mc.curve( n = name, d = 1, p=[(0, 0, 0),(0, 0.136093, 0),(0, 0.140995, 0.0246402),(0, 0.154952, 0.0455291),(0, 0.175841, 0.0594866),(0, 0.200481, 0.0643878),(0, 0.225121, 0.0594866),(0, 0.24601, 0.0455291),(0, 0.259968, 0.0246401),(0, 0.264869, 0),(0, 0.259968, -0.0246402),(0, 0.24601, -0.0455291),(0, 0.225121, -0.0594866),(0, 0.200481, -0.0643878),(0, 0.175841, -0.0594866),(0, 0.154952, -0.045529),(0, 0.140995, -0.0246401),(0, 0.136093, 0)] )
    sdk_grp = mc.group( n = name + '_sdk', em=True)
    adj_grp = mc.group( n = name + '_adj', em=True)
    mc.parent( ctl, sdk_grp)
    mc.parent( sdk_grp,adj_grp)
    mc.setAttr(name + '.overrideEnabled', True)
    mc.setAttr(name + '.overrideColor', color_control) 
    #mc.select('curveShape1.cv[0:17]')
    #mc.scale(10,10,10, r=1, ocp=1 )
 
def RectangleSide(name, color_control):
    ctl = mc.curve( n= name, d = 1, p=[(0, -0.5, 1), (0, -0.5, -1), (3, -0.5, -1), (3, -0.5, 1), (0, -0.5, 1), (0, 0.5, 1), (3, 0.5, 1), (3, -0.5, 1),(3, -0.5, -1),(3, 0.5, -1),(3, 0.5, 1), (3, 0.5, -1), (3, 0.5, -1), (0, 0.5, -1), (0, -0.5, -1), (0, 0.5, -1), (0, 0.5, 1)] )
    sdk_grp = mc.group( n = name + '_sdk', em=True)
    adj_grp = mc.group( n = name + '_adj', em=True)
    mc.parent( ctl, sdk_grp)
    mc.parent( sdk_grp,adj_grp)
    mc.setAttr(name + '.overrideEnabled', True)
    mc.setAttr(name + '.overrideColor', color_control) 
    
def rectangleFront(name, color_control):
    ctl = mc.curve( n= name, d = 1, p=[(-1,0.5,2),(-1,-0.5,2),(1,-0.5,2),(1,0.5,2),(-1,0.5,2),(-1,0.5,-1),(-1,-0.5,-1),(-1,-0.5,2),(-1,-0.5,-1),(1,-0.5,-1),(1,0.5,-1),(-1,0.5,-1),(1,0.5,-1),(1,0.5,2),(1,-0.5,2),(1,-0.5,-1)] )
    sdk_grp = mc.group( n = name + '_sdk', em=True)
    adj_grp = mc.group( n = name + '_adj', em=True)
    mc.parent( ctl, sdk_grp)
    mc.parent( sdk_grp,adj_grp)
    mc.setAttr(name + '.overrideEnabled', True)
    mc.setAttr(name + '.overrideColor', color_control) 
    
def Orient(name, color_control):
    ctl = mc.curve( n= name, d = 1, p=[(.1,.1,-.2),(.1,.3,-.14),(.2,.3,-.14),(0,.6,0),(-.2,.3,-.14),(-.1,.3,-.14),(-.1,.1,-.2),(-.3,.1,-.14),(-.3,.2,-.14),(-.3,.2,-.14),(-.6,0,0),(-.3,-.2,-.14),(-.3,-.1,-.14),(-.1,-.1,-.2),(-.1,-.3,-.14),(-.2,-.3,-.14),(0,-.6,0),(.2,-.3,-.14),(.1,-.3,-.14),(.1,-.1,-.2),(.3,-.1,-.14),(.3,-.2,-.14),(.6,0,0),(.3,.2,-.14),(.3,.1,-.14),(.1,.1,-.2)] )
    sdk_grp = mc.group( n = name + '_sdk', em=True)
    adj_grp = mc.group( n = name + '_adj', em=True)
    mc.parent( ctl, sdk_grp)
    mc.parent( sdk_grp,adj_grp)
    mc.setAttr(name + '.overrideEnabled', True)
    mc.setAttr(name + '.overrideColor', color_control) 

def Cube(name, color_control):
    ctl = mc.curve( n= name, d = 1, p=[(-0.5, .5, -.5),(-.5,.5,.5),(-.5,-.5,.5),(-.5,-.5,-.5),(-.5,.5,-.5),(.5,.5,-.5),(.5,-.5,-.5),(-.5,-.5,-.5),(-.5,-.5,.5),(.5,-.5,.5),(.5,.5,.5),(-.5,.5,.5),(.5,.5,.5),(.5,.5,-.5),(.5,-.5,-.5),(.5,-.5,.5)])
    sdk_grp = mc.group( n = name + '_sdk', em=True)
    adj_grp = mc.group( n = name + '_adj', em=True)
    mc.parent( ctl, sdk_grp)
    mc.parent( sdk_grp,adj_grp)
    mc.setAttr(name + '.overrideEnabled', True)
    mc.setAttr(name + '.overrideColor', color_control) 
    
def Arrow(name, color_control):
    ctl = mc.curve( n= name, d = 1, p=[[-1.0, 0.0, -.34], [-4.4849208809999995e-05, 0.0, -.34], [0.0, 0.0, -0.66], [0.99, 0.0, 0.0], [0.0, 0.0, 0.66], [-4.4849208809999995e-05, 0.0, .34], [-1.0, 0.0, 0.34], [-1.0, 0.0, -.34], [-1.0, 0.0, -.34]])
    sdk_grp = mc.group( n = name + '_sdk', em=True)
    adj_grp = mc.group( n = name + '_adj', em=True)
    mc.parent( ctl, sdk_grp)
    mc.parent( sdk_grp,adj_grp)
    mc.setAttr(name + '.overrideEnabled', True)
    mc.setAttr(name + '.overrideColor', color_control) 
    
def doubleArrow(name, color_control):
    ctl = mc.curve( n= name, d = 1, p=[[-0.267803, 0.0, -0.245486 ],[-0.267803, 0.0, -0.490972 ],[-1.004261, 0.0, 0 ],[-0.267803, 0.0, 0.490972 ],[-0.267803, 0.0, 0.245486 ],[0.267803, 0.0, 0.245486 ],[0.267803, 0.0, 0.490972 ],[1.004261, 0.0, 0 ],[0.267803, 0.0, -0.490972 ],[0.267803, 0.0, -0.245486 ],[-0.267803, 0.0, -0.245486]])
    sdk_grp = mc.group( n = name + '_sdk', em=True)
    adj_grp = mc.group( n = name + '_adj', em=True)
    mc.parent( ctl, sdk_grp)
    mc.parent( sdk_grp,adj_grp)
    mc.setAttr(name + '.overrideEnabled', True)
    mc.setAttr(name + '.overrideColor', color_control) 

def CircleCross(name, color_control):
    ctl = mc.curve( n= name, d = 1, p=[[2.8654901189999996e-32, 0.8179224464, -5.670627187e-17], [9.891247576999999e-17, 0.7941551068, -0.1957416536], [1.92076518e-16, 0.7242343588, -0.3801075138], [2.740777712e-16, 0.6122237424, -0.542382907], [3.401506205e-16, 0.4646329075, -0.6731369771], [3.864551522e-16, 0.2900392968, -0.7647707728], [4.10300315e-16, 0.09858965641, -0.8119588708], [4.10300315e-16, -0.09858965641, -0.8119588708], [3.864551522e-16, -0.2900392968, -0.7647707728], [3.401506205e-16, -0.4646329075, -0.6731369771], [2.740777712e-16, -0.6122237424, -0.542382907], [1.92076518e-16, -0.7242343588, -0.3801075138], [9.891247576999999e-17, -0.7941551068, -0.1957416536], [1.099554263e-31, -0.8179224464, -2.1759496760000002e-16], [-9.891247576999999e-17, -0.7941551068, 0.1957416536], [-1.92076518e-16, -0.7242343588, 0.3801075138], [-2.740777712e-16, -0.6122237424, 0.542382907], [-3.401506205e-16, -0.4646329075, 0.6731369771], [-3.864551522e-16, -0.2900392968, 0.7647707728], [-4.10300315e-16, -0.09858965641, 0.8119588708], [-4.10300315e-16, 0.09858965641, 0.8119588708], [-3.864551522e-16, 0.2900392968, 0.7647707728], [-3.401506205e-16, 0.4646329075, 0.6731369771], [-2.740777712e-16, 0.6122237424, 0.542382907], [-1.92076518e-16, 0.7242343588, 0.3801075138], [-9.891247576999999e-17, 0.7941551068, 0.1957416536], [2.8654901189999996e-32, 0.8179224464, -5.670627187e-17], [0.0, 1.15366584, 0.0], [0.0, -1.15366584, 0.0], [0.0, 0.0, 0.0], [5.123305514e-16, 0.0, -1.15366584], [-5.123305514e-16, 0.0, 1.15366584]])
    sdk_grp = mc.group( n = name + '_sdk', em=True)
    adj_grp = mc.group( n = name + '_adj', em=True)
    mc.parent( ctl, sdk_grp)
    mc.parent( sdk_grp,adj_grp)
    mc.setAttr(name + '.overrideEnabled', True)
    mc.setAttr(name + '.overrideColor', color_control) 
    
def CircleOrient(name, color_control):
    ctl = mc.curve( n= name, d = 1, p=[[0.0, 0.0, -0.2737484795], [0.0, 0.0, -1.124885106], [-9.461291464e-18, 4.477446994e-17, -0.9703704894], [-6.690143356e-18, 0.1092583325, -1.015626773], [-1.0794202269999999e-33, 0.1545146155, -1.124885106], [6.690143356e-18, 0.1092583325, -1.234143437], [9.461291464e-18, -8.299010147000001e-17, -1.279399721], [6.690143356e-18, -0.1092583325, -1.234143437], [-2.8508717669999997e-33, -0.1545146155, -1.124885106], [-6.690143356e-18, -0.1092583325, -1.015626773], [-9.461291464e-18, 4.477446994e-17, -0.9703704894], [4.946798863e-17, -4.339104665e-16, -0.8078735631], [4.486856436e-17, -0.3231515597, -0.7327592642], [3.4979150219999997e-17, -0.5712528746, -0.5712528746], [2.11890328e-17, -0.7232772501, -0.3460431664], [-1.4905670399999998e-32, -0.8078735631, 2.4342807099999997e-16], [-1.728760449e-17, -0.7496689331, 0.2823280067], [-3.4979150219999997e-17, -0.5712528746, 0.5712528746], [-4.459268599e-17, -0.3340286437, 0.7282538283], [-4.946798863e-17, 2.341015471e-16, 0.8078735631], [-4.5463743350000005e-17, 0.2996853784, 0.7424792749], [-3.4979150219999997e-17, 0.5712528746, 0.5712528746], [-1.648250013e-17, 0.7551151587, 0.2691796548], [-5.643706012999999e-33, 0.8078735631, 9.216871375e-17], [1.897528541e-17, 0.7382524119, -0.3098899277], [3.4979150219999997e-17, 0.5712528746, -0.5712528746], [4.4690055720000005e-17, 0.3301896376, -0.7298439968], [4.946798863e-17, -4.339104665e-16, -0.8078735631], [4.946798863e-17, -4.339104665e-16, -0.8078735631]])
    sdk_grp = mc.group( n = name + '_sdk', em=True)
    adj_grp = mc.group( n = name + '_adj', em=True)
    mc.parent( ctl, sdk_grp)
    mc.parent( sdk_grp,adj_grp)
    mc.setAttr(name + '.overrideEnabled', True)
    mc.setAttr(name + '.overrideColor', color_control) 
    
def Cone(name, color_control):
    ctl = mc.curve( n= name, d = 1, p=[[0.24974547549999992, 0.002873577053999987, 0.4325716493], [-0.24974547549999998, 0.0028735770539999803, 0.4325716493], [6.661338147750939e-16, 1.0018554789999998, -1.436788527e-09], [0.24974547549999992, 0.002873577053999987, 0.4325716493], [0.4994909509, 0.0028735770539999594, -1.436788527e-09], [6.661338147750939e-16, 1.0018554789999998, -1.436788527e-09], [0.24974547549999992, 0.002873577053999987, -0.4325716522], [0.4994909509, 0.0028735770539999594, -1.436788527e-09], [6.661338147750939e-16, 1.0018554789999998, -1.436788527e-09], [-0.24974547549999998, 0.0028735770539999803, -0.4325721517], [0.24974547549999992, 0.002873577053999987, -0.4325716522], [6.661338147750939e-16, 1.0018554789999998, -1.436788527e-09], [-0.49949095089999995, 0.002873577053999987, -8.078092608000001e-08], [-0.24974547549999998, 0.0028735770539999803, -0.4325721517], [6.661338147750939e-16, 1.0018554789999998, -1.436788527e-09], [-0.24974547549999998, 0.0028735770539999803, 0.4325716493], [-0.49949095089999995, 0.002873577053999987, -8.078092608000001e-08]])
    sdk_grp = mc.group( n = name + '_sdk', em=True)
    adj_grp = mc.group( n = name + '_adj', em=True)
    mc.parent( ctl, sdk_grp)
    mc.parent( sdk_grp,adj_grp)
    mc.setAttr(name + '.overrideEnabled', True)
    mc.setAttr(name + '.overrideColor', color_control) 
    
def Cross(name, color_control):
    ctl = mc.curve( n= name, d = 1, p=[[4.340776215e-17, 0.3, -0.3], [1.610899942e-16, 0.725484838, -0.3], [1.610899942e-16, 0.725484838, 0.3], [4.340776215e-17, 0.3, 0.3], [8.054499711e-17, 0.3, 0.725484838], [-8.054499711e-17, -0.3, 0.725484838], [-4.340776215e-17, -0.3, 0.3], [-1.610899942e-16, -0.725484838, 0.3], [-1.610899942e-16, -0.725484838, -0.3], [-4.340776215e-17, -0.3, -0.3], [-8.054499711e-17, -0.3, -0.725484838], [8.054499711e-17, 0.3, -0.725484838], [4.340776215e-17, 0.3, -0.3]])
    sdk_grp = mc.group( n = name + '_sdk', em=True)
    adj_grp = mc.group( n = name + '_adj', em=True)
    mc.parent( ctl, sdk_grp)
    mc.parent( sdk_grp,adj_grp)
    mc.setAttr(name + '.overrideEnabled', True)
    mc.setAttr(name + '.overrideColor', color_control) 
    
def Square(name, color_control):
    ctl = mc.curve( n= name, d = 1, p=[[-1.456834653e-16, -0.6561, 0.6561], [1.456834653e-16, 0.6561, 0.6561], [1.456834653e-16, 0.6561, -0.6561], [-1.456834653e-16, -0.6561, -0.6561], [-1.456834653e-16, -0.6561, 0.6561]])
    sdk_grp = mc.group( n = name + '_sdk', em=True)
    adj_grp = mc.group( n = name + '_adj', em=True)
    mc.parent( ctl, sdk_grp)
    mc.parent( sdk_grp,adj_grp)
    mc.setAttr(name + '.overrideEnabled', True)
    mc.setAttr(name + '.overrideColor', color_control) 
    
def Circle(name, color_control):
    ctl = mc.circle(n=name)    
    sdk_grp = mc.group( n = name + '_sdk', em=True)
    adj_grp = mc.group( n = name + '_adj', em=True)
    mc.parent( ctl, sdk_grp)
    mc.parent( sdk_grp, adj_grp)
    mc.setAttr(name + '.overrideEnabled', True)
    mc.setAttr(name + '.overrideColor', color_control) 
    