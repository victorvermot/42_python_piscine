def all_thing_is_obj(object: any) -> int:
    match type(object).__name__:
        case 'list':
            print(f"List: {type(object)}")
        case 'set':
            print(f"Set: {type(object)}")
        case 'tuple':
            print(f"Tuple: {type(object)}")
        case 'dict':
            print(f"Dict: {type(object)}")
        case 'str':
            print(f"{object} is in the kitchen: {type(object)}")
        case _:
            print("Type not found")
    return 42

def main():
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello" : "titi!"}
    all_thing_is_obj(ft_list)
    all_thing_is_obj(ft_tuple)
    all_thing_is_obj(ft_set)
    all_thing_is_obj(ft_dict)
    all_thing_is_obj("Brian")
    print(all_thing_is_obj(10))

if __name__ == "__main__":
    main()