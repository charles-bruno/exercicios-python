class HelloWorld:
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print(f"Hello, {self.name}")


if __name__ == "__main__":
    hello = HelloWorld("Charles")
    hello()
