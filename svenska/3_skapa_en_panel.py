# ——————————————————————————————————————————————————————————————————————
# Aktivitet 3: Skapa en panel
# ——————————————————————————————————————————————————————————————————————

# Paneler används ofta för att visa och gruppera UI-element som hör samman.

# En panels plats i användargränssnittet bestäms av följande attribut

# bl_space_type - typiskt sätt detsamma som editor-typen
# bl_region_type - ytan som panelen placeras på inom editorn
# bl_category - kategorin panelen hör hemma i - om applicerbart (valfri text)
# bl_label - namnet på panelen (valfri text)

# Klasser som skapar egna användargränssnitt behöver alltid sin egna draw-metod.
# Inuti denna beskrivs alla dess UI-element som till exempel rader, kolumner, knappar osv.

# Lägg till följande kod i kodblocket nedan, tryck sedan Run Script (play-knappen högst upp ▲)

""" Ignorera denna rad

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

Ignorera denna rad """

# ——————————————————————————————————————————————————————————————————————

# LÄGG TILL KODEN NEDANFÖR
# vvvvvvvvvvvvvvvvvvv



# ^^^^^^^^^^^^^^^^^^^^
# LÄGG TILL KODEN OVANFÖR

# ——————————————————————————————————————————————————————————————————————

# Denna kod placerar panelen i 3D-vyportens sidopanel
# 3D Viewport ▶ N-panel ▶ Learn-bpy ▶ Hello World

# Experimentera med att lägga till fler UI-element i panelens draw-metod.

# Några exempel

""" Ignorera denna rad

        # Exempel på operator-knapp
        op = layout.operator("mesh.primitive_cube_add", icon="MESH_CUBE")
        op.scale = (1, 1, 1)
        
        # Exempel på property
        if context.object is not None:
            layout.prop(context.object, "location")
        
        # Exempel på flera kolumner
        row = layout.row()
        col1 = row.column()
        col2 = row.column()
        col1.label(text="Column 1")
        col2.label(text="Column 2")
        
        # Exempel på subpanel
        header, panel = layout.panel("my_panel_id", default_closed=False)
        header.label(text="Hello World")
        if panel:
            panel.label(text="Success")

Ignorera denna rad """

# Fler funktioner går att hitta i referensen för UILayout.

# Namnkonvention
# UPPER_CASE_PT_lower_case 
# PT - Panel Type

# Registrering
# Kom ihåg att paneler måste registreras.


# Referenser
# https://docs.blender.org/api/current/bpy.types.Panel.html
# https://docs.blender.org/api/current/bpy.types.UILayout.html
# https://docs.blender.org/api/current/bpy_types_enum_items/space_type_items.html
# https://docs.blender.org/api/current/bpy_types_enum_items/region_type_items.html
# https://developer.blender.org/docs/release_notes/4.1/python_api/#layout-panels