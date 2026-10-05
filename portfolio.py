from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/works/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/works/area/areaofacircle', methods=['GET', 'POST'])
def areaofacircle():
    result = None
    if request.method == 'POST':
        radius_input = request.form.get('inputRadius', '0')
        
        try:
            radius = float(radius_input)
            result = f"{math.pi * (radius ** 2):.2f}"

        except:
            result = "Error: Please enter a valid number!"

    return render_template('areaofacircle.html', result=result)

@app.route('/works/area/areaofatriangle', methods=['GET', 'POST'])
def areaofatriangle():
    result = None
    if request.method == 'POST':
        base_input = request.form.get('inputBase', '0')
        height_input = request.form.get('inputHeight', '0')

        try:
            base, height = float(base_input), float(height_input)
            result = (base * height) / 2
        
        except:
            result = "Error: Please enter a valid number!"
    
    return render_template('areaofatriangle.html', result=result)

@app.route('/works/linkedlist')
def linkedlist():
    return render_template('linkedlist.html')
  
        

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)