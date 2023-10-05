ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[-1] = "World"
ft_tuple = list(ft_tuple)
ft_tuple[-1] = "Suisse"
ft_tuple = tuple(ft_tuple)
ft_set_to_list = ["Hello", "Lausanne"]
# Impossible to guarantee that
# the elements will be in the correct order in a set.
ft_set = set(ft_set_to_list)
ft_dict["Hello"] = "42Lausanne"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)