# ——————————————————————————————————————————————————————————————————————
# Aktivitet 2: Egen operator
# ——————————————————————————————————————————————————————————————————————

# "Operator" är Blenders ramverk för att skapa de handlingar användaren ska kunna utföra.

# Operators kommer med en hel del praktiska förmågor som bidrar till ett bra UI/UX.
# Några av dessa är

# - Bli placerade i menyer som knappar
# - Skapa nya interaktioner inuti 3D-vyporten
# - Registreras i 'Undo'-kön
# - Köras från hotkeys

# Lägg till följande kod i kodblocket nedan, tryck sedan Run Script (play-knappen högst upp ▲)

""" Ignorera denna rad

import bpy


class LEARN_BPY_OT_hello_world(bpy.types.Operator):
    bl_idname = "wm.hello_world"
    bl_label = "Hello World Operator"
    
    def execute(self, context):
        self.report({"INFO"}, "Hello, World!")
        return {"FINISHED"}


bpy.utils.register_class(LEARN_BPY_OT_hello_world)

def menu_func(self, context):
    self.layout.operator("wm.hello_world")

bpy.types.VIEW3D_MT_view.append(menu_func)

Ignorera denna rad """

# ——————————————————————————————————————————————————————————————————————

# LÄGG TILL KODEN NEDANFÖR
# vvvvvvvvvvvvvvvvvvv



# ^^^^^^^^^^^^^^^^^^^^
# LÄGG TILL KODEN OVANFÖR

# ——————————————————————————————————————————————————————————————————————

# 3D Viewport ▶ View ▶ Hello World Operator

# I detta exempel placerar vi operatorn i slutet på View-menyn,
# men den kan också hittas med hjälp av Blenders sökfunktion (F3).

# Inuti execute-metoden körs den huvudsakliga koden av operatorn.

# Dess 'bl_idname' består av en kategori och operatorns namn.
# Några vanliga kategorier inkluderar wm, object, mesh och view3d.
# wm = Window Manager

# Namnkonvention
# Här används namnkonventionen UPPER_CASE_OT_lower_case åt klassens namn 
# med OT som förkortning på Operator Type.

# Registrering
# I Blender måste vi registrera klasser som definierar operators, paneler, 
# menyer eller property groups.
# Andra klasser, som bara innehåller hjälpfunktioner exempelvis, ska inte registreras.
# Tumregeln kan man säga är "Kommer klassen synas eller gå att interagera med? Registrera."


# Referenser
# https://docs.blender.org/api/current/bpy.types.Operator.html