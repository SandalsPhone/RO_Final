from flask import Flask
from io import BytesIO
from matplotlib.figure import Figure
import base64

import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    f = Figure()
    ax = f.subplots()
    
    pred = pd.read_csv("https://raw.githubusercontent.com/Mingmong123/jupy/main/testy.csv")
    
    y = pred["test_y"]
    x = pred["Unnamed: 0"]
    
    ax.plot(x,y)
    ax.set(xlabel="Total Hari Lewat Setelah 26 November 2021", ylabel = "Harga Cabai Merah")
    ax.set_title("Prediksi Harga Cabai Rawit Merah Menggunakan Efek Musim")
    
    buf = BytesIO()
    f.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    
    return f"<img src='data:image/png;base64,{data}'/>"
    
if __name__  == '__main__':
        app.run(debug=True)
