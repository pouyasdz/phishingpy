# import
import json
from src import script

# application class
app = script.application

# main class for select template and run script
class main:
    def __init__(self):
        template = self.getPages()
        app(template)
    
    def getPages(self):
        platformList = []
        templateList = []
        # read json config and load with json format
        templates = open("./src/config.json")
        jsonTemplates = json.load(templates)
        
        # close open config file
        templates.close()
        
        # all pages(templates)
        pages = jsonTemplates["pages"]
        
        for keys in pages.keys():
            platformList.append(keys)
            
        for item in platformList:
            print("[0{}] {} \n".format(platformList.index(item), item))
        
        try:
            selectPlatform = int(input(">> "))
            
            # check if index exist
            platformList[selectPlatform]
            
            templatesFromSelectedPlatform = pages[platformList[selectPlatform]]
            
            for keys in templatesFromSelectedPlatform.keys():
                templateList.append(keys)
                
            for item in templateList:
                print("[0{}] {} \n".format(templateList.index(item), item))
            
            selectedPage = int(input(">> "))
            
            finalTarget =  templatesFromSelectedPlatform[templateList[selectedPage]]
            
            return finalTarget
        except IndexError:
            print("not avalable !")
        except ValueError:
            print("enter just number!")
        
        
if __name__ == "__main__":
    main()