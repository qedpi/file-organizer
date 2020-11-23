import os

DOWNLOAD_DIR = os.path.join('D:', '0 Downloads')
DST_DIRS = {'comedy': os.path.join('D:', 'comedy')}
VIDEO_EXTENSIONS = [f'.{ext}' for ext in 'mkv mp4'.split()]

COMEDY_TAGS = '''
Stephen.Colbert 
Seth.Meyers
Bill.Maher
Jimmy.Kimmel 
Jimmy.Fallon
James.Corden
Samantha.Bee
Daily.Show
'''

genres = {'comedy': COMEDY_TAGS}
genre_of = {}

for name, tags in genres.items():
    for label in tags.split():
        genre_of[label] = name
