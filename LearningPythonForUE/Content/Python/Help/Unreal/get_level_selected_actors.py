import unreal

def get_selected_level_actors():
    editor_actor_subs = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    actors = editor_actor_subs.get_selected_level_actors()
    return actors

actors = get_selected_level_actors()
print(actors)