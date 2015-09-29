"""
distribution.py
Author: Adam Pikielny
Credit:
http://stackoverflow.com/questions/6797984/how-to-convert-string-to-lowercase-in-python
https://docs.python.org/2/tutorial/datastructures.html
http://www.tutorialspoint.com/python/python_tuples.htm

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""

#input
string=input("Please enter a string of text (the bigger the better): ")
print("\n")
lowercase=string.lower()

#setting up alphabet list
mylist=[]

alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabet.reverse()
for letter in alphabet:
    mylist.append(lowercase.count(letter))


zipped=list((zip(mylist,alphabet)))

zipped.sort(reverse=True)
print(zipped)


for x in zipped:
    #need to alphabetize within one frequency
    #for i in range()
    if x[0]!=0:
        print(x[1]*x[0])