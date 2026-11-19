from flask import Flask, render_template, request
from modules.dsa import LinkedList, Stack, InfixToPostfix, ReverseStrings, Queue
from modules.sort import ALGORITHMS, run_sort_with_steps
from modules.binarytree import BinaryTree, build_tree_from_sequence
import math
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
my_linked_list = LinkedList()
my_stack = Stack()
my_queue = Queue()

@app.route('/')
def cake():
    return render_template('cake.html')

@app.route('/portfolio')
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
        radius_input = request.form.get('inputRadius', '0').strip()
        
        try:
            radius = float(radius_input)
            if radius < 0:
                result = "Error: Radius cannot be negative!"
            else:
                result = f"{math.pi * (radius ** 2):.2f}"
        except ValueError:
            result = "Error: Please enter a valid number!"
        except Exception as e:
            print("ERROR!", e)
            result = "An error has occurred!"

    return render_template('areaofacircle.html', result=result)

@app.route('/works/area/areaofatriangle', methods=['GET', 'POST'])
def areaofatriangle():
    result = None
    if request.method == 'POST':
        base_input = request.form.get('inputBase', '0').strip()
        height_input = request.form.get('inputHeight', '0').strip()

        try:
            base, height = float(base_input), float(height_input)
            if base < 0 or height < 0:
                result = "Error: Base and height cannot be negative!"
            else:
                result = (base * height) / 2
        except ValueError:
            result = "Error: Please enter a valid number!"
        except Exception as e:
            print("ERROR!", e)
            result = "An error has occurred!"
    
    return render_template('areaofatriangle.html', result=result)

@app.route('/works/linkedlist', methods=['GET', 'POST'])
def linkedlist():
    result = None
    selected_action = 'insert_at_beginning'  
    
    if request.method == 'POST':
        input_value = request.form.get('inputValue', '').strip()
        input_node = request.form.get('inputNode', '').strip()
        selected_action = request.form.get('action', 'insert_at_beginning').strip()
        
        try:
            if selected_action == "insert_at_beginning":
                if not input_value:
                    result = "Error: Value cannot be empty or spaces only!"
                else:
                    my_linked_list.insert_at_beginning(input_value)
                    result = f"{input_value}, successfully added!"

            elif selected_action == "insert_at_end":
                if not input_value:
                    result = "Error: Value cannot be empty or spaces only!"
                else:
                    my_linked_list.insert_at_end(input_value)
                    result = f"{input_value}, successfully added!"

            elif selected_action == "insert_after":
                if not input_node or not input_value:
                    result = "Error: Target node and new value cannot be empty or spaces only!"
                else:
                    inserted = my_linked_list.insert_after(input_node, input_value)
                    if inserted:
                        result = f"{input_value}, was successfully added after {input_node}!"
                    else:
                        result = f"Task aborted. {input_node} not found!"

            elif selected_action == "remove_at_beginning":
                removed_data = my_linked_list.remove_beginning()
                if removed_data is None:
                    result = "The linked list is already empty!"
                else:
                    result = f"{removed_data}, successfully removed!"

            elif selected_action == "remove_at_end":
                removed_data = my_linked_list.remove_at_end()
                if removed_data is None:
                    result = "The linked list is already empty!"
                else:
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
            print("ERROR!", e)
            result = "An error has occurred!"

    current_list = my_linked_list.to_list()
    return render_template('linkedlist.html', list_values=current_list, result=result, selected_action=selected_action)

@app.route('/works/stack', methods=['GET', 'POST'])
def stack():
    result = None
    selected_action = 'push'

    if request.method == "POST":
        selected_action = request.form.get('action', 'push')
        input_value = request.form.get('inputValue', '').strip()

        try:
            if selected_action == "push":
                if not input_value:
                    result = "Error: Value cannot be empty or spaces only!"
                else:
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
    return render_template('stack.html', list_values=current_stack, result=result, selected_action=selected_action)

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
    selected_action = 'enqueue' 
    
    if request.method == "POST":
        input_value = request.form.get('inputValue', '').strip()
        selected_action = request.form.get('action', 'enqueue')
        
        try:
            if selected_action == "enqueue":
                if not input_value:
                    result = "Error: Value cannot be empty or spaces only!"
                else:
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
                    result = "The queue contains elements/items"
            elif selected_action == "get_size":
                size = my_queue.get_size()
                result = f"The size of the queue is {size}"
            else:
                raise KeyError
                
        except Exception as e:
            print("ERROR!", e)
            result = "An error has occurred!"

    current_queue = my_queue.to_list()
    return render_template('queuedequeue.html', list_values=current_queue, result=result, selected_action=selected_action)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    success = None

    if request.method == "POST":
        subject_name = (request.form.get("subject_name") or "").strip()
        sender_email = (request.form.get("email") or "").strip()
        message_body = (request.form.get("message") or "").strip()

        receiver_email = os.getenv("MAIL_USERNAME")
        app_password = os.getenv("MAIL_PASSWORD")

        if not subject_name or not sender_email or not message_body:
            success = False
        elif not receiver_email or not app_password:
            print("Transmission failed: MAIL_USERNAME or MAIL_PASSWORD is missing.")
            success = False
        else:
            msg = MIMEMultipart()
            msg["Subject"] = f"[Aperture Dispatch] Transmission from {subject_name}"
            msg["From"] = receiver_email
            msg["To"] = receiver_email
            msg["Reply-To"] = sender_email

            body = (
                f"Subject / Name: {subject_name}\n"
                f"Sender Email: {sender_email}\n\n"
                f"Message:\n{message_body}"
            )
            msg.attach(MIMEText(body, "plain"))

            try:
                with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as server:
                    server.starttls()
                    server.login(receiver_email, app_password)
                    server.sendmail(receiver_email, receiver_email, msg.as_string())
                success = True
            except Exception as e:
                print(f"Transmission failed: {e}")
                success = False

    return render_template("contact.html", success=success)

def _parse_tree_tokens(raw_text):
    """Parse comma-separated tokens; use '#' or 'null' to represent empty child slots."""
    if not raw_text or not raw_text.strip():
        return []
    tokens = [t.strip() for t in raw_text.replace("\n", ",").split(",") if t.strip()]
    parsed = []
    for tok in tokens:
        if tok.lower() in {"#", "null", "none", "-"}:
            parsed.append(None)
        else:
            parsed.append(tok)
    return parsed

def _serialize_level_order(bt):
    """Serialize current tree back into comma-separated level-order tokens."""
    if not bt.root:
        return ""
    out = []
    queue = [bt.root]
    while queue:
        curr = queue.pop(0)
        out.append(str(curr.value))
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return ", ".join(out)

@app.route("/tree", methods=["GET", "POST"])
def tree():
    default_seq = "A, B, C, D, E, F, G"
    raw_values = default_seq
    operation = "build"
    parent_val = ""
    child_val = ""
    target_val = ""
    status_log = "Initialized binary tree using BinaryTree class."
    highlighted_val = None
    error_message = None

    if request.method == "POST":
        operation = request.form.get("operation", "build")
        raw_values = request.form.get("values", "").strip()
        parent_val = request.form.get("parent_val", "").strip()
        child_val = request.form.get("child_val", "").strip()
        target_val = request.form.get("target_val", "").strip()

        try:
            tokens = _parse_tree_tokens(raw_values)
            bt = build_tree_from_sequence(tokens)

            if operation == "set_root":
                root_input = target_val or child_val
                if not root_input:
                    raise ValueError("Provide a Target / Root Value to set or replace root.")
                bt.set_root(root_input)
                raw_values = _serialize_level_order(bt)
                highlighted_val = root_input
                status_log = f"Set '{root_input}' as root node."

            elif operation == "search":
                query_val = target_val or parent_val or child_val
                if not query_val:
                    raise ValueError("Provide a Target Value to search for in the tree.")
                found = bt.search(query_val)
                if not found:
                    raise ValueError(f"Node '{query_val}' not found in binary tree.")
                highlighted_val = str(found.value)
                status_log = f"Search hit: located node '{found.value}' in tree."

            elif operation == "delete":
                del_val = target_val or parent_val
                if not del_val:
                    raise ValueError("Provide a Target Value to delete from the tree.")
                removed = bt.delete_node(del_val)
                if not removed:
                    raise ValueError(f"Node '{del_val}' not found; nothing deleted.")
                raw_values = _serialize_level_order(bt)
                status_log = f"Deleted node '{del_val}' from binary tree."

            elif operation == "insert_left":
                if not parent_val or not child_val:
                    raise ValueError("Provide both Parent Node and New Child Value to insert left.")
                target_node = bt.search(parent_val)
                if not target_node:
                    raise ValueError(f"Parent node '{parent_val}' not found in tree.")
                bt.insert_left(target_node, child_val)
                raw_values = _serialize_level_order(bt)
                highlighted_val = child_val
                status_log = f"Inserted '{child_val}' to the left of '{target_node.value}'."

            elif operation == "insert_right":
                if not parent_val or not child_val:
                    raise ValueError("Provide both Parent Node and New Child Value to insert right.")
                target_node = bt.search(parent_val)
                if not target_node:
                    raise ValueError(f"Parent node '{parent_val}' not found in tree.")
                bt.insert_right(target_node, child_val)
                raw_values = _serialize_level_order(bt)
                highlighted_val = child_val
                status_log = f"Inserted '{child_val}' to the right of '{target_node.value}'."

            elif operation == "clear":
                raw_values = ""
                bt = BinaryTree(None)
                status_log = "Binary tree cleared."

            else:
                status_log = f"Constructed binary tree with {bt.count_nodes()} node(s)."

        except ValueError as exc:
            error_message = str(exc)
            bt = build_tree_from_sequence(_parse_tree_tokens(raw_values))

    else:
        bt = build_tree_from_sequence(_parse_tree_tokens(raw_values))

    preorder_str = bt.preorder_traversal(bt.root, "").strip()
    inorder_str = bt.inorder_traversal(bt.root, "").strip()
    postorder_str = bt.postorder_traversal(bt.root, "").strip()

    return render_template(
        "tree.html",
        raw_values=raw_values,
        operation=operation,
        parent_val=parent_val,
        child_val=child_val,
        target_val=target_val,
        status_log=status_log,
        highlighted_val=highlighted_val,
        error_message=error_message,
        levels=bt.to_levels(),
        node_count=bt.count_nodes(),
        tree_height=bt.height(),
        preorder_out=preorder_str if preorder_str else "EMPTY",
        inorder_out=inorder_str if inorder_str else "EMPTY",
        postorder_out=postorder_str if postorder_str else "EMPTY",
    )
    
@app.route("/sortingalgorithms", methods=["GET", "POST"])
def sortingalgorithms():
    selected_algo = "bubble"
    raw_input = "38, 27, 43, 3, 9, 82, 10"
    sorted_result = None
    algorithm_label = None
    error_message = None
    sort_steps = []

    if request.method == "POST":
        selected_algo = request.form.get("algorithm", "bubble")
        raw_input = request.form.get("numbers", "").strip()

        tokens = [token.strip() for token in raw_input.replace(",", " ").split() if token.strip()]
        if not tokens:
            error_message = "Please enter at least one number to sort."
        else:
            try:
                parsed_numbers = [float(t) if "." in t else int(t) for t in tokens]
                algorithm_label, sorted_result, sort_steps = run_sort_with_steps(selected_algo, parsed_numbers)
            except ValueError:
                error_message = "Invalid input detected. Enter numbers separated by commas or spaces."

    return render_template(
        "sortingalgorithms.html",
        algorithms=ALGORITHMS,
        selected_algo=selected_algo,
        raw_input=raw_input,
        sorted_result=sorted_result,
        algorithm_label=algorithm_label,
        error_message=error_message,
        sort_steps=sort_steps,
    )
    
if __name__ == "__main__":
    app.run(debug=True)