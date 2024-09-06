from flask import Flask, render_template, jsonify, request, redirect, url_for
import requests, json

app = Flask(__name__)

@app.route('/')
def get_list_characters_page():
    url = 'https://rickandmortyapi.com/api/character/'
    response = requests.get(url)
    data_dict = response.json()

    return render_template('characters.html', characters=data_dict['results'])


@app.route('/load_more', methods=['GET'])
def load_more():
    page = request.args.get('page', 1, type=int)
    url = f'https://rickandmortyapi.com/api/character/?page={page}'
    response = requests.get(url)
    data_dict = response.json()
    return jsonify(data_dict['results'])


@app.route('/profile/<id>')
def get_profile(id):
    url = f'https://rickandmortyapi.com/api/character/{id}'
    response = requests.get(url)
    data_dict = response.json()

    return render_template('profile.html', profile=data_dict)


@app.route('/episodes')
def get_episodes():
    url = 'https://rickandmortyapi.com/api/episode/'
    response = requests.get(url)
    data_dict = response.json()

    return render_template('episodes.html', episodes=data_dict['results'])



@app.route('/locations')
def get_locations():
    url = 'https://rickandmortyapi.com/api/location/'
    response = requests.get(url)
    locations_dict = response.json()
    
    locations = []

    for location in locations_dict['results']:

        residents = []
        
        #montando o dict das infos necessárias do characters residentes da localidade
        for resident_url in location['residents']:
            resident_response = requests.get(resident_url)
            resident_data = resident_response.json()
            residents.append({
                'id': resident_data['id'],
                'name': resident_data['name'],
                'image': resident_data['image']  # Adiciona o campo de imagem
            })

        location_info = {
            'id': location['id'],
            'name': location['name'],
            'type': location['type'],
            'dimension': location['dimension'],
            'residents': residents
        }
        locations.append(location_info)

    return render_template('locations.html', locations=locations)



@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()

    # Verifica se a busca é um número (possivelmente um ID)
    if query.isdigit():
        # Redireciona diretamente para a página de perfil do personagem
        return redirect(url_for('get_profile', id=query))
    
    # Caso contrário, realiza a busca por nome
    if query:
        url = f'https://rickandmortyapi.com/api/character/?name={query}'
        response = requests.get(url)
        data_dict = response.json()

        # Verifica se encontrou personagens
        if 'results' in data_dict:
            return render_template('characters.html', characters=data_dict['results'])
        else:
            return render_template('characters.html', characters=[], message="Nenhum personagem encontrado.")
    else:
        return redirect('/')




@app.route('/lista')
def get_list_characters():
    url = 'https://rickandmortyapi.com/api/character/'
    response = requests.get(url)
    characters_dict = response.json()

    characters = []

    for character in characters_dict['results']:
        character_info = {
            'id': character['id'],
            'name': character['name'],
            'status': character['status'],
            'species': character['species'],
            'type': character['type'],
            'gender': character['gender'],
            'origin': {
                'name': character['origin']['name'],
                'url': character['origin']['url'],
            },
            'location': {
                'name': character['location']['name'],
                'url': character['location']['url'],
            },
            'image': character['image'],
            'episode': character['episode']
        }
    
        characters.append(character_info)
    
    return jsonify({'results': characters})



if __name__ == "__main__":
    app.run(debug=True)
