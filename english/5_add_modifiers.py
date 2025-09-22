# ——————————————————————————————————————————————————————————————————————
# Activity 5: Create Modifiers
# ——————————————————————————————————————————————————————————————————————

# Modifiers are stored on objects and their appearances.

# In newer versions of Blender, it's common for a modifier to consist of
# nodes, i.e. Geometry Nodes.

# For this activity you will need to create a new Geometry Nodes group,
# and edit the variable below to match the name you gave the node group.

GEOMETRY_NODES_NAME = "Geometry Nodes"

# Now we will test adding modifiers to the active object.

# Add the following code to the code block below, then press Run Script (play button at the top ▲)

""" Ignore this line

import bpy


active_object = bpy.context.active_object

if active_object is None:
    raise Exception("No active object, cancelled")


active_object.modifiers.clear() # Removes all modifiers

# Adds a new Subdivision modifier
subsurf = active_object.modifiers.new(name="MySubdivision", type="SUBSURF")
subsurf.levels = 2
subsurf.render_levels = 3

# Adds a new Geometry Nodes modifier
nodes_modifier = active_object.modifiers.new(name="MyGeometryNodes", type="NODES")
nodes_modifier.node_group = bpy.data.node_groups[GEOMETRY_NODES_NAME]

Ignore this line """

# ——————————————————————————————————————————————————————————————————————

# ADD CODE BELOW
# vvvvvvvvvvvvvvvvvvvv



# ^^^^^^^^^^^^^^^^^^^^
# ADD CODE ABOVE

# ——————————————————————————————————————————————————————————————————————

# This code demonstrates basic handling of modifiers in Blender.
# We learn to clear existing modifiers, add new ones (Subdivision and
# Geometry Nodes), and configure their settings programmatically.

# Combining Python with Geometry Nodes is a powerful way to create
# tools.


# References
# https://docs.blender.org/api/current/bpy.types.Modifier.html
# https://docs.blender.org/api/current/bpy.types.NodesModifier.html