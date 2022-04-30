while True:
    try:
        binary = input("Input: ")
        if "exit" in binary:
            break #it will stop the code if 'exit' is typed
        else:
            binary = int(binary, 2) #Takes only 1 and 0 as input
            length = len(str(binary)) #checks the length of the input
            L = 0.5
            dec = 0
            while length != 0:
                length = length - 1
                digit = str(binary)[length]
                digit = int(digit)
                L = L * 2
                mult = L * digit
                dec = dec + mult
                if length == 0:
                    print(dec)
    except Exception as e:
        print("Something went wrong, Please try again!")
        print("Error code: ", e)
        pass
