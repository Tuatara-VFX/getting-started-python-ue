import unreal

menu_owner = "TestPy-My Tools"
tool_menus = unreal.ToolMenus.get()

def create_main_menu_section():
    #G et a reference to the Main Menu (The top bar)
    main_menu = tool_menus.extend_menu("LevelEditor.MainMenu")

    # Add a new category to the top bar, called a subMenu
    main_menu.add_sub_menu(menu_owner, "", "MyTools", "My Tools", "Tooltip")

    # Register a new menu on the My Tools subMenu we just made
    custom_menu = tool_menus.register_menu("LevelEditor.MainMenu.MyTools", "", unreal.MultiBoxType.MENU, True)

    # Add a new vertical section.  Sections are the visual splitting of different parts of the menu with a label at the top
    custom_menu.add_section("Level", "Level")

    # return tool_menus.register_menu("LevelEditor.MainMenu.MyTools.Create", "", unreal.MultiBoxType.MENU, False)

    entry = unreal.ToolMenuEntryExtensions.init_menu_entry(
        menu_owner, #owner
        "statUnit", #name - used to reference this entry
        "Place cubes", #label - Display Name on the button
        "Runs the stat unit console command", #tooltip
        unreal.ToolMenuStringCommandType.COMMAND, #command type - COMMAND, PYTHON, CUSTOM - Determines what sort of command to run.  CUSTOM is for supporting future languages.
        "", #custom command type - Only used is commandType is CUSTOM
        "stat unit") #command string - Run this command
    custom_menu.add_menu_entry("Level", entry) #Add the new entry to our menu

    custom_menu.add_section("Assets", "Assets")

    entry = unreal.ToolMenuEntryExtensions.init_menu_entry(
        menu_owner, #owner
        "statUnit", #name - used to reference this entry
        "Batch Renaming", #label - Display Name on the button
        "Runs the stat unit console command", #tooltip
        unreal.ToolMenuStringCommandType.COMMAND, #command type - COMMAND, PYTHON, CUSTOM - Determines what sort of command to run.  CUSTOM is for supporting future languages.
        "", #custom command type - Only used is commandType is CUSTOM
        "stat unit") #command string - Run this command
    custom_menu.add_menu_entry("Assets", entry) #Add the new entry to our menu

    custom_menu.add_section("Materials", "Materials")

    entry = unreal.ToolMenuEntryExtensions.init_menu_entry(
        menu_owner, #owner
        "statUnit", #name - used to reference this entry
        "Instance materials", #label - Display Name on the button
        "Runs the stat unit console command", #tooltip
        unreal.ToolMenuStringCommandType.COMMAND, #command type - COMMAND, PYTHON, CUSTOM - Determines what sort of command to run.  CUSTOM is for supporting future languages.
        "", #custom command type - Only used is commandType is CUSTOM
        "stat unit") #command string - Run this command
    custom_menu.add_menu_entry("Materials", entry) #Add the new entry to our menu

    custom_menu.add_section("Other", "Other")
    sub_menu = custom_menu.add_sub_menu(menu_owner, "Other", "Sub-menu", "Sub-menu", "")

    entry = unreal.ToolMenuEntryExtensions.init_menu_entry(
        menu_owner, #owner
        "statUnit", #name - used to reference this entry
        "Example", #label - Display Name on the button
        "Runs the stat unit console command", #tooltip
        unreal.ToolMenuStringCommandType.COMMAND, #command type - COMMAND, PYTHON, CUSTOM - Determines what sort of command to run.  CUSTOM is for supporting future languages.
        "", #custom command type - Only used is commandType is CUSTOM
        "stat unit") #command string - Run this command
    sub_menu.add_menu_entry("commands", entry) #Add the new entry to our menu

def run():
    tool_menus.unregister_owner_by_name(menu_owner)

    my_tools_menu = create_main_menu_section()

    tool_menus.refresh_all_widgets()


run()