# STYLE ***************************************************************************
# content = assignment (Python Advanced)
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#**********************************************************************************


# COMMENT --------------------------------------------------
# Not optimal
def set_color(ctrlList=None, color=None):

    for ctrlName in ctrlList:
        try: mc.setAttr(ctrlName + 'Shape.overrideEnabled', 1)           
        except: pass
            
        try:
            if color == 1:   mc.setAttr(ctrlName + 'Shape.overrideColor', 4)               
            elif color == 2: mc.setAttr(ctrlName + 'Shape.overrideColor', 13)               
            elif color == 3: mc.setAttr(ctrlName + 'Shape.overrideColor', 25)                
            elif color == 4 or color == 5: mc.setAttr(ctrlName + 'Shape.overrideColor', 17)                               
            elif color == 6: mc.setAttr(ctrlName + 'Shape.overrideColor', 15)               
            elif color == 7: mc.setAttr(ctrlName + 'Shape.overrideColor', 6)      
            elif color == 8: mc.setAttr(ctrlName + 'Shape.overrideColor', 16)               
        except: pass
            
# EXAMPLE
# set_color(['circle','circle1'], 8)


