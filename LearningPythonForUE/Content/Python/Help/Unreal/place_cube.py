import unreal

def spawn_cube():
    
    # Get the system to control the actors
    editor_actor_subs = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)

    # Generate a world space position (0, 0, 0)
    location = unreal.Vector()

    # We want to create a StaticMeshActor
    actor_class = unreal.StaticMeshActor

    # Place it in the level
    static_mesh_actor = editor_actor_subs.spawn_actor_from_class(actor_class, location)

    # Load and add the cube to it
    static_mesh = unreal.EditorAssetLibrary.load_asset("/Engine/BasicShapes/Cube.Cube")
    static_mesh_actor.static_mesh_component.set_static_mesh(static_mesh)


spawn_cube()
