# imports the create app function from init.py
from website_stuff import create_app

app = create_app()
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024
# runs the flask application only if the main.py file is run directly
print('ALKSJDLFJDSALFSAJJDFLKFDSALKFJSALFKJDSAFLKSJFLKJDSFLKDSAKJFDSALKJFDSLKFSJDFLDSAJFLDSJFDSALKFJDSALKF')
if __name__ == '__main__':
    app.run(debug=True, port=5000)

