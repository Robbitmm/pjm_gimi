from modulos.fileManager import *
from modulos.docMerger import *

class main:
    def __init__(self):
        self.main()

    def main(self):
        path = 'C:/Users/dudum/OneDrive/Área de Trabalho/Outros/Programação/Python/Automation/Gimi/PROCESSO/E-21123/Ordem de Serviço 1/Item 1/PROGRAMAÇÃO'
        path1 = 'C:/Users/dudum/OneDrive/Área de Trabalho/Outros/Programação/Python/Automation/Gimi/PROCESSO/E-21123/Ordem de Serviço 1/Item 1/DOCUMENTO'
        
        file_manager = fileManager()
        mergeDocs = docManager()
        docs_list = []

        docs = os.listdir(path1)
        for doc in docs:
            docs_list.append(os.path.join(path1, doc))

        mergeDocs.merger(docs_list)
        
        
        #files_copy = file_manager.copy(path)

        #print(files_copy)

if __name__ == "__main__":
    main()

