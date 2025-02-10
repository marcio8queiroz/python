import os
import pathlib

print("----------------------------------")
print("Usando o módulo os")
print("----------------------------------")
print(os.getcwd())
print("Listando os arquivos do diretório atual", os.listdir())
# os.mkdir("eije")
# os.rmdir("eije")
caminho_os = os.path.join(os.getcwd(), "conjuntos.py")
print("o caminho é = ", caminho_os)
print("é arquivo?", os.path.isfile("conjuntos.py"))
print("é diretório?", os.path.isdir("erp"))

print("----------------------------------")
print("Usando o módulo pathlib")
print("----------------------------------")
print(pathlib.Path.cwd())
print("Listando os  arquivos do diretório atual", list(pathlib.Path(".").iterdir()))
# pathlib.Path("eije").mkdir()
# pathlib.Path("eije").rmdir()
caminho_path = pathlib.Path(pathlib.Path.cwd()) / "conjuntos.py"
print("o caminho é = ", caminho_path)

print("é arquivo?", caminho_path.is_file())
print("é diretório?", caminho_path.is_dir())