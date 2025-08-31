# ——————————————————————————————————————————————————————————————————————
# Rekommenderade Preferenser
# ——————————————————————————————————————————————————————————————————————

# Interface ▶ Display ▶ Developer Extras (På)
# Interface ▶ Display ▶ Python Tooltips  (På)

# Händig men ej nödvändig
# Keymap ▶ Preferences ▶ Spacebar Action (Search)
# (Annars finns sökfunktionen också på knappen 'F3')


# ——————————————————————————————————————————————————————————————————————
# Stoppa exakvering av kod vid frys
# ——————————————————————————————————————————————————————————————————————

# Blender har en tendens att frysa när vi testar vår kod.
# Se därför till att ha konsollen öppen när du utvecklar ditt add-on.
# Vid en frys: gå in i konsollen och tryck Ctrl + C tills att Blender låser upp sig.

# Window ▶ Toggle System Console


# ——————————————————————————————————————————————————————————————————————
# Python-moduler
# ——————————————————————————————————————————————————————————————————————

# bpy - Huvudmodul för Blender Python
# bpy_extras - Utility-moduler associerade med bpy-modulen

# bmesh - Blenders modul för att skapa och redigera meshar

# bl_math - Matematiska funktioner (clamp, lerp, smoothstep)
# mathutils - Matematiska typer och operationer (Vector, Color, Euler, Quaternion...)

# gpu - Python wrappers för Blenders GPU-implementering
# gpy_extras - Utility-moduler associerade med gpu-modulen

# aud - Ljud-modul


# ——————————————————————————————————————————————————————————————————————
# Blender Python i VSCode
# ——————————————————————————————————————————————————————————————————————

# De två nödvändiga justeringarna vi måste göra för att Blender Python ska bete sig
# i VSCode är

# 1) Installera fake-bpy-module (för korrekt syntax highlighting)

pip install fake-bpy-module

# 2) Stänga av inställningen "reportInvalidTypeForm" 
# (för att undvika en onödig varning runt property-definitioner)

"python.analysis.diagnosticSeverityOverrides": {
        "reportInvalidTypeForm" : "none"
    }


# Extensions i VSCode
# För att underlätta utvecklingen kan du även installera extensions.
# Ett populärt exempel är: Blender Development av Jacques Lucke
# https://marketplace.visualstudio.com/items?itemName=JacquesLucke.blender-development
