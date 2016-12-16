class Report(object):
    def __init__(self, user_count=0, document_count=0, user_count_by_roles=None, import_count=0, export_count=0):
        self.user_count = user_count
        self.document_count = document_count
        if user_count_by_roles is None:
            self.user_count_by_roles = {'admin': 0, 'manager': 0, 'author': 0, 'reviewer': 0, 'visitor': 0}
        else:
            self.user_count_by_roles = user_count_by_roles
        self.import_count = import_count
        self.export_count = export_count

    def general_overview_report(self):
        return "The Repository had {} users, {} documents; there have been {} imports and {} exports".format(
            self.user_count, self.document_count, self.import_count, self.export_count
        )