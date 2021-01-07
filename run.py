import sanic
from datetime import datetime

now = datetime.now()
app = sanic.app.Sanic(name='xDash')
response = sanic.response
cur_time_short = now.strftime("[%Y-%m-%d %H:%M:%S]")

@app.route('/')
def func(request):
    return response.file('index.html')

@app.route('/login')
def func(request):
    return response.file('login.html')


@app.route('css/skeleton.css')
def func(request):
    return response.file('skeleton.css')

@app.route('css/normalize.css')
def func(request):
    return response.file('normalize.css')

@app.route('css/style.css')
def func(request):
    return response.file('style.css')

@app.route('js/auth.js')
def func(request):
    return response.file('auth.js')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
