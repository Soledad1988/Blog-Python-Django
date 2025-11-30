function eliminarUsuario(id) {
    Swal.fire({
        title: "¿Estás segura de eliminar este usuario?",
        text: "Esta acción no se puede deshacer.",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#d33",
        cancelButtonColor: "#3085d6",
        confirmButtonText: "Sí, eliminar",
        cancelButtonText: "Cancelar"
    }).then((result) => {
        if (result.isConfirmed) {
            fetch(`/usuarios/${id}/eliminar/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken"),
                    "X-Requested-With": "XMLHttpRequest",
                }
            })
            .then(response => {
                if (response.ok) {
                    Swal.fire(
                        "Eliminado",
                        "El usuario ha sido eliminado con éxito.",
                        "success"
                    ).then(() => {
                        location.reload();
                    });
                } else {
                    Swal.fire(
                        "Error",
                        "No se pudo eliminar el usuario.",
                        "error"
                    );
                }
            })
            .catch(() => {
                Swal.fire(
                    "Error",
                    "Hubo un problema con la solicitud.",
                    "error"
                );
            });
        }
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}