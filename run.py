import sanic
from sanic import Blueprint
import pymongo
from datetime import datetime
import json
import bcrypt

now = datetime.now()
app = sanic.app.Sanic(name='AIO-API')
response = sanic.response
cur_time_short = now.strftime("[%Y-%m-%d %H:%M:%S]")

@app.route('/')
def func(request):
    return response.file('/home/onx/github/xDash/index.html')

@app.route('/login')
def func(request):
    return response.file('/home/onx/github/xDash/login.html')


@app.route('css/skeleton.css')
def func(request):
    return response.file('/home/onx/github/xDash/skeleton.css')

@app.route('css/normalize.css')
def func(request):
    return response.file('/home/onx/github/xDash/normalize.css')

@app.route('css/style.css')
def func(request):
    return response.file('/home/onx/github/xDash/style.css')

@app.route('js/auth.js')
def func(request):
    return response.file('/home/onx/github/xDash/auth.js')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)