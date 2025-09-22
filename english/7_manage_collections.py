# ——————————————————————————————————————————————————————————————————————
# Activity 7: Managing Collections
# ——————————————————————————————————————————————————————————————————————

# Blender's collections function as groups of objects.

# We can access collections through two different paths

# bpy.data.collections - Flat structure of all collections in the blend file

# bpy.context.scene.collection - Scene tree structure with parent/child relationships


# Here are some of the collection attributes and what they refer to

# objects     - the objects that the collection contains
# all_objects - the objects that the collection and its child collections contain

# children           - collections that are direct children of this collection
# children_recursive - all collections that are children of this collection

# objects.link()  - function to link an object to the collection
# children.link() - function to link another collection to this collection

# hide_viewport   - hides the collection in the viewport when set to True
# hide_render     - hides the collection during rendering
# hide_select     - hides the collection from selection


# A common use case for collections is organizing scene objects.
# There are several methods for this, one of which is to match the object's
# type (mesh, light, camera, etc.) with its corresponding collection.
# This is what we will do below.

# To ensure that a collection exists, we can use this
# helper function. The function returns a collection with the specified name.
# If it doesn't exist, it creates a new one.

import bpy

def get_or_create_collection(collection_name, link_to_scene=True):
    collections = bpy.data.collections
    
    col = collections.get(collection_name)
    
    if col is None:
        col = collections.new(collection_name)
        
    # Collections must become children of the scene's 'Scene Collection'
    # to become part of the scene hierarchy & appear in the outliner
    if link_to_scene == True:
        scene_collection = bpy.context.scene.collection
        if col.name not in scene_collection.children:
            scene_collection.children.link(col)
    
    return col

# Add the following code to the code block below, then press Run Script (play button at the top ▲)

""" Ignore this line

import bpy


type_to_collection_dict = {
    "MESH": get_or_create_collection("Mesh Objects"),
    "LIGHT": get_or_create_collection("Light Objects"),
    "CAMERA": get_or_create_collection("Camera Objects")
}

current_scene = bpy.context.scene

for obj in current_scene.objects:
    matching_collection = type_to_collection_dict.get(obj.type)
    
    if matching_collection is None:
        continue

    if obj.name not in matching_collection.objects:
        matching_collection.objects.link(obj)

Ignore this line """

# ——————————————————————————————————————————————————————————————————————

# ADD CODE BELOW
# vvvvvvvvvvvvvvvvvvvv



# ^^^^^^^^^^^^^^^^^^^^
# ADD CODE ABOVE

# ——————————————————————————————————————————————————————————————————————

# We decide ourselves how Blender should handle cases where objects already exist in a collection.
# If we don't address this issue, an error message will otherwise occur.

# According to Blender's design, an object can belong to multiple collections simultaneously.
# This can be utilized in certain workflows, but in others it may be desirable
# to remove the object from its previous collection before making a new link.


# References
# https://docs.blender.org/api/current/bpy.types.Collection.html