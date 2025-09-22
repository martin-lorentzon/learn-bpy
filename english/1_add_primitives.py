# ——————————————————————————————————————————————————————————————————————
# Activity 1: Create primitives
# ——————————————————————————————————————————————————————————————————————

# Blender is largely controlled by operators - small programs that perform 
# a specific action.
# When a new cube is added, Blender uses an "add-cube-operator" behind the scenes.

# Add the following code in the code block below, then press Run Script (play button at the top ▲)

""" Ignore this line

import bpy

bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 2))

bpy.ops.mesh.primitive_cone_add(radius1=1, depth=2, location=(-3, 0, 1))

bpy.ops.mesh.primitive_monkey_add(size=2, location=(3, 0, 1))

Ignore this line """

# ——————————————————————————————————————————————————————————————————————

# ADD CODE BELOW
# vvvvvvvvvvvvvvvvvvvv



# ^^^^^^^^^^^^^^^^^^^^
# ADD CODE ABOVE

# ——————————————————————————————————————————————————————————————————————

# Note that these commands start with 'bpy.ops' which tells us that they are operators.

# Similar to functions, operators allow us to use parameters to control its behaviour.

# Executing existent operators in script is a quick way to automate common tasks;
# however, it may not offer us the flexibility to solve more complex problems.
# For this we could create and expose our own custom operators in the UI.


# References
# https://docs.blender.org/api/current/bpy.ops.html
# https://docs.blender.org/api/current/bpy.context.html