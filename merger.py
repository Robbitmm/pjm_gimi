from modulos.docMerger import *

class main:
    def __init__(self):
        self.main()

    def main(self):
        path1 = input('Insira o caminho dos documentos do Word que deseja juntar: ')

        mergeDocs = docManager()

        mergeDocs.merger(path1)

if __name__ == "__main__":
    main()

