import unittest

from docgen import generator
from documents import Document


class TestDocument(unittest.TestCase):
    """Test the document class"""

    def test_creation(self):
        document = Document('title1', 'desc1', 'author1', ['1.pdf', '2.pdf'], 'pdf')

    def test_properties(self):
        document = Document('title1', 'desc1', 'author1', ['1.pdf', '2.pdf'], 'pdf')
        self.assertEqual(document.title, 'title1')
        self.assertEqual(document.description, 'desc1')
        self.assertEqual(document.author, 'author1')
        self.assertEqual(document.files, ['1.pdf', '2.pdf'])
        self.assertEqual(document.doc_format, 'pdf')

    def test_visibility(self):
        document = Document('title1', 'desc1', 'author1', ['1.pdf', '2.pdf'], 'pdf')
        self.assertFalse(document.is_public())
        document.make_public()
        self.assertTrue(document.is_public())
        document.make_private()
        self.assertFalse(document.is_public())

    def test_generator_general(self):
        for extension in generator.extensions['general']:
            for name in generator.filename_parts['general']:
                document = Document('title1', 'desc1', 'author1', name + extension, extension)
                self.assertTrue(document.doc_format in generator.extensions['general'])

    def test_generator_office(self):
        for extension in generator.extensions['office']:
            for name in generator.filename_parts['office']:
                document = Document('title1', 'desc1', 'author1', name + extension, extension)
                self.assertTrue(document.doc_format in generator.extensions['office'])

    def test_generator_image(self):
        for extension in generator.extensions['image']:
            for name in generator.filename_parts['image']:
                document = Document('title1', 'desc1', 'author1', name + extension, extension)
                self.assertTrue(document.doc_format in generator.extensions['image'])
