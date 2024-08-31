function loadMoreCharacters(page) {
  fetch(`/load_more?page=${page}`)
    .then((response) => response.json())
    .then((data) => {
      let characterContainer = document.getElementById("character-container");
      data.forEach((character) => {
        let characterElement = document.createElement("div");
        characterElement.classList.add("col-sm-3", "col-6", "mb-4"); // Adicionei "mb-4" para margin-bottom
        characterElement.innerHTML = `
        <br>
        </h3> <!-- Adicionei "mt-2" para margin-top -->
        <h3 class="h5 mt-2 d-flex justify-content-between">
            <small> ${character.name}</small>
          <blockquote class="lead">
                #${character.id}
          </blockquote>
        </h3>
          <img src="${character.image}" alt="${character.name}" class="img-fluid img-thumbnail">
          <h3 class="h5 mt-2 d-flex justify-content-between">
              Status: ${character.status}
          </h3>
          <h3 class="h5 mt-2 d-flex justify-content-between">
              Location: ${character.location['name']}
          </h3>
          <p>
            <a href="/profile/${character.id}" class="btn btn-primary">Ver perfil</a>
          </p>
   
        `
        ;
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



document.addEventListener('DOMContentLoaded', function () {
  var modalButtons = document.querySelectorAll('[data-bs-toggle="modal"]');

  modalButtons.forEach(function (button) {
      button.addEventListener('click', function () {
          var targetModal = button.getAttribute('data-bs-target');
          var modalElement = document.querySelector(targetModal);
          
          if (modalElement) {
              var modal = bootstrap.Modal.getOrCreateInstance(modalElement);
              modal.show();
          }
      });
  });
});