from ..turing_machine import TuringMachine
from .generic_automaton import GenericAutomaton

class HotelOrderRecognizeAutomaton(GenericAutomaton):

  def __init__(self):
    super().__init__()
  
  @GenericAutomaton.deathstatefunction
  def __QDead (self):
    return 'fail'
  
  @GenericAutomaton.finalstatefunction
  def __Qf (self,turingMachine:TuringMachine):
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
      return self.__QDead()
  
  @GenericAutomaton.initialstatefunction
  def __Q0 (self, turingMachine:TuringMachine):
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
    
  @GenericAutomaton.statefunction
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
    
  @GenericAutomaton.statefunction
  def __Q2 (self, turingMachine:TuringMachine):
    write = ''
    value = turingMachine.Read()

    if value == '__obj__':
      write = '__obj__'
      turingMachine.WriteAndMove(write, +1)
      return self.__Qf(turingMachine)
    
    else:
      return self.__QDead()
    
  

