
class TuringMachine:
    
  def __init__(self):
    self.__coil = ['<']
    self.__pointer = 1

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
  

  def Read(self):
    if self.__pointer + 1 > len(self.__coil):
      return '__empty__'
    else:
      return self.__coil[self.__pointer]
  
  def Write(self, value):
    if value != '__empty__':
      self.__coil[self.__pointer] = value

  def WriteAndMove(self, valueToWrite, movement):
    if valueToWrite != '__empty__':
      self.__coil[self.__pointer] = valueToWrite
    self.__pointer += movement