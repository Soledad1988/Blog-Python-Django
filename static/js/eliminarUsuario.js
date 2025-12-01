console.log("JS eliminarUsuario.js CARGADO");

document.addEventListener("click", function (e) {

    if (e.target.classList.contains("eliminar-usuario-btn")) {
        e.preventDefault();

        const url = e.target.dataset.url;

        Swal.fire({
            title: "¿Eliminar usuario?",
            text: "Esta acción no se puede deshacer.",
            icon: "warning",
            showCancelButton: true,
            confirmButtonText: "Sí, eliminar",
            cancelButtonText: "Cancelar"
        }).then((result) => {

            if (result.isConfirmed) {

                fetch(url, {
                    method: "POST",
                    headers: {
                        "X-CSRFToken": getCookie("csrftoken")
                    },
                })
                .then(response => response.json())
                .then(data => {

                    if (data.ok) {
                        Swal.fire("Eliminado", data.msg, "success");
                        setTimeout(() => location.reload(), 800);
                    } else {
                        Swal.fire("Error", data.msg, "error");
                    }

                });
            }
        });

    }
});


// CSRF helper
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + "=")) {
                cookieValue = cookie.substring(name.length + 1);
                break;
            }
        }
    }
    return cookieValue;
}
