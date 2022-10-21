class Character():
    def __init__(self,name,image,answer):
        self.name = name
        self.image = image
        self.answer_list = answer
    def chat(self,num):
        return self.answer_list[num]
