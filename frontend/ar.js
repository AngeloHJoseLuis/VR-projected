fetch("http://127.0.0.1:8000/api/ar_models/")
    .then(response => response.json())
    .then(models => {
        models.forEach(model => {
            let marker = document.createElement("a-marker");
            marker.setAttribute("type", "pattern");
            marker.setAttribute("url", "marker.patt");

            let model3D = document.createElement("a-entity");
            model3D.setAttribute("gltf-model", `url(${model.archivo})`);
            marker.appendChild(model3D);

            document.querySelector("a-scene").appendChild(marker);
        });
    });
