from ..turing_machine import TuringMachine
from .generic_automaton import GenericAutomaton

class BinaryComplementAutomaton(GenericAutomaton):

  def __init__(self):
    super().__init__()
  
  @GenericAutomaton.initialstatefunction
  def __Q0 (self, turingMachine:TuringMachine):
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
      return self.__QDead()

  @GenericAutomaton.statefunction
  def __Q1 (self, turingMachine:TuringMachine):
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
  
  @GenericAutomaton.deathstatefunction
  def __QDead (self):
    return 'fail'

  @GenericAutomaton.finalstatefunction
  def __Qf (self):
    return 'finished'

  

