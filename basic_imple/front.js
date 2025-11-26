        // FUNCIÓN 1: Enviar datos al endpoint POST /saludar
        async function enviarDatos() {

            // Tomamos el nombre escrito en el input
            const nombreUsuario = document.getElementById('inputNombre').value;

            // Enviamos la petición al backend usando fetch
            const response = await fetch('http://127.0.0.1:8000/saludar', {
                method: 'POST',        // Método HTTP Post
                headers: {
                    'Content-Type': 'application/json'  // Indicamos que enviamos JSON
                },
                body: JSON.stringify({ nombre: nombreUsuario })  
                // Convertimos nuestro dato a JSON antes de enviarlo
            });

            if (!response.ok) {
                const error = await response.json();
                document.getElementById('textoRespuesta').innerText = "ERROR: " + error.detail;
                return;
            }

            // Convertimos la respuesta a JSON
            const data = await response.json();

            // Mostramos la respuesta en el HTML
            document.getElementById('textoRespuesta').innerText = data.respuesta;
        }

        async function enviarDespedida(){
            const nombreUsuario = document.getElementById('inputNombre').value;
            const response = await fetch('http://127.0.0.1:8000/despedir', {
                method: 'POST',        // Método HTTP Post
                headers: {
                    'Content-Type': 'application/json'  // Indicamos que enviamos JSON
                },
                body: JSON.stringify({ nombre:nombreUsuario})
            });

            if (!response.ok) {
                const error = await response.json();
                document.getElementById('textoRespuesta').innerText = "ERROR: " + error.detail;
                return;
            }

            const data = await response.json();
            document.getElementById('textoRespuesta').innerText = data.respuesta;
        }


    

        

    