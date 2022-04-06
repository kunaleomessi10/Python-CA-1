class Employee:
  employdata = {}

  def __init__(self, StaffID, LastName, FirstName, RegHours, HourlyRate, OTMultiple, TaxCredit, StandardBand):
    self.StaffID = StaffID
    self.LastName = LastName
    self.FirstName = FirstName
    self.RegHours = RegHours
    self.HourlyRate = HourlyRate
    self.OTMultiple = OTMultiple
    self.TaxCredit = TaxCredit
    self.StandardBand = StandardBand
    Employee.employdata[StaffID] = self