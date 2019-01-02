class PyAluxException(Exception):
    pass


class InvalidCategoryException(PyAluxException):
    pass


class InvalidTagException(PyAluxException):
    pass


class UnknownPageFormatException(PyAluxException):
    pass


class NoArticlesFoundException(PyAluxException):
    pass


class UnknownUrlException(PyAluxException):
    pass


class NotVideoUrlException(UnknownUrlException):
    pass


class BadPostException(PyAluxException):
    pass


class NoVideosFoundException(PyAluxException):
    pass
