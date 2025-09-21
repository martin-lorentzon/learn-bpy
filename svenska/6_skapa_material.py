# ——————————————————————————————————————————————————————————————————————
# Aktivitet 6: Skapa material
# ——————————————————————————————————————————————————————————————————————

# Material i Blender definieras med hjälp av nodträd.
# Ett material kan innehålla olika typer av noder. Varje nod har sina
# egna inputs och outputs. Noder kopplas samman genom att skapa en länk
# från en nods output till en annan nods input.

# I detta exempel ska vi:

# - Skapa ett nytt material
# - Hitta en specifik nod (Principled BSDF)
# - Lägga till en ny Image Texture-nod
# - Koppla ihop nya Image Texture-noden med BSDF-noden


# Lägg till följande kod i kodblocket nedan, tryck sedan Run Script (play-knappen högst upp ▲)

""" Ignorera denna rad

# Tar bort materialet om det existerar sedan tidigare
if my_material is not None:
    materials.remove(my_material)

# Skapar ett nytt material
my_material = materials.new("Test Material")

# De olika delarna av nodträdet
my_material.use_nodes = True
node_tree = my_material.node_tree
nodes = node_tree.nodes
links = node_tree.links

# Exempel på att hitta en nod av en särskild typ
bsdf_node = None
for node in nodes:
    if node.bl_idname == "ShaderNodeBsdfPrincipled":
        bsdf_node = node
        break

# Skapar en ny Image Texture-nod
image_node = nodes.new("ShaderNodeTexImage")
image_node.location = (-500, 100)

# Skapar en länk mellan Image Texture-noden och BSDF-noden
from_socket = image_node.outputs[0]
to_socket = bsdf_node.inputs[0]
links.new(from_socket, to_socket)

Ignorera denna rad """

# ——————————————————————————————————————————————————————————————————————

import bpy


materials = bpy.data.materials
my_material = materials.get("Test Material")

# LÄGG TILL KODEN NEDANFÖR
# vvvvvvvvvvvvvvvvvvv



# ^^^^^^^^^^^^^^^^^^^^
# LÄGG TILL KODEN OVANFÖR

# ——————————————————————————————————————————————————————————————————————

# För att se resultatet navigerar du till shader-editorn
# och väljer materialet 'Test Material'.

# Denna kod skapar ett nytt material, hittar Principled BSDF-noden
# och länkar den med en ny Image Texture-nod.

# Om materialet redan finns tar koden bort materialet innan det
# skapas på nytt, detta kan vara önskevärt om vi uppdaterar ett
# material ur ett materialbibliotek t.ex.

# För att hitta en nod av en specifik typ (t.ex. 'Mix Color')
# så använder vi strikt dess bl_idname, klassens unika identifierare.

# Om du vill kan du experimentera med att lägga till - samt länka -
# fler typer av noder.

# För att ta reda på vilka möjliga nodtyper som finns kan vi använda
# oss av denna hjälpfunktion

import bpy

def print_all_node_names():
    for name in dir(bpy.types):
        cls = getattr(bpy.types, name)
        if isinstance(cls, type) and issubclass(cls, bpy.types.Node):
            print(cls.__name__)

print_all_node_names()


# Referenser
# https://docs.blender.org/api/current/bpy.types.Material.html
# https://docs.blender.org/api/current/bpy.types.Node.html