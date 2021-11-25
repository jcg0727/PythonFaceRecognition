import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import cv2
from flask import Flask
from flask import request
import base64
import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
from flask.templating import render_template



app = Flask(__name__)


@app.route('/', methods = ['GET' , 'POST'])
def test():
    img = request.form['imgBase64']
    id11 = request.form['id1']
    pwd11 = request.form['pwd1']
    gubun11 = request.form['gubun1']
    img1 = img.split(",")[1]
    img2 = Image.open(BytesIO(base64.b64decode(img1)))
    plt.imshow(img2)
    imgarr = np.array(img2) 
    
    imgarr = cv2.cvtColor(imgarr, cv2.COLOR_BGR2RGB)
    a = 'test.jpg'
    cv2.imwrite(a, imgarr)
    
    ids = ["2021001004","2021001004","2021001004","2021001004","2021001004", "2021001004","2021001001","2021001001","2021001001","2021001001","2021001001","2021001001"] 

    img = cv2.imread(a, 1)
    img_t = cv2.resize(img,(64,64))
    img_t = img_t.reshape((1,64,64,3))
    
    model = tf.keras.models.load_model("my_brain.h5")
     
    predictions = model.predict(img_t)
    result = (np.argmax(predictions[0]))
    checkId = (ids[result])
    return render_template('test.jsp',a=checkId, b=id11, c=pwd11, d=gubun11)

@app.route('/attendance', methods = ['GET' , 'POST'])
def attendance():
    studentNo = request.form['studentNo1']
    print("0000000000000studentNo : " + studentNo)
    classNo = request.form['classNo1']
    print("0000000000000classNo : " + classNo)
    
    img = request.form['imgBase64']
    img1 = img.split(",")[1]
    img2 = Image.open(BytesIO(base64.b64decode(img1)))
    plt.imshow(img2)
    imgarr = np.array(img2) 
    
    imgarr = cv2.cvtColor(imgarr, cv2.COLOR_BGR2RGB)
    a = 'test.jpg'
    cv2.imwrite(a, imgarr)
    
    ids = ["2021001004","2021001004","2021001004","2021001004","2021001004", "2021001004","2021001001","2021001001","2021001001","2021001001","2021001001","2021001001"] 

    img = cv2.imread(a, 1)
    img_t = cv2.resize(img,(64,64))
    img_t = img_t.reshape((1,64,64,3))
    
    model = tf.keras.models.load_model("my_brain.h5")
     
    predictions = model.predict(img_t)
    result = (np.argmax(predictions[0]))
    checkId = (ids[result])
    print("0000000000000checkId : " + checkId)
    return render_template('attendance.jsp', a=checkId, b=studentNo, c=classNo)


if __name__ == '__main__':
    app.run(debug=True)
    cv2.waitKey(0)
    cv2.destroyAllWindows()