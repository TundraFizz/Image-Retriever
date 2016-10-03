from urllib.request import urlretrieve  # Gets file from URL
import imghdr                           # Identify unknown file types
import shutil                           # Delete directory recursively
import os                               # Directory management


class ImageRetriever:
    def __init__(self):
        self.record = ""
        self.dir = "img/"
        self.url = "http://forums.na.leagueoflegends.com/"
        self.url += "board/attachment.php?attachmentid="
        first_id = 1
        final_id = 9999999
        first_id = 999998
        final_id = 1000002
        id_length = len(str(final_id))
        self.initialize_directory()

        for id in range(first_id, final_id + 1):
            status = ""
            try:
                self.get_file(id)
                # Record in a text file that it was found
                target = open("found.txt", "a")
                target.write(self.record)
                target.close()
            except:
                # Record in a text file that it wasn't found
                status = " (not found)"
                target = open("not-found.txt", "a")
                target.write(self.record)
                target.close()

            print("Processed: {:{}}/{}{}".format
                  (id, id_length, final_id, status))

    def get_file(self, id):
        id = str(id)                      # Convert the int to a string
        self.record = id + "\n"           # Save a record of it for logging
        file = self.dir + id              # Combine dir and id to get the file
        urlretrieve(self.url + id, file)  # Attempt to download the file
        ext = "." + imghdr.what(file)     # Find out what the file extension is
        os.rename(file, file + ext)       # Rename, adding the extension
        self.record = id + ext + "\n"     # Save a record of it for logging

    def initialize_directory(self):
        try:
            os.remove("found.txt")
        except:
            pass

        try:
            os.remove("not-found.txt")
        except:
            pass

        if os.path.exists(self.dir):
            shutil.rmtree(self.dir)

        os.makedirs(self.dir)

imageRetriever = ImageRetriever()
