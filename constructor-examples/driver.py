from pda_constructor import *

# constructing pda for correct bracket sequences

automata = pda()
automata.add_state(state('q', first=True, final=True))
automata.add_rule('q', 'q', '(', '(')
automata.add_rule('q', 'q', ')', ')', 'NULL', "That's the comment")
automata.add_rule('q', 'q', stack_taken='S', stack_placed='(S)S')
automata.add_rule('q', 'q', stack_taken='S')
automata.print_grammar()
automata.print_grammar("ex1")

# other features demonstration

# automata.leave_comment("Another very important comment.", 'q', 'q', stack_taken='S')
# automata.print_grammar()

# automata.add_state(state('r'))
# automata.add_rule('q', 'r', '(', ')')
# automata.print_grammar()
# automata.delete_state(state('r'))
# automata.print_grammar()

# automata.delete_rule('q', 'q', ')', ')')
# automata.print_grammar()
