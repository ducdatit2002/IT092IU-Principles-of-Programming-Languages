import sys

def func_A(a):
    print('this is function A, ', a)

def func_B(b):
    print('this is function B', b)

def func_C( a, b):
    re = a + b
    print('re: ', re)
    return a+b

# python demo.py a b 

def main(args):
    print("Arguments passed to the script:") 
    a = args[0]
    func_A(a)
    b = args[1]   
    func_C(a, b)
    for arg in args:
        print(arg)    

# argv[1:] vs argv

if __name__ == "__main__":
    main(sys.argv[1:])
