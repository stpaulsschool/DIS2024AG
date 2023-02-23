from app import app
@app.route('/')
@app.route('/index')
def index():
    return "Hello everyone in Year 11 Dis solutions. "
