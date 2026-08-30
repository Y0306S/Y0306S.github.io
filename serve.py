"""Local preview. Save any HTML/CSS file and the browser reloads."""

from livereload import Server

server = Server()
server.watch("*.html")
server.watch("css/*.css")
server.watch("cv/*")
server.watch("img/*")
server.serve(port=5500, host="127.0.0.1", debug=True, open_url_delay=0.4)
