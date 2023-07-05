#PALINDROME

# input_string = input("Enter a string: ")
# reverse = input_string[::-1]
# if reverse == input_string:
#     print(input_string,"is a Palindrome")
# else:
#     print("Not a Palindrome!")

# #DFA
# def process_input(dfa, input_string):
#     current_state = dfa['start_state']
#     for symbol in input_string:
#         if symbol not in dfa['alphabet']:
#             raise ValueError("Invalid symbol in the input string.")
#         if current_state not in dfa['transition'] or symbol not in dfa['transition'][current_state]:
#             return False
#         current_state = dfa['transition'][current_state][symbol]
#     return current_state in dfa['accept_states']


# # Take DFA details as user input
# dfa = {}
# dfa['states'] = input("Enter the states of DFA (comma-separated): ").split(',')
# dfa['alphabet'] = input("Enter the alphabet of DFA (comma-separated): ").split(',')
# dfa['start_state'] = input("Enter the start state of DFA: ")
# dfa['accept_states'] = input("Enter the accepting states of DFA (comma-separated): ").split(',')

# dfa['transition'] = {}
# for state in dfa['states']:
#     dfa['transition'][state] = {}
#     for symbol in dfa['alphabet']:
#         dfa['transition'][state][symbol] = input(f"Enter the next state for transition from {state} on symbol {symbol}: ")

# # Usage example
# input_string = input("Enter an input string: ")
# if process_input(dfa, input_string):
#     print("Accepted")
# else:
#     print("Rejected")

#NFA
# def process_input(nfa, input_string):
#     current_states = nfa['epsilon_closure'](nfa['start_state'])
#     for symbol in input_string:
#         next_states = set()
#         for state in current_states:
#             if state in nfa['transition'] and symbol in nfa['transition'][state]:
#                 next_states.update(nfa['transition'][state][symbol])
#         current_states = set()
#         for state in next_states:
#             current_states.update(nfa['epsilon_closure'](state))
#     return any(state in nfa['accept_states'] for state in current_states)


# def epsilon_closure(nfa, states):
#     closure = set(states)
#     stack = list(states)

#     while stack:
#         state = stack.pop()
#         if state in nfa['transition'] and '' in nfa['transition'][state]:
#             epsilon_states = nfa['transition'][state]['']
#             for epsilon_state in epsilon_states:
#                 if epsilon_state not in closure:
#                     closure.add(epsilon_state)
#                     stack.append(epsilon_state)

#     return closure


# # Take NFA details as user input
# nfa = {}
# nfa['states'] = input("Enter the states of NFA (comma-separated): ").split(',')
# nfa['alphabet'] = input("Enter the alphabet of NFA (comma-separated): ").split(',')
# nfa['start_state'] = input("Enter the start state of NFA: ")
# nfa['accept_states'] = input("Enter the accepting states of NFA (comma-separated): ").split(',')

# nfa['transition'] = {}
# for state in nfa['states']:
#     nfa['transition'][state] = {}
#     for symbol in nfa['alphabet']:
#         next_states = input(f"Enter the next states for transition from {state} on symbol {symbol} (comma-separated): ").split(',')
#         nfa['transition'][state][symbol] = next_states

# epsilon_transitions = {}
# for state in nfa['states']:
#     epsilon_transitions[state] = {}
#     next_states = input(f"Enter the next states for epsilon transitions from {state} (comma-separated): ").split(',')
#     epsilon_transitions[state][''] = next_states

# nfa['epsilon_closure'] = lambda states: epsilon_closure(nfa, states)


# # Usage example
# input_string = input("Enter an input string: ")
# if process_input(nfa, input_string):
#     print("Accepted")
# else:
#     print("Rejected")






#NFA TO DFA
# def epsilon_closure(states, epsilon_transitions):
#     closure = set(states)
#     stack = list(states)
    
#     while stack:
#         state = stack.pop()
        
#         if state in epsilon_transitions:
#             epsilon_states = epsilon_transitions[state]
#             for epsilon_state in epsilon_states:
#                 if epsilon_state not in closure:
#                     closure.add(epsilon_state)
#                     stack.append(epsilon_state)
    
#     return closure


# def move(states, symbol, transitions):
#     move_states = set()
    
#     for state in states:
#         if state in transitions and symbol in transitions[state]:
#             move_states.update(transitions[state][symbol])
    
#     return move_states


# def nfa_to_dfa(nfa_states, nfa_alphabet, nfa_start_state, nfa_accepting_states, nfa_transitions, nfa_epsilon_transitions):
#     dfa_states = []
#     dfa_alphabet = nfa_alphabet
#     dfa_start_state = frozenset(epsilon_closure({nfa_start_state}, nfa_epsilon_transitions))
#     dfa_accepting_states = []
#     dfa_transitions = {}
#     queue = [dfa_start_state]
#     visited = {dfa_start_state}
    
#     while queue:
#         current_state = queue.pop(0)
#         dfa_states.append(current_state)
        
#         if any(state in nfa_accepting_states for state in current_state):
#             dfa_accepting_states.append(current_state)
        
#         for symbol in dfa_alphabet:
#             next_states = move(current_state, symbol, nfa_transitions)
#             next_states = frozenset(epsilon_closure(next_states, nfa_epsilon_transitions))
            
#             if next_states:
#                 dfa_transitions.setdefault(current_state, {})[symbol] = next_states
                
#                 if next_states not in visited:
#                     visited.add(next_states)
#                     queue.append(next_states)
    
#     return dfa_states, dfa_alphabet, dfa_start_state, dfa_accepting_states, dfa_transitions


# # Example NFA parameters
# nfa_states = {'q0', 'q1', 'q2'}
# nfa_alphabet = {'0', '1'}
# nfa_start_state = 'q0'
# nfa_accepting_states = {'q2'}
# nfa_transitions = {
#     'q0': {'0': {'q0'}, '1': {'q1'}},
#     'q1': {'0': set(), '1': set()},
#     'q2': {'0': {'q2'}, '1': {'q2'}}
# }
# nfa_epsilon_transitions = {
#     'q0': {'q1'},
#     'q2': {'q0'}
# }

# # Convert NFA to DFA
# dfa_states, dfa_alphabet, dfa_start_state, dfa_accepting_states, dfa_transitions = nfa_to_dfa(
#     nfa_states, nfa_alphabet, nfa_start_state, nfa_accepting_states, nfa_transitions, nfa_epsilon_transitions
# )

# # Print the resulting DFA
# print("DFA States:", dfa_states)
# print("DFA Alphabet:", dfa_alphabet)
# print("DFA Start State:", dfa_start_state)
# print("DFA Accepting States:", dfa_accepting_states)
# print("DFA Transitions:")
# for state, transitions in dfa_transitions.items():
#     for symbol, next_states in transitions.items():
#         print(state, "--", symbol, "-->", next_states)

# #Pattern Searching
# def compute_transition_table(pattern, alphabet):
#     m = len(pattern)
#     transition_table = [[0] * len(alphabet) for _ in range(m + 1)]
    
#     for state in range(m + 1):
#         for symbol in alphabet:
#             k = min(m + 1, state + 2)
#             while k > 0:
#                 k -= 1
#                 if pattern[:k] == pattern[state - k + 1:state] + symbol:
#                     break
#             transition_table[state][alphabet.index(symbol)] = k
    
#     return transition_table


# def search_pattern(text, pattern):
#     alphabet = list(set(text))
#     transition_table = compute_transition_table(pattern, alphabet)
#     n = len(text)
#     m = len(pattern)
#     state = 0
    
#     for i in range(n):
#         state = transition_table[state][alphabet.index(text[i])]
#         if state == m:
#             print("Pattern found at index", i - m + 1)
    
#     if state != m:
#         print("Pattern not found in the text")


# # Example usage
# text = "ABABDABACDABABCABAB"
# pattern = "ABABCABAB"
# print(text)
# print("pattern to find: ",pattern)
# search_pattern(text, pattern)












