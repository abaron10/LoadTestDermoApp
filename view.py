
from flask import Flask
from flask import request
import os
import time

app = Flask(__name__)


@app.route('/crear_consulta',methods = ['POST'])
def Suma():
    message = ""
    user_name = os.getenv("user_name")
    
    if request.method == 'POST':
        try:
            nombre_paciente = request.json["nombre_paciente"] 
            apellido_paciente = request.json["apellido_paciente"]
            edad = request.json["edad"]
            rh = request.json["rh"]
            estado_civil = request.json["estado_civil"]
            eps = request.json["eps"]

        except:
            return {"message": "Inserte todos los datos para poder crear la consulta."}, 404

        time.sleep(0.5)
        return {"message": "consulta medica creada con exito"}, 200
        
        


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 4000))
    app.run(debug=True, host='0.0.0.0', port=port)