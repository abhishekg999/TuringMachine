"""
Abhishek Govindarasu

This program uses the turing machine code in turingmachine.py
with the specified values of the tuple M() shown below
to reverse a binary number.

This is a very simple 1 state turing machine, that reverses
a binary number, for example 1001 becomes 0110. The input
is already going to be on the tape.
"""

from turingmachine import TuringMachine

if __name__ == "__main__":
    Q = ('A','H')
    G = (0, 1, " ")
    S = (1)
    B = (" ")
    Start = ('A')
    Finish = ('H')
    Delta = {
            'A' : {0 : ['A', 1, 'R'], 1 : ['A', 0, 'R'], B : ['H', B, 'N']},
            }


    M = TuringMachine(Q, S, G, B, Start, Finish, Delta, [1,1,0,1,1,0])
    print(M)

    print(M.showTape(4990, 5010))
    M.run()
    print(M.showTape(4990, 5010))
    
    print(M.getRes())

"""
Console Output:

Q : ('A', 'H')
Sigma : 1
Gamma : (0, 1, ' ')
Blank :  
Start : A
Finish : H
Delta : {'A': {0: ['A', 1, 'R'], 1: ['A', 0, 'R'], ' ': ['H', ' ', 'N']}}
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 1, 1, 0, 1, 1, 0, ' ', ' ', ' ', ' ']
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 0, 0, 1, 0, 0, 1, ' ', ' ', ' ', ' ']
"""