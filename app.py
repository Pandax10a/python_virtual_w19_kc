from re import search
import wikipedia

# user_input = input('which page you want to see? ')
# print(search(wikipedia.page(user_input)))

try:
    user_input = wikipedia.page(input('what do you want to see? '))
    print(user_input.title)
    print(user_input.content)
except wikipedia.exceptions.PageError:
    print('does not exist')


