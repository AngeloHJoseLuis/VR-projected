// fetch('http://127.0.0.1:8000/api/escenas/')
//     .then(response => response.json())
//     .then(data => {
//         data.forEach(escena => {
//             let entity = document.createElement('a-entity');
//             entity.setAttribute('gltf-model', `url(${escena.archivo})`);
//             entity.setAttribute('position', '0 1 -3');
//             document.querySelector('a-scene').appendChild(entity);
//         });
//     })
//     .catch(error => console.error('Error:', error));

fetch('http://127.0.0.1:8000/api/escenas/')
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (!Array.isArray(data)) {
            throw new Error("La respuesta no es un array válido.");
        }

        const scene = document.querySelector('a-scene');
        if (!scene) {
            throw new Error("No se encontró el elemento <a-scene> en el DOM.");
        }

        data.forEach(escena => {
            if (!escena.archivo) {
                console.warn("Escena sin archivo 3D:", escena);
                return;
            }

            let entity = document.createElement('a-entity');
            entity.setAttribute('gltf-model', `url(${escena.archivo})`);
            entity.setAttribute('position', '0 1 -3');
            entity.setAttribute('crossorigin', 'anonymous'); // Para evitar problemas de CORS
            scene.appendChild(entity);
        });
    })
    .catch(error => console.error('Error al cargar las escenas:', error));
