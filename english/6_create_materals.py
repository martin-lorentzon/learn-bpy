# ——————————————————————————————————————————————————————————————————————
# Activity 6: Create materials
# ——————————————————————————————————————————————————————————————————————

# Materials in Blender are defined using node trees.
# A material can contain different types of nodes. Each node has its own
# inputs and outputs. Nodes are connected by creating a link
# from one node's output to another node's input.

# In this example we will:

# - Create a new material
# - Find a specific node (Principled BSDF)
# - Add a new Image Texture node
# - Connect the new Image Texture node with the material's BSDF node


# Add the following code to the code block below, then press Run Script (play button at the top ▲)

""" Ignore this line

import bpy


materials = bpy.data.materials
my_material = materials.get("Test Material")

# Removes the material if it exists from before
if my_material is not None:
    materials.remove(my_material)

# Creates a new material
my_material = materials.new("Test Material")

# The different parts of the node tree
my_material.use_nodes = True
node_tree = my_material.node_tree
nodes = node_tree.nodes
links = node_tree.links

# Example of finding a node of a specific type
bsdf_node = None
for node in nodes:
    if node.bl_idname == "ShaderNodeBsdfPrincipled":
        bsdf_node = node
        break

# Creates a new Image Texture node
image_node = nodes.new("ShaderNodeTexImage")
image_node.location = (-500, 100)

# Creates a link between the Image Texture node and the BSDF node
from_socket = image_node.outputs[0]
to_socket = bsdf_node.inputs[0]
links.new(from_socket, to_socket)

Ignore this line """

# ——————————————————————————————————————————————————————————————————————

# ADD THE CODE BELOW
# vvvvvvvvvvvvvvvvvvvv



# ^^^^^^^^^^^^^^^^^^^^
# ADD THE CODE ABOVE

# ——————————————————————————————————————————————————————————————————————

# To see the result, navigate to the shader editor
# and select the material 'Test Material'.

# This code creates a new material, finds the Principled BSDF node
# and links it with a new Image Texture node.

# If the material already exists, the code removes the material before
# creating a new one, this can be desirable if we for example
# are updating a material from a material library.

# To find a node of a specific type (e.g. 'Mix Color')
# we strictly use its bl_idname, the class's unique identifier.

# If you want, you can experiment with adding - as well as linking -
# more types of nodes.

# To find out what possible node types exist, we can use
# this helper function

import bpy

def print_all_node_names():
    for name in dir(bpy.types):
        cls = getattr(bpy.types, name)
        if isinstance(cls, type) and issubclass(cls, bpy.types.Node):
            print(cls.__name__)

print_all_node_names()


# References
# https://docs.blender.org/api/current/bpy.types.Material.html
# https://docs.blender.org/api/current/bpy.types.Node.html