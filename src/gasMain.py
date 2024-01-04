'''
 Project: MPG Desktop Application
 Module:  gasMain.py
 
 Description: 
 This is the entry point for the Gas Desktop Application  


 Name          Date         Issue   
 R. Gaisey   11/12/23    initial commits 
 R. Gaisey   11/18/23    added logging
 R. Gaisey   11/19/23    add entry MVP
 R. Gaisey   12/04/23    simplified date input
 R. Gaisey   12/29/23    updated to include range and estimated mileage display

 '''

import logging
import logging.config

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from utilities.displayValues import displayValues
import utilities.cmn_functions as util


logging.config.fileConfig("logging.conf")
logger = logging.getLogger()


class CustomWindow(Screen):
    """
    CustomwWindow class is not implemented yet.

    Attributes
    ----------
    name : obj_type


    Methods
    -------
    N/A
    """
    pass


class SummaryWindow(Screen):
    '''
    SummaryWindow class represents the main grapical screen of the application.

    Attributes
    ----------
    overall_mileage: float
      number of miles travelled
    overall_mpg: float
      miles per gallon
    overall_cpm: float
       cost per mile
    overall_cpg: float
       cost per gallon

    recent_mileage: float
      number of miles travelled
    recent_mpg: float
      miles per gallon
    recent_cpm: float
       cost per mile
    recent_cpg: float
       cost per gallon

    Methods
    -------
    on_enter()
    update_display
    addnewEntry
    updateValues
    on_stop()
    
    '''

    dv = displayValues()

    def on_enter(self, *args):
        self.update_display()

        return super().on_enter(*args)


    def update_display(self):
        logger.info("Updating Display values")

        self.est_range.text       = util.format_float(self.dv.get_est_range(), 2)
        self.est_mileage.text     = util.format_float(self.dv.get_est_mileage(), 2)

        self.overall_mileage.text = util.format_float(self.dv.get_overall_mileage(), 2)
        self.overall_mpg.text     = util.format_float(self.dv.get_overall_mpg(), 2)
        self.overall_cpm.text     = f'${util.format_float(self.dv.get_overall_cpm(), 2)}'
        self.overall_cpg.text     = f'${util.format_float(self.dv.get_overall_cpg(), 2)}'

        self.recent_mileage.text = util.format_float(self.dv.get_recent_mileage(), 2)
        self.recent_mpg.text     = util.format_float(self.dv.get_recent_mpg(), 2)
        self.recent_cpm.text     = f'${util.format_float(self.dv.get_recent_cpm(), 2)}'
        self.recent_cpg.text     = f'${util.format_float(self.dv.get_recent_cpg(), 2)}'


    def add_new_entry(self):
        logger.info("Adding new entry")

        try:
            price = float(self.new_cost.text)
            mileage = float(self.new_mileage.text)
            gallons = float(self.new_gallons.text)
            station = self.new_station.text
            notes   = self.new_notes.text

            #Replace with Date validity checking
            day = self.new_date.text

            self.dv.db.add_entry(day, gallons, mileage, \
                             price, station, notes)
            self.update_values()
        except TypeError as te:
            # Create popup window here detailing correct format
            logger.exception("Received badly formatted input: %s", te)
            return -1
        except ValueError as ve:
            #Create popup window here detailing correct format
            logger.exception("Received badly formatted input: %s", ve)
            return -1
        return 1


    def update_values(self):
        logger.info("Forced update of display values")
        self.dv.set_to_stale()
        self.update_display()


    def on_stop(self):
        logger.info("Closing GasApp")
        self.dv.db.save_tree_to_file(True)

        return


class WindowManager(ScreenManager):
    pass


class BasicApp(App):
    logger.info("Starting MPG Desktop Application")

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
