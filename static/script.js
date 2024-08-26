let currentPage = {{ current_page }};
        
document.getElementById('load-more').addEventListener('click', function() {
    currentPage++;
    fetch(`/?page=${currentPage}`)
        .then(response => response.text())
        .then(data => {
            const parser = new DOMParser();
            const doc = parser.parseFromString(data, 'text/html');
            const newCharacters = doc.querySelector('#character-list').innerHTML;
            document.getElementById('character-list').innerHTML = newCharacters;
        })
        .catch(error => console.error('Error:', error));
});