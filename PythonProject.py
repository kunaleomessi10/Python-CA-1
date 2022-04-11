#GIT LINK
#https://github.com/kunaleomessi10/Python-CA-1/blob/main/PythonProject.py
#https://github.com/kunaleomessi10/Python-CA-1.git

import unittest


class Employee:

    def __init__(self, S_ID, Last_Name, First_Name, Reg_Hours, Hourly_Rate, OT_Multiple, Tax_Credit, Standard_Band):
        self.StaffID = S_ID
        self.LastName = Last_Name
        self.FirstName = First_Name
        self.RegHours = Reg_Hours
        self.HourlyRate = Hourly_Rate
        self.OTMultiple = OT_Multiple
        self.TaxCredit = Tax_Credit
        self.StandardBand = Standard_Band

    def ComputePayment(self, HoursWorked, date):
        NetPay= {}
        NetPay["name"] = self.FirstName + " " + self.LastName
        NetPay["Date"] = date
    
    #   Regular Hours Worked
        HoursWorked = int(HoursWorked)
        NetPay["Regular Hours Worked"] = HoursWorked

    #   Regular pay
        RegPay = self.HourlyRate * self.RegHours
        NetPay["Regular pay"] = RegPay

    #   Overtime Hours Worked
        OverTime = 0
        OTR =0
        if HoursWorked > self.RegHours:
            OverTime = HoursWorked - self.RegHours
            NetPay["Overtime Hours Worked"] = OverTime
#   Overtime Rate    
            OTR = self.HourlyRate * self.OTMultiple
            NetPay["Overtime Rate"] = OTR
        else:
            NetPay["Overtime Hours Worked"] = 0
            NetPay["Overtime Rate"] = 0

    #   Overtime Pay
        OTP = OverTime* OTR
        NetPay["Overtime Pay"] = OTP

    #   Gross Pay    
        GrossPay = int(RegPay) + int(OTP)
        NetPay["Gross Pay"] = GrossPay

    #   Standard Rate Pay
        StandardPay = self.StandardBand
        NetPay["Standard Rate Pay"] = StandardPay

    #   Higher Rate Pay        
        HRP = GrossPay - StandardPay
        NetPay["Higher Rate Pay"] = HRP

    #   Standard Tax
        StandardTax = StandardPay * 0.2
        NetPay["Standard Tax"] = StandardTax

    #   Higher Tax
        HigherTax = HRP * 0.4
        NetPay["Higher Tax"] = HigherTax

    #   Total Tax
        TotalTax = StandardTax + HigherTax
        NetPay["Total Tax"] = TotalTax

    #   Net Deductions
        NetDeduction = float(TotalTax) - self.TaxCredit
        NetPay["Net Deductions"] = NetDeduction

    # Net pay is final pay user will get after deductions
        netpay = GrossPay - NetDeduction
        NetPay["Net Pay"]= netpay

        return NetPay

jg= Employee(12345,'Green','Joe', 37, 16, 1.5, 72, 710)

class test1(unittest.TestCase):

    # Net pay is always less than gross
    def testNetLessEqualGross(self):
        e=Employee(12345,'Green','Joe', 37, 16, 1.5, 72, 710)
        pi=e.ComputePayment(1,'31/10/2021')
        self.assertLessEqual(pi['Net Pay'],pi['Gross Pay'])

    #Overtime pay or overtime hours cannot be negative.
    def testOvertimenotNegative(self):
        e=Employee(12345,'Green','Joe', 37, 16, 1.5, 72, 710)
        pi=e.ComputePayment(1,'31/10/2021')
        self.assertGreaterEqual(0,pi['Overtime Pay'])

    #Higher Tax cannot be negative.
    def testHigherTaxnotNegative(self):
        e=Employee(12345,'Green','Joe', 37, 16, 1.5, 72, 710)
        pi=e.ComputePayment(10,'31/10/2021')
        self.assertGreaterEqual(0,pi['Higher Tax'])

    #Net Pay cannot be negative.
    def testNetPayCannotNegative(self):
        e=Employee(12345,'Green','Joe', 37, 16, 1.5, 72, 710)
        pi=e.ComputePayment(10,'31/10/2021')
        self.assertGreaterEqual(pi['Net Pay'],0)

    #Regular Hours Worked cannot exceed hours worked
    def testRegularHoursWorked(self):
        e=Employee(12345,'Green','Joe', 37, 16, 1.5, 72, 710)
        pi=e.ComputePayment(10,'31/10/2021')
        self.assertGreaterEqual(pi['Regular Hours Worked'],10)


if __name__ == '__main__':
    unittest.main()