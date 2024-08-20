class Animal:
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

def demonstrate_static_binding():
    """This function demonstrates static binding (early binding)."""
    animal = Animal()
    sound = animal.sound()  # The method to be called is determined at compile-time
    return f"Static Binding: {sound}"

def demonstrate_dynamic_binding():
    """This function demonstrates dynamic binding (late binding)."""
    dog = Dog()
    cat = Cat()
    
    # The method to be called is determined at runtime based on the object
    dog_sound = dog.sound()
    cat_sound = cat.sound()
    
    return f"Dynamic Binding with Dog: {dog_sound}\nDynamic Binding with Cat: {cat_sound}"

def main():
    print(demonstrate_static_binding())
    print(demonstrate_dynamic_binding())

if __name__ == "__main__":
    main()