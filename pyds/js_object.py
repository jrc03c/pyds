# from https://github.com/bcherry/js-py/blob/master/js.py
class JSObject(object):
  def __init__(self, *args, **kwargs):
    for arg in args:
      self.__dict__.update(arg)

    self.__dict__.update(kwargs)

  def __getitem__(self, name):
    return self.__dict__.get(name, None)

  def __setitem__(self, name, val):
    return self.__dict__.__setitem__(name, val)

  def __delitem__(self, name):
    if self.__dict__.has_key(name):
      del self.__dict__[name]

  def __getattr__(self, name):
    return self.__getitem__(name)

  def __setattr__(self, name, val):
    return self.__setitem__(name, val)

  def __delattr__(self, name):
    return self.__delitem__(name)

  def __iter__(self):
    return self.__dict__.__iter__()

  def __repr__(self):
    return self.__dict__.__repr__()

  def __str__(self):
    return self.__dict__.__str__()
