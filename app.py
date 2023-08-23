from flask import Flask, render_template, request, jsonify, Response
import privateGPT
import traceback
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    print("chat route called")
    try:
        message = request.form['message']
        response = privateGPT.run_model(message)
        print("this is flask print",response)
        print("result",response['result'])
        return jsonify({'response': response['result']})
        
        # # Convert the answer to a JSON string
        # answer_str = json.dumps(response, indent=4)
        
        # # Return the answer string with the correct content type
        # return Response(answer_str, content_type='text/plain; charset=utf-8')
    except Exception as e:
        print("Exception occurred:", str(e))
        return Response(str(e), status=500, content_type='text/plain; charset=utf-8')



if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host = '0.0.0.0', port=8080)
