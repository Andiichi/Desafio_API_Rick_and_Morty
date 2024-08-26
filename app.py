from flask import Flask, render_template, jsonify
import urllib.request, json

app = Flask(__name__)


@app.route('/')
def get_list_characters_page():
    url = 'https://rickandmortyapi.com/api/character/'
    response = urllib.request.urlopen(url)
    data = response.read()
    data_dict = json.loads(data)

    return render_template('characters.html', characters=data_dict['results'])

@app.route('/profile/<id>')
def get_profile(id):
    url = 'https://rickandmortyapi.com/api/character/' + id
    response = urllib.request.urlopen(url)
    data = response.read()
    data_dict = json.loads(data)

    return render_template('profile.html', profile=data_dict)


@app.route('/episode/<id>')
def get_episodes(id):
    url = 'https://rickandmortyapi.com/api/episode/' + id
    response = urllib.request.urlopen(url)
    data = response.read()
    data_dict = json.loads(data)

    return render_template('episodes.html', profile=data_dict)


@app.route('/lista')
def get_list_characters():
    url = 'https://rickandmortyapi.com/api/character/'
    response = urllib.request.urlopen(url)
    characters = response.read()
    characters_dict = json.loads(characters)

    characters = []

    for character in characters_dict['results']:
        character_info = {
            'id': character['id'],
            'name': character['name'],
            'status': character['status'],
            'species': character['species'],
            'type': character['type'],
            'gender': character['gender'],
            # 'origin': {
            #     'name': character['origin']['name'],
            #     'url': character['origin']['url'],
            # },
            # 'location': {
            #     'name': character['location']['name'],
            #     'url': character['location']['url'],
            # },
            'image': character['image'],
            # 'episode': character['episode']
        }
    
        characters.append(character_info)
    
    return jsonify({'results': characters})
