class Meta(type):
    def __new__(cls,  class_name, bases, attrs):
        print(attrs)

        new_att = {}
        for name, val in attrs.items():
            if name.startswith("__"):
                new_att[name] = val
            else:
                new_att[name.upper()] = val

        print(new_att)
        return type(class_name, bases, new_att)


""" With the meta class we can modify the Dog class """


class Dog(metaclass=Meta):
    x = 10
    y = 12

    def hello(self):
        return "Hi!"


d = Dog()
print(d.X)
print(d.HELLO())
