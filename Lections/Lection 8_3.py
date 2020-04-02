class Singleton(object):
    __instance = None
    counter = 0

    @staticmethod
    def inst():
        if Singleton.__instance == None:
            Singleton.__instance = Singleton()
        return Singleton.__instance

    #single call check
    def __init__(self):
        print("Constructor called!")

    def count(self):
        self.counter += 1
        print(self.counter)


a = Singleton.inst()
b = Singleton.inst()

a.count()
b.count()

c = Singleton.inst()
c.count()