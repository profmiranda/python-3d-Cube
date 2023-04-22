class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


if __name__ == '__main__':
    my_class_instance = MyClass()
    print(my_class_instance.i)
    print(my_class_instance.f())
    my_class_instance.i = 123456
    print(my_class_instance.i)
