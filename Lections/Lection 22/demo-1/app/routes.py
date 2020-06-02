from app import app

counter = 0

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/test2')
def test():
    global counter
    counter += 1
    return 'Yeeehaaaa! {}'.format(counter)