#!/usr/bin/env python3


class Staff:
    def __init__(self, pPosition, pName, pPay):
        self._position = pPosition
        self.name = pName
        self.pay = pPay
        print('creating Staff object')

    def __str__(self):
        return "Position = %s\nName %s\nPay %d\n" \
            % (self._position, self.name, self.pay)

    def calculatePay(self):
        prompt = '\nEnter number of hours worked for %s: ' % (self.name)
        hours = input(prompt)
        prompt = '\nEnter hourly rate for %s: ' % (self.name)
        hourlyRate = input(prompt)
        self.pay = int(hours)*int(hourlyRate)
        return self.pay

    @property
    def position(self):
        print("Getter Method")
        return self._position

    @position.setter
    def position(self, value):
        if value == 'Manager' or value == 'Basic':
            self._position = value
        else:
            print('Position is invalid. No changes made.')


class ManagementStaff(Staff):
    def __init__(self, pName, pPay, pAllowance, pBonus):
        super().__init__('Manager', pName, pPay)
# alternatively
#       Staff.__init__(self, 'Manager',pName, pPay);
# super(ManagementStaff, self).__init__('Manager', pName, pPay)
        self.allowance = pAllowance
        self.bonus = pBonus

    def calculatePay(self):
        basicPay = super().calculatePay()
        self.pay = basicPay + self.allowance
        return self.pay

    def calculatePerfBonus(self):
        prompt = 'Enter performance grade for %s: ' \
            % (self.name)
        grade = input(prompt)
        if (grade == 'A'):
            self.bonus = 1000
        else:
            self.bonus = 0
        return self.bonus


class BasicStaff(Staff):
    def __init__(self, pName, pPay):
        super().__init__('Basic', pName, pPay)

#########################################################


name1 = Staff('Basic', 'Yvonne', 0)
name2 = ManagementStaff('Dave', 0, 50, 100)
name2.calculatePerfBonus()
name2.calculatePay()
name3 = BasicStaff('Bob', 0)
name3.calculatePay()


print(name2)
print(name3)
