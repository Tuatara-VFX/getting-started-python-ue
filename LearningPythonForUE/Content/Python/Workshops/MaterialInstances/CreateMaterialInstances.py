import unreal

def get_selected_content_browser_assets():
    # https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/EditorUtilityLibrary.html?highlight=editorutilitylibrary#unreal.EditorUtilityLibrary
    editor_utility = unreal.EditorUtilityLibrary()
    selected_assets = editor_utility.get_selected_assets()

    return selected_assets

def log_asset_types(assets):
    for asset in assets:
        unreal.log(f"Asset {asset.get_name()} is a {type(asset)}")

def find_material_in_assets(assets):
    for asset in assets:
        if type(asset) is unreal.Material:
            return asset
    return None

def find_textures2D_in_assets(assets):
    textures = []
    for asset in assets:
        if type(asset) is unreal.Texture2D:
            textures.append(asset)
    return textures

# https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/AssetTools.html?highlight=create_asset#unreal.AssetTools.create_asset
def create_material_instance(parent_material, asset_path, new_asset_name):

    # Create the child material
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    material_factory = unreal.MaterialInstanceConstantFactoryNew()
    new_asset = asset_tools.create_asset(new_asset_name, asset_path, None, material_factory)

    # Assign its parent
    unreal.MaterialEditingLibrary.set_material_instance_parent(new_asset, parent_material)

    return new_asset

def get_random_color():
    return unreal.LinearColor(unreal.MathLibrary.rand_range(0, 1), unreal.MathLibrary.rand_range(0, 1), unreal.MathLibrary.rand_range(0, 1))

def get_random_bright_color():
    return unreal.LinearColor(unreal.MathLibrary.rand_range(0.5, 1), unreal.MathLibrary.rand_range(0.5, 1), unreal.MathLibrary.rand_range(0.5, 1))

def create_material_instance_for_texture(parent_material, instance_name, texture, color):
    
        unreal.log(f"Creating material instance {instance_name} for texture {texture.get_name()}")
    
        material_asset_path = unreal.Paths.get_path(texture.get_path_name())
    
        material_instance = create_material_instance(parent_material, material_asset_path, instance_name)
    
        # Assign the texture
        unreal.MaterialEditingLibrary.set_material_instance_texture_parameter_value(material_instance, "MainTex", texture)
    
        # Assign a random color
        unreal.MaterialEditingLibrary.set_material_instance_vector_parameter_value(material_instance, "Color", color)
    
        # Save the asset
        unreal.EditorAssetLibrary.save_asset(material_instance.get_path_name(), only_if_is_dirty = True)
    
        return material_instance

def create_material_instances_for_each_texture(material, textures):

    material_instances = []

    for texture in textures:

        material_name = f"{material.get_name()}_{texture.get_name()}"
        material_instance = create_material_instance_for_texture(material, material_name, texture, get_random_bright_color())

        material_instances.append(material_instance)

    return material_instances    

def create_material_instances_variations(parent_material, textures):
    
    material_instances = []

    for texture in textures:
        variation_count = 2
        for i in range(variation_count):

            material_name = f"{parent_material.get_name()}_{texture.get_name()}_{i}"
            material_instance = create_material_instance_for_texture(parent_material, material_name, texture, get_random_bright_color())
        
            material_instances.append(material_instance)
    
    return material_instances


def run():
    unreal.log("Running create material instances script")

    selected_assets = get_selected_content_browser_assets()
    log_asset_types(selected_assets)

    material = find_material_in_assets(selected_assets)
    textures = find_textures2D_in_assets(selected_assets)
    selected_assets = []

    if not material:
        unreal.log_error("No material selected")
        return

    if not textures:
        unreal.log_error("No textures selected")
        return

    unreal.log(f"Selected material: {material.get_name()}")
    unreal.log(f"{len(textures)} textures selected")

    material_instances = create_material_instances_variations(material, textures)

    # Open the editor for these new material instance
    # asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    # asset_tools.open_editor_for_assets(material_instances)



run()
