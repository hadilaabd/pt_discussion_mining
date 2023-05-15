import xml.sax
import csv

class PostHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.Id = ""
        self.PostTypeId = ""
        self.Title = ""
        self.Body = ""
        self.Tags = ""
        self.post_count = 0
        self.csv_file = open('data/posts.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.csv_file)
        self.writer.writerow(['Id', 'PostTypeId', 'Title', 'Body', 'Tags'])

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "row":
            if self.post_count < 760000000:
                self.Id = attributes["Id"]
                self.Id = attributes["PostTypeId"]
                self.Title = attributes.get("Title", "")
                self.Body = attributes.get("Body", "")
                self.Tags = attributes.get("Tags", "")
                if self.Title != "" and self.Tags != "":
                    self.writer.writerow([self.Id, self.PostTypeId, self.Title, self.Body, self.Tags])
                    self.post_count += 1

    def endElement(self, tag):
        self.CurrentData = ""

    def characters(self, content):
        pass

    def xml_reader(file_path):
        xml_file = open(file_path, "r", encoding="utf-8")
        xml.sax.parse(xml_file, PostHandler())
        xml_file.close()

if __name__ == "__main__":
    PostHandler.xml_reader("data/Posts.xml")