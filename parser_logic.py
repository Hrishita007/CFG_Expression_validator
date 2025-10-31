import nltk
import re

def load_grammar():
    with open("grammar.cfg") as file:
        grammar = nltk.CFG.fromstring(file.read())
    return grammar


def tokenize(expr):
    # Add spaces around operators and parentheses
    expr = re.sub(r'([\+\-\*/\(\)])', r' \1 ', expr)
    tokens = expr.split()

    # Keep a mapping of identifiers to their real names
    id_map = []
    processed_tokens = []
    for t in tokens:
        if re.match(r'^[a-zA-Z]\w*$', t):  # variable like a, b, abc
            processed_tokens.append('id')
            id_map.append(t)
        else:
            processed_tokens.append(t)
    return processed_tokens, id_map


def parse_expression(expr, grammar):
    tokens, id_map = tokenize(expr)
    parser = nltk.ChartParser(grammar)

    # Empty input case
    if not tokens:
        return False, "Empty expression provided."

    # Check for invalid symbols
    for t in tokens:
        if t not in ['id', '+', '-', '*', '/', '(', ')']:
            return False, f"Invalid symbol '{t}' found."

    try:
        parses = list(parser.parse(tokens))
        if parses:
            tree = parses[0]

            # Replace 'id' leaves with actual variable names
            i = 0
            for pos in tree.treepositions('leaves'):
                if tree[pos] == 'id' and i < len(id_map):
                    tree[pos] = id_map[i]
                    i += 1

            return True, tree
        else:
            # Handle common errors
            if expr.count('(') != expr.count(')'):
                return False, "Unbalanced parentheses detected."
            elif re.search(r'[\+\-\*/]$', expr.strip()):
                return False, "Operator at the end without operand."
            elif re.search(r'^[\+\-\*/]', expr.strip()):
                return False, "Expression cannot start with an operator."
            elif re.search(r'[\+\-\*/]{2,}', expr):
                return False, "Consecutive operators found."
            else:
                return False, "Expression does not follow grammar rules."
    except ValueError as e:
        return False, f"Grammar error: {str(e)}"
    except Exception as e:
        return False, f"Parsing failed: {str(e)}"
