class Employee:
    def __init__(self, name, salary, id, position, experience):
        self.name = name
        self.salary = salary
        self.position = position
        self.id=id

class Developer(Employee):
    def __init__(self, name, salary, id, position, tech, focus, experience):
        self.tech = tech
        self.area_of_work = focus
        super().__init__(name, salary, id , position, experience)

class Testing(Employee):
    pass

class sales(Employee):
    pass

class TechLead(Employee):
    def __init__(self, name, salary, id, position, tech, team, experience):
        self.team = team
        super().__init__(name, salary, id , position, experience)
