from db.database import Database
from helper.WriteAJson import writeAJson
from dataset.produto_database import dataset

compras = Database(database="database", collection="produtos", dataset=dataset)
#compras.resetDatabase()

result1 = compras.collection.aggregate([
    {"$group": {"_id": "$cliente_id", "total": {"$sum": "$total"} } }, # formata os documentos
    {"$sort": {"total": -1} } # ordena os documentos

    # percebam que não utilizamos o sifrão '$' no campo 'total' do Stage $sort
    # porque o campo 'total' é dos documentos formatados pelo Stage $group

		# Conceito de 'field paths' em pipeline expressions (DOCS)
])

writeAJson(result1,"result1")







