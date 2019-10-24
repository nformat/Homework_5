from datetime import datetime

class Person():

    def __init__(self, full_name="", birthday=0):
        if type(full_name) is not str or len(full_name.split()) != 2:
            raise Exception("Полное имя должно быть строкой из двух слов разделенных пробелом")
        if birthday < 1900 or birthday > 2019:
            raise  Exception("Указанна неверная дата рождения")
        self.full_name = full_name
        self.birthday = birthday

    def get_name (self):
        return self.full_name.split()[0]


    def get_sername(self):
        return self.full_name.split()[1]


    def get_year(self, age_in=None):
        if age_in is None: age_in = datetime.now().year
        print(age_in)
        return age_in-self.birthday

    def __str__(self):
        return f"\nObject {self.__class__}\nfull_name: {self.full_name}, birthday: {self.birthday}"



###############################

class Employee(Person):

    def __init__(self, full_name="", birthday=0, position="", exp=0, salary=0):
        Person.__init__(self, full_name, birthday)
        self.position = position
        self.exp = exp
        self.salary = salary

    def exp_position(self):
        pref = "Junior" if self.exp < 3 else "Middle" if self.exp >= 3 and self.exp < 6 else "Senior "
        return f"{pref} {self.position}"


    def up_sal(self, up):
        self.salary += up


    def __str__(self):
        return f"\nObject {self.__class__}\nfull_name: {self.full_name}, birthday: {self.birthday}, position:" \
               f" {self.position}, exp: {self.exp}, salary: {self.salary}"



##############################
class ITEmployee(Employee):

    def __init__(self, *args, **kwargs):
        Employee.__init__(self, *args, **kwargs)
        self.skills = []


    def add_skill(self, *new_skill):
        for i in new_skill:
            self.skills.append(i)

    def __str__(self):
        return f"\nObject {self.__class__}\nfull_name: {self.full_name}, birthday: {self.birthday}, position:" \
               f" {self.position}, exp: {self.exp}, salary: {self.salary}, skills: {self.skills}"

if __name__ == "__main__":

    p = Person("Jim Bean", 1985)
    print("Имя: ", p.get_name())
    print("Фамилия: ", p.get_sername())
    print("Лет:", p.get_year())
    print(p)

    p2 = Employee("Scott Redle", 1980, "Administrator", 5, 3000)
    p2.up_sal(20)

    print("\nКласс Employee:\n", p2.full_name+" на должности ", p2.exp_position()+" получает ", p2.salary)
    print(p2)

    p3 = ITEmployee("John Dou", 1975, "Analitic", 1, 2000)
    p3.add_skill("SIEM", "DLP", "CRM")

    print("\nКласс ITEmployee:\nУ ", p3.full_name+" следующие навыки:", *p3.skills)
    print(p3)



