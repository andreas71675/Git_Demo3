import one
print("Top Level in two.py")

one.func()

if __name__ == '__main__':
    print("two.py has been run directly")
else:
    print("two.py has been imported")
