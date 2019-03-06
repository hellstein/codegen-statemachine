import os
class Writer:
    """
    Write parser result into python file
    """
    def __init__(self, directory):
        self.directory = directory
        os.mkdir(self.directory)

    def createStates(self, content):
        """
        Generate xxx_state.py
        """
        for fname, code in content.items():
            with open(os.path.join(self.directory, fname), 'w') as f:
                f.write(code)

    def createContext(self, content):
        """
        Write init info into context.py
        """
        with open(os.path.join(self.directory, 'context.py'), 'w') as f:
            f.write(content)
