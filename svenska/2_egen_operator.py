# ——————————————————————————————————————————————————————————————————————
# Aktivitet 2: Egen operator
# ——————————————————————————————————————————————————————————————————————

# "Operator" är Blenders ramverk för att skapa de handlingar användaren
# ska kunna utföra.

# De kommer med en hel del praktiska förmågor som bidrar till ett bra UI/UX.
# De kan bland annat

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
        print("Hello, World!")
        return {"FINISHED"}


bpy.utils.register_class(LEARN_BPY_OT_hello_world)  # Registrerar operatorn

def draw_func(self, context):
    self.layout.operator("wm.hello_world")

bpy.types.VIEW3D_MT_view.append(draw_func)

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

# Registrering
# I Blender måste vi registrera klasser som definierar operators, paneler, 
# menyer eller property groups.
# Andra klasser, som bara innehåller hjälpfunktioner exempelvis, ska inte registreras.
# Tumregeln kan man säga är- Kommer klassen synas eller gå att interagera med? Registrera.

# För att ta reda på vilka möjliga menyer som finns kan vi använda oss 
# av denna hjälpfunktion

import bpy

def print_all_menu_names():
    for name in dir(bpy.types):
        cls = getattr(bpy.types, name)
        if isinstance(cls, type) and issubclass(cls, bpy.types.Menu):
            print(cls.__name__)

print_all_menu_names()


# Referenser
# https://docs.blender.org/api/current/bpy.types.Operator.html