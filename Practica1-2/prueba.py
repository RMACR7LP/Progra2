# -*- coding: utf-8 -*-
class DFA:
    current_state = None
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state
        return
    
    def transition_to_state_with_input(self, input_value):
        if ((self.current_state, input_value) not in self.transition_function.keys()):
            self.current_state = None
            return
        self.current_state = self.transition_function[(self.current_state, input_value)]
        return
    
    def in_accept_state(self):
        return self.current_state in accept_states
    
    def go_to_initial_state(self):
        self.current_state = self.start_state
        return
    
    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        for inp in input_list:
            self.transition_to_state_with_input(inp)
            continue
        return self.current_state
        return self.in_accept_state()   
        
    pass

    
        


Digitos = ['0','1','2','3','4','5','6','7','8','9']
Migitos = ['-1','-2','-3','4','5','6','7','8','9']
alfabeto =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','ñ','á','é','í','ó','ú','Á','É','Í','Ó','Ú']

states = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16};
alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','ñ','á','é','í','ó','ú','Á','É','Í','Ó','Ú','0','1','2','3','4','5','6','7','8','9'}

tf = dict()
for d in Digitos:
    tf[(0,d)] = 2
    tf[(1,d)] = 2
    tf[(2,d)] = 2
    tf[(3,d)] = 6
    tf[(6,d)] = 6
    tf[(5,d)] = 8
    tf[(8,d)] = 8
    tf[(10,d)] = 13
    tf[(12,d)] = 14
    tf[(13,d)] = 13
    tf[(14,d)] = 14
    tf[(15,d)] = 14
for a in alfabeto:
    tf[(0,a)] = 16
    tf[(16,a)] = 16
tf[(0,'-')] = 1
tf[(2,'.')] = 3
tf[(2, '*')] = 4
tf[(2, '+')] = 5
tf[(2, '-')] = 5
tf[(2,'i')] = 11
tf[(4, '1')] = 7
tf[(6, '*')] = 4
tf[(6, '+')] = 5
tf[(6, '-')] = 5
tf[(7, '0')] = 9
tf[(8,'.')] = 10
tf[(8, 'i')] = 11
tf[(9, '^')] = 12
tf[(12,'-')] = 15
tf[(13,'i')] = 11

start_state = 0
accept_states = { 2, 6, 11, 14, 16}

d = DFA(states, alphabet, tf, start_state, accept_states)

inp_program = list('-2.0987*10^-5')

cadena= 'Alan Mathison Turing, OBE (Paddington, Londres, 23 de junio de 1912-Wilmslow, Cheshire, 7*10^28'
cadena_semi_limpia = cadena.replace(",", " ")
cadena_limpia = cadena_semi_limpia.replace("."," ")            
for i in cadena_limpia.split():
    d.run_with_input_list(list(i))
    if d.run_with_input_list(list(i))==2:
        print 'Entero'
        for i in cadena:
            cadena.replace(str(i),"<font color=red>")
        print cadena
    elif d.run_with_input_list(list(i))==6: 
        print 'Real'
    elif d.run_with_input_list(list(i))==11:
        print 'Complejo'
    elif d.run_with_input_list(list(i))==14:
        print 'Notación Científica'
    elif d.run_with_input_list(list(i))==16:
        print 'palabra'
    else:
        print False

print cadena
