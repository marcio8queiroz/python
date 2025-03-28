# import xml.etree.ElementTree as ET
from lxml import etree

# crregar um arquivo xml
arvore = etree.parse("nfe.xml")
raiz = arvore.getroot()
print(raiz)

# definindo o namespace
NS = {"nfe": "http://www.portalfiscal.inf.br/nfe"}

# listar valor do elemento cUF na tag <ide>
ide = arvore.find(".//nfe:ide", NS)
print(ide)

if ide is not None:
    cUF = ide.find("nfe:cUF", NS)
    print(f" valor da tag cUf = {cUF.text}")

# alter o nome doemitente

emitente = arvore.find(".//nfe:emit", NS)
print(emitente)

if emitente is not None:
    xNome = emitente.find("nfe:xNome", NS)
    print(f" valor da tag xNome = {xNome.text}")
    xNome.text = "Outra Empresa"
    print(f" valor da tag xNome = {xNome.text}")

# adicionando novas informações no xml
info_adicional = etree.Element("{http://www.portalfiscal.inf.br/nfe}InfoAdicionalT2Ti")
info_adicional.text = "Informação Adicionada pela Aplicação"
ide.append(info_adicional)

arvore.write("nfe2.xml", encoding="utf-8")