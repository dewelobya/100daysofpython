#Määrittele aluksi luokat

#PayrollSystem, jossa metodi calculate_payroll, joka saa parametrinaan työntekijöiden listan. Metodi laskee ja tulostaa  työntekijöiden palkat.
#SalaryEmployee, Employee-luokan aliluokka, jolla on oma attribuutti monthly_salary ja metodi calculate_salary, joka palauttaa työntekijän kuukausipalkan.
 
#Kirjoita seuraavaksi pääohjelma,
#joka kysyy työntekijöiden nimet kuten Employee-tehtävässä sekä lisäksi kysyy SalaryEmployee-luokan kuukausipalkat luoden tietojen perusteella SalaryEmployee-oliot.
#jossa syntyneet SalaryEmployee-oliot viedään listaan.
#jossa käyttäjä lopettaa ohjelman suorittamisen antamalla '0' nimen sijasta.
#joka lopuksi PayrollSystem-luokan avulla tulostaa palkkalaskelmat kuten esimerkissä alla.


class PayrollSystem:
    def calculate_payroll(self, employees):
        print("Palkkalaskelmat:")
        print("================")
        for employee in employees:
            payroll = employee.calculate_salary()
            print("Työntekijä:", employee.name)
            print("Kuukausipalkka:", payroll)
            print()


class Employee:
    def __init__(self, name):
        self.name = name


class SalaryEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


payroll_system = PayrollSystem()
employees = []

while True:
    name = input("Anna työntekijän nimi (0 lopetus): ")
    if name == "0":
        break
    monthly_salary = float(input("Anna kuukausipalkka: "))
    employee = SalaryEmployee(name, monthly_salary)
    employees.append(employee)

payroll_system.calculate_payroll(employees)


#ei toimi
