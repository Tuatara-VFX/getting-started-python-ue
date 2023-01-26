import unreal
import sys

# https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/AssetTools.html?highlight=create_asset#unreal.AssetTools.create_asset

def create_material_instance(parent_material, asset_path, new_asset_name):

    # Create the child material
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    material_factory = unreal.MaterialInstanceConstantFactoryNew()
    new_asset = asset_tools.create_asset(new_asset_name, asset_path, None, material_factory)

    # Assign its parent
    unreal.MaterialEditingLibrary.set_material_instance_parent(new_asset, parent_material)

    return new_asset


selected_materials = unreal.EditorUtilityLibrary.get_selected_assets()

if not selected_materials or len(selected_materials) != 1:
    unreal.EditorDialog.show_message("Error", "Select one material in the Content Browser and run the script", unreal.AppMsgType.OK)
    sys.exit()

create_material_instance(selected_materials[0], "/Game/Python/Help/Unreal", "MaterialInstanceTest")