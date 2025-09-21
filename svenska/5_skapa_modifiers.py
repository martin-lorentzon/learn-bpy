# ——————————————————————————————————————————————————————————————————————
# Aktivitet 7: Skapa Modifiers
# ——————————————————————————————————————————————————————————————————————

# Modifiers lagras på objekt och ändrar ett objekts utseende.

# I nyare versioner av Blender är det vanligt att en modifier består av
# noder, dvs. Geometry Nodes.

# Inför denna aktivit behöver du skapa en ny Geometry Nodes-grupp,
# och redigera variabeln nedan för att matcha namnet du gav nodgruppen.

GEOMETRY_NODES_NAME = "Geometry Nodes"

# Nu ska vi testa att lägga till modifiers på det aktiva objektet.

# Lägg till följande kod i kodblocket nedan, tryck sedan Run Script (play-knappen högst upp ▲)

""" Ignorera denna rad

import bpy


active_object = bpy.context.active_object

if active_object is None:
    raise Exception("No active object, cancelled")


active_object.modifiers.clear() # Tar bort alla modifiers

# Lägger till en ny Subdivision-modifier
subsurf = active_object.modifiers.new(name="MySubdivision", type="SUBSURF")
subsurf.levels = 2
subsurf.render_levels = 3

# Lägger till en ny Geometry Nodes-modifier
nodes_modifier = active_object.modifiers.new(name="MyGeometryNodes", type="NODES")
nodes_modifier.node_group = bpy.data.node_groups[GEOMETRY_NODES_NAME]

Ignorera denna rad """

# ——————————————————————————————————————————————————————————————————————

# LÄGG TILL KODEN NEDANFÖR
# vvvvvvvvvvvvvvvvvvv



# ^^^^^^^^^^^^^^^^^^^^
# LÄGG TILL KODEN OVANFÖR

# ——————————————————————————————————————————————————————————————————————

# Denna kod demonstrerar grundläggande hantering av modifiers i Blender.
# Vi lär oss att rensa befintliga modifiers, lägga till nya (Subdivision och
# Geometry Nodes), samt konfigurera deras inställningar programmatiskt.

# Att kombinera Python med Geometry Nodes är ett kraftfullt sätt att skapa
# verktyg på.


# Referenser
# https://docs.blender.org/api/current/bpy.types.Modifier.html
# https://docs.blender.org/api/current/bpy.types.NodesModifier.html