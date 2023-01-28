# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 16:31:53 2023

@author: Ulderico Di Caprio
"""

import numpy as np

class Splitter():
    def __init__(self, people_name):
        '''
        Initiate the instance of the splitter. At this stage, you have to mention
        how many people are in the group.
        
        Parameters
        ----------
        people_name: list
            List containing the name of the people within the group. The list has
            to strings.
        
        Returns
        -------
        None.
        
        '''
        
        self.p_name = people_name
        self.create_structure()
        
    def create_structure(self):
        '''
        Create the matematical elements needed for the code to run. 
        It specify the number of people within the group and create the data structures
        to contain the information that will be logged during the code usage.
        
        Parameters
        ----------
        None.
        
        Returns
        -------
        None.
        
        '''  
        self.Np = len(self.p_name)
        self.from_database = np.zeros((0, self.Np))
        self.to_database = np.zeros((0, self.Np))
        self.amount_database = np.zeros((0,1))
        self.money_flow_matrix = np.zeros((self.Np, self.Np))
    
    def add_expense(self, from_, amount = 0, to_ = 'everyone'):
        '''
        
        Parameters
        ----------
        from_ : list or string
            List containing the names of the people that made the payment. The only string
            allowed at the input is the string 'everyone'. In case only one person paying 
            the bill, you can insert the name in a list
        amount : float, optional
            Amount of the payed bill. The default is 0.
        to_ : list or string, optional
            List containing the names of the people which expenses were in the bill. The 
            only string allowed at the input is the string 'everyone'. In case the bill was
            payed for only one person, you can insert the name in a list. 
            The default is 'everyone'.

        Returns
        -------
        None.

        '''
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
        '''
        Calculates the debit of the people.

        Returns
        -------
        None.

        '''
        self.debit = np.dot(self.amount_database.reshape(1, -1)[0]/np.sum(self.to_database , axis=1), 
                            self.to_database )
        
    def calculate_credit(self):
        '''
        Calculates the credit of the people.

        Returns
        -------
        None.

        '''
        self.credit = np.dot(self.amount_database.reshape(1, -1)[0]/np.sum(self.from_database, axis=1), 
                             self.from_database)
    
    def run_calculation(self):
        '''
        Calculate the debit and the credit of the people updating the value of the net.

        Returns
        -------
        None.

        '''
        self.calculate_debit()
        self.calculate_credit()
        self.net = self.credit-self.debit