class Calci():
    def __init__(self, tokens):
        self._tokens = tokens
        self._current = tokens[0]
    
    def expression(self):
        eq_result = self.term()
        while self._current is '+':
            self.next()
            eq_result += self.term()
            print(result)
        while self._current is '-':
            self.next()
            eq_result -= self.term()
        return eq_result

    def factor(self):
        eq_result = None
        if self._current.isdigit():
            eq_result = float(self._current)
            self.next()
        elif self._current is '(':
            self.next()
            eq_result = self.exp()
            self.next()
        return eq_result

    def next(self): 
        self._tokens = self._tokens[1:]
        self._current = self._tokens[0] if len(self._tokens) > 0 else None

    def term(self):
        eq_result = self.factor()
        while self._current is '*':
            self.next()
            eq_result *= self.factor()
        while self._current is '/':
            self.next()
            eq_result /= self.factor()
        return eq_result

if __name__ == '__main__':
    while True:
        print("please enter your calculation expression")
        my_list = list(input('> '))
        tokens = []
        for i in range(len(my_list)):
            if my_list[i].isdigit() and len(tokens) > 0 and tokens[-1].isdigit():
                tokens[-1] += my_list[i]
            else:
                tokens.append(my_list[i])
        print (Calci(tokens).expression() )