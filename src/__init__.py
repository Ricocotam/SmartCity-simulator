__name__ = '.'.join(__name__.split('/'))
__package__ = '.'.join('.'.join(__name__.split('/')).split('.')[:-1])