class Project(object):
    """
    We have to store our documents for using them in various projects.
    The projects has the following attributes:
        - project name which identify the project
        - description of the project goals
        - members
        - documents
    """
    def __init__(self, name, description, members, documents):
        self.name = name
        self.description = description
        self.members = members
        self.documents = documents


