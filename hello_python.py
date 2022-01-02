class HelloWorld:
    def __init__(self, name, sobrenome):
        self.name = name
        self.sobrenome = sobrenome

    def __call__(self, *args, **kwargs):
        print(f"Olá!, {self.name} {self.sobrenome}")


if __name__ == "__main__":
    hello = HelloWorld("Charles", "Bruno")
    hello()
