#first name, second name, salary, experiance (years) and manager



class Employee:
    def __init__(self, first_name, second_name, salary, experiance, manager):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary
        self.experiance = experiance
        self.manager = manager

        # g) Each employee gets the salary, defined in field Salary.
        #  If experiance of employee is > 2 years, he gets bonus + 200$, if experiance is > 5 years
        # he gets salary*1.2 + bonus 500
        if self.experiance > 5:
            self.salary *= 1.2
            self.salary += 500

        elif self.experiance > 2:
            self.salary += 200

# j) Redefine string representation for employee as follows:
#"@firstName@ @secondName@, manager:@manager secondName@, experiance:@experiance@"
    def __str__(self):
        #return self.first_name + " " + self.second_name + " manager: " + self.manager + " experiance: " + isinstance(self.experiance, str)
        return "%s %s manager: %s experiance: %s" % (self.first_name, self.second_name, self.manager, self.experiance)

class Developer(Employee):
    def __str__(self):
        return "I am dev"

# c) Each designer has effectivness coefficient(0-1)
class Design(Employee):
    def __init__(self, eff_coef, first_name, second_name, salary, experiance, manager):
        super().__init__(first_name, second_name, salary, experiance, manager)
        self.eff_coef = eff_coef
        # h) Each designer gets the salary = salary*effCoeff
        self.salary = self.salary*self.eff_coef

        if eff_coef > 1 or eff_coef < 0:
            print("Effectivness Coefficient should be from 0 to 1")




class Manager(Employee):
    def __init__(self, first_name, second_name, salary, experiance, manager, developers, designers):
        super().__init__(first_name, second_name, salary, experiance, manager)
        self.developers = developers
        self.designers = designers

        # i) Each manager gets salary +
        # ii) 200$ if his team has >5 members
        # iii) 300$ if his team has >10 members
        # iiii) salary*1.1 if more than half of team members are developers.

        if (self.designers + self.developers) > 10:
            self.salary += 300
        elif self.designers + self.developers > 5:
            self.salary += 200
        if self.developers - self.designers > 0:
            self.salary *= 1.1





class Department(Employee, Manager):
    def __init__(self, first_name, second_name, salary, experiance, manager, developers, designers):
        super().__init__(first_name, second_name, salary, experiance, manager, developers, designers)

    # e) Department should have list of managers(which have their own teams)
        managerList = []
        if self.designers + self.developers > 0:
            managerList.append(self.first_name)

    # f) Department should be able to give salary
    # (for each employee message: "@firstName@ @secondName@: got salary: @salaryValue@")
    def __str__(self):
        #return self.first_name + " " + self.second_name + " : got salary: " + isinstance(self.salary, str)
        return "%s %s : got salary: %s" % (self.first_name, self.second_name, self.salary)



