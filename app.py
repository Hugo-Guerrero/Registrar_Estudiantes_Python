from flask import Flask, request, jsonify
from supabase import create_client, Client
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Conectar con Supabase usando URL y API Key
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

app = Flask(__name__)

# Endpoint POST: agregar estudiante
@app.route('/estudiantes', methods=['POST'])
def agregar_estudiante():
    data = request.get_json()
    # Insertar en la tabla "estudiantes"
    nuevo = supabase.table("estudiantes").insert(data).execute()
    return jsonify({"mensaje": "Estudiante agregado exitosamente"}), 201

# Endpoint GET: obtener estudiantes
@app.route('/estudiantes', methods=['GET'])
def obtener_estudiantes():
    estudiantes = supabase.table("estudiantes").select("*").execute()
    return jsonify(estudiantes.data)

if __name__ == '__main__':
    app.run(debug=True)
