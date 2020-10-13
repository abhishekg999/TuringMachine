# TuringMachine | Abhishek

This is a simple simulation of a turing machine. This is an exact recreation
of the mathematical concepts and simplicity of a turing machine. This 
code can simulate any turing machine, by changing the values in the 
main function. Not all values are necessary to change, but the main 
necessary changes is the delta function, blank, and the start and finish 
values. 

The first program solves the busy beaver problem. This is a problem
to write the maximum amount of consecutive 1's in a program while
ensuring the program halts. For a 3 state turing machine, the max
amount of 1's is 6, and this code shows this.

The second program reverses a binary string. For example the string
100101, becomes 011010. 

The third program implements this machine in a more
complex example. It is a 6 state turing machine that performs
addition.

An actual turing machine uses theoretically infinite tape, however
this uses tape of size 10000 + any possible input existing tape. 

Do view the other files and see the results of their outputs in
the comments at the bottom of the files.



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


#You can click on the individual files to see the console output.
