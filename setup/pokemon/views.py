from django.shortcuts import render
import requests

def personagem(request):
    base_url = "https://pokeapi.co/api/v2/"
    pokemon_name_or_id = request.GET.get('pokemon', 'pikachu')  
    url = f"{base_url}pokemon/{pokemon_name_or_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        name = data['name'].capitalize() 
        sprite_url = data['sprites']['front_default']  
        context = {
            'name': name,
            'id': data['id'],
            'height': data['height'],
            'weight': data['weight'],
            'abilities': [ability['ability']['name'] for ability in data['abilities']],
            'sprite_url': sprite_url  
        }
    else:
        context = {'error': 'Erro ao acessar a PokeAPI'}

    return render(request, 'home.html', context)
