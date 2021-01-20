'''
If statements

'''


Quiz: Guess My Number
You decide you want to play a game where you are hiding a number from someone. Store this number in a variable called 'answer'. Another user provides a number called 'guess'. By comparing guess to answer, you inform the user if their guess is too high or too low.

Fill in the conditionals below to inform the user about how their guess compares to the answer.

# '''
# You decide you want to play a game where you are hiding
# a number from someone.  Store this number in a variable
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 7
guess = 7

if guess < answer:
    result = "Oops!  Your guess was too low."
elif guess > answer:
    result = "Oops!  Your guess was too high."
elif guess==answer:
    result = "Nice!  Your guess matched the answer!"

print(result)

#---------------------------------------------
# '''
# Depending on where an individual is from we need to tax them
# appropriately.  The states of CA, MN, and
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and
# the corresponding state to assure that they are taxed by the right
# amount.
# '''
state = 'MN'
purchase_amount = 100
result= (purchase_amount)

if state=='CA':
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state=='MN':
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state=='NY':
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)

#--------------------------------------------------------------
'''
You will use a new variable prize to store a prize name if one was won, and then use the truth value of this variable to compose the result message. This will involve two if statements.

1st conditional statement: update prize to the correct prize name based on points.
2nd conditional statement: set result to the correct phrase based on whether prize is evaluated as True or False.

If prize is None, result should be set to "Oh dear, no prize this time."
If prize contains a prize name, result should be set to "Congratulations! You won a {}!".format(prize). This will avoid having the multiple result assignments for different prizes.
At the beginning of your code, set prize to None, as the default value.
'''


points = 174

points = 174  # use this input when submitting your answer

# set prize to default value of None
prize = None

# use the value of points to assign prize to the correct prize name
if points <= 50:
    prize = "wooden rabbit"
elif 151 <= points <= 180:
    prize = "wafer-thin mint"
elif points >= 181:
    prize = "penguin"

# use the truth value of prize to assign result to the correct message
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."

print(result)



#------------------------------------------
'''
For Loops
Practice: Quick Brown Fox
Use a for loop to take a list and print each element of the list in its own line.
'''

sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

for i in sentence:
    print(i)

'''
Practice: Multiples of 5
Write a for loop below that will print out every whole number that is a multiple of 5 and less than or equal to 30.
'''
# Write a for loop using range() to print out multiples of 5 up to 30 inclusive
for i in range(5, 35, 5):
    print(i)

#------------------------------------------
Quiz: Create Usernames
Write a for loop that iterates over the names list to create a usernames list. To create a username for each name, make everything lowercase and replace spaces with underscores. Running your for loop over the list:

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

should create the list:

usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

HINT: Use the .replace() method to replace the spaces with underscores. Check out how to use this method in this Stack Overflow answer.

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for index in names:
    usernames.append(index.lower().replace(" ", "_"))
#print (names)
print(usernames)

#----------------------------------------------
'''
Quiz: Modify Usernames with Range
Write a for loop that uses range() to iterate over the positions in usernames to modify the list. Like you did in the previous quiz, change each name to be lowercase and replace spaces with underscores. After running your loop, this list

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

should change to this:

usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here


print(usernames)
  
'''

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here


print(usernames)

#-------------------------------------------
'''
Quiz: Tag Counter
Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags. XML is a data language similar to HTML. You can tell if a string is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">". Keep track of the number of tags using the variable count.

You can assume that the list of strings will not contain empty strings.

'''

tokens = ['<greeting>', 'Hello World!', '</greeting>']

count = 0
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)

#-----------------------------------
'''
Quiz: Create an HTML List
Write some code, including a for loop, that iterates over a list of strings and creates a single string, html_str, which is an HTML list. For example, if the list is items = ['first string', 'second string'], printing html_str should output:

<ul>
<li>first string</li>
<li>second string</li>
</ul>
That is, the string's first line should be the opening tag <ul>. Following that is one line per element in the source list, surrounded by <li> and </li> tags. The final line of the string should be the closing tag </ul>.
  '''

items = ['first string', 'second string']
html_str = "<ul>\n"          # The "\n" here is the end-of-line char, causing
                             # chars after this in html_str to be on next line

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)
