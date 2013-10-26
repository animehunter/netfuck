import sys
import timeit

class State():
    def __init__(self, code):
        self.cells = [0] * 30000  # expandable cells
        self.cp = 0 # cell pointer
        self.pc = 0 # program counter
        self.jumps = [0] * len(code)
    def incptr(s): s.cp += 1
    def decptr(s): s.cp -= 1
    def add(s): s.cells[s.cp] += 1
    def sub(s): s.cells[s.cp] -= 1
    def output(s): sys.stdout.write(chr(s.cells[s.cp]))
    def input(s): s.cells[s.cp] = ord(sys.stdin.read(1))
    def loopstart(s):
        if not s.cells[s.cp]: s.pc = s.jumps[s.pc]
    def loopend(s):
        if s.cells[s.cp]: s.pc = s.jumps[s.pc]

def interpret(code):
    symbols = set('><+-.,[]')
    code = ''.join(c for c in code if c in symbols)
    codelen = len(code)
    state = State(code)
    stk = []
    for i, c in enumerate(code):
        if c == '[':
            stk.append(i)
        elif c == ']':
            state.jumps[i] = stk.pop() # jump back to the previous matching [
            state.jumps[state.jumps[i]] = i # jump to the next matching ]
    state.jumps = tuple(state.jumps)
    cmds = [None]*127
    cmds[ord('>')] = state.incptr
    cmds[ord('<')] = state.decptr
    cmds[ord('+')] = state.add
    cmds[ord('-')] = state.sub
    cmds[ord('.')] = state.output
    cmds[ord(',')] = state.input
    cmds[ord('[')] = state.loopstart
    cmds[ord(']')] = state.loopend
    funclist = tuple(cmds[ord(c)] for c in code)
    while state.pc != codelen:
        funclist[state.pc]()
        state.pc += 1

def main():
    with open(sys.argv[1]) as f:
        interpret(f.read())

if __name__ == '__main__':
    print(timeit.timeit(main, number=1))

