class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def is_balanced(symbols):
    stack = Stack()

    for symbol in symbols:
        if symbol in "([{":
            stack.push(symbol)
        else:
            if stack.is_empty():
                return "Несбалансированно"
            else:
                top = stack.pop()
                if (symbol == ")" and top != "(") or \
                   (symbol == "]" and top != "[") or \
                   (symbol == "}" and top != "{"):
                    return "Несбалансированно"

    if stack.is_empty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"

if __name__ == '__main__':
    string_1 = '(((([{}]))))'
    string_2 = '[([])((([[[]]])))]{()}'
    string_3 = '{{[()]}}'
    string_4 = '}{}'
    string_5 = '{{[(])]}}'
    string_6 = '[[{())}]'
    print(is_balanced(string_1))
    print(is_balanced(string_2))
    print(is_balanced(string_3))
    print(is_balanced(string_4))
    print(is_balanced(string_5))
    print(is_balanced(string_6))