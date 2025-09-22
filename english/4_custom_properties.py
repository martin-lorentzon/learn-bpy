# ——————————————————————————————————————————————————————————————————————
# Activity 4: Custom Properties
# ——————————————————————————————————————————————————————————————————————

# Properties can be used to give data blocks new properties that are stored
# and exposed within Blender's user interface.
# They can consist of different data types (e.g. text, integers, boolean values etc.)
# and are often used to provide metadata or control functionality in scripts/add-ons.

# In this example we will create our own custom properties and
# expose them in Blender's user interface.

# Add the following code to the code block below, then press Run Script (play button at the top ▲)

""" Ignore this line

# Extends the object type with a new custom property
bpy.types.Object.part_name = bpy.props.StringProperty(
                             name="Part Name",
                             default="-Missing Part Name-"
                             )

bpy.types.Object.lod_level = bpy.props.IntProperty(
                             name="Level of detail",
                             description="The quality of this part, lower=better",
                             min=0,
                             max=4,
                             default=0
                             )

bpy.types.Object.has_issue = bpy.props.BoolProperty(name="Has Issue(s)", default=False)

Ignore this line """

# ——————————————————————————————————————————————————————————————————————

import bpy


class LEARN_BPY_PT_properties_panel(bpy.types.Panel):
    bl_label = "Custom Properties"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Learn-bpy"
    
    # The poll method determines when the panel should be visible
    @classmethod
    def poll(cls, context):
        result = context.active_object is not None
        return result
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        
        if context.object.has_issue:
            row.alert = True
        
        row.prop(context.object, "part_name")
        
        layout.prop(context.object, "lod_level")
        layout.prop(context.object, "has_issue")
        

# —————————————————— #
#    Registration    #
# —————————————————— #

# ADD THE CODE BELOW
# vvvvvvvvvvvvvvvvvvvv



# ^^^^^^^^^^^^^^^^^^^^
# ADD THE CODE ABOVE

bpy.utils.register_class(LEARN_BPY_PT_properties_panel)

# ——————————————————————————————————————————————————————————————————————

# These properties are now displayed in their own panel
# 3D Viewport ▶ N-panel ▶ Learn-bpy ▶ Custom Properties

# Scene objects are not alone in being able to be extended in this way.
# We can also define properties on scenes, materials, collections, cameras, etc.

# More use cases for properties are

# - Creating parameters for operators (see second reference)

# - Grouping of properties with Property Groups (see third reference)

# - Add-on preferences (see example in Text Editor ▶ Templates ▶ New Add-on)


# References
# https://docs.blender.org/api/current/bpy.props.html
# https://docs.blender.org/api/current/bpy.props.html#operator-example
# https://docs.blender.org/api/current/bpy.props.html#propertygroup-example