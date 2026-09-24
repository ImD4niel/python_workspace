#hybrid inheritence
class employee:
    def work(self):
        print("employee dev")

class FrontEndDev(employee):
    def render(self):
        print("rendering")

class BackEndDev(employee):
    def correct_db(self):
        print("beckend")

class FullStackdev(FrontEndDev,BackEndDev):
    def deploy(self):
        print("deploy")

q=FullStackdev()  #intantiation
q.deploy()
q.correct_db
q.render
q.work
print(FullStackdev.__mro__)



