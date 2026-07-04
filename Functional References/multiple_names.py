def greet():
    print("Hello")

func_dict = {
    "hi": greet,
    "hello": greet,
    "welcome": greet
}

func_dict["hi"]()
func_dict["hello"]()
func_dict["welcome"]()