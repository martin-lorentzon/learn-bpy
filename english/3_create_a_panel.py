# ——————————————————————————————————————————————————————————————————————
# Activity 3: Create a panel
# ——————————————————————————————————————————————————————————————————————

# Panels are often used to display and group UI elements.

# A panel's location in the user interface is determined by the following attributes

# bl_space_type  - typically the same as the editor type
# bl_region_type - the area where the panel is placed within the editor
# bl_category    - the category the panel belongs to - if applicable (optional text)
# bl_label       - the name of the panel (optional text)

# See the third and fourth references below to know what possible values
# exist for bl_space_type and bl_region_type.

# Classes that create custom user interfaces always need their own draw method.
# The draw method describes all its UI elements, such as rows, columns,
# buttons, etc.


# Add the following code in the code block below, then press Run Script (play button at the top ▲)

""" Ignore this line

import bpy


class LEARN_BPY_PT_hello_world(bpy.types.Panel):
    bl_label = "Hello World"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Learn-bpy"
    
    def draw(self, context):
        layout = self.layout
        
        layout.label(text="Hello, World!")
        

bpy.utils.register_class(LEARN_BPY_PT_hello_world)

Ignore this line """

# ——————————————————————————————————————————————————————————————————————

# ADD THE CODE BELOW
# vvvvvvvvvvvvvvvvvvvv



# ^^^^^^^^^^^^^^^^^^^^
# ADD THE CODE ABOVE

# ——————————————————————————————————————————————————————————————————————

# This code places the panel in the 3D viewport's side panel
# 3D Viewport ▶ N-panel ▶ Learn-bpy ▶ Hello World

# Experiment with adding more UI elements in the panel's draw method.

# Some examples

""" Ignore this line

        # Example of operator button
        op = layout.operator("mesh.primitive_cube_add", icon="MESH_CUBE")
        op.scale = (1, 1, 1)
        
        # Example of property
        if context.object is not None:
            layout.prop(context.object, "location")
        
        # Example of multiple columns
        row = layout.row()
        col1 = row.column()
        col2 = row.column()
        col1.label(text="Column 1")
        col2.label(text="Column 2")
        
        # Example of subpanel
        header, panel = layout.panel("my_panel_id", default_closed=False)
        header.label(text="Hello World")
        if panel:
            panel.label(text="Success")

Ignore this line """

# More functions can be found in the reference for UILayout.

# Registration
# Remember that panels must be registered.


# References
# https://docs.blender.org/api/current/bpy.types.Panel.html
# https://docs.blender.org/api/current/bpy.types.UILayout.html
# https://docs.blender.org/api/current/bpy_types_enum_items/space_type_items.html
# https://docs.blender.org/api/current/bpy_types_enum_items/region_type_items.html
# https://developer.blender.org/docs/release_notes/4.1/python_api/#layout-panels