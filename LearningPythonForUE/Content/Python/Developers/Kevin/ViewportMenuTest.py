import unreal

menu_owner = "questToolViewerOwner"
tool_menus = unreal.ToolMenus.get()


@unreal.uclass()
class createEntry_QuestToolViewer(unreal.ToolMenuEntryScript):

    @unreal.ufunction(override=True)
    def execute(self, context):
        pass
        registry = unreal.AssetRegistryHelpers.get_asset_registry()
        asset = unreal.EditorAssetLibrary.load_asset(
            "/Game/Blueprints/Blutilities/ForDesign/QuestUtilities/QuestEditorsMenu")
        bp = unreal.EditorUtilitySubsystem().find_utility_widget_from_blueprint(asset)
        if bp == None:
            bp = unreal.EditorUtilitySubsystem().spawn_and_register_tab(asset)

    def init_as_toolbar_button(self):
        self.data.menu = "LevelEditor.LevelEditorToolBar"
        self.data.advanced.entry_type = unreal.MultiBlockType.TOOL_BAR_BUTTON
        self.data.icon = unreal.ScriptSlateIcon(
            "EditorStyle", "LevelEditor.Tabs.EditorModes")
        self.data.advanced.style_name_override = "CalloutToolbar"


def AddToolbarStringCommands(menu):

    menu.add_section("StringCommands", "String Commands")

    # Button
    entry = unreal.ToolMenuEntryExtensions.init_menu_entry(
        menu_owner,
        "TestStringPy",
        "TestStringPy",
        "Test Python toolbar button",
        unreal.ToolMenuStringCommandType.PYTHON,
        "",
        "print(\"test python toolbar button pressed\")")
    entry.type = unreal.MultiBlockType.TOOL_BAR_BUTTON

    menu.add_menu_entry("StringCommands", entry)

    # Combo button
    entry = unreal.ToolMenuEntryExtensions.init_menu_entry(
        menu_owner,
        "TestComboPy",
        "Custom Menu",
        "Tooltip",
        unreal.ToolMenuStringCommandType.CUSTOM,
        "",
        "")
    unreal.ToolMenuEntryExtensions.set_label(entry, "Custom menu")
    entry.type = unreal.MultiBlockType.TOOL_BAR_COMBO_BUTTON
    entry.set_label("Custom menu")
    entry.set_icon("EditorStyle", "LevelEditor.Tabs.EditorModes")
    menu.add_menu_entry("StringCommands", entry)

    # main_menu = tool_menus.extend_menu("LevelEditor.LevelEditorToolBar.PlayToolBar")
    # main_menu.add_sub_menu(menu_owner, "", "MyTools", "My Tools", "Tooltip")

    # Create menu that goes with the combo button above
    sub_menu = tool_menus.register_menu(
        "LevelEditor.LevelEditorToolBar.PlayToolBar.TestComboPy", "Custom menu", unreal.MultiBoxType.MENU, False)
    entry = unreal.ToolMenuEntryExtensions.init_menu_entry(
        menu_owner,
        "TestComboItem",
        "Test Item",
        "Tooltip",
        unreal.ToolMenuStringCommandType.COMMAND,
        "",
        "ke * doMyTest")
    sub_menu.add_menu_entry("Section01", entry)


def Run():
    if True:  # Testing stuff for iteration, set to True to reload when this script runs
        # For Testing: Allow iterating on this menu python file without restarting editor
        tool_menus.unregister_owner_by_name(menu_owner)

    entry = createEntry_QuestToolViewer()
    entry.init_as_toolbar_button()
    entry.init_entry(menu_owner, "questeditorBrowserEntry", "",
                     "", "Custom Action", "Open Custom Menu")
    toolbar = tool_menus.extend_menu(
        "LevelEditor.LevelEditorToolBar.PlayToolBar")
    toolbar.add_menu_entry_object(entry)

    AddToolbarStringCommands(toolbar)

    tool_menus.refresh_all_widgets()


Run()
