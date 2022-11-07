from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello Finch </h1>')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', { 'finches': finches })


class Finch:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

finches = [
  Finch('Lolo', 'yellow', 'Kinda rude.', 3),
  Finch('Sachi', 'also yellow', 'Looks like a turtle.', 0),
  Finch('Fancy', 'color', 'Happy fluff ball.', 4),
  Finch('Bonk', 'color', 'Meows loudly.', 6)
]