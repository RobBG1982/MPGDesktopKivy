'''
 Project: MPG Desktop Application
 Module:  calculateValues.py
 
 Description: 
 This module will calculate and return values related to gas mileage:
  - miles per gallon
  - cost per gallon
  - cost per mile
  - total mileage
 
 Name          Date     Issue   
 R. Gaisey   11/12/23

 '''


from database import EntryTags as tags
from database import DataBase


class displayValues():

  def __init__(self):

    self.db = DataBase("utilities/gas_raw.xml")
    self.db.print_entries()

    self.stale = True

    self.overall_mileage = 0
    self.overall_cost    = 0
    self.overall_gallons = 0

    self.recent_mileage = 0
    self.recent_cost    = 0
    self.recent_gallons = 0


  def set_to_stale(self):
    self.stale = True
    return
  
  def set_all_values(self):
    self.set_overall_values()
    self.set_recent_values()
    self.stale = False

    return 


  def set_overall_values(self):
    sum_price   = 0 
    sum_gallons = 0
    max_index = self.db.get_size() -1

    self.overall_mileage = float(self.db.Entries[max_index][tags.MILEAGE]) - float(self.db.Entries[0][tags.MILEAGE])
    for entry in self.db.Entries:
      sum_price   += float(entry[tags.PRICE])    
      sum_gallons += float(entry[tags.GALLONS])
    
    self.overall_cost = sum_price
    self.overall_gallons = sum_gallons
    return 


  def set_recent_values(self):
    sum_price   = 0 
    sum_gallons = 0
    max_index = self.db.get_size() -1

    self.recent_mileage = float(self.db.Entries[max_index][tags.MILEAGE]) - float(self.db.Entries[max_index-10][tags.MILEAGE])
    for x in range(max_index-10, max_index):
      sum_price   += float(self.db.Entries[x][tags.PRICE])    
      sum_gallons += float(self.db.Entries[x][tags.GALLONS])

    self.recent_cost = sum_price
    self.recent_gallons = sum_gallons
    return 


  def get_overall_mileage(self):
    if self.stale == True:
      self.set_all_values()

    return self.overall_mileage  

  
  def get_overall_mpg(self):  
    if self.stale == True:
      self.set_all_values()
    
    try:
      return self.overall_mileage/self.overall_gallons 
    except ZeroDivisionError:
      return -1


  def get_overall_cpm(self):
    if self.stale == True:
      self.set_all_values()

    try:
      return self.overall_cost/self.overall_mileage 
    except ZeroDivisionError:
      return -1


  def get_overall_cpg(self):
    if self.stale == True:
      self.set_all_values()

    try:
      return self.overall_cost/self.overall_gallons 
    except ZeroDivisionError:
      return -1
    


  def get_recent_mileage(self):
    if self.stale == True:
      self.set_all_values()    
     
    return self.recent_mileage


  def get_recent_mpg(self):
    if self.stale == True:
      self.set_all_values()
  
    try:
      return self.recent_mileage/self.recent_gallons 
    except ZeroDivisionError:
      return -1


  def get_recent_cpm(self):
    if self.stale == True:
      self.set_all_values()

    try:
      return self.recent_cost/self.recent_mileage 
    except ZeroDivisionError:
      return -1


  def get_recent_cpg(self):
    if self.stale == True:
      self.set_all_values()

    try:
      return self.recent_cost/self.recent_gallons 
    except ZeroDivisionError:
      return -1
