import requests

joke_url ="https://official-joke-api.appspot.com/random_joke"
dad_joke="https://icanhazdadjoke.com/"
mood=input("Choose any one option from dad or fun :- ")
if mood=="Dad":
    url_type=dad_joke
else:
    url_type=joke_url

def get_Random_joke(mood,url_type):
    joke=requests.get(url=joke_url)
    # print(url_type)
    # print(joke.json()['setup']+joke.json()['punchline'])
    response_joke=joke.json()['setup']+joke.json()['punchline']

    return response_joke

output=get_Random_joke(mood,url_type)

print(output)