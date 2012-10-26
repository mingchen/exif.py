import pyexiv2

def foo():
    for i in range(290):
        file = 'xuelu/xuelu_%03d.jpg' % i
        exif = Exif(file);
        set_attr('Exif.Image.Artist', 'Xue Lu')

exif = Exif('test.jpg')
exif.get_attr('Exif.Image.Artist')

class Exif:
    def __init__(self, file):
        self.metadata = pyexiv2.ImageMetadata(file)
        self.metadata.read()

    def get_attr(self, name):
        return self.metadata[name]

    def set_attr(self, name, value):
        """
            name    EXIF attribute name e.g. 'Exif.Image.Artist'
            value   EXIF attribute value
        """
        metadata[name] = value
        metadata.write()

def main(argc, argv)
    pass

if __name__ == '__main__':
    main

