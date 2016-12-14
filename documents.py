import os


class Document(object):
    """Document of the repository"""

    def __init__(self, title, description, author, files, doc_format):
        self._title = title
        self._spaceless_title = title.replace(" ", "")
        self._description = description
        self._author = author
        self._files = files
        self._doc_format = doc_format
        self._state = 'new'
        self._is_public = False

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def spaceless_title(self):
        return self._spaceless_title

    @spaceless_title.setter
    def spaceless_title(self, value):
        raise ValueError("You can't set the spaceless title.")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def files(self):
        return self._files

    @files.setter
    def files(self, value):
        self._files = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        """Validating state changes, restricts to correct order."""

        if value in ['new', 'pending', 'accepted', 'rejected']:
            if self._state == "new" and value == "pending":
                self._state = value

            if self._state == "pending" and value in ['accepted', 'rejected']:
                self._state = value
        else:
            raise ValueError('The "{}" is an invalid document state!'.format(value))

    @property
    def doc_format(self):
        return self._doc_format
    
    @doc_format.setter
    def doc_format(self, value):
        self._doc_format = value

    def is_public(self):
        return self._is_public

    def make_public(self):
        self._is_public = True

    def make_private(self):
        self._is_public = False


class DocumentManager(object):
    """Manage documents"""

    def __init__(self, document_location):
        self._document_location = document_location

    def add_document(self, document):
        with open(os.path.join(self._document_location, document.spaceless_title), 'w') as doc_file:
            doc_file.write(document.title + '\n')
            doc_file.write(document.description + '\n')
            doc_file.write(document.author + '\n')
            doc_file.write(document.files + '\n')
            doc_file.write(document.state + '\n')
            doc_file.write(document.is_public() + '\n')

    def update_document(self, document):
        self.remove_document(document)
        self.add_document(document)

    def remove_document(self, document):
        doc_file_path = os.path.join(self._document_location, document.spaceless_title)
        if os.path.exists(doc_file_path):
            os.remove(doc_file_path)
        else:
            raise ValueError('The document {} does not exist!'.format(document.spaceless_title))

    def list_documents(self):
        return [f for f in os.listdir(self._document_location)
                if os.path.isfile(os.path.join(self._document_location, f))]

    def load_document(self, title):
        with open(os.path.join(self._document_location, title)) as doc_file:
            title = doc_file.readline().strip()
            author = doc_file.readline().strip()
            files = doc_file.readline().strip()
            doc_format = doc_file.readline().strip()
            state = doc_file.readline().strip()
            is_public = doc_file.readline().strip()
        doc = Document(title, author, files, doc_format, state)
        if is_public == "True":
            doc.make_public()
        return doc

    def find_document_by_title(self, title):
        spaceless_title = title.replace(" ", "")
        doc_file_path = os.path.join(self._document_location, spaceless_title)
        if os.path.exists(doc_file_path):
            doc = self.load_document(spaceless_title)
            return doc
        else:
            raise ValueError('The document {} does not exist!'.format(spaceless_title))

    def find_document_by_author(self):
        pass

    def find_document_by_format(self):
        pass
