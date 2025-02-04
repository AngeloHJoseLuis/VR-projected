fetch('http://127.0.0.1:8000/api/escenas/')
    .then(response => response.json())
    .then(data => {
        data.forEach(escena => {
            let entity = document.createElement('a-entity');
            entity.setAttribute('gltf-model', `url(${escena.archivo})`);
            entity.setAttribute('position', '0 1 -3');
            document.querySelector('a-scene').appendChild(entity);
        });
    })
    .catch(error => console.error('Error:', error));
