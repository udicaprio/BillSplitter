# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 16:31:53 2023

@author: Ulderico Di Caprio
"""

import numpy as np

class Splitter():
    def __init__(self, people_name):
        self.p_name = people_name
        self.create_structure()
        
    def create_structure(self):
        self.Np = len(self.p_name)
        self.from_database = np.zeros((0, self.Np))
        self.to_database = np.zeros((0, self.Np))
        self.amount_database = np.zeros((0,1))
        self.money_flow_matrix = np.zeros((self.Np, self.Np))
    
    def add_expense(self, from_, amount = 0, to_ = 'everyone'):
        from_line = np.zeros(self.Np)
        to_line = np.zeros(self.Np)
        
        if to_ == 'everyone':
            to_ = self.p_name
        if from_ == 'everyone':
            from_ = self.p_name
        
        for pidx in range(self.Np):
            name = self.p_name[pidx]
            if name in to_:
                to_line[pidx] = 1
            if name in from_:
                from_line[pidx] = 1
            
        self.from_database = np.vstack((self.from_database, from_line))
        self.to_database = np.vstack((self.to_database, to_line))
        self.amount_database = np.vstack((self.amount_database, amount))
        
    def calculate_debit(self):
        self.debit = np.dot(self.amount_database.reshape(1, -1)[0]/np.sum(self.to_database , axis=1), 
                            self.to_database )
        
    def calculate_credit(self):
        self.credit = np.dot(self.amount_database.reshape(1, -1)[0]/np.sum(self.from_database, axis=1), 
                             self.from_database)
    
    def run_calculation(self):
        self.calculate_debit()
        self.calculate_credit()
        self.net = self.credit-self.debit