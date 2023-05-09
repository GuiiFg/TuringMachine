from ..turing_machine import TuringMachine

class BinaryComplementAutomaton:

  def __init__(self):
    self.__state = 'Q0'

  @property
  def state (self):
    return self.__state
  
  def Start(self, automaton:TuringMachine):
    return self.__Q0(automaton)
    
  def __Q0 (self, automaton:TuringMachine):
    self.__state = 'Q0'
    write = ''
    value = automaton.Read()

    if value == '1':
      write = '0'
      automaton.WriteAndMove(write, 1)
      return self.__Q0(automaton)
    elif value == '0':
      write = '1'
      automaton.WriteAndMove(write, 1)
      return self.__Q0(automaton)
    elif value == '__empty__':
      write = '__empty__'
      automaton.WriteAndMove(write, -1)
      return self.__Q1(automaton)
    else:
      return 'fail'

  def __Q1 (self, automaton:TuringMachine):
    self.__state = 'Q1'
    write = ''
    value = automaton.Read()

    if value == '1':
      write = '1'
      automaton.WriteAndMove(write, -1)
      return self.__Q1(automaton)
    elif value == '0':
      write = '0'
      automaton.WriteAndMove(write, -1)
      return self.__Q1(automaton)
    elif value == '<':
      automaton.WriteAndMove('<', +1)
      return self.__Qf()
    else:
      return 'fail'

  def __Qf (self):
    self.__state = 'Qf'
    return 'finished'

  

