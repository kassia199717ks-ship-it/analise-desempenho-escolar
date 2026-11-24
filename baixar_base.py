from pathlib import Path
from urllib.request import urlretrieve
from zipfile import ZipFile

destino = Path("dados")
destino.mkdir(exist_ok=True)
url = "https://archive.ics.uci.edu/static/public/320/student+performance.zip"
zip_path = destino / "student-performance-original.zip"

print("Baixando o arquivo oficial do UCI...")
urlretrieve(url, zip_path)

with ZipFile(zip_path) as arquivo:
    nome = next(n for n in arquivo.namelist() if n.endswith("student-por.csv"))
    conteudo = arquivo.read(nome)

saida = destino / "student-por.csv"
saida.write_bytes(conteudo)
print(f"Base original salva em: {saida}")
print("Não edite esse arquivo; o notebook trabalha com uma cópia em memória.")
