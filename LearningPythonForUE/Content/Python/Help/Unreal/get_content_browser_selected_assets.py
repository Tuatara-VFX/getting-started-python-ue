import unreal

def get_selected_assets():
    return unreal.EditorUtilityLibrary.get_selected_assets()

assets = get_selected_assets()
print(assets)