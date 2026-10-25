from flask import Flask, render_template, request
from dsa import LinkedList, Stack, InfixToPostfix, ReverseStrings, Queue
import math


app = Flask(__name__)
my_linked_list = LinkedList()
my_stack = Stack()
my_queue = Queue()

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
        input_value = request.form.get('inputValue', '')
        input_node = request.form.get('inputNode', '')
        selected_action = request.form.get('action', '')

        try:

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
                if removed_data is None:
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
            result = "An error has occurred!"

    current_list = my_linked_list.to_list()
    return render_template('linkedlist.html', list_values=current_list, result=result)

@app.route('/works/stack', methods=['GET', 'POST'])
def stack():
    result = None
    if request.method == "POST":
        input_value = request.form.get('inputValue', '').strip()
        selected_action = request.form.get('action', '')

        try:
            if selected_action == "push":
                my_stack.push(input_value)
                result = f"{input_value}, successfully added!"
            elif selected_action == "pop":
                removed_data = my_stack.pop()
                if removed_data is None:
                    result = "The stack is already empty!"
                else:
                    result = f"{removed_data}, successfully removed!"
            elif selected_action == "peek":
                top = my_stack.peek()
                if top is None:
                    result = "The stack is empty!"
                else:
                    result = f"{top}, is at the top!"

            elif selected_action == "is_empty":
                if my_stack.is_empty():
                    result = "The stack is empty"
                else:
                    result = "The stack contains elements/items"
            else:
                raise KeyError

        except Exception as e:
            print("ERROR", e)
            result = "An error has occurred!"

    current_stack = my_stack.to_list()
    return render_template('stack.html', list_values=current_stack, result=result)

@app.route('/works/stack/reversestrings', methods=['GET', 'POST'])
def reversestrings():
    result = None
    if request.method == "POST":
        string_input = request.form.get('inputString', '')

        try:
            reversed_string = ReverseStrings(string_input)
            result = reversed_string.reverse()

        except Exception as e:
            print("ERROR:", e)
            result = "An error has occurred!"
    return render_template('reversestrings.html', result=result)


@app.route('/works/stack/infixtopostfix', methods=['GET', 'POST'])
def infixtopostfix():
    result = None
    if request.method == "POST":
        equation_input = request.form.get('inputEquation', '')

        try:
            equation = InfixToPostfix(equation_input)
            result = equation.parse()

        except Exception as e:
            print("ERROR:", e)
            result = "An error has occurred!"

    return render_template('infixtopostfix.html', result=result)

@app.route('/works/queuedequeue', methods=['GET', 'POST'])
def queuedequeue():
    result = None
    if request.method == "POST":
        input_value = request.form.get('inputValue', '')
        selected_action = request.form.get('action', '')

        try:
            if selected_action == "enqueue":
                my_queue.enqueue(input_value)
                result = f"{input_value}, successfully added!"
            elif selected_action == "dequeue":
                removed_data = my_queue.dequeue()
                if removed_data is None:
                    result = "The queue is empty!"
                else:
                    result = f"{removed_data}, successfully removed!"
            elif selected_action == "is_empty":
                if my_queue.is_empty():
                    result = "The queue is empty"
                else:
                    result = "The stack contains elements/items"
            elif selected_action == "get_size":
                size = my_queue.get_size()
                result = f"The size of the queue is {size}"
            else:
                raise KeyError

        except Exception as e:
            print("ERROR!", e)
            result = "An error has occurred!"

    current_queue = my_queue.to_list()
    return render_template('queuedequeue.html', list_values=current_queue, result=result)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)