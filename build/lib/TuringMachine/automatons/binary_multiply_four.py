from ..turing_machine import TuringMachine
from .generic_automaton import GenericAutomaton

class BinaryMultiplyFourAutomaton(GenericAutomaton):
    
  def __init__(self):
    super().__init__()

  @GenericAutomaton.deathstatefunction
  def __QDead (self):
    return False
  
  @GenericAutomaton.finalstatefunction
  def __Qf (self):
    return True
  
  @GenericAutomaton.initialstatefunction
  def __Q1 (self, turingMachine:TuringMachine):

    value = turingMachine.Read()

    if value == 1:
      turingMachine.WriteAndMove(1, 1)
      return self.__Q1(turingMachine)
    elif value == 0:
      turingMachine.WriteAndMove(0, 1)
      return self.__Q1(turingMachine)
    elif value == None:
      turingMachine.WriteAndMove(0, 1)
      return self.__Q2(turingMachine)
    else:
      return self.__QDead()
    
  @GenericAutomaton.statefunction
  def __Q2 (self, turingMachine:TuringMachine):

    value = turingMachine.Read()

    if value == None:
      turingMachine.WriteAndMove(0,-1)
      return self.__Q3(turingMachine)
    else:
      return self.__QDead()
    
  @GenericAutomaton.statefunction
  def __Q3 (self, turingMachine:TuringMachine):

    value = turingMachine.Read()

    if value == 0:
      turingMachine.WriteAndMove(0, -1)
    elif value == 1:
      turingMachine.WriteAndMove(1, -1)
    elif value == '<':
      turingMachine.WriteAndMove('<', 1)
      return self.__Qf()
    else:
      return self.__QDead()



  
  