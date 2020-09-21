"""
Abhishek Govindarasu

This program uses the turing machine code in turingmachine.py
with the specified values of the tuple M() shown below
to solve the busy beaver game.

This is a 3 state turing machine that solves this problem.
The theoretical limit for a 3 state turing machine solution
is 6, which this machine successfully solves. 

The busy beaver game is a computer science problem
to print a finite number of 1's on a tape that is all
zero using a turing machine. The machine must halt
at some point, so it cannot print infinite ones in 
one direction.
"""

from turingmachine import TuringMachine 

if __name__ == '__main__':
    Q = ('A', 'B', 'C', 'H')
    G = (0, 1)
    S = (1)
    B = (0)
    Start = ('A')
    Finish = ('H')
    Delta = {
            'A' : {0 : ['B', 1, 'R'], 1 : ['C', 1, 'L']},
            'B' : {0 : ['A', 1, 'L'], 1 : ['B', 1, 'R']},
            'C' : {0 : ['B', 1, 'L'], 1 : ['H', 1, 'R']} 
            }


    
    M = TuringMachine(Q, S, G, B, Start, Finish, Delta)
    print(M)
    M.run(True, 4990, 5010)


"""
Console Output:

Q : ('A', 'B', 'C', 'H')
Sigma : 1
Gamma : (0, 1)
Blank : 0
Start : A
Finish : H
Delta : {'A': {0: ['B', 1, 'R'], 1: ['C', 1, 'L']}, 'B': {0: ['A', 1, 'L'], 1: ['B', 1, 'R']}, 'C': {0: ['B', 1, 'L'], 1: ['H', 1, 'R']}}
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
"""