
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

# Eget-tempo-inlärningsmaterial för utveckling av Blender add-ons

# Materialet är skrivet för att fungera inuti Blenders egna text-editor.

# Nedan hittar du praktiska tips som kommer att underlätta i skriptandet.


# ——————————————————————————————————————————————————————————————————————
# Rekommenderade Preferenser
# ——————————————————————————————————————————————————————————————————————

# Interface ▶ Display ▶ Developer Extras (På)
# Interface ▶ Display ▶ Python Tooltips  (På)

# Window ▶ Toggle System Console

# Händig men ej nödvändig
# Keymap ▶ Preferences ▶ Spacebar Action (Search)
# (Sökfunktionen finns också på knappen 'F3')


# ——————————————————————————————————————————————————————————————————————
# Vart du hittar information
# ——————————————————————————————————————————————————————————————————————

# - Blenders användargränssnitt
# - Blenders API-dokumentation: https://docs.blender.org/api/current
# - Python Standard Library: https://docs.python.org/3/library


# ——————————————————————————————————————————————————————————————————————
# Stoppa exakvering av kod vid frys
# ——————————————————————————————————————————————————————————————————————

# Blender har en tendens att frysa när vi testar vår kod.
# Se därför till att ha konsollen öppen när du utvecklar ditt add-on.

# Vid en frys: gå in i konsollen och tryck Ctrl + C tills att Blender låser upp sig


# ——————————————————————————————————————————————————————————————————————
# Python-moduler
# ——————————————————————————————————————————————————————————————————————

# bpy        - Huvudmodul för Blender Python
# bpy_extras - Utility-moduler associerade med bpy-modulen

# bmesh - Blenders modul för att skapa och redigera meshar

# bl_math   - Matematiska funktioner (clamp, lerp, smoothstep)
# mathutils - Matematiska typer och operationer (Vector, Color, Euler, Quaternion...)

# gpu        - Python wrappers för Blenders GPU-implementering
# gpu_extras - Utility-moduler associerade med gpu-modulen

# aud - Ljud-modul


# ——————————————————————————————————————————————————————————————————————
# Blenders namngivningskonvention (för klasser)
# ——————————————————————————————————————————————————————————————————————

#                   {CATEGORY}_{TYPE}_{name}


# - Types: Operator(OT), Panel(PT), Menu(MT), Header(HT)

# - Menyer i vyporten beskrivs t.ex. med 'VIEW3D_MT_{something}'

# - 'CAMER_ADDON_OT_add_camera' är t.ex. ett lämpligt klassnamn
#   åt en ny operator


# ——————————————————————————————————————————————————————————————————————
# Minimalistisk setup för Blender Python i VSCode
# ——————————————————————————————————————————————————————————————————————

# De två nödvändiga justeringarna vi måste göra för att Blender Python 
# ska bete sig korrekt i VSCode är

# 1) Installera fake-bpy-module (för korrekt syntax highlighting)

pip install fake-bpy-module

# 2) Stänga av inställningen "reportInvalidTypeForm" i ens settings.json-fil
# (undviker en onödig varning runt property-definitioner)

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
