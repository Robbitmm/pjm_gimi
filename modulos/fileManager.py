import os, json, shutil

class fileManager:
    def readJson(self, json_path):
        data = open(json_path, encoding="utf-8")
        files = json.load(data,)
        
        return files    

    def nameDecoder(self, file_name):
        names_path = './config/nomenclaturas.json'
        name_meanings = self.readJson(names_path)
        name_properties = file_name.upper().split(".")

        produto, tipo, familia = name_properties[0], name_properties[1], name_properties[2]
        numero_sequencia, numero_variavel = name_properties[3], name_properties[4]
        bitola, material = name_properties[5][0], name_properties[5][1]

        name_properties = {
            "name": file_name,
            "produto": name_meanings["produtos"][produto]["nome"].capitalize(),
            "tensao": name_meanings["produtos"][produto]["tensao"].capitalize(),
            "tipo": name_meanings["tipos"][tipo].capitalize(),
            "familia": name_meanings["familias"][familia].capitalize(),
            "numero_sequencia": numero_sequencia,
            "numero_variavel": numero_variavel,
            "bitola": name_meanings["bitolas"][bitola].upper(),
            "material": name_meanings["materiais"][material].upper()
        }

        return name_properties

    def fileRootPath(self, file):
        paths = self.readJson('./config/config.json')
        path_padrao = paths["CAMINHO_PADRAO"]

        file_path = f"{path_padrao.upper()}/{file['tensao'].upper()} TENSÃO/{file['produto'].upper()}/{file['familia'].upper()}"
        file["caminho_padrao"] = file_path

        return file

    def fileInfo(self, from_path):
        files_on_path = os.listdir(from_path)
        files = []

        for file in files_on_path:
            try:
                filename, extension = os.path.splitext(file)
                extension = extension[1:]
                name_info = self.nameDecoder(filename)
                name_info = self.fileRootPath(name_info)

                if extension == "": extension = 'folder'

                name_info["extension"] = extension

                files.append(name_info)
            except:
                print('[Failed]')
                return
            
        return files
    
    def copy(self, to_path):
        files_info = []
        valid_extensions = ['txt']
        files_info = self.fileInfo(to_path)

        for file in files_info:            
            file_name = f"{file['name']}.{file['extension']}"

            if file['extension'].lower() not in valid_extensions: continue

            try:
                
                print(f"[Copiando]: {file_name}")

                shutil.copy(f"{file['caminho_padrao'].upper()}/{file_name.upper()}", f"{to_path.upper()}/{file_name.upper()}")
            except:
                print(f"[Arquivo não encontrado]: {file['name']}")
                continue