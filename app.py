from engine import get_animal
from flask import Flask, request

app = Flask(__name__)

@app.route('/image', methods=['POST'])
def import_image():
    animal = { "count" : 0 , "animal" : "nil"}
    file = request.files.get('data')
    if file:
        file.save('image.jpg')
        animal = get_animal()
    return animal

@app.route('/healthcheck' , methods=['GET'])
def healthcheck():
    print("STATUS OK")
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
