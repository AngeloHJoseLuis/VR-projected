// fetch("http://127.0.0.1:8000/api/ar_models/")
//     .then(response => response.json())
//     .then(models => {
//         models.forEach(model => {
//             let marker = document.createElement("a-marker");
//             marker.setAttribute("type", "pattern");
//             marker.setAttribute("url", "marker.patt");

//             let model3D = document.createElement("a-entity");
//             model3D.setAttribute("gltf-model", `url(${model.archivo})`);
//             marker.appendChild(model3D);

//             document.querySelector("a-scene").appendChild(marker);
//         });
//     });

fetch("http://127.0.0.1:8000/api/ar_models/")
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(models => {
        if (!Array.isArray(models)) {
            throw new Error("La respuesta de la API no es una lista de modelos.");
        }

        const scene = document.querySelector("a-scene");
        if (!scene) {
            throw new Error("No se encontró el elemento <a-scene> en el DOM.");
        }

        models.forEach(model => {
            if (!model.archivo) {
                console.warn("Modelo sin archivo 3D:", model);
                return;
            }

            let marker = document.createElement("a-marker");
            marker.setAttribute("preset", "custom");
            marker.setAttribute("type", "pattern");
            marker.setAttribute("url", "marker.patt"); // Asegúrate de que marker.patt esté accesible

            let model3D = document.createElement("a-entity");
            model3D.setAttribute("gltf-model", `url(${model.archivo})`);
            model3D.setAttribute("scale", "0.5 0.5 0.5");  // Ajuste del tamaño del modelo
            model3D.setAttribute("position", "0 0 0");  
            model3D.setAttribute("crossorigin", "anonymous"); // Evita problemas CORS
            marker.appendChild(model3D);

            scene.appendChild(marker);
        });
    })
    .catch(error => console.error("Error al cargar los modelos AR:", error));
