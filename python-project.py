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

