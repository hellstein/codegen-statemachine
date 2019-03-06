{{ import_code }}
class Context:
    def __init__(self):
        self.states = {{ states }} 
        self.current = self.states[0] 

    def setState(self, index):
        self.current = self.states[index]

{{ transition_code }}

if __name__ == "__main__":
    cxt = Context()
    cxt.{{ initaction }}()

