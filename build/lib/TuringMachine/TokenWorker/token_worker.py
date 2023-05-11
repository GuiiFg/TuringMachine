class TokenWorker: 
  
  def __init__(self, dicionary:dict = None, input:object = None) :
    self.__tokenslist = []
    self.__objectslist = []
    self.__input = input
    self.__dicionary:dict = dicionary

    if self.__input != None and type(self.__input) == str:
      self.__input = self.__input.upper()
      self.GenerateTokensWithPhrase(self.__input)

  @property
  def dicionary (self):
    return self.__dicionary
  
  @dicionary.setter
  def dicionary (self, value):
    self.__dicionary =  value

  @property
  def tokenslist (self):
    return self.__tokenslist
  
  @tokenslist.setter
  def tokenslist (self, value):
    self.__tokenslist =  value

  @property
  def objectslist (self):
    return self.__objectslist
  
  @objectslist.setter
  def objectslist (self, value):
    self.__objectslist =  value
  
  def GenerateTokensWithPhrase(self, phrase):
    phrase = phrase.upper()

    self.__input = phrase

    self.__objectslist = phrase.lstrip().split(' ')

    for i in self.__objectslist:
      self.__tokenslist.append(self.GetTypeOfValue(i))

    return self.__tokenslist

  def GetTypeOfValue (self, value):
    finalKey = None
    for key in list(self.__dicionary.keys()):
      if value in [(x if type(x) != str else x.upper()) for x in self.__dicionary[key]]:
        finalKey = key
        break

    return finalKey
