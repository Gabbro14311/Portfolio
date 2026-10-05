from flask import Flask, render_template, request
from dsa import LinkedList
import math


app = Flask(__name__)
my_linked_list = LinkedList()

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

@app.route('/works/linkedlist', methods=['GET', 'POST'])
def linkedlist():
    result = None
    if request.method == 'POST':
        try:
            input_value = request.form.get('inputValue', '')
            input_node = request.form.get('inputNode', '')
            selected_action = request.form.get('action', '')

            if selected_action == "insert_at_beginning":
                my_linked_list.insert_at_beginning(input_value)
                result = f"{input_value}, successfully added!"

            elif selected_action == "insert_at_end":
                my_linked_list.insert_at_end(input_value)
                result = f"{input_value}, successfully added!"

            elif selected_action == "insert_after":
                inserted = my_linked_list.insert_after(input_node, input_value)
                if inserted:
                    result = f"{input_value}, was sucessfully added after {input_node}!"
                else:
                    result = f"Task aborted. {input_node} not found!"
                    
            elif selected_action == "remove_at_beginning":
                removed_data = my_linked_list.remove_beginning()
                result = f"{removed_data}, successfully removed!"

            elif selected_action == "remove_at_end":
                removed_data = my_linked_list.remove_at_end()
                result = f"{removed_data}, successfully removed!"

            elif selected_action == "remove":
                removed_data = my_linked_list.remove_at(input_value)
                if removed_data == None:
                    result = f"{input_value} does not exist!"
                else:
                    result = f"{input_value}, successfully removed!"

            elif selected_action == "search":
                found = my_linked_list.search(input_value)
                
                if found:
                    result = f"{input_value} was found in the Linked List!"
                else:
                    result = f"{input_value} was not found in the Linked List!"

            else:
                raise KeyError



        except Exception as e:
            print("ERROR:", e)
            result = "An error has occured"

    current_list = my_linked_list.to_list()
    return render_template('linkedlist.html', list_values=current_list, result=result)

  
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)