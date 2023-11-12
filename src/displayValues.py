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
 R. Gaisey   11/7/23

 '''


from database import EntryTags as tags
from database import DataBase


class displayValues():

  def __init__(self):

    self.db = DataBase("utilities/gas_raw.xml")
    self.db.print_entries()

    self.stale = True

    self.overall_mileage = 0
    self.overall_mpg     = 0
    self.overall_cpm     = 0
    self.overall_cpg     = 0


    self.recent_mileage = 0
    self.recent_mpg     = 0
    self.recent_cpm     = 0
    self.recent_cpg     = 0


    self.custom_mileage = 0
    self.custom_mpg     = 0
    self.custom_cpm     = 0
    self.custom_cpg     = 0

  def get_overall_mileage(self):
    if self.stale == True:
      max_index = self.db.get_size() -1
      self.overall_mileage = float(self.db.Entries[max_index][tags.MILEAGE]) - float(self.db.Entries[0][tags.MILEAGE])
    
      
    return self.overall_mileage


  def get_overall_mpg(self):
    
    if self.stale == True:
      sum_gallons = 0
      max_index = self.db.get_size() -1
      mileage = float(self.db.Entries[max_index][tags.MILEAGE]) - float(self.db.Entries[0][tags.MILEAGE])
      for entry in self.db.Entries:
        sum_gallons += float(entry[tags.GALLONS])

      self.overall_mpg = float(mileage)/float(sum_gallons)


    return self.overall_mpg 

  def get_overall_cpm(self):

    if self.stale == True:
      sum_price = 0
      max_index = self.db.get_size()- 1
      mileage = float(self.db.Entries[max_index][tags.MILEAGE]) - float(self.db.Entries[0][tags.MILEAGE])
      for entry in self.db.Entries:
        sum_price += float(entry[tags.PRICE])

      self.overall_cpm = mileage/sum_price


    return self.overall_cpm 


  def get_overall_cpg(self):
    if self.stale == True:
      sum_price = 0
      sum_gallons = 0
      max_index = self.db.get_size() -1
      mileage = float(self.db.Entries[max_index][tags.MILEAGE]) - float(self.db.Entries[0][tags.MILEAGE])
      for entry in self.db.Entries:
        sum_price += float(entry[tags.PRICE])
        sum_gallons += float(entry[tags.GALLONS])

      self.overall_cpg = sum_price/sum_gallons


    return self.overall_cpg




  def get_recent_mileage(self):
    if self.stale == True:
      max_index = self.db.get_size() -1
      self.recent_mileage = float(self.db.Entries[max_index][tags.MILEAGE]) - float(self.db.Entries[max_index-10][tags.MILEAGE])
    
      
    return self.recent_mileage

  def get_recent_mpg(self):
    if self.stale == True:
      sum_gallons = 0
      max_index =  self.db.get_size() - 1
      mileage = float(self.db.Entries[max_index][tags.MILEAGE]) - float(self.db.Entries[max_index-10][tags.MILEAGE])

      for x in range(max_index-10, max_index):
        sum_gallons += float(self.db.Entries[x][tags.GALLONS])

      self.recent_mpg = float(mileage)/float(sum_gallons)
  
    return self.recent_mpg

  def get_recent_cpm(self):
    if self.stale == True:
      sum_gallons = 0
      max_index =  self.db.get_size() - 1
      mileage = float(self.db.Entries[max_index][tags.MILEAGE]) - float(self.db.Entries[0][tags.MILEAGE])

      for x in range(max_index-10, max_index):
        sum_gallons += float(self.db.Entries[x][tags.GALLONS])

      self.recent_cpm = float(mileage)/float(sum_gallons)
  
    return self.recent_cpm

  def get_recent_cpg(self):
    if self.stale == True:
      sum_price = 0
      sum_gallons = 0
      max_index =  self.db.get_size() - 1
      for x in range(max_index-10, max_index):
        sum_price += float(self.db.Entries[x][tags.PRICE])
        sum_gallons += float(self.db.Entries[x][tags.GALLONS])

      self.recent_cpg = sum_price/sum_gallons

    return self.recent_cpg
 
  

  def get_custom_mileage():
    return

  def get_custom_mpg():
    return

  def get_custom_cpm():
    return 

  def get_custom_cpg():
    return 
