# Very very dumb "chatbot", not even AI, just for learning purposes

# responses dict
responses = {
    "hello": "hello user",
    "how are you" : "good how about you"
}

def main():
    print("ybot")
    while (True):
        message = input("$ ")

        # exit
        if message.lower() == "exit":
            print("goodbye !")
            return
        
        # adding knowledge at runtime
        if message.lower().startswith("!"):
            splitted_msg_list = message.lower().split(" ")
            key = splitted_msg_list[0][1:] # remove the '!'
            value = " ".join(splitted_msg_list[1:])
            responses[key] = value
            print("chatbot : i'll remember that !")
            continue
        
        match = False
        # input content checking
        for response in responses.keys():
            if message.lower().startswith(response):
                print(f"chatbot : {responses[response]}")
                match = True
        if not match:
            print("chatbot : idk what you say man")
        
        

if __name__ == "__main__":
    main()