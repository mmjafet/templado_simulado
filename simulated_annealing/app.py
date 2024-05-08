from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

# Página principal con el formulario para seleccionar el script a ejecutar
@app.route('/')
def index():
    return render_template('index.html', resultado=None)

# Acción para ejecutar el script seleccionado
@app.route('/execute', methods=['POST'])
def execute():
    # Obtiene el script seleccionado del formulario
    script_name = request.form.get('script')

    # Define el comando para ejecutar el script Python
    script_path = f"{script_name}.py"

    # Ejecuta el script y captura la salida estándar y la salida de error
    process = subprocess.Popen(
        ["python3", script_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()  # Obtiene la salida y los errores

    # Determina si hubo errores o se ejecutó correctamente
    if stderr:
        resultado = f"Error: {stderr.decode('utf-8')}"  # Captura y muestra los errores
    else:
        resultado = stdout.decode("utf-8")  # Muestra la salida del script

    # Renderiza la plantilla con el resultado
    return render_template('index.html', resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
