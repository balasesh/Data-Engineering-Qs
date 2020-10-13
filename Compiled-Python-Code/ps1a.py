#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 10:17:14 2020

@author: bsura
"""

def house_hunting(salary, portion_saved, dream_house):
    portion_down_payment = 0.25*dream_house
    monthly_salary = salary/12
    rate = 0.04
    monthly_saving = portion_saved*monthly_salary
    number_of_months = 0
    current_savings = 0
    
    while current_savings < portion_down_payment:
        current_savings += monthly_saving
        current_savings += (current_savings*rate)/12
        number_of_months +=1

    return number_of_months
    

def get_input():
    a = input("Enter your annual salary: ")
    b = input("Enter the percent of your salary to save, as a % : ")
    c = input("Enter the cost of your dream home: ")
    salary = round(float(a),2)
    portion_saved = round(float(b)/100,2)
    dream_house = round(float(c),2)
    number_of_months = house_hunting(salary,portion_saved,dream_house)

    
    print "Number of months:​ ", number_of_months

get_input()
    