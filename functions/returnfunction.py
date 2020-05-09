def display(name):
    def message():
        return 'Hello '
    return message

fun = display()
print(fun())