import TuringMachine

def BinaryComplementTest():
  fitasDeTeste = [
    ['<', 1, 0, 1],
    ['<', 0, 1, 1],
    ['<', 1, 0, 1, 0, 1, 0],
    ['<', 0, 0, 1, 1, 1],
  ]

  fitasDeResultado = [
    ['<', 0, 1, 0],
    ['<', 1, 0, 0],
    ['<', 0, 1, 0, 1, 0, 1],
    ['<', 1, 1, 0, 0, 0],
  ]

  for i in range(len(fitasDeTeste)):
    turing_machine = TuringMachine.TuringMachine()
    turing_machine.coil = fitasDeTeste[i]

    turing_machine.automatons['BinaryComplement'] = TuringMachine.Automatons.BinaryComplementAutomaton()

    turing_machine.run('BinaryComplement')

    if turing_machine.automatons['BinaryComplement'].isFinalState:
      print(f'Test {i + 1} - Success!')
    else:
      print(f'Test {i + 1} - Error!')

BinaryComplementTest()
# 
# import TuringMachine
# 
# turing_machine = TuringMachine.TuringMachine()
# turing_machine.coil = ['<', 1, 0, 1]
# 
# turing_machine.automatons['BinaryComplement'] = TuringMachine.Automatons.BinaryComplementAutomaton()
# turing_machine.automatons['BinaryFourMultiply'] = TuringMachine.Automatons.BinaryMultiplyFourAutomaton()
# 
# turing_machine.toDict()
# 
# turing_machine.run('BinaryComplement')
# turing_machine.run('BinaryFourMultiply')

import TuringMachine

myMachine = TuringMachine.TuringMachine()

myMachine.coil = [1,2,3]
print(myMachine.coil)

myMachine.coil = []
print(myMachine.coil)