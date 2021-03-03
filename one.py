def func():
    print("function in one.py")

print("top level in one.py")

if __name__ == '__main__':
    print("one.py has been run directly")
else:
    print("one.py has been imported")
    from firstmodul import first_func
    first_func()
    
