We need to first determine the question, firstly we need to enter the machine, understand the port and scan it: (IP:10.82.180.204)
Open Port is 1337, so;
Analyze command: nc 10.82.180.204 1337
Then, we have This: -XOR encoded text has flag 1: 3222180926570b391c222312213322125e36193527042741370a262c1a03141e2c422314121a002b
What is the encryption key?- (We're figure this out with python code.)
Flag definetly starts with THM{ (definetly ends with "}") 
Hex 32 XOR T (Hex 54) = f | Hex 22 XOR H (Hex 48) = j | Hex 18 XOR M (Hex 4D) = U | Hex 09 XOR { (Hex 7B) = r || (We got fjUr, but didnt know the fifth one)
After running python file, we need to see something , end with "}" , and this is V hex 56 this mean we need to 26 XOR 56! and this is V! Python code is solved the problem!
