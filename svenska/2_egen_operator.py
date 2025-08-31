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
from bpy.utils import register_class

class LEARN_BPY_OT_hello_world(bpy.types.Operator):
    bl_idname = "wm.hello_world"
    bl_label = "Hello World Operator"
    
    def execute(self, context):
        print("Hello, World!")
        return {"FINISHED"}


register_class(LEARN_BPY_OT_hello_world)

def menu_func(self, context):
    self.layout.operator("wm.hello_world")

bpy.types.VIEW3D_MT_view.append(menu_func)

Ignorera denna rad """

# LÄGG TILL KODEN NEDANFÖR
# vvvvvvvvvvvvvvvvvvv



# ^^^^^^^^^^^^^^^^^^^^
# LÄGG TILL KODEN OVANFÖR

# Kom ihåg att vi måste registrera operatorn för att den ska fungera ihop med Blender.

# I detta exemplet placerar vi operatorn i slutet på View-menyn,
# den kan också hittas med hjälp av Blenders sökfunktion (F3).

# 3D Viewport ▶ View ▶ Hello World Operator