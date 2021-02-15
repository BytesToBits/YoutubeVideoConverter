import youtube_dl as yt

yt_options = {
    'outtmpl': '%(extractor)s-%(id)s-%(title)s-%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

source = yt.YoutubeDL(yt_options)

class YTSource:
    def __init__(self, url):
        self.url = url
    
    def convert(self, convertType):
        source.params['format'] = convertType

        data = source.extract_info(self.url, download=False)

        if 'entries' in data:
            data = data['entries'][0]

        return data