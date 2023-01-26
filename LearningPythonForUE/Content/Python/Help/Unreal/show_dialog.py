from datetime import date
import unreal
 
today = str(date.today())
unreal.EditorDialog.show_message("The title", today, unreal.AppMsgType.OK)