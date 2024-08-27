function loadMoreCharacters(page) {
  fetch(`/load_more?page=${page}`)
    .then((response) => response.json())
    .then((data) => {
      let characterContainer = document.getElementById("character-container");
      data.forEach((character) => {
        let characterElement = document.createElement("div");
        characterElement.classList.add("col-4");
        characterElement.innerHTML = `
        
                     <div class="col-sm-2 col-6">
             
                    <img src="${character.image}" alt="${character.name}" class=" img-fluid img-thumbnail">
                    
                    <h3 class="h5">${character.name}</h3>
                    <div class="d-grid gap-2 d-md-block">
                        <a href="/profile/${character.id}" 
                        class="btn btn-primary">Ver perfil</a>
                    </div>
      
                </div>
           
                `;
        characterContainer.appendChild(characterElement);
      });
    })
    .catch((error) => console.error("Error:", error));
}

document.addEventListener("DOMContentLoaded", function () {
  let page = 1;

  document.getElementById("load-more").addEventListener("click", function () {
    page++;
    loadMoreCharacters(page);
  });

  // Carrega a primeira página de personagens ao carregar a página
  loadMoreCharacters(page);
});
