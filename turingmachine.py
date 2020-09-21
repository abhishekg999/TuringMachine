"""
Abhishek Govindarasu
Period 3
Math Modeling

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
"""

class TuringMachine():
    __tapeLength = 10000
    __tape = []
    __datastart = int(__tapeLength/2)

    def __init__(self, Q : set, sigma : set, gamma : set, dunion, start : set, finish : set, delta : dict, tape=[]):
        self.Q = Q
        self.Sigma = sigma
        self.Gamma = gamma
        self.DUnion = dunion
        self.start = start #member of Q
        self.finish = finish #member of Q
        self.delta = delta
        
        if tape:
            self.__tape = [self.DUnion for _ in range(self.__datastart)] + tape + [self.DUnion for _ in range(self.__datastart)]
            self.__tapeLength = len(self.__tape)
        else:
            self.__tape = [self.DUnion for _ in range(self.__tapeLength)]
  
    
    def run(self, debug=False, lb=0, ub=__tapeLength):
        state = self.start
        head = self.__datastart
        
        if debug:
            print(self.showTape(lb, ub))
            
        while state != self.finish:
            res = self.delta[state][self.__tape[head]]
            state = res[0]
            self.__tape[head] = res[1]
            if res[2] == 'L':
                head -= 1
            elif res[2] == 'R':
                head += 1
                
            if debug:
                print(self.showTape(lb, ub))

            
    def showTape(self, lb=0, ub=__tapeLength):
        return self.__tape[lb:ub]
        
    def resetTape(self):
        self.__tapeLength = 10000
        self.__tape = [self.DUnion for _ in range(self.__tapeLength)]
        self.__datastart = int(__tapeLength/2)
        
        
    def __str__(self):
        return "Q : {}\nSigma : {}\nGamma : {}\nBlank : {}\nStart : {}\nFinish : {}\nDelta : {}".format(self.Q, self.Sigma, self.Gamma, self.DUnion, self.start, self.finish, self.delta)
        
    
    

#The console output for individual machines can be found in the comments of their code.
