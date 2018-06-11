class MyClass:

  def g(self):
    return 'hello world'

class OtherClass(MyClass):
  def __init__(self, iterable):
    self.items_list = []
    self.__update(iterable)

  def update(self, iterable):
    for item in iterable
      self.items_list.append(item)

  __update = update

class Mapping:
  def __init__(self, iterable):
    self.items_list = []
    self.__update(iterable)

  def update(self, keys, values):
    for item in zip(keys, values):
      self.items_list.append(item)
  
  __update = update #private copy of update

class MappingSubclass(Mapping):
  def update(self, keys, values):
    for item in zip(keys, values):
      self.items_list.append(item)


class Employee:
  pass

john = Employee()
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

class Reverse:
  def __init__(self, data):
    self.data = data
    self.index = len(data)

  def __iter__(self):
    return self

  def __next__(self):
    if self.index == 0:
      raise StopIteration
    self.index = self.index - 1
    return self.data[self.index]