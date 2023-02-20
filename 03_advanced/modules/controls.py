import json

import maya.cmds as cmds

'''
Change this module to classes allow me to write the groups lines once instead of do it multiple
times for every shape
'''

####################################################################################################
json_path = r'J:\\python advance\\aparejador\\03_advanced\\data\\controles_points.json'
with open(json_path, 'r') as points_json:
    points_data = json.load(points_json)

class Control:
    def __init__(self, name, color_name):
        self.name = name
        self.color = self.get_color(color_name)
        self.sdk_grp = cmds.group(name=f'{name}_sdk', empty=True)
        self.adj_grp = cmds.group(name=f'{name}_adj')

    def get_color(cls, color_name):
        colors = {
            "Yellow": 17,
            "Green": 14,
            "Red": 13,
            "Blue": 6,
            "Pink": 20,
            "Little Blue": 18,
            "White": 16,
            'Little Green': 19
        }
        return colors.get(color_name)

class Cube(Control):
    def __init__(self, name, color_name):
        super().__init__(name, color_name)
        self.generate()

    def generate(self):
        cmds.curve(name=self.name, degree=1, point=points_data['Cube'])
        cmds.setAttr(f'{self.name}.overrideEnabled', True)
        cmds.setAttr(f'{self.name}.overrideColor', self.color)
        cmds.parent(self.name, self.sdk_grp)
class Sphere(Control):
    def __init__(self, name, color_name):
        super().__init__(name, color_name)
        self.generate()
    def generate(self):
        cmds.circle(name=self.name)
        cmds.circle(name=f'{self.name}1')
        cmds.circle(name=f'{self.name}2')
        cmds.select(f'{self.name}1.cv[0:7]', replace=True)
        cmds.rotate(90, 0, 0)
        cmds.select(f'{self.name}2.cv[0:7]')
        cmds.rotate(0, 90, 0)
        cmds.select(f'{self.name}1Shape', f'{self.name}2Shape')
        cmds.select(self.name, add=1)
        cmds.parent(r=True, s=True)
        cmds.delete(f'{self.name}1', f'{self.name}2')
        
        cmds.parent(self.name, self.sdk_grp)
        cmds.parent(self.sdk_grp, self.adj_grp)

class Pin(Control):
    def __init__(self, name, color_name):
        super().__init__(name, color_name)
        self.generate()
    def generate(self):
        cmds.curve(n=self.name, degree=1, point=points_data['Pin'])
        cmds.select('curveShape1.cv[0:17]')
        cmds.scale(10,10,10, r=1, ocp=1 )
        cmds.setAttr(f'{self.name}.overrideEnabled', True)
        cmds.setAttr(f'{self.name}.overrideColor', self.color)
        cmds.parent(self.name, self.sdk_grp)
        
        
class RectangleSide(Control):
    def __init__(self, name, color_name):
        super().__init__(name, color_name)
        self.generate()
    def generate(self):
        cmds.curve(name=self.name, degree=1, point=points_data['RectangleSide'])
        cmds.setAttr(f'{self.name}.overrideEnabled', True)
        cmds.setAttr(f'{self.name}.overrideColor', self.color)
        cmds.parent(self.name, self.sdk_grp)

class RectangleFront(Control):
    def __init__(self, name, color_name):
        super().__init__(name, color_name)
        self.generate()
    def generate(self):
        cmds.curve(name=self.name, degree=1, point=points_data['RectangleFront'])
        cmds.setAttr(f'{self.name}.overrideEnabled', True)
        cmds.setAttr(f'{self.name}.overrideColor', self.color)
        cmds.parent(self.name, self.sdk_grp)

class Orient(Control):
    def __init__(self, name, color_name):
        super().__init__(name, color_name)
        self.generate()
    def generate(self):
        cmds.curve(name=self.name, degree=1, point=points_data['Orient'])
        cmds.setAttr(f'{self.name}.overrideEnabled', True)
        cmds.setAttr(f'{self.name}.overrideColor', self.color)
        cmds.parent(self.name, self.sdk_grp)

class Arrow(Control):
    def __init__(self, name, color_name):
        super().__init__(name, color_name)
        self.generate()
    def generate(self):
        cmds.curve(name=self.name, degree=1, point=points_data['Arrow'])
        cmds.setAttr(f'{self.name}.overrideEnabled', True)
        cmds.setAttr(f'{self.name}.overrideColor', self.color)
        cmds.parent(self.name, self.sdk_grp)

class DoubleArrow(Control):
    def __init__(self, name, color_name):
        super().__init__(name, color_name)
        self.generate()
    def generate(self):
        cmds.curve(name=self.name, degree=1, point=points_data['DoubleArrow'])
        cmds.setAttr(f'{self.name}.overrideEnabled', True)
        cmds.setAttr(f'{self.name}.overrideColor', self.color)
        cmds.parent(self.name, self.sdk_grp)
    
class CircleCross(Control):
    def __init__(self, name, color_name):
        super().__init__(name, color_name)
        self.generate()   
    def generate(self):
        cmds.curve(name=self.name, degree=1, point=points_data['CircleCross'])
        cmds.setAttr(f'{self.name}.overrideEnabled', True)
        cmds.setAttr(f'{self.name}.overrideColor', self.color)
        cmds.parent(self.name, self.sdk_grp)
    
class CircleOrient(Control):
    def __init__(self, name, color_name):
        super().__init__(name, color_name)
        self.generate()
    def generate(self):
        cmds.curve(name=self.name, degree=1, point=points_data['CircleOrient'])
        cmds.setAttr(f'{self.name}.overrideEnabled', True)
        cmds.setAttr(f'{self.name}.overrideColor', self.color)
        cmds.parent(self.name, self.sdk_grp)
    
class Cone(Control):
    def __init__(self, name, color_name):
        super().__init__(name, color_name)
        self.generate()
    def generate(self):
        cmds.curve(name=self.name, degree=1, point=points_data['Cone'])
        cmds.setAttr(f'{self.name}.overrideEnabled', True)
        cmds.setAttr(f'{self.name}.overrideColor', self.color)
        cmds.parent(self.name, self.sdk_grp)
    
class Cross(Control):
    def __init__(self, name, color_name):
        super().__init__(name, color_name)
        self.generate()
    def generate(self):
        cmds.curve(name=self.name, degree=1, point=points_data['Cross'])
        cmds.setAttr(f'{self.name}.overrideEnabled', True)
        cmds.setAttr(f'{self.name}.overrideColor', self.color)
        cmds.parent(self.name, self.sdk_grp)
class Circle(Control):
    def __init__(self, name, color_name):
        super().__init__(name, color_name)
        self.generate()
    def generate(self):
        cmds.circle(name=self.name) 
        cmds.setAttr(f'{self.name}.overrideEnabled', True)
        cmds.setAttr(f'{self.name}.overrideColor', self.color)
        cmds.parent(self.name, self.sdk_grp)

class Square(Control):
    def __init__(self, name, color_name):
        super().__init__(name, color_name)
        self.generate()
    def generate(self):
        cmds.curve(name=self.name, degree=1, point=points_data['Square'])
        cmds.setAttr(f'{self.name}.overrideEnabled', True)
        cmds.setAttr(f'{self.name}.overrideColor', self.color)
        cmds.parent(self.name, self.sdk_grp)

# Cube(color_name = 'Yellow', name = f'Hand_ctrl')