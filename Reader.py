
class Reader():
    def __init__(self,file_path):
        self.file_path = file_path
        self.content = []
    
    def get_content(self):
        file = open(self.file_path,"r")
        for line in file:
            line_list = line.strip("\n").split(" ")
            for x in  line_list:
                self.content.append(x)
        return self.content

print(Reader("ExampleProg.txt").get_content())
        
        
