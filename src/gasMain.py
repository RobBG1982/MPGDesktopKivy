'''
 Project: MPG Desktop Application
 Module:  gasMain.py
 
 Description: 
 This is the entry point for the Gas Desktop Aplication  


 Name          Date     Issue   
 R. Gaisey   11/1/23

 '''




from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from database import EntryTags as tags
from kivy.properties import ObjectProperty
from database import DataBase




class CustomWindow(Screen):
    pass


class SummaryWindow(Screen):
    overall_mileage = ObjectProperty(None)
    overall_mpg     = ObjectProperty(None)
    overall_cpm     = ObjectProperty(None)
    overall_cpg     = ObjectProperty(None)

    recent_mileage = ObjectProperty(None)
    recent_mpg     = ObjectProperty(None)
    recent_cpm     = ObjectProperty(None)
    recent_cpg     = ObjectProperty(None)

    def on_enter(self, *args):
        self.overall_mileage.text = db.Entries[4][tags.MILEAGE]
        self.overall_mpg.text = str(float(db.Entries[4][tags.MILEAGE])/float(db.Entries[4][tags.GALLONS]))
        self.overall_cpm.text = str(float(db.Entries[4][tags.PRICE])/float(db.Entries[4][tags.MILEAGE]))
        self.overall_cpg.text = str(float(db.Entries[4][tags.PRICE])/float(db.Entries[4][tags.GALLONS]))
        return super().on_enter(*args)
    




class WindowManager(ScreenManager):
    pass


class TopLayout(RelativeLayout):
	pass
    
class BasicApp(App):
    def build(self):
        return sm

# Designate Our .kv design file 
kv = Builder.load_file('topLayout.kv')

sm = WindowManager()
db = DataBase("utilities/gas_raw.xml")
db.print_entries()

screens = [CustomWindow(name="custom"), SummaryWindow(name="summary")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "summary"

if __name__=="__main__":
    BasicApp().run()
