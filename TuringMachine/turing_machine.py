class TuringMachine:
    
  def __init__(self):
    self.__coil = ['<', None]
    self.__pointer = 1
    self.__automatons = {}

  @property
  def isInInit (self):
    return self.__pointer == 1
  
  @property
  def automatons (self):
    return self.__automatons
  
  @property
  def pointer (self):
    return self.__pointer
  
  @pointer.setter
  def pointer (self, value):
    self.__pointer = value

  @property
  def coil (self):
    return self.__coil
  
  @coil.setter
  def coil (self, value):
    self.__coil = value
  
  def run (self, automatonName):
    if automatonName in self.__automatons.keys():
      automaton = self.__automatons[automatonName]
      automaton.Start(self)

  def Read(self):
    if self.__pointer + 1 > len(self.__coil):
      self.__coil.append(None)
      return None
    else:
      return self.__coil[self.__pointer]
  
  def Write(self, value):
    if value != '__empty__':
      self.__coil[self.__pointer] = value

  def WriteAndMove(self, valueToWrite, movement):
    if self.__pointer + 1 > len(self.__coil):
      self.__coil.append(valueToWrite)
    else:
      self.__coil[self.__pointer] = valueToWrite
    self.__pointer += movement