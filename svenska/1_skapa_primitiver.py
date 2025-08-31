# ——————————————————————————————————————————————————————————————————————
# Aktivitet 1: Skapa primitiver
# ——————————————————————————————————————————————————————————————————————

# Blender styrs till stor del av operators - små programdelar som utför specifika handlingar.
# När du utför en handling i Blender, t.ex. lägga till en kub, används bakom kulisserna en
# "skapa-kub-operator".

# Lägg till följande kod i kodblocket nedan, tryck sedan Run Script (play-knappen högst upp ▲)

""" Ignorera denna rad

import bpy

bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 2))

bpy.ops.mesh.primitive_cone_add(radius1=1, depth=2, location=(-3, 0, 1))

bpy.ops.mesh.primitive_monkey_add(size=2, location=(3, 0, 1))

bpy.ops.object.light_add(type='SUN', location=(0, -3, 0), rotation=(0.52, 0, 0.35))

Ignorera denna rad """

# LÄGG TILL KODEN NEDANFÖR
# vvvvvvvvvvvvvvvvvvv



# ^^^^^^^^^^^^^^^^^^^^
# LÄGG TILL KODEN OVANFÖR

# Notera att dessa kommandon börjar med 'bpy.ops' vilket säger oss att de är operators.
