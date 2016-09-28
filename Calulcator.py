class Calculator():
    def __init__(self, tokens):
        self._tokens = tokens
        self._current = tokens[0]
    
    def exp(self):
        result = self.term()
        while self._current is '+':
            self.next()
            result += self.term()
            print(result)
        while self._current is '-':
            self.next()
            result -= self.term()
        return result

    def factor(self):
        result = None
        if self._current.isdigit():
            result = float(self._current)
            self.next()
        elif self._current is '(':
            self.next()
            result = self.exp()
            self.next()
        return result

    def next(self): 
        self._tokens = self._tokens[1:]
        self._current = self._tokens[0] if len(self._tokens) > 0 else None

    def term(self):
        result = self.factor()
        while self._current is '*':
            self.next()
            result *= self.factor()
        while self._current is '/':
            self.next()
            result /= self.factor()
        return result

if __name__ == '__main__':
    while True:
        lst = list(input('> '))
        tokens = []
        for i in range(len(lst)):
            if lst[i].isdigit() and len(tokens) > 0 and tokens[-1].isdigit():
                tokens[-1] += lst[i]
            else:
                tokens.append(lst[i])
        print (Calculator(tokens).exp() )