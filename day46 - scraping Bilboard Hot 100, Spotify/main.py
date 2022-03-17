from spoti import SpotiManager
from credentials import USER_ID, SECRET, URI

if __name__ == '__main__':
    manager = SpotiManager(URI, SECRET, USER_ID)
    manager.create_playlist()
