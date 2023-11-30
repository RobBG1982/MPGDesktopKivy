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
from displayValues import displayValues 
import utilities.cmn_functions as util
import logging
import logging.config
from datetime import datetime

logging.config.fileConfig("logging.conf")
logger = logging.getLogger()


class CustomWindow(Screen):
    pass


class SummaryWindow(Screen):
         
    dv = displayValues()

    
    def on_enter(self, *args):
        self.update_display()
        
        return super().on_enter(*args)
   

    def update_display(self):
        logger.info("Updating Display values")

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

        try:
            price = float(self.new_cost.text)
            mileage = float(self.new_mileage.text)
            gallons = float(self.new_gallons.text)
            station = self.new_station.text
            notes   = self.new_notes.text
            
            date = datetime.strptime(self.new_date.text, '%m/%d/%Y')

            self.dv.db.add_entry(date, gallons, mileage, \
                             price, station, notes)
            self.updatevalues()
        except TypeError as te:
           #Create popup window here detailing correct format
           logger.exception(f"{te}")
           return -1
        except ValueError as ve:
           #Create popup window here detailing correct format
           logger.exception(f"{ve}")
           return -1


    def updatevalues(self):
        logger.info("Forced update")
        self.dv.set_to_stale()
        self.update_display()

    
    def on_stop(self, *args):
        self.dv.db.save_tree_to_file(True)
        
        return super().on_enter(*args)


class WindowManager(ScreenManager):
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