from sip import wrappertype as pyqtWrapperType
from abc import ABCMeta

class MainWindowMeta( pyqtWrapperType, ABCMeta ): pass
