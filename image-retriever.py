from urllib.request import urlretrieve  # Gets file from URL
import imghdr                           # Identify unknown file types
import os                               # Directory management


class ImageRetriever:
    def __init__(self):
        self.dir = "img/"
        self.url = "http://forums.na.leagueoflegends.com/"
        self.url += "board/attachment.php?attachmentid="
        first_id = 1
        final_id = 9999999
        id_length = len(str(final_id))

        if not os.path.exists(self.dir):
            os.makedirs(self.dir)

        for id in range(first_id, final_id + 1):
            status = ""
            try:
                self.get_file(id)
            except:
                status = " (not found)"
            print("Processed: {:{}}/{}{}".format
                  (id, id_length, final_id, status))

    def get_file(self, id):
        id = str(id)                      # Convert the int to a string
        file = self.dir + id              # Combine dir and id to get the file
        urlretrieve(self.url + id, file)  # Attempt to download the file
        ext = "." + imghdr.what(file)     # Find out what the file extension is
        os.rename(file, file + ext)       # Rename, adding the extension

imageRetriever = ImageRetriever()
