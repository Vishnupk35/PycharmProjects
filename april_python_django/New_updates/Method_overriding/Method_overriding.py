class Ide:
    def functionalities(self):
        funcs=["create_file","rename","delete"]
        return funcs
class Pycharm(Ide):
    def functionalities(self):
        funcs=super().functionalities()
        funcs.append("execute")
        funcs.append("debug")
        return funcs
py=Pycharm()
print(py.functionalities()) #['create_file', 'rename', 'delete', 'execute', 'debug']
#When we override the parent class information stays and we can add child class information