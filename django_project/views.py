import requests
from django.shortcuts import render 

def index(request):
  response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
  data = response.json()
  fact = data['text']

  r3 = requests.get('https://dog.ceo/api/breeds/image/random')
  res3 = r3.json()
  dog = res3['message']

  # This is the assignment for the Hackathon, 
  # Instructions: 
  # Use this API and randomize the students
  response2 = requests.get('https://freetestapi.com/api/v1/students') # Use this API
  data2 = response2.json()
  name = data2[0]['name']

  
  
  return render(request, 'index.html', {'fact': fact, 'dog': dog,'name': name})



def food(request):
    # Fetch random meal data from The Meal DB API
    response_meal = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
    meal_data = response_meal.json()
    meals = meal_data.get('meals', [])
 # Fetch random meal data from The coktaildb API
    response_drinks = requests.get('https://www.thecocktaildb.com/api/json/v1/1/random.php')
    drinks_data = response_drinks.json()
    drinks = drinks_data.get('drinks', [])
  

    return render(request, 'food.html', {'meals': meals, 'drinks': drinks})

def art(request):
    api_key = 'f04407e1-42e3-48b8-a341-61ea77e5318a'  # Replace 'your_api_key_here' with your actual API key
    url = 'https://iiif.harvardartmuseums.org/collections/top'
    params = {
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    artdata = response.json()
    pics =  artdata.get('@context', [])

    

    return render(request, 'art.html', {'pics' :pics})
   
