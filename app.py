from flask import Flask, render_template, jsonify, request, redirect, url_for
import requests, json

app = Flask(__name__)

# Redireciona para a primeira página de personagens
@app.route('/')
def get_page():
    return redirect(url_for('get_list_characters_page', page=1))



@app.route('/characters')
def get_list_characters_page():
    # Obtém o número da página da query string, por padrão é 1
    page_id = request.args.get('page', 1, type=int)

    # URL da API com a página solicitada
    url = f'https://rickandmortyapi.com/api/character?page={page_id}'
    response = requests.get(url)
    data_dict = response.json()

    # Extraindo os dados de paginação
    next_page = data_dict['info']['next']
    prev_page = data_dict['info']['prev']
    total_pages = data_dict['info']['pages']  # Número total de páginas

    # Determinando o intervalo de páginas para exibir
    start_page = max(page_id - 1, 1)
    end_page = min(page_id + 2, total_pages)

    # Determinando o próximo e o anterior com base no número da página atual
    next_page_num = page_id + 1 if next_page else None
    prev_page_num = page_id - 1 if prev_page else None

    return render_template('characters.html',
                           characters=data_dict['results'],
                           current_page=page_id,
                           total_pages=total_pages,
                           next_page=next_page_num,
                           prev_page=prev_page_num,
                           start_page=start_page,
                           end_page=end_page)




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
