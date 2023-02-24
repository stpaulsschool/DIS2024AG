from app import app
#@app.route('/')
#def default():
    #return "<h2> Hello this is the default route"

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Andrew'}

    return """
    <html>
        <head>
            <title>Homepage - Microblog</title>
            </head>
            <body>
                <h1>Hello, """+user['username'] + """!</h1>
            </body>
    </html>
            """
