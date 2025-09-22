# ——————————————————————————————————————————————————————————————————————
# Activity 2: Custom operator
# ——————————————————————————————————————————————————————————————————————

# "Operator" is Blender's framework for creating the actions that users
# should be able to perform.

# They come with a lot of practical capabilities that contribute to a good UI/UX.
# They can, among other things:

# - Be placed in menus as buttons
# - Create new interactions inside the 3D viewport
# - Be registered in the 'Undo' queue
# - Be executed from hotkeys


# Let's create a simple operator

# Add the following code to the code block below, then press Run Script (play button at the top ▲)

""" Ignore this line

import bpy


class LEARN_BPY_OT_hello_world(bpy.types.Operator):
    bl_idname = "wm.hello_world"
    bl_label = "Hello World Operator"
   
    def execute(self, context):
        print("Hello, World!")
        return {"FINISHED"}

    
bpy.utils.register_class(LEARN_BPY_OT_hello_world)  # Registers the operator

def draw_func(self, context):
    self.layout.operator("wm.hello_world")

bpy.types.VIEW3D_MT_view.append(draw_func)

Ignore this line """

# ——————————————————————————————————————————————————————————————————————

# ADD THE CODE BELOW
# vvvvvvvvvvvvvvvvvvvv



# ^^^^^^^^^^^^^^^^^^^^
# ADD THE CODE ABOVE

# ——————————————————————————————————————————————————————————————————————

# In this example, we place the operator at the end of the View menu
# 3D Viewport ▶ View ▶ Hello World Operator

# ...but it can also be found using Blender's search function (F3).

# The main code of the operator goes in the execute methond.

# 'context' gives us access to the operator's context variables such as

# - context.object    # The active object
# - context.active_object     # The active object (as long as it's visible in the scene)
# - context.selected_objects  # The selected objects
# - context.material  # The active material


# Its 'bl_idname' consists of a category and the operator's name.
# Some common categories include wm, object, mesh and view3d.
# wm = Window Manager

# Registration
# In Blender, we must register classes that define operators, panels,
# menus or property groups.
# Other classes, only containing helper functions for example, should not be registered.
# The general rule of thumb is: Will the class be visible or interactable? Register it.

# To find out what possible menus exist, we can use
# this helper function

import bpy

def print_all_menu_names():
    for name in dir(bpy.types):
        cls = getattr(bpy.types, name)
        if isinstance(cls, type) and issubclass(cls, bpy.types.Menu):
            print(cls.__name__)

print_all_menu_names()


# References
# https://docs.blender.org/api/current/bpy.types.Operator.html
# https://docs.blender.org/api/current/bpy.context.html