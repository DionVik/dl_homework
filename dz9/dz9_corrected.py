#Классы тегов
class Tag:
    tag = '<tag></tag>'

    def get_html(self):
        return self.tag

class Image(Tag):
    tag = '<img>'

class Input(Tag):
    tag = '<input></input>'

class Text(Tag):
    tag = '<p></p>'

class Link(Tag):
    tag = '<a></a>'

tags_map = {
    'image':Image,
    'input':Input,
    'p':Text,
    'a':Link,
    ' ':Tag
    }
#Класс фабрики тегов
class TagFactory():
    
    def create_tag(self, tag_type):
        tag_ = self.get_tag(tag_type)
        return tag_
        
    def get_tag(self, tag_type):
        tag = tags_map.get(tag_type)
        return tag()
# class TagFactory():
    
    # def create_tag(self, tagType):
        # tag_ = self.get_tag(tagType)
        # return tag_
        
    # def get_tag(self, tagType):
        # if tagType == '':
            # return Tag()
        # elif tagType == 'image':
            # return Image()
        # elif tagType == 'input':
            # return Input()
        # elif tagType == 'p':
            # return Text()
        # elif tagType == 'a':
            # return Link()
#------------------------------------- 
factory = TagFactory()
elements = ['image', 'input', 'p', 'a', ' ']
for el in elements:
    print(factory.create_tag(el).get_html())
