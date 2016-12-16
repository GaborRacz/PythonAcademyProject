"""Repository

The repository is in a dedicated directory. This directory contains the following subdirectories by default:

    documents/  - document data and metadata files
    logs/       - logs of the repository events
    projects/   - project files
    users/      - user metadata files
    paths.ini   - the path of the main parts of the repository
    roles.txt   - user roles

The documents directory contains subdirectories which name is the document identifier.

For document metadata we save them to text files with the same name and .info extension next to the directories.

The paths.ini file contains the (relative or absolute) paths of mentioned subdirectories.

The roles.txt contains the user names and the list of assigned roles.
"""

import os
import shutil
from datetime import datetime


import reports
from users import UserManager
from documents import DocumentManager
from iniformat.writer import write_ini_file


class Repository(object):
    """Represents the document management system as a repository"""

    def __init__(self, name, location):
        self._name = name
        self._location = location
        self.load()
        self._user_manager = UserManager(location)
        self._document_manager = DocumentManager(location)

    def load(self):
        """Try to load an existing repository"""
        if os.path.exists(self._location):
            if os.path.isdir(self._location):
                pass
            else:
                raise ValueError('The repository should be a directory!')
        else:
            self.initialize()

    def initialize(self):
        """Initialize a new repository"""
        os.makedirs(self._location)
        for dir_name in ['documents', 'logs', 'projects', 'users']:
            os.makedirs('{}/{}'.format(self._location, dir_name))
        role_file_path = '{}/roles.txt'.format(self._location)
        with open(role_file_path, 'w'):
            os.utime(role_file_path, None)
        self.create_default_path_file()
        self._creation_date = datetime.now()

    def create_default_path_file(self):
        data = {
            'directories': {
                'documents': 'documents',
                'logs': 'logs',
                'projects': 'projects',
                'users': 'users'
            }
        }
        write_ini_file('{}/paths.ini'.format(self._location), data)

    def import_documents(self, path):
        if self._user_manager.count_users() < 1:
            raise ValueError("Can't import without users")

        for document_id in os.listdir(path):
            shutil.copy(os.path.join(path, document_id), os.path.join(self._document_manager._document_location, "documents"))

    def export_documents(self, document_ids, target):
        for id in document_ids:
            for document in os.listdir(self._document_manager._document_location):
                if id == document:
                    shutil.copy(os.path.join(self._document_manager._document_location, "documents", id), target)

    def create_backup(self, name, target="/backup"):
        self.backup_creation_date = datetime.now()
        self.users = self._user_manager.count_users()
        self.documents = self._document_manager.count_documents()
        shutil.copytree(self._location, os.path.join(target, name))

    def restore_backup(self, name, source="/backup"):
        shutil.rmtree(self._location)
        shutil.copytree(os.path.join(source, name), self._location)

    def show_backup_info(self):
        print("The backup was taken at {} .".format(self.backup_creation_date))
        print("There were {} users in the repository.".format(self.users))
        print("There were {} documents in the repository.".format(self.documents))

    def create_report(self):
        return reports.Report()
