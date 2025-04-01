# Creating a class to represent an individual team member
class TeamMember:
    # Initializing team member with name, role, and skill level
    def __init__(self, name, role, skill_level):
        self.name = name
        self.role = role
        self.skill_level = skill_level  # Represents expertise, e.g., beginner, intermediate, expert

# Creating a class to manage project details and team assignments
class Project:
    # Setting up project with a name, deadline, and an empty team list
    def __init__(self, project_name, project_deadline):
        self.project_name = project_name
        self.project_deadline = project_deadline
        self.team_members = []  # List to hold TeamMember objects

    # Adding a team member to the project, with duplicate checking
    def assign_member(self, team_member):
        # Checking if the member is already on the team
        if team_member in self.team_members:
            print(f"Error: {team_member.name} is already part of {self.project_name}.")
            return False
        else:
            # Adding new member and confirming assignment
            self.team_members.append(team_member)
            print(f"{team_member.name} has been added to {self.project_name}.")
            return True

    # Displaying all project details, including team members
    def display_project_info(self):
        print(f"Project Name: {self.project_name}")
        print(f"Deadline: {self.project_deadline}")
        print("Assigned Team Members:")
        # Showing team details or indicating if team is empty
        if self.team_members:
            for member in self.team_members:
                print(f" - {member.name}, Role: {member.role}, Skill Level: {member.skill_level}")
        else:
            print(" - No team members assigned yet.")

# Setting up a sample project and team for demonstration
def main():
    # Instantiating a new project
    web_project = Project("Website Redesign", "2025-06-30")

    # Creating individual team members with different roles and skills
    member1 = TeamMember("Alice", "Developer", "Expert")
    member2 = TeamMember("Bob", "Designer", "Intermediate")
    member3 = TeamMember("Charlie", "Tester", "Beginner")

    # Assigning team members to the project
    web_project.assign_member(member1)
    web_project.assign_member(member2)
    web_project.assign_member(member3)

    # Testing duplicate assignment prevention
    web_project.assign_member(member1)  # Should show an error

    # Printing full project information
    print("\nProject Details:")
    web_project.display_project_info()

# Running the program
if __name__ == "__main__":
    main()