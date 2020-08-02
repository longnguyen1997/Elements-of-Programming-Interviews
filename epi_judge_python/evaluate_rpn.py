from test_framework import generic_test


ops = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b
}


def evaluate(expression: str) -> int:
    op_stack = []  # Stack.
    for exp in expression.split(','):
        if exp not in '+-*/':
            op_stack.append(int(exp))
        else:
            b = op_stack.pop()
            a = op_stack.pop()
            op_stack.append(ops[exp](a, b))
    return op_stack[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
