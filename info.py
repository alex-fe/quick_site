from datetime import datetime
from html import escape

counter = 0


class Project(object):
    def __init__(self, title, desc, date_=None, url=None, image=None):
        global counter
        self.id = counter
        counter += 1

        self.title = title
        self.url = url
        self.desc = desc
        self.image = image
        if date_:
            self.date = datetime.strptime(date_, '%Y-%m-%d')
        else:
            self.date = None

    def __repr__(self):
        return self.title

    @property
    def slug(self):
        return ' '.join(self.title.split()[:3]).lower().replace(" ", '-')


with open(
    "/Users/alexfeldman/CS/Personal_site/alex_site_2/static/project_script.txt", "r"
) as file_:
    contents = escape(file_.read())
contents = contents.split("\n\n\n")


projects = [
    Project(
        'Full Stack Developer at ShareYourself',
        contents[0].strip(),
        None,
        "https://beta.shareyourself.org/",
        'ShareYourselfLogo.svg'
    ),
    Project(
        'SMS Movie Bot',
        contents[1].strip(),
        "2018-09-28",
        None,
        "movie_bot.gif"
    ),
    Project(
        'Graphml to .SVG Converter',
        contents[2].strip(),
        "2018-11-29",
        "https://pypi.org/project/graphml2svg/",
        'Random.jpg'
    )
]
