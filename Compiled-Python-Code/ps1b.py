#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 11:29:29 2020

@author: bsura
"""

def house_hunting(salary, portion_saved, dream_house, inc_raise):
    portion_down_payment = 0.25*dream_house
    rate = 0.04
    number_of_months = 0
    current_savings = 0
    
    monthly_salary = salary/12
    monthly_saving = portion_saved*monthly_salary
    
    while current_savings < portion_down_payment:
        if number_of_months > 0 and number_of_months%6 == 0:
                salary += salary*inc_raise
                monthly_salary = salary/12
                monthly_saving = portion_saved*monthly_salary
#                print(str(monthly_saving) +  " & " + str(number_of_months))
        
        current_savings += monthly_saving
        current_savings += (current_savings*rate)/12
        number_of_months +=1

    return number_of_months
    

def get_input():
    a = input("Enter your annual salary: ")
    b = input("Enter the percent of your salary to save, as a % : ")
    c = input("Enter the cost of your dream home: ")
    d = input("Enter the raise of your salary semianually, as a % : ")
    salary = round(float(a),2)
    portion_saved = round(float(b)/100,2)
    dream_house = round(float(c),2)
    inc_raise  = round(float(d)/100,2)
    number_of_months = house_hunting(salary,portion_saved,dream_house, inc_raise)
    
#   number_of_months = house_hunting(120000.00,0.05,500000, 0.03)
#   number_of_months = house_hunting(80000,0.1,800000, 0.03)
#   number_of_months = house_hunting(75000,0.05,1500000, 0.05)
    
    print "Number of months:​ ", number_of_months

get_input()
    