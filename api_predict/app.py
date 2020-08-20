# importar os pacotes necessários
import os

import numpy as np
import tensorflow as tf
from flask import Flask, jsonify, request, render_template, current_app
from flask_restful import Api

# instanciar Flask object
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
app.config['MEDIA_ROOT'] = os.path.join(PROJECT_ROOT, 'images/')
# api
api = Api(app)

# carregar modelo
model = tf.keras.models.load_model('model/my_model')

@app.route('/', methods = ['GET'])
def new():
   return render_template('upload.html')

@app.route('/uploader', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
      imagem = request.files.get('file')
      filename = secure_filename(imagem.filename)
      path = os.path.join(current_app.config['MEDIA_ROOT'], filename)
      imagem.save(path)

      test_image = image.load_img(path, target_size=(64, 64))
      test_image = image.img_to_array(test_image)
      test_image = np.expand_dims(test_image, axis=0)
      result = model.predict(test_image)
      print(result)
      alfa = result[0][0]
      if alfa == 1:
         prediction = 'dog'
      else:
         prediction = 'cat'
      return jsonify({'previsao': prediction})



if __name__ == '__main__':
    app.run()