from PIL import Image 
from pythumb import Thumbnail

size = (750, 422)

youtube_button = Image.open('data/youtube-button.png')

with open('links.txt', 'r') as links:
    content = links.readlines()
    index = 1
    for link in content:
        t = Thumbnail(link)
        t.fetch()
        t.save('data/thumbs', index)

        with Image.open(f'data/thumbs/{index}.jpg') as thumb:
            thumb.thumbnail(size)
            t2 = thumb.convert('L')
            thumb.paste(t2)
            thumb.paste(youtube_button, (0,0), youtube_button)
            thumb.save(f"data/final_thumbs/{index}.jpg")

        index += 1

