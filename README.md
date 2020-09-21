# TuringMachine
a simple, functional turing machine implementation in python, with examples.

BinAddition performs binary addition of 2 strings with a 6 state turing machine.
BinReverse reverses a binary string with a 1 state turing machine.
BusyBeaver solves the busy beaver game with a 3 state turing machine.

To use:

from turingmachine import TuringMachine
M = TuringMachine(Q, Sigma, Gamma, Blank, Start, Finish, Delta, tape=[])
The tape by default is at length 10000 with head starting at index 5000.

If a default input tape is used then the tape will be 10000 + length(input) 
but head will remain at 5000.

to run:
M.run()

M.showTape(lowerbound, upperbound) will print a section of tape.
For all examples the range 5000 += [5,10] is used however more can be used.


