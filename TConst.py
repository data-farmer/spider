import sys
class TConst(object):
    class TConstError(Exception): 
        pass
    def __setattr__(self, key, value):
        if self.__dict__.has_key(key):
            raise self.TConstError, "changeing const.%s"% key
        else:
            self.__dict__[key] = value
    def __getattr__(self, key):
        if self.__dict__.has_key(key):
            return self.key
        else:
            return None
sys.modules[__name__] = TConst()
