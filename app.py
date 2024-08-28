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
    data_dict = response.json()

    return render_template('locations.html', locations=data_dict['results'])

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












# from flask import Flask, render_template, jsonify, request
# import requests, urllib.request, json

# app = Flask(__name__)

# @app.route('/')
# def get_list_characters_page():
#     url = 'https://rickandmortyapi.com/api/character/'
#     response = urllib.request.urlopen(url)
#     data = response.read()
#     data_dict = json.loads(data)

#     return render_template('characters.html', characters=data_dict['results'])



# @app.route('/load_more', methods=['GET'])
# def load_more():
#     # Retorna os personagens de uma página específica como JSON
#     page = request.args.get('page', 1, type=int)
#     url = f'https://rickandmortyapi.com/api/character/?page={page}'
#     response = requests.get(url)
#     data_dict = response.json()
#     return jsonify(data_dict['results'])

# @app.route('/profile/<id>')
# def get_profile(id):
#     url = 'https://rickandmortyapi.com/api/character/' + id
#     response = urllib.request.urlopen(url)
#     data = response.read()
#     data_dict = json.loads(data)

#     return render_template('profile.html', profile=data_dict)

# @app.route('/episodes')
# def get_episodes():
#     url = 'https://rickandmortyapi.com/api/episode/'
#     response = urllib.request.urlopen(url)
#     data = response.read()
#     data_dict = json.loads(data)

#     return render_template('episodes.html', episodes=data_dict['results'])

# @app.route('/lista')
# def get_list_characters():
#     url = 'https://rickandmortyapi.com/api/character/'
#     response = urllib.request.urlopen(url)
#     characters = response.read()
#     characters_dict = json.loads(characters)

#     characters = []

#     for character in characters_dict['results']:
#         character_info = {
#             'id': character['id'],
#             'name': character['name'],
#             'status': character['status'],
#             'species': character['species'],
#             'type': character['type'],
#             'gender': character['gender'],
#             'origin': {
#                 'name': character['origin']['name'],
#                 'url': character['origin']['url'],
#             },
#             'location': {
#                 'name': character['location']['name'],
#                 'url': character['location']['url'],
#             },
#             'image': character['image'],
#             'episode': character['episode']
#         }
    
#         characters.append(character_info)
    
#     return jsonify({'results': characters})



# if __name__ == "__main__":
#     app.run(debug=True)