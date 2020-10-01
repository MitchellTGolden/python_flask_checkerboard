from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')        
def checkerboard():
    return render_template('index.html')
@app.route('/<int:num>')        
def checkerboard2(num):
    return render_template('index2.html', num = num)
@app.route('/<int:num>/<int:num2>')        
def checkerboard3(num, num2):
    return render_template('index3.html', num = num, num2 = num2)
@app.route('/<int:num>/<int:num2>/<string:color1>/<string:color2>')
def checkerboard4(num, num2, color1, color2):
    return render_template('index4.html', num = num, num2 = num2, color1 = color1, color2 = color2)



if __name__=="__main__":  
    app.run(debug=True)
