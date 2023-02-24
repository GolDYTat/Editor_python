import ctypes
import view
 
ctypes.windll.shcore.SetProcessDpiAwareness(True)

view.window