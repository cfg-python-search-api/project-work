import requests

def recipe_search(ingredient):
    app_id= '9faba4be'
    app_key = '0b2e438f001911bfb8bbb24baa8dac41'
    url = f'https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}'





    response = requests.get(url)

    data = response.json()
    return data['hits']

recipe_search('cheese')

def run():
   ingredient = input('Enter an ingredient: ')
   results = recipe_search(ingredient)

   for result in results:
       recipe = result['recipe']

       print(recipe['label'])
       print(recipe['url'])
       print()

run()