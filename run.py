import sanic
from datetime import datetime
from os import environ
from jinja2 import Environment, PackageLoader, select_autoescape
from firstclass_dotenv import Dotenv

dotenv = Dotenv

try:
    dotenv.load()
except:
    print("Could not .env file, using os environment variables...")

env = Environment(
    loader=PackageLoader("./public"),
    autoescape=select_autoescape(["html", "xml", "tpl"]),
    enable_async=True,
)


async def template(tpl, **kwargs):
    template = env.get_template(tpl)
    content = await template.render_async(kwargs)
    return response.html(content)


now = datetime.now()
app: sanic.Sanic = sanic.app.Sanic(name="xDash")
response = sanic.response
cur_time_short = now.strftime("[%Y-%m-%d %H:%M:%S]")
api_url = environ.get("API_URL", "http://localhost:6969/v1")
app.static("/", "./public")


@app.route("/")
def func(request):
    return template("index.j2", api_url=api_url)


@app.route("/login")
def func(request):
    return template("login.j2")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=environ.get("PORT", 8000))
