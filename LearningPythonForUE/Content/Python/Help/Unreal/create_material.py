import unreal

# https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/AssetTools.html?highlight=create_asset#unreal.AssetTools.create_asset

def create_material(asset_path, new_asset_name):
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    material_factory = unreal.MaterialFactoryNew()
    new_asset = asset_tools.create_asset(new_asset_name, asset_path, None, material_factory)

create_material("/Game/Python/Help/Unreal", "MaterialTest")