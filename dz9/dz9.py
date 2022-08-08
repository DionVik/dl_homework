#Классы тегов
class Tag:
    def __init__(self):
        self.tag = '<tag></tag>'

    def getHtml(self):
        return self.tag

class Image(Tag):
    def __init__(self):
        self.tag = '<img>'

class Input(Tag):
    def __init__(self):
        self.tag = '<input></input>'

class Text(Tag):
    def __init__(self):
        self.tag = '<p></p>'

class Link(Tag):
    def __init__(self):
        self.tag = '<a></a>'

#Класс интерфейса для фабрики тегов
class TagCreation:
    def createTag(self, tagType):
        tag_ = self.getTag(tagType)
        return tag_

    def getTag(self, tagType):
        pass
        
#Класс фабрики тегов        
class TagFactory(TagCreation):
    def getTag(self, tagType):
        if tagType == '':
            return Tag()
        elif tagType == 'image':
            return Image()
        elif tagType == 'input':
            return Input()
        elif tagType == 'p':
            return Text()
        elif tagType == 'a':
            return Link()
#------------------------------------- 
factory = TagFactory()
elements = ['image', 'input', 'p', 'a', '']
for el in elements:
    print(factory.createTag(el).getHtml())
