

class PupaError(Exception):
    """ Base class for exceptions from within Pupa """


class DataImportError(PupaError):
    """ A generic error related to the import process. """


class NoMembershipsError(DataImportError):
    """ An attempt was made to import a person without any memberships. """

    def __init__(self, ids):
        super(NoMembershipsError, self).__init__('no memberhips for {} people: \n{}'.format(
            len(ids), ', '.join(ids))
        )
