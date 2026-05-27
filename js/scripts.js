/*!
* Start Bootstrap - Resume v7.0.6 (https://startbootstrap.com/theme/resume)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-resume/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Activate Bootstrap scrollspy on the main nav element
    const sideNav = document.body.querySelector('#sideNav');
    if (sideNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#sideNav',
            rootMargin: '0px 0px -40%',
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});


// Attendre que le document soit prêt
document.addEventListener("DOMContentLoaded", () => {

    // Fonction pour charger et afficher les données de l'AC
    window.openModalAC = function (acId) {
        fetch('competences.json')
            .then(response => response.json())
            .then(data => {
                const acData = data[acId];

                if (acData) {
                    // Remplissage des textes
                    document.getElementById('modalTitle').textContent = `Détails ${acId} : ${acData.titre}`;
                    document.getElementById('modalContext').textContent = acData.contexte;
                    document.getElementById('modalAction').textContent = acData.action;
                    document.getElementById('modalResult').textContent = acData.resultat;

                    // Gestion de la couleur de l'en-tête (bg-primary, bg-warning, bg-info...)
                    const modalHeader = document.getElementById('modalHeader');
                    modalHeader.className = `modal-header text-white ${acData.theme}`;

                    // Création des badges pour les outils
                    const toolsContainer = document.getElementById('modalTools');
                    toolsContainer.innerHTML = ""; // On vide les anciens badges
                    acData.outils.forEach(outil => {
                        const badge = document.createElement('span');
                        badge.className = `badge ${acData.theme} text-dark me-1`;
                        badge.textContent = outil;
                        toolsContainer.appendChild(badge);
                    });

                    // Affichage de la modale via Bootstrap
                    const myModal = new bootstrap.Modal(document.getElementById('dynamicModal'));
                    myModal.show();
                } else {
                    console.error("Les données pour cet AC n'ont pas été trouvées.");
                }
            })
            .catch(error => console.error('Erreur lors du chargement du JSON:', error));
    };
});