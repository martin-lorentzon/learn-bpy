# ——————————————————————————————————————————————————————————————————————
# Aktivitet 5: Hantera kollektioner
# ——————————————————————————————————————————————————————————————————————

# Blenders kollektioner fungerar som grupper av objekt.

# Vi kan komma åt kollektioner med två olika vägar

# bpy.data.collections - Platt struktur av alla kollektioner i blend-filen

# bpy.context.scene.collection - Scenträdets struktur med parent/child-relationer


# Här är några av kollektioners attribut och vad de refererar till

# objects     - de objekt kollektionen innehåller
# all_objects - de objekt kollektionen samt dess child-kollektioner innehåller

# children           - kollektioner som är direkt child av denna kollektion
# children_recursive - alla kollektioner som är child av denna kollektion

# objects.link()  - funktion för att länka ett objekt till kollektionen
# children.link() - funktion för att länka en annan kollektion till denna kollektion

# hide_viewport   - gömmer kollektionen i vyporten om satt till True
# hide_render     - gömmer kollektionen under rendering
# hide_select     - gömmer kollektionen för markering


# Ett vanligt use case för kollektioner är sortering av scenobjekt.
# Det finns flera metoder för detta, varav en är att matcha objektets
# typ (mesh, ljus, kamera osv.) med dess korresponderande kollektion.
# Detta är vad vi kommer att göra nedan.

# För att försäkra oss om att en kollektion existerar kan vi använda denna
# hjälpfunktion. Funktionen returnerar en kollektion med det angivna namnet.
# Finns den inte, skapas den på nytt.

import bpy

def get_or_create_collection(collection_name, link_to_scene=True):
    collections = bpy.data.collections
    
    col = collections.get(collection_name)
    
    if col is None:
        col = collections.new(collection_name)
        
    # Kollektioner måste bli child till scenens 'Scene Collection'
    # för att bli en del av scenens hierarki & synas i scenträdet
    if link_to_scene == True:
        scene_collection = bpy.context.scene.collection
        if col.name not in scene_collection.children:
            scene_collection.children.link(col)
    
    return col

# Lägg till följande kod i kodblocket nedan, tryck sedan Run Script (play-knappen högst upp ▲)

""" Ignorera denna rad

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

Ignorera denna rad """

# ——————————————————————————————————————————————————————————————————————

# LÄGG TILL KODEN NEDANFÖR
# vvvvvvvvvvvvvvvvvvv



# ^^^^^^^^^^^^^^^^^^^^
# LÄGG TILL KODEN OVANFÖR

# ——————————————————————————————————————————————————————————————————————

# Vi väljer själva hur Blender ska hantera fall där objekt redan finns in kollektion.
# Om vi inte gör något åt saken uppstår annars ett felmeddelande.

# Ett objekt kan enligt Blenders design ingå i flera kollektioner samtidigt.
# Detta kan utnyttjas i vissa arbetsflöden, men i andra kan det vara önskvärt 
# att ta bort objektet från dess tidigare kollektion innan en ny länkning görs.


# Referenser
# https://docs.blender.org/api/current/bpy.types.Collection.html