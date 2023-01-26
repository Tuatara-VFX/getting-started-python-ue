import unreal

def get_selected_level_actors():
    editor_actor_subs = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    actors = editor_actor_subs.get_selected_level_actors()
    return actors

def spread_actors(actors):
    for i in range(len(actors)):
        x = i * 200
        world_pos = unreal.Vector(x, 0.0, 0.0)

        actor = actors[i]
        actor.set_actor_location(world_pos, sweep=False, teleport=True)

actors = get_selected_level_actors()
spread_actors(actors)