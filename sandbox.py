msg = "hello"
print(msg)

# Interpreter
class Interpreter:
    def visit(self,node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(node)
    def no_visit_method(self, node):
        raise Exception(f'No visit_{type(node).__name__} method defined')
    
    def visit_NumberNode(self, node):
        print('Found nuber node!')

    def visit_BinOpNode():
        print('Found bin op node!')
    
    def visit_UnaryOpNode(self, node):
        print('found unary op node!')

# Run
