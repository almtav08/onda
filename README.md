# Guía de instalación
1. Instalar la última versión de Python desde la web: [https://www.python.org/downloads/](https://www.python.org/downloads/)
    1. La instalación se debe hacer de manera personalizada y asegurandose de tener la casilla de ```Add Python to PATH``` marcada.
    2. Continuar con las pantallas de la instalación hasta finalizar el proceso. Es posible que sea necesario reiniciar el equipo.
2. Crear la carpeta donde se vaya a crear el chatbot.
3. Abrir un terminal del sistema en esta carpeta. Si no se desea usar un entorno virtual saltar pasos 4 y 5.
4. Crear un entorno virtual de Python con el siguiente comando:
    ```python -m venv venv```
5. Activar el entorno virtual con el siguiente comando:
    - En Windows:
        ```venv\Scripts\activate```
    - En Linux:
        ```source venv/bin/activate```
    - En MacOS:
        ```source venv/bin/activate```
6. Instalar las dependencias del proyecto con el siguiente comando:
    ```pip install gradio_client openai streamlit```


# Guía de ejecución
1. Para editar el código del chatbot es recomendable usar un editor de código como Visual Studio Code. Se puede editar con cualquier editor de texto plano.
2. Se tiene que crear un archivo ```.py```, por ejemplo, ```chat.py```.
3. Para obtener un chatbot funcional se deben de seguir todos los pasos (cada uno corresponde con un archivo)
4. Para ejecutar el chatbot se debe de ejecutar el siguiente comando en el terminal:
    ```streamlit run chat.py```

# Guía de despliegue
1. Seguir los pasos de la guía de despliegue oficial [https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app).
2. Se debe de tener una cuenta en Streamlit y en GitHub.
3. Se debe de tener un repositorio en GitHub con el código del chatbot.
4. Para poder subir el código a Github es necesario tener Git instalado. Se puede descargar desde [https://git-scm.com/downloads](https://git-scm.com/downloads).
5. Para subir el código se recomienda seguir los pasos de la guía oficial de GitHub [https://docs.github.com/es/get-started/quickstart/set-up-git](https://docs.github.com/es/get-started/quickstart/set-up-git).
