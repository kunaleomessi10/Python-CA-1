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
        
        HoursWorked = int(HoursWorked)
        NetPay["Regular Hours Worked"] = HoursWorked

        RegPay = self.HourlyRate * self.RegHours
        NetPay["Regular pay"] = RegPay
        
        OverTime = HoursWorked - self.RegHours
        
        OTR = self.HourlyRate * self.OTMultiple
        
        OTP = int(OverTime) * int(OTR)
        
        GrossPay = int(RegPay) + int(OTP)
        
        StandardPay = self.StandardBand
        
        HRP = GrossPay - StandardPay
        
        StandardTax = StandardPay * 0.2
        
        HigherTax = HRP * 0.4
        
        TotalTax = StandardTax + HigherTax
        
        NetDeduction = float(TotalTax) - self.TaxCredit

        return NetPay

jg= Employee(12345,'Green','Joe', 37, 16, 1.5, 72, 710)
print(jg.ComputePayment(42, '10/12/2021'))