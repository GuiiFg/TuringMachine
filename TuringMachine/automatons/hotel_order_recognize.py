from ..turing_machine import TuringMachine

class HotelOrderRecognizeAutomaton:

  def __init__(self):
    self.__state = 'Q0'

  @property
  def state (self):
    return self.__state
  
  def Start (self, turingMachine:TuringMachine):
    return self.__Q0(turingMachine)
  
  def __QDead (self):
    self.__state = 'QDead'
    return 'fail'
  
  def __Qf (self,turingMachine:TuringMachine):
    self.__state = 'Qf'
    write = ''
    value = turingMachine.Read()

    if value != '<':
      write = value
      turingMachine.WriteAndMove(write, -1)
    elif value == '<':
      write = value
      turingMachine.WriteAndMove(write, +1)
      return 'success'
    else:
      return 'fail'
  
  def __Q0 (self, turingMachine:TuringMachine):
    self.__state = 'Q0'
    write = ''
    value = turingMachine.Read()

    if value == '__suj__':
      write = '__suj__'
      turingMachine.WriteAndMove(write, +1)
      return self.__Q0(turingMachine)
    
    elif value == '__verb__':
      write = '__verb__'
      turingMachine.WriteAndMove(write, +1)
      return self.__Q1(turingMachine)
    
    else:
      return self.__QDead()
    
  def __Q1 (self, turingMachine:TuringMachine):
    self.__state = 'Q1'
    write = ''
    value = turingMachine.Read()

    if value == '__verb__':
      write = '__verb__'
      turingMachine.WriteAndMove(write, +1)
      return self.__Q1(turingMachine)
    
    elif value == '__pron__':
      write = '__pron__'
      turingMachine.WriteAndMove(write, +1)
      return self.__Q2(turingMachine)
    
    elif value == '__obj__':
      write = '__obj__'
      turingMachine.WriteAndMove(write, +1)
      return self.__Qf(turingMachine)
    
    else:
      return self.__QDead()
    
  def __Q2 (self, turingMachine:TuringMachine):
    self.__state = 'Q2'
    write = ''
    value = turingMachine.Read()

    if value == '__obj__':
      write = '__obj__'
      turingMachine.WriteAndMove(write, +1)
      return self.__Qf(turingMachine)
    
    else:
      return self.__QDead()
    
  

