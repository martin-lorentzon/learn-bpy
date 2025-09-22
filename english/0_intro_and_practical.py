
                 ####               
                 ######             
                    ######          
       #####################        
     ##########################     
             #######      #######   
           ######    :::::   #####  
        ########   :::::::::  ##### 
      ##########   :::::::::   #####
   ####### #####   :::::::::   #####
 #######   ######    :::::    ##### 
#####       #######        #######  
             ####################   
                ###############     
                   ########         


# █░░ █▀▀ ▄▀█ █▀█ █▄░█ ▄▄ █▄▄ █▀█ █▄█
# █▄▄ ██▄ █▀█ █▀▄ █░▀█ ░░ █▄█ █▀▀ ░█░

# https://github.com/martin-lorentzon/learn-bpy

# Self-paced learning material for developing Blender add-ons

# The material is written to work inside Blender's own text editor.

# Below you'll find practical tips that will make scripting easier.


# ——————————————————————————————————————————————————————————————————————
# Recommended Preferences
# ——————————————————————————————————————————————————————————————————————

# Interface ▶ Display ▶ Developer Extras (On)
# Interface ▶ Display ▶ Python Tooltips  (On)

# Window ▶ Toggle System Console

# Handy but not necessary
# Keymap ▶ Preferences ▶ Spacebar Action (Search)
# (The search function is also available on the 'F3' key)


# ——————————————————————————————————————————————————————————————————————
# Where you find information
# ——————————————————————————————————————————————————————————————————————

# - Blender's user interface
# - Blender's API documentation: https://docs.blender.org/api/current
# - Python Standard Library: https://docs.python.org/3/library


# ——————————————————————————————————————————————————————————————————————
# How to stop code execution if Blender freezes
# ——————————————————————————————————————————————————————————————————————

# Blender has a tendency to freeze when we test our code.
# Therefore, make sure to have the console open when developing your add-on.

# In case of a freeze: go into the console and press Ctrl + C until Blender unlocks itself


# ——————————————————————————————————————————————————————————————————————
# Python modules
# ——————————————————————————————————————————————————————————————————————

# bpy        - Main module for Blender Python
# bpy_extras - Utility modules associated with the bpy module

# bmesh - Blender's module for creating and editing meshes

# bl_math   - Mathematical functions (clamp, lerp, smoothstep)
# mathutils - Mathematical types and operations (Vector, Color, Euler, Quaternion...)

# gpu        - Python wrappers for Blender's GPU implementation
# gpu_extras - Utility modules associated with the gpu module

# aud - Audio module


# ——————————————————————————————————————————————————————————————————————
# Blender's naming convention (for classes)
# ——————————————————————————————————————————————————————————————————————

#                   {CATEGORY}_{TYPE}_{name}


# - Types: Operator(OT), Panel(PT), Menu(MT), Header(HT)

# - Viewport menus are described with e.g. 'VIEW3D_MT_{something}'

# - 'CAMERA_ADDON_OT_add_camera' would be a suitable class name
#   for a new operator


# ——————————————————————————————————————————————————————————————————————
# Minimalist setup for Blender Python in VSCode
# ——————————————————————————————————————————————————————————————————————

# The two necessary adjustments we need to make for Blender Python 
# to behave correctly in VSCode are

# 1) Install fake-bpy-module (for correct syntax highlighting)

pip install fake-bpy-module

# 2) Turn off the "reportInvalidTypeForm" setting in your settings.json file
# (avoids an unnecessary warning around property definitions)

"python.analysis.diagnosticSeverityOverrides": {
        "reportInvalidTypeForm" : "none"
    }


# ——————————————————————————————————————————————————————————————————————
# Blender Conference 2025: Modern add-on development
# ——————————————————————————————————————————————————————————————————————

# https://www.youtube.com/watch?v=GP53gDHGiIQ

# "The basics of building an add-on, from copy-pasting code from Blender's UI
# to connecting a debugger and stepping through your Python code."

# "import bpy: modern add-on development" by dr. Sybren A. Stüvel at Blender Conference 2025