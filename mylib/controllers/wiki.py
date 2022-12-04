import wikipedia


def wiki(name="War Goddess", length=1):
    """This is a wikipedia fetcher"""
    print('calling wiki')
    my_wiki = wikipedia.summary(name, length)
    print('my_wiki: ' + my_wiki)
    return my_wiki

def search_wiki(name):
    """Search Wikipedia for names"""

    results = wikipedia.search(name)
    return results