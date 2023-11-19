'''
 Project: MPG Desktop Application
 Module:  gasMain.py
 
 Description: 
 This is the entry point for the Gas Desktop Application  


 Name          Date         Issue   
 R. Gaisey   11/12/23    initial commits 
 R. Gaisey   11/18/23    added logging
 R. Gaisey   11/19/23    add entry MVP

 '''
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.relativelayout import RelativeLayout
from displayValues import displayValues 
import utilities.displayMath as util
import logging
import logging.config


logging.config.fileConfig("logging.conf")
logger = logging.getLogger()

rawValues_filename = "utilities/gas_raw.xml"

class CustomWindow(Screen):
    pass


class SummaryWindow(Screen):
         
    dv = displayValues()

    
    def on_enter(self, *args):
        self.update_display()
        
        return super().on_enter(*args)
    

    def update_display(self):
        logger.info("Updating Display values")
        logger.debug(self)

        self.overall_mileage.text = util.format_float(self.dv.get_overall_mileage(), 2)
        self.overall_mpg.text     = util.format_float(self.dv.get_overall_mpg(), 2)
        self.overall_cpm.text     = f'${util.format_float(self.dv.get_overall_cpm(), 2)}'
        self.overall_cpg.text     = f'${util.format_float(self.dv.get_overall_cpg(), 2)}'

        self.recent_mileage.text = util.format_float(self.dv.get_recent_mileage(), 2)
        self.recent_mpg.text     = util.format_float(self.dv.get_recent_mpg(), 2)
        self.recent_cpm.text     = f'${util.format_float(self.dv.get_recent_cpm(), 2)}'
        self.recent_cpg.text     = f'${util.format_float(self.dv.get_recent_cpg(), 2)}'

        return
   
    def addnewentry(self):
        logger.info("Adding new entry")
        logger.debug(self)

        self.dv.db.add_entry(self.new_date.text, self.new_gallons.text, self.new_mileage.text, \
                             self.new_cost.text, self.new_station.text, self.new_notes.text )
        self.updatevalues()

        logger.debug("End of newEntry")


    def updatevalues(self):
        logger.info("Forced update")
        logger.debug(self)
        self.dv.set_to_stale()
        self.update_display()




class WindowManager(ScreenManager):
    pass


class TopLayout(RelativeLayout):
	pass
    
class BasicApp(App):
    logger.info("Starting MPG Desktop Aplication")

    def build(self):
        return sm

# Designate Our .kv design file 
kv = Builder.load_file('topLayout.kv')

sm = WindowManager()


screens = [CustomWindow(name="custom"), SummaryWindow(name="summary")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "summary"

if __name__=="__main__":
    BasicApp().run()