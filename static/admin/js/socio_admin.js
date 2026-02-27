document.addEventListener("DOMContentLoaded", function() {

    const tipoSelect = document.getElementById("id_tipo");
    const condicionSelect = document.getElementById("id_condicion");

    function cargarCondiciones(tipoId) {
        if (!tipoId) {
            condicionSelect.innerHTML = "";
            return;
        }

        fetch(`/ajax/cargar-condiciones/?tipo_id=${tipoId}`)
            .then(response => response.json())
            .then(data => {
                condicionSelect.innerHTML = "";

                data.forEach(condicion => {
                    const option = document.createElement("option");
                    option.value = condicion.id;
                    option.text = condicion.nombre;
                    condicionSelect.appendChild(option);
                });
            });
    }

    if (tipoSelect) {
        tipoSelect.addEventListener("change", function() {
            cargarCondiciones(this.value);
        });
    }

});
