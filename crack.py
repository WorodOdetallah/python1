# cybersecurity
from string import digits

for i in digits:
    for j in digits:
        for k in digits:
            for l in digits:
                print(i, j, k, l)


# we can modify our code 
from string import ascii_letters
 
for i in ascii_letters:
    for j in ascii_letters:
        for k in ascii_letters:
            for l in ascii_letters:
                print(i, j, k, l)    
# this will print all the possible combinations of letters and numbers.

### What would happen if we asked for a password that was four letters, numbers, or punctuations? 
# We would have over 78,000,000 possibilities open to us!
# We can modify our code as follows:

from string import ascii_letters, digits, punctuation

for i in ascii_letters + digits + punctuation:
    for j in ascii_letters + digits + punctuation:
        for k in ascii_letters + digits + punctuation:
            for l in ascii_letters + digits + punctuation:
                print(i, j, k, l)

                