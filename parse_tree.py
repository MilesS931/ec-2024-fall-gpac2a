# Copilot helped with code
# I do not know python yet

import random
import operator

class ParseTree:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def evaluate(self, state):

        if isinstance(self.value, (int, float)):
            return self.value

        # Assume the state contains all terminal values in its dictionary.
        if self.value in state:
            return state[self.value]

        # Define a mapping of operation strings to functions
        operations = { 
            '+': operator.add, 
            '-': operator.sub, 
            '*': operator.mul, 
            '/': lambda x, y: x / y if y != 0 else float('inf'), 
            'RAND': lambda x, y: random.uniform(x, y) 
        }

        # Evaluate the children recursively
        left_val = self.left.evaluate(state) if self.left else 0
        right_val = self.right.evaluate(state) if self.right else 0

        # Apply the operation
        if self.value in operations:
            return operations[self.value](left_val, right_val) 
        return 0

    @classmethod
    def full(cls, depth, terminals, nonterminals, max_depth):
        if depth == max_depth:
            terminal_value = random.choice(terminals)
            if terminal_value == 'C': # Check for terminal 'C'
                return cls.terminalC()
            return ParseTree(value=terminal_value)
        else:
            nonterminal_value = random.choice(nonterminals)
            left_child = cls.full(depth + 1, terminals, nonterminals, max_depth)
            right_child = cls.full(depth + 1, terminals, nonterminals, max_depth)
            return ParseTree(value=nonterminal_value, left=left_child, right=right_child)

    @classmethod 
    def grow(cls, depth, terminals, nonterminals, max_depth):
        if depth == max_depth or (depth > 0 and random.choice([True, False])):
            terminal_value = random.choice(terminals) 
            if terminal_value == 'C': # Check for terminal 'C'
                return cls.terminalC()
            return ParseTree(value=terminal_value)
        else: 
            nonterminal_value = random.choice(nonterminals) 
            left_child = cls.grow(depth + 1, terminals, nonterminals, max_depth) 
            right_child = cls.grow(depth + 1, terminals, nonterminals, max_depth) 
            return ParseTree(value=nonterminal_value, left=left_child, right=right_child) 
            
    @classmethod
    def terminalC(cls):
        terminal_value = random.uniform(-10, 10)
        return ParseTree(value=terminal_value)