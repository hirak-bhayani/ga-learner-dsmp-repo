### Project Overview

 Middle of the night & I receive this message:
**Hello lieutenant! It's with an emergency that our agency wishes to use your Python skills (*grin grin*). Your mission, if you choose to accept it, would be to help us decipher a message that we received from our intelligence. We have multiple text files that need to be read and have certain operations performed to get our final message.
Good luck. The fate of humanity lies in your hands.**

I took it up & decided to see if I could help decipher the messages received.


### Learnings from the project

 The key thing that I learnt from this project was solving problems logically through the use of concepts like string operations, conditional statements & loops, functions and file input/outputs.


### Approach taken to solve the problem

 My goal was to extract individual message bits and bring it all together to decipher the final message.

**The individual message bits were extracted step wise as follows:**
- My first task involved writing a function that read the contents of one of the files that I had received from the intelligence dept. 
- I then had to conduct operations to extract messages from disparate files & fuse them into a singular message. (In this case, it involved floor division of the messages i.e. numbers extracted). 
- I then substituted a certain message received (Green) using if-else loops to derive its actual meaning (i.e. Green = Data scientist). 
- Consequently, I coded a function that took two messages from different files and created a third list that contained words present in the first message but not overlapping with the contents of the second message. This function made use of list comprehensions & joins and returned the third list that had combined words. 
- My next task had me extracting words of even length from the message received using lambda and filter functions.

The final step involved bringing all the messages obtained through the individual message bits together into a final single message & writing that into a file.


