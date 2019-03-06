from parser import Parser
from writer import Writer
import argparse


class CLI:
    def __init__(self):
        self.cli = argparse.ArgumentParser()
        self.cli.add_argument('--states', dest='states')
#        self.cli.add_argument('--transitions', dest='transitions')
        self.cli.add_argument('--init', dest='init')

if __name__ == "__main__":
    cli = CLI().cli
    cfgfiles = vars(cli.parse_args())
#    stateConf, transitionConf, initConf = cfgfiles["states"], cfgfiles["transitions"], cfgfiles["init"]
#    parser = Parser(stateConf, transitionConf, initConf)
    stateConf, initConf = cfgfiles["states"], cfgfiles["init"]
    parser = Parser(stateConf, initConf)
    ctx_code = parser.genContextCode()
    states_code = parser.genStatesCode()
    w = Writer('dist')
    w.createStates(states_code)
    w.createContext(ctx_code)
