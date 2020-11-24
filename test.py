import requests

def recipe_searchy(ingredient, diet):
    app_id= '9faba4be'
    app_key = '0b2e438f001911bfb8bbb24baa8dac41'
    url = f'https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}&diet={diet}'

    response = requests.get(url)

    data = response.json()
    return data['hits']

def recipe_searchn(ingredient):
    app_id= '9faba4be'
    app_key = '0b2e438f001911bfb8bbb24baa8dac41'
    url = f'https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}'

    response = requests.get(url)

    data = response.json()
    return data['hits']


def run():
    ingredient = input('Welcome to MAKE WASTE WORK FOR IT: A Waste-Reducing Recipe Generator. Enter 1 or more ingredients: ')
    diet_yn = input('Do you have any dietary requirements? (Y/N)')
    if diet_yn == 'Y':
        diet = input('Enter diet requirement (balanced/high-protein/ high-fiber/ low-fat/ low-sodium) : ')
        results = recipe_searchy(ingredient, diet)
        print(f"The following recipes contain(s) {ingredient} and give you a {diet} diet. Thank you for reducing food waste!")
        for result in results:
            recipe = result['recipe']

            print()
            print(recipe['label'])
            print(recipe['url'])
            print("This recipe contains " + str(int(recipe['calories'])) + " calories")
    elif diet_yn == 'N':
        results = recipe_searchn(ingredient)
        print(f"The following recipes contain(s) {ingredient}. Thank you for reducing food waste!")
        for result in results:
            recipe = result['recipe']

            print()
            print(recipe['label'])
            print(recipe['url'])
            print("This recipe contains " + str(int(recipe['calories'])) + " calories")

run()