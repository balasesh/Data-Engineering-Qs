#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 11:29:29 2020

@author: bsura
"""

def house_hunting(x):
    total_cost = 1000000
    semi_annual_raise = 0.07
    current_savings = 0
    portion_down_payment = 0.25 * total_cost
    epsilon = 100
    low = 0
    high = 10000
    step = 0
    
    while True:
        portion_saved = (low + high) / 2
        annual_salary = x
        current_savings = 0
        for mo in range(0, 36):
            monthly_salary = annual_salary / 12
            current_savings = current_savings + float((monthly_salary * portion_saved) / 10000) + (current_savings * 0.04) / 12
            if mo % 6 == 0:
                annual_salary = annual_salary + (annual_salary * semi_annual_raise)
        print 'current savings: ' + str(current_savings)
        if abs(current_savings - portion_down_payment) <= epsilon:
            return portion_saved, step, current_savings
        # decrease portion_save
        elif abs(current_savings - portion_down_payment) > epsilon and current_savings > portion_down_payment:
            high = portion_saved
        # increase portion_save
        elif abs(current_savings - portion_down_payment) > epsilon and current_savings < portion_down_payment:
            low = portion_saved
        if high - low <= 1 :
            return -1,-1,-1
        step += 1
    
    return -1,-1,-1
        
def get_input():
    x = float(input('Enter your starting salary: '))
    portion_saved, step, current_savings = house_hunting(x)
    
    if step >= 0:
        print 'Best saving rate: ', '%.2f' % (portion_saved / 100), '%'
        print 'Step in binary search: ', step
        print 'Current Savings : ', current_savings
    else: 
        print('It is not possible to pay the down payment in three years.')

get_input()