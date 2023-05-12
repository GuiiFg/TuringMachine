
import TuringMachine
from TuringMachine.automatons import GenericAutomaton

# Gerando erro por 2 estados iniciais
class MyAutomatonWithError(GenericAutomaton):

  def __init__(self):
    super().__init__()

  @GenericAutomaton.initialstatefunction
  def MyInitialStateFunc(self, mt:TuringMachine.TuringMachine):
    return 'ok'

  @GenericAutomaton.initialandfinalstatefunction
  def teste(self, mt:TuringMachine.TuringMachine):
    return 'ok'