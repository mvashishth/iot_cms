from flask import Flask, Response, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def get_data():
    print("HELLO")
    return Response(request.data)

if __name__ == '__main__':
    app.run(debug=True)
