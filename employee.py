# Define Employee, SalariedEmployee, and WageEmployee
# Employee:  get_name, set_name
# get_paycheck:  do nothing
class Employee:
  def __init__(self, name):
    self.name = name
  def get_name(self):
    return self.name
  def set_name(self, name):
    self.name = name
  def get_paycheck(self):
    pass

# SalariedEmployee:  get_salary, set_salary
# get_paycheck:  salary / 25 (pay periods / yr)
PAY_PERIODS_PER_YEAR = 25
class SalariedEmployee (Employee):
  def __init__(self, name, salary):
    Employee.__init__(self, name)
    self.salary = salary
  def get_salary(self):
    return self.salary
  def set_salary(self, sal):
    if sal >= 0:
      self.salary = sal
  def get_paycheck(self):
    paycheck = self.salary / PAY_PERIODS_PER_YEAR
    # If PAY_PERIODS_PER_YEAR is in class scope:
    # paycheck = self.salary / SalariedEmployee.PAY_PERIODS_PER_YEAR
    return paycheck

# WageEmployees: get_wage, set_wage, get_hours, set_hours
# get_paycheck:  wage * hours
class WageEmployee (Employee):
  def __init__(self, name, wage, hours):
    Employee.__init__(self, name)
    self.wage = wage
    self.hours = hours
  def get_wage(self):
    return self.wage
  def set_wage(self, wage):
    self.wage = wage
  def get_hours(self):
    return self.hours
  def set_hours(self, hrs):
    self.hours = hrs
  def get_paycheck(self):
    return self.wage * self.hours

if __name__ == '__main__':
  jeff = SalariedEmployee('Jeff', 20000)
  destiny = WageEmployee("Destiny", 20.50, 40)
  matt = Employee('Matt')
  
  print(f"Jeff's paycheck is ${jeff.get_paycheck():.2f}") # 800
  print(f"Destiny's paycheck is ${destiny.get_paycheck():.2f}") # 820

  destiny.set_wage(destiny.get_wage() * 1.1)
  print(f"Destiny's paycheck after 10% raise:  ${destiny.get_paycheck():.2f}") # 902

  employees = [ jeff, destiny, matt ]
  print("Employee paychecks: ")
  for emp in employees:
    print(f"{emp.get_name():^8} {emp.get_paycheck()}")
