import facebook

class FbModule:
    def __init__(self):
        self.settings = {
            "page_id"      : "100002504936732",
            "access_token" : "EAADf9v7CVOoBAONgKPczcy9f3fKGNCleCQwKWkxVvtHZBdZBLH9UOveJdqCI8hGxhIROAqD3A17tVP4KBsXjX15Bo1hZA0I7hN5xVwbir5SYXD61dHMZAcyVvlDJUmlZB9rLrsF5QNC4kUFgTCpr8GCKfEvYzcn0ZD"
        }
        self.graph = self.getFbAPI(self.settings)

    def getFbAPI(self, settings):
        graph = facebook.GraphAPI(settings['access_token'])
        response = graph.get_object('me/accounts')
        pageAccessToken = None
        for page in response['data']:
            if page['id'] == settings['page_id']:
                pageAccessToken = page['access_token']
                graph = facebook.GraphAPI(page_access_token)
        return graph

    def postPhoto(self, photoPath, message):
        status = self.graph.put_photo(image=open(photoPath, 'rb'), message='Look at this cool photo!')
        print "Photo is posted."
