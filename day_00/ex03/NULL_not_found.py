def NULL_not_found(object: any) -> int:
    match type(object).__name__:
        case 'NoneType':
            print(f"Nothing: {object} {type(object)}")
        case 'float':
            print(f"Cheese: {object} {type(object)}")
        case 'int':
            print(f"Zero: {object} {type(object)}")
        case 'str':
            print(f"Empty: {type(object)}")
        case 'bool':
            print(f"Fake: {object} {type(object)}")
        case _:
            print("Type not found")
    return 1
