from maya import cmds

# Create cube
cube = cmds.polyCube()
cubeShape = cube[0]

# Create a circle
circle = cmds.circle()
circleShape = circle[0]

# Parent the cube inside the circle
cmds.parent(cubeShape, circleShape)

# Create cube translation values
cmds.setAttr(cubeShape +".translate", lock=True)
cmds.setAttr(cubeShape + ".rotate", lock=True)
cmds.setAttr(cubeShape + ".scale", lock=True)
