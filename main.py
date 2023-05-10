import TuringMachine

def BinaryComplementTest():
  fitasDeTeste = [
    ['<', '1', '0', '1'],
    ['<', '0', '1', '1'],
    ['<', '1', '0', '1', '0', '1', '0'],
    ['<', '0', '0', '1', '1', '1'],
  ]

  fitasDeResultado = [
    ['<', '0', '1', '0'],
    ['<', '1', '0', '0'],
    ['<', '0', '1', '0', '1', '0', '1'],
    ['<', '1', '1', '0', '0', '0'],
  ]

  for i in range(len(fitasDeTeste)):
    automaton = TuringMachine.BinaryComplementAutomaton()

    turing_machine = TuringMachine.TuringMachine()
    turing_machine.coil = fitasDeTeste[i]

    automaton.Start(turing_machine)

    if automaton.isFinalState:
      print(f'Test {i + 1} - Success!')
    else:
      print(f'Test {i + 1} - Error!')

BinaryComplementTest()
