(function () {

    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('Tem certeza que quer Deletar?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
    
})();