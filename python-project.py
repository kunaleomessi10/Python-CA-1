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
        NetPay["Overtime Hours Worked"] = OverTime
        
        OTR = self.HourlyRate * self.OTMultiple
        NetPay["Overtime Rate"] = OTR
        
        OTP = int(OverTime) * int(OTR)
        NetPay["Overtime Pay"] = OTP
        
        GrossPay = int(RegPay) + int(OTP)
        NetPay["Gross Pay"] = GrossPay

        StandardPay = self.StandardBand
        NetPay["Standard Rate Pay"] = StandardPay
        
        HRP = GrossPay - StandardPay
        NetPay["Higher Rate Pay"] = HRP

        StandardTax = StandardPay * 0.2
        NetPay["Standard Tax"] = StandardTax

        HigherTax = HRP * 0.4
        NetPay["Higher Tax"] = HigherTax

        TotalTax = StandardTax + HigherTax
        NetPay["Total Tax"] = TotalTax

        NetDeduction = float(TotalTax) - self.TaxCredit
        NetPay["Net Deductions"] = NetDeduction

        return NetPay

jg= Employee(12345,'Green','Joe', 37, 16, 1.5, 72, 710)
print(jg.ComputePayment(42, '10/12/2021'))