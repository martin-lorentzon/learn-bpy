# ——————————————————————————————————————————————————————————————————————
# Aktivitet 4: Custom Properties
# ——————————————————————————————————————————————————————————————————————

# Properties kan användas för att ge datablock nya egenskaper som lagras
# och exponeras inom Blenders användargränssnitt.
# De kan bestå av olika datatyper (t.ex. text, heltal, booleska värden osv.)
# och används ofta för att ge metadata eller styra funktionalitet i scripts/add-ons.

# Lägg till följande kod i kodblocket nedan, tryck sedan Run Script (play-knappen högst upp ▲)

""" Ignorera denna rad

# Utökar objekt-typen med en ny custom property
bpy.types.Object.part_name = StringProperty(
                             name="Part Name",
                             default="-Missing Part Name-"
                             )
bpy.types.Object.lod_level = IntProperty(
                             name="Level of detail",
                             description="The quality of this part, lower=better",
                             min=0,
                             max=4,
                             default=0
                             )
bpy.types.Object.has_issue = BoolProperty(name="Has Issue(s)", default=False)

Ignorera denna rad """

# ——————————————————————————————————————————————————————————————————————

import bpy
from bpy.props import StringProperty, IntProperty, BoolProperty


class LEARN_BPY_PT_properties_panel(bpy.types.Panel):
    bl_label = "Custom Properties"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Learn-bpy"
    
    # Poll-metoden bestämmer när panelen ska synas
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
#    Registrering    #
# —————————————————— #

# LÄGG TILL KODEN NEDANFÖR
# vvvvvvvvvvvvvvvvvvv



# ^^^^^^^^^^^^^^^^^^^^
# LÄGG TILL KODEN OVANFÖR

bpy.utils.register_class(LEARN_BPY_PT_properties_panel)

# ——————————————————————————————————————————————————————————————————————

# Dessa properties visas nu i en egen panel
# 3D Viewport ▶ N-panel ▶ Learn-bpy ▶ Custom Properties

# Scenobjekt är inte ensamma i att kunna bli utvecklade på detta vis.
# Även scener, material, collections, kameror, m.m. kan vi definiera properties på.

# Fler användningsområden för properties inkluderar

# - Skapa parametrar för operators (se andra refensen)

# - Preferenser (finns exempel i Text Editor ▶ Templates ▶ New Add-on)

# - Gruppering av egenskaper med Property Groups (se tredje referensen)


# Referenser
# https://docs.blender.org/api/current/bpy.props.html
# https://docs.blender.org/api/current/bpy.props.html#operator-example
# https://docs.blender.org/api/current/bpy.props.html#propertygroup-example