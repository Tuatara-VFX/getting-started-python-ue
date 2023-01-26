import unreal
import time

# https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/ScopedSlowTask.html?highlight=scopedslowtask#unreal.ScopedSlowTask
def show_example_progress_bar():

    step_count = 200

    with unreal.ScopedSlowTask(step_count) as progress_bar:
        progress_bar.make_dialog(True)

        for i in range(step_count):
            if progress_bar.should_cancel():
                break

            # Tell the progress bar what will happen for the next second
            progress_bar.enter_progress_frame(1, "Something is happening...")

            # Fake slow process, remove this when using the progress bar in a real example
            time.sleep(.1)

show_example_progress_bar()
