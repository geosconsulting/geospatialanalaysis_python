import zipfile

zip= open("../dati/hancock.zip","rb")
zipShape =zipfile.ZipFile(zip)


for fileName in zipShape.namelist():
    out = open(fileName,"wb")
    out.write(zipShape.read(fileName))
    out.close()

import tarfile
tar = tarfile.open("hancock.tar.gz","w:gz")
tar.add("hancock.shp")
tar.add("hancock.shx")
tar.add("hancock.dbf")
tar.close()
#shpName,shxName,dbfName= zipShape.namelist()
# shpFile=open(shpName,"wb")
# shxFile=open(shxName,"wb")
# dbfFile=open(dbfName,"wb")
# 
# shpFile.write( zipShape.read( shpName))
# shxFile.write( zipShape.read( shxName))
# dbfFile.write( zipShape.read( dbfName))
# 
# shpFile.close()
# shxFile.close()
# dbfFile.close()