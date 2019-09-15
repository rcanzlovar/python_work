#!/usr/bin/env python3


class ProgStaff: 
    companyName = 'Programming Lab'

    def __init__(self, pSalary):
        self.salary = pSalary

    def printInfo(self):
        print("Company Name is",ProgStaff.companyName)
        print("Salary is ",self.salary)


peter = ProgStaff(2500)
john = ProgStaff(2500)
