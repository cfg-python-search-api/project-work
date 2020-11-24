import requests

def recipe_search(ingredient, diet):
    app_id= '9faba4be'
    app_key = '0b2e438f001911bfb8bbb24baa8dac41'
    url = f'https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}&diet={diet}'

    response = requests.get(url)

    data = response.json()
    return data['hits']


def run():
   ingredient = input('Enter 1 or more ingredients: ')
   diet = input('Enter diet requirement (balanced/high-protein/ high-fiber/ low-fat/ low-sodium) : ')
   results = recipe_search(ingredient, diet)

   for result in results:
       recipe = result['recipe']

       print(f"The following recipes contain(s) {ingredient} and give you a {diet} diet.")
       print()
       print(recipe['label'])
       print(recipe['url'])
       print("This recipe contains " +  str(int(recipe['calories'])) + " calories")

run()