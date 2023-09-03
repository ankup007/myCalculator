from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to perform the calculation
def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operator"

@app.route('/calculate', methods=['POST'])
def calculate_endpoint():
    try:
        data = request.get_json()
        a = float(data.get('a'))
        b = float(data.get('b'))
        operator = data.get('operator')

        result = calculate(a, b, operator)
        response = {'result': result}
        return jsonify(response)
    except ValueError:
        return jsonify({'error': 'Invalid input. Please enter valid numbers.'}), 400
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
