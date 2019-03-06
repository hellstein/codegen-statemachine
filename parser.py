import json
from jinja2 import Environment, Template, FileSystemLoader
class Parser:
    """
    parse the state, transition and init configuration
    """
    def __init__(self, stateConf, initConf):
        self.stateConf, self.initConf = stateConf, initConf
        self.statenames, self.transitions = [], []
        self.initstate, self.initaction = '', ''
        self.parse()

    def parse(self):
        content = {}
        with open(self.stateConf, 'r') as f:
            data = json.load(f)
            self.statenames = list(data.keys())
            self.transitions = list(set([x for y in [d['transitions'].keys() for s, d in data.items()] for x in y]))
            self.info = data

        with open(self.initConf, 'r') as f:
            data = json.load(f)
            self.initstate, self.initaction = data['state'], data['action']
        self.statenames.remove(self.initstate)
        self.statenames.insert(0, self.initstate)

    def genStatesCode(self):
        """
        Generate code file according to self.content
        codeinfo = {
            '<filename>': '<code>',
        }
        """
        env = Environment(
            loader=FileSystemLoader(searchpath='./templates')
        )
        substate_tmpl = env.get_template('state_tmpl.py')
        transition_none_tmpl = env.get_template('transition_none.py')
        transition_ok_tmpl = env.get_template('transition_ok.py')
        state_tmpl = env.get_template('state.py')
        stateinfo_tmpl = env.get_template('state_info.py')
        codeinfo = {}
        for s, d in self.info.items():
            trans_code = []
            for t in self.transitions:
                if t in d['transitions'].keys():
                    trans_code.append(transition_ok_tmpl.render(transition=t, post=d['transitions'][t]))
                else:
                    trans_code.append(transition_none_tmpl.render(transition=t))
            codeinfo[s.lower()+".py"] = substate_tmpl.render(state=s.title(), description=d['description']) + '\n' + '\n'.join(trans_code) + '\n'

        trans_code = []
        for t in self.transitions:
            trans_code.append(transition_none_tmpl.render(transition=t))
        stateinfo = '\n'.join([stateinfo_tmpl.render(state=s, index=i) for i, s in enumerate(self.statenames)]) + '\n'
        codeinfo['state.py'] = state_tmpl.render(stateinfo=stateinfo) + '\n' + '\n'.join(trans_code) + '\n' 
        return codeinfo

    def genContextCode(self):
        """
        Generate code file according to self.states, self.initstate, self.initaction
        """
        env = Environment(
            loader=FileSystemLoader(searchpath='./templates')
        )
        ctx_tmpl = env.get_template('context.py')
        import_tmpl = env.get_template('import.py')

        states_code = '['+', '.join([s.title()+'()' for s in self.statenames])+']'
        
        importinfo = '\n'.join([import_tmpl.render(pkg=s.lower(), api=s.title()) for s in self.statenames])
        return ctx_tmpl.render({"states": states_code, "initaction": self.initaction, "importinfo": importinfo})
