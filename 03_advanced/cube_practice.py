import maya.cmds as cmds


# CUBE CLASS

# 1. CREATE an abstract class "Cube" with the functions:
#    translate(x, y, z), rotate(x, y, z), scale(x, y, z) and color(R, G, B)
#    All functions store and print out the data in the cube (translate, rotate, scale and color).

# 2. ADD an __init__(name) and create 3 cube objects.

# 3. ADD the function print_status() which prints all the variables nicely formatted.

# 4. ADD the function update_transform(ttype, value).
#    "ttype" can be "translate", "rotate" and "scale" while "value" is a list of 3 floats.
#    This function should trigger either the translate, rotate or scale function.

#    BONUS: Can you do it without using ifs?

# 5. CREATE a parent class "Object" which has a name, translate, rotate and scale.
#    Use Object as the parent for your Cube class.
#    Update the Cube class to not repeat the content of Object.



class Object:
    def __init__(self, name, translate, rotate, scale):
        self.cube = cmds.polyCube(name=name)
        cmds.move(translate[0],translate[1],translate[2])
        cmds.rotate(rotate[0],rotate[1],rotate[2])
        cmds.scale(scale[0],scale[1],scale[2])

class Cube(Object):
    def __init__(self, name, translate, rotate, scale):
        super().__init__(name, translate, rotate, scale)


    def translate(self):
        cmds.select(self.cube)
        self.translation = cmds.xform(q=True, translation=True)
        print(f'translate : {self.translation}')

    def rotate(self):
        cmds.select(self.cube)
        self.rotation = cmds.xform(q=True, rotation=True)
        print(f'rotate : {self.rotation}')

    def scale(self):
        cmds.select(self.cube)
        self.scale = cmds.xform(q=True, scale=True, relative=True)
        print(f'scale : {self.scale}')

    def color(self):
        #color = cmds.xform(q=True, translation=True)
        #print(color)
        pass

    def print_status(self):
        self.translate()
        self.rotate()
        self.scale()
        self.color()

    def translation(value):
        cmds.select(self.cube)
        cmds.move(value)

    def rotation(value):
        cmds.select(self.cube)
        cmds.rotate(value)

    def scaling(value):
        cmds.select(self.cube)
        cmds.scale(value)

    def update_transform(self, ttype, value):
        movement = {
           'translate' : self.translation,
           'rotate' : self.rotation,
           'scale' : self.scaling,
        }

        movement.get(ttype)(value[0],value[1],value[2])
        # try:
        #     movement.get(ttype)(value)
        # except:
        #     print(f'{ttype} or {value} invalid')

        

cube1 = Cube('cube1', (2,2,2), (0,0,0), (1,1,1))

cube1.update_transform('translate', (8,8,8))
cube1.print_status()