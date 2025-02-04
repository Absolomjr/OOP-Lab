# Part (a) - Defining the Person and Employee classes
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Employee(Person):
    def __init__(self, name, age, gender, employee_id, department):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.department = department
        self.tasks = []  # List to store assigned tasks

    # Part (b) - Method to assign a task
    def assign_task(self, task):
        if task in self.tasks:
            print(f"Task '{task}' is already assigned to {self.name}.")
        else:
            self.tasks.append(task)
            print(f"Task '{task}' assigned to {self.name}.")

    # Part (d) - Method to display employee information
    def display_employee_info(self):
        tasks_display = ", ".join(self.tasks) if self.tasks else "No tasks assigned."
        print(f"Name: {self.name}, Department: {self.department}, Tasks: {tasks_display}")

# Part (c) - Creating employee objects and assigning tasks
employee1 = Employee("Alice", 30, "Female", 101, "Engineering")
employee2 = Employee("Bob", 35, "Male", 102, "Marketing")

employee1.assign_task("Complete project report")
employee1.assign_task("Attend team meeting")
employee2.assign_task("Prepare marketing plan")
employee2.assign_task("Complete project report")  # Example of assigning the same task

# Part (d) - Displaying employee information
employee1.display_employee_info()
employee2.display_employee_info()
