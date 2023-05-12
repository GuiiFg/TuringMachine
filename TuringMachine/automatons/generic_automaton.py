from ..turing_machine import TuringMachine
import inspect

class GenericAutomaton:

  def __init__(self):
    self.__state = None
    self.__isDeadState = None
    self.__isFinalState = None
    self.__isInitialState = None

  @property
  def state (self):
    return self.__state
  
  @property
  def isInitialState (self):
    return self.__isInitialState
  
  @property
  def isFinalState (self):
    return self.__isFinalState
  
  @property
  def isDeadState (self):
    return self.__isDeadState

  def statefunction (function):
    def __wrapper (*arg, **kwargs):
      arg[0].__isDeadState = False
      arg[0].__isFinalState = False
      arg[0].__isInitialState = False
      arg[0].__state = function.__name__[2:] if function.__name__[:2] == '__' else function.__name__
      arg[0].__state = arg[0].__state if function.__name__[:1] == '_' else arg[0].__state
      function(*arg, **kwargs)
    return __wrapper
  
  def initialstatefunction (function):
    def __wrapper (*arg, **kwargs):
      arg[0].__isDeadState = False
      arg[0].__isFinalState = False
      arg[0].__isInitialState = True
      arg[0].__state = function.__name__[2:] if function.__name__[:2] == '__' else function.__name__
      arg[0].__state = arg[0].__state if function.__name__[:1] == '_' else arg[0].__state
      function(*arg, **kwargs)
    return __wrapper
  
  def initialandfinalstatefunction (function):
    def __wrapper (*arg, **kwargs):
      arg[0].__isDeadState = False
      arg[0].__isFinalState = True
      arg[0].__isInitialState = True
      arg[0].__state = function.__name__[2:] if function.__name__[:2] == '__' else function.__name__
      arg[0].__state = arg[0].__state if function.__name__[:1] == '_' else arg[0].__state
      function(*arg, **kwargs)
    return __wrapper
  
  def deathstatefunction (function):
    def __wrapper (*arg, **kwargs):
      arg[0].__isDeadState = True
      arg[0].__isFinalState = False
      arg[0].__isInitialState = False
      arg[0].__state = function.__name__[2:] if function.__name__[:2] == '__' else function.__name__
      arg[0].__state = arg[0].__state if function.__name__[:1] == '_' else arg[0].__state
      function(*arg, **kwargs)
    return __wrapper
  
  def finalstatefunction (function):
    def __wrapper (*arg, **kwargs):
      arg[0].__isDeadState = False
      arg[0].__isFinalState = True
      arg[0].__isInitialState = False
      arg[0].__state = function.__name__[2:] if function.__name__[:2] == '__' else function.__name__
      arg[0].__state = arg[0].__state if function.__name__[:1] == '_' else arg[0].__state
      function(*arg, **kwargs)
    return __wrapper
  
  def __getInitalState(self):
    initialFuncs = list(self.__getInitalStateName())
    if len(initialFuncs) > 1:
      raise ValueError('The automaton need have only one inital state!')
    return initialFuncs[0]
  
  def __getInitalStateName(self):
    sourcelines = inspect.getsourcelines(self.__class__)[0]
    for i,line in enumerate(sourcelines):
      line = line.strip()
      if line.split('(')[0].strip() in ['@GenericAutomaton.initialstatefunction', '@GenericAutomaton.initialandfinalstatefunction']:
        nextLine = sourcelines[i+1]
        name = nextLine.split('def')[1].split('(')[0].strip()
        yield(name)

  def Start (self, turingMachine:TuringMachine):
    
    initFunc = self.__getInitStateMethod()
    initFunc(self, turingMachine)

  def __getInitStateMethod (self):
    initialStateMethodName = '_' + self.__class__.__name__ + self.__getInitalState()
    func = None
    for x in inspect.getmembers(self.__class__, predicate=inspect.isfunction):
      if x[0] == initialStateMethodName:
        func = x[1]

    return func