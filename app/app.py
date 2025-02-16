import os
from urllib.parse import urlparse
from flask import Flask, render_template

# Static directory
static_dir = 'static'

# Default Flask port
flask_port = 5000

# Use the absolute proxy path. If True, Application URL will be /absproxy/{{port}}/
use_absproxy = False

# Get the proxy URI from the environment variable
proxy_uri = os.getenv('VSCODE_PROXY_URI', '')
if use_absproxy:
    proxy_uri = proxy_uri.replace('/proxy', '/absproxy')
proxy_uri = proxy_uri.replace('{{port}}', str(flask_port))
proxy_path = urlparse(proxy_uri).path.rstrip('/') if proxy_uri else ''
static_path = f"{proxy_path}/{static_dir}" if proxy_path else f'/{static_dir}'

app = Flask(__name__, static_url_path=static_path, static_folder=static_dir)


if proxy_uri:
    class FixProxyPathMiddleware():
        def __init__(self, app: Flask, static_dir, proxy_path):
            self.app = app
            self.static_dir = static_dir
            self.proxy_path = proxy_path

        def __call__(self, environ, start_response):
            if use_absproxy:
                environ['PATH_INFO'] = environ['PATH_INFO'].removeprefix(self.proxy_path)

            # If the request is for the static directory, rewrite the path to include the proxy path
            if environ['PATH_INFO'].startswith(f'/{self.static_dir}'):
                environ['PATH_INFO'] = self.proxy_path + environ['PATH_INFO']

            return self.app(environ, start_response)

    app.wsgi_app = FixProxyPathMiddleware(app.wsgi_app, static_dir, proxy_path)


@app.route("/")
def home():
    return render_template("index.html")
