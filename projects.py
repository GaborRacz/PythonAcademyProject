import os
import storage_utils

class Project(object):
    """
    We have to store our documents for using them in various projects.
    The projects has the following attributes:
        - project name which identify the project
        - description of the project goals
        - members
        - documents
    """
    def __init__(self, name, description, members=None, documents=None):
        if members is None:
            members = []
        if documents is None:
            documents = []
        self.name = name
        self.description = description
        self.members = members
        self.documents = documents

    def has_required_roles(self):
        manager = False
        admin = False
        for member in self.members:
            if member.role == "manager":
                manager = True
            if member.role == "admin":
                admin = True
        return manager and admin


class ProjectManager(object):
    """
    Creating, listing and removing projects
    """

    def __init__(self, project_location, user_manager):
        self.project_location = project_location
        self.user_manager = user_manager

    def save_project(self, project_id, project):
        with open(os.path.join(self.project_location, str(project_id)), 'w') as project_file:
            project_file.write(project.name + '\n')
            project_file.write(project.description + '\n')
            project_file.write(str(project.members) + '\n')
            project_file.write(str(project.documents) + '\n')

    def add_project(self, project):
        project_id = storage_utils.get_next_id(self.project_location)
        self.save_project(project_id, project)
        return project_id

    def update_project(self, project_id, project):
        self.remove_project(project_id)
        self.save_project(project_id, project)

    def remove_project(self, project_id):
        project_file_path = os.path.join(self.project_location, str(project_id))
        if os.path.exists(project_file_path):
            os.remove(project_file_path)
        else:
            raise ValueError('The project {} does not exist!'.format(project_id))

    def list_project(self):
        return [p for p in os.listdir(self.project_location)
                if os.path.isfile(os.path.join(self.project_location, p))]

    def load_project(self, project_id):
        with open(os.path.join(self.project_location, str(project_id))) as project_file:
            name = project_file.readline().strip()
            description = project_file.readline().strip()
            members = project_file.readline().strip()
            documents = project_file.readline().strip()
        return Project(name, description, members, documents)

    def find_project_by_id(self, project_id):
        project_file_path = os.path.join(self.project_location, str(project_id))
        if os.path.exists(project_file_path):
            return self.load_project(project_id)
        else:
            raise ValueError('The project {} does not exist!'.format(project_id))

    def find_project_by_name(self):
        pass

    def count_projects(self):
        return len(os.listdir(self.project_location))
