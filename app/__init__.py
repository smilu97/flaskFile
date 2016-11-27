from flask import Flask 
app = Flask(__name__)
import os

STATIC_DIR = os.getcwd() + '/file/'

def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(STATIC_DIR, filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)

@app.route('/<path:path>')
def servFile(path):  # pragma: no cover
    mimetypes = {
        ".css": "text/css",
        ".html": "text/html",
        ".js": "application/javascript",
        ".jpg": "image/jpeg",
        ".png": "image/png"
    }
    while True :
    	idx = path.find('..')
    	if idx == -1 : break
    	path = path[idx+1:]
    complete_path = os.path.join(STATIC_DIR, path)
    ext = os.path.splitext(path)[1]
    mimetype = mimetypes.get(ext, "text/html")
    content = get_file(complete_path)
    return Response(content, mimetype=mimetype)

if __name__=='__main__':
	app.run(debug=True)