# Chatbot con OpenAI y OpenRouter

Este es un chatbot basado en OpenAI que utiliza la API de OpenRouter para generar respuestas a preguntas del usuario.

## Requisitos

Antes de ejecutar este código, asegúrate de tener instalado lo siguiente:

- Python 3.7 o superior
- Virtualenv (opcional, pero recomendado)
- Las siguientes librerías de Python:
  - `openai`
  - `python-dotenv`

## Instalación

1. Clona este repositorio:
   ```sh
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # En macOS/Linux
   .venv\Scripts\activate     # En Windows
   ```

3. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```

4. Crea un archivo `.env` en la raíz del proyecto y agrega tu clave de API:
   ```ini
   API_KEY_OR=tu_api_key_aqui
   ```

## Uso

Ejecuta el script con:
```sh
python app.py
```

Luego puedes interactuar con el chatbot escribiendo preguntas en la terminal. Para salir, escribe `exit`.

## Licencia

Este proyecto está bajo la licencia MIT. Puedes modificarlo y distribuirlo libremente.

---

### Notas adicionales
- Asegúrate de registrar una cuenta en [OpenRouter](https://openrouter.ai/) y obtener tu API Key.
- Si encuentras algún problema, revisa que las variables de entorno estén correctamente configuradas y que el entorno virtual esté activado antes de ejecutar el script.

