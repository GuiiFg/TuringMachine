from ..turing_machine import TuringMachine

class BinaryComplementAutomaton:

  def __init__(self):
    self.__state = 'Q0'

  @property
  def state (self):
    return self.__state
  
  def Start(self, turingMachine:TuringMachine):
    return self.__Q0(turingMachine)
    
  def __Q0 (self, turingMachine:TuringMachine):
    self.__state = 'Q0'
    write = ''
    value = turingMachine.Read()

    if value == '1':
      write = '0'
      turingMachine.WriteAndMove(write, 1)
      return self.__Q0(turingMachine)
    elif value == '0':
      write = '1'
      turingMachine.WriteAndMove(write, 1)
      return self.__Q0(turingMachine)
    elif value == '__empty__':
      write = '__empty__'
      turingMachine.WriteAndMove(write, -1)
      return self.__Q1(turingMachine)
    else:
      self.__state = 'QDead'

  def __Q1 (self, turingMachine:TuringMachine):
    self.__state = 'Q1'
    write = ''
    value = turingMachine.Read()

    if value == '1':
      write = '1'
      turingMachine.WriteAndMove(write, -1)
      return self.__Q1(turingMachine)
    elif value == '0':
      write = '0'
      turingMachine.WriteAndMove(write, -1)
      return self.__Q1(turingMachine)
    elif value == '<':
      turingMachine.WriteAndMove('<', +1)
      return self.__Qf()
    else:
      return self.__QDead()
    
  def __QDead (self):
    self.__state = 'QDead'
    return 'fail'

  def __Qf (self):
    self.__state = 'Qf'
    return 'finished'

  

