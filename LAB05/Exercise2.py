def calculate_static_sum():
    static_number1 = 10  
    static_number2 = 20 
    
    def add_static_numbers():
        return static_number1 + static_number2 
    
    return add_static_numbers()

def calculate_dynamic_sum():
    dynamic_number1 = 10 
    dynamic_number2 = 20  
    
    def add_dynamic_numbers():
        return dynamic_lookup('dynamic_number1') + dynamic_lookup('dynamic_number2')  
    
    return add_dynamic_numbers()

def dynamic_lookup(var_name):
    import inspect
    for frame in inspect.stack():
        if var_name in frame[0].f_globals or var_name in frame[0].f_locals:
            return frame[0].f_globals.get(var_name, frame[0].f_locals.get(var_name))
    raise NameError(f"{var_name} not found")

def demonstrate_scoping():
    global dynamic_number1, dynamic_number2
    dynamic_number1 = 100  
    dynamic_number2 = 200  
    
    static_result = calculate_static_sum()
    print(f"Static Scoping Result: {static_result}")
    
    dynamic_result = calculate_dynamic_sum()
    print(f"Dynamic Scoping Result: {dynamic_result}")

if __name__ == "__main__":
    demonstrate_scoping()

    