from re import search
import wikipedia
import webbrowser

# user_input = input('which page you want to see? ')
# print(search(wikipedia.page(user_input)))

try:
    user_input = wikipedia.page(input('what do you want to see? '))
    # print(user_input.title)
    # print(user_input.content)
    print(user_input.url)
    webbrowser.open_new(user_input.url)
except wikipedia.exceptions.PageError:
    print('does not exist')
except KeyError:
    print('type something with a meaning')


