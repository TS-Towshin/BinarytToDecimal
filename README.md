# BinarytToDecimal
## commads:
 - Type `exit` to stop the program
### How it works:
  it takes binary as input and checks the length of the binary. a value of 0.5 is set as 'L' and a vlue of 0 as 'dec'. A loop is set. In the loop, the length is getting shorter by 1 everytime it completes a round. Its taking the value of length as binary's (length)th number as digit. Now the predefiened value of 'L' is multiplied by 2 which makes it 1. Now its multiplying 'L' with 'digit'. Another predefiened value is 'dec' which is 0. Now 'dec' is added with 'digit'. when length becomes 0, before breaking the loop it meets the condition and prints the 'dec' which is the ectual result. The decimal number.
  ## Example:
  ##### binary = 1000001
  ##### length = 7
  ##### L = 0.5
  ##### dec = 0
  ##### While length != 0: (This loop will continue as long as length is not equal to 0)
    length = length - 1 = 7 - 1 = 6
    digit = str(binary)[length] = 1
    L = L * 2 = 0.5 * 2 = 1
    mult = L * digit = 1 * 1 = 1
    dec = dec + mult = 0 + 1 = 1
      if length == 0:
        print(dec)
 ##### This will repeat until length becomes 0
    length = length - 1 = 6 - 1 = 5
    digit = str(binary)[length] = 0
    L = L * 2 = 1 * 2
    mult = L * digit = 2 * 0 = 0
    dec = dec + mult = 1 + 0 = 1


    length = length - 1 = 5 - 1 = 4
    digit = str(binary)[length] = 0
    L = L * 2 = 2 * 4
    mult = L * digit = 4 * 0 = 0
    dec = dec + mult = 1 + 0 = 1


    length = length - 1 = 4 - 1 = 3
    digit = str(binary)[length] = 0
    L = L * 2 = 4 * 2 = 8
    mult = L * digit = 8 * 0 = 0
    dec = dec + mult = 1 + 0 = 1


    length = length - 1 = 3 - 1 = 2
    digit = str(binary)[length] = 0
    L = L * 2 = 8 * 2 = 16
    mult = L * digit = 16 * 0 = 0
    dec = dec + mult = 1 + 0 = 1
    
    
    length = length - 1 = 2 - 1 = 1
    digit = str(binary)[length] = 0
    L = L * 2 = 16 * 2 = 32
    mult = L * digit = 32 * 0 = 0
    dec = dec + mult = 1 + 0 = 1
    
    length = length - 1 = 1 - 1 = 0
    digit = str(binary)[length] = 1
    L = L * 2 = 23 * 2 = 64
    mult = L * digit = 64 * 1 = 64
    dec = dec + mult = 1 + 64 = 54
    
    
    Now that the condition(length = 0) has met, it will print dec so the output will be 65
    
##### The result is 65 which is correct
