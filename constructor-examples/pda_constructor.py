class state:

    def __init__(self, name, first=False, receiving=False, final=False):
        self.classification = [first, receiving, final]
        self.name = name
        self.rules = []


class pda:

    def __init__(self):
        self.input_alphabet = []
        self.states = []
        self.stack_alphabet = []

    def add_state(self, state_: state):
        self.states.append(state_)

    def add_rule(self, from_state_name, to_state_name, alpha_taken="EPS", stack_taken="NULL", stack_placed="NULL"):
        for state_ in self.states:
            if state_.name == from_state_name:
                state_.rules.append((to_state_name, alpha_taken, stack_taken, stack_placed))
                self.input_alphabet = list(set(self.input_alphabet + [alpha_taken]))
                self.stack_alphabet = list(set(self.stack_alphabet + [stack_taken] + [stack_placed]))
                for state__ in self.states:
                    if state__.name == to_state_name:
                        state__.classification[1] = True
                        return

    def delete_state(self, state_):
        self.states = [state__ for state__ in self.states if state__.name != state_.name]
        for state__ in self.states:
            state__.rules = [rule for rule in state__.rules if rule[0] != state_.name]

    def delete_rule(self, from_state_name, to_state_name, alpha_taken="EPS", stack_taken="NULL", stack_placed="NULL"):
        for state_ in self.states:
            if state_.name == from_state_name:
                state_.rules = [rule for rule in state_.rules if
                                rule != (to_state_name, alpha_taken, stack_taken, stack_placed)]

    def print_grammar(self, filename=None):
        if filename is not None:
            outfile = open(filename + ".in", "w")
        else:
            outfile = None

        for state_ in self.states:
            print('"' + str(state_.name) + '"', end=' ', file=outfile)
        print(',', file=outfile)

        for state_ in self.states:
            if state_.classification[0]:
                print('"' + str(state_.name) + '"', end=' ', file=outfile)
        print(',', file=outfile)

        for state_ in self.states:
            if state_.classification[1]:
                print('"' + str(state_.name) + '"', end=' ', file=outfile)
        print(',', file=outfile)

        for state_ in self.states:
            if state_.classification[2]:
                print('"' + str(state_.name) + '"', end=' ', file=outfile)
        print(',', file=outfile)

        for alpha in self.input_alphabet:
            if alpha != 'EPS':
                print("'" + str(alpha) + "'", end=' ', file=outfile)
        print(',', file=outfile)

        unnecessary = ['NULL', 'EMPTY']
        for alpha1 in self.stack_alphabet:
            for alpha2 in self.stack_alphabet:
                if alpha2 != alpha1 and alpha2 in alpha1 and alpha1 != 'NULL' and alpha1 != 'EMPTY' \
                        and alpha2 != 'NULL' and alpha2 != 'EMPTY':
                    unnecessary.append(alpha1)
        for alpha in self.stack_alphabet:
            if alpha not in unnecessary:
                print("`" + str(alpha) + "`", end=' ', file=outfile)

        for state_ in self.states:
            for rule in state_.rules:
                print(',', file=outfile)
                print('"' + str(state_.name) + '"', end=' ', file=outfile)

                if rule[1] != 'EPS':
                    print("'" + str(rule[1]) + "'", end=' ', file=outfile)
                else:
                    print("EPS", end=' ', file=outfile)

                if rule[2] == 'NULL':
                    print("NULL", end=' ', file=outfile)
                elif rule[2] == 'EMPTY':
                    print("EMPTY", end=' ', file=outfile)
                else:
                    print("`" + str(rule[2]) + "`", end=' ', file=outfile)

                print("~", end=' ', file=outfile)
                print('"' + str(rule[0]) + '"', end=' ', file=outfile)

                if rule[3] == 'NULL':
                    print("NULL", end=' ', file=outfile)
                elif rule[3] == 'EMPTY':
                    print("EMPTY", end=' ', file=outfile)
                else:
                    print("`" + str(rule[3]) + "`", end=' ', file=outfile)

        print('\n', file=outfile)
