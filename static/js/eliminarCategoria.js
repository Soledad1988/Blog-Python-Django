document.addEventListener("DOMContentLoaded", function () {

    const botonesEliminar = document.querySelectorAll('.eliminar-categoria-btn');

    botonesEliminar.forEach(boton => {

        boton.addEventListener('click', function (e) {
            e.preventDefault();

            const url = this.dataset.url;

            Swal.fire({
                title: "¿Eliminar categoría?",
                text: "Se eliminará permanentemente",
                icon: "warning",
                showCancelButton: true,
                confirmButtonText: "Sí, eliminar",
                cancelButtonText: "Cancelar"
            }).then((result) => {

                if (result.isConfirmed) {

                    fetch(url, {
                        method: 'POST',
                        headers: {
                            "X-CSRFToken": getCookie("csrftoken")
                        }
                    })
                    .then(response => {
                        if (response.redirected) {
                            window.location.href = response.url;
                        }
                    })
                    .catch(error => console.error("Error:", error));
                }
            });
        });
    });
});


// CSRF helper (igual que antes)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
