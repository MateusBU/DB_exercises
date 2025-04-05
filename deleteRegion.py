import sqlalchemy as sa
import occurrences as oc

engine = sa.create_engine("sqlite:///DB/occurrences.db")

metadata = sa.MetaData()
sa.MetaData.reflect(metadata, bind=engine) #access data from the metadata (important to change some data)

#it is possible, because reflect was used
tbCity = metadata.tables[oc.municipality.__tablename__] 
print(tbCity.c.city)

deleteRegion = sa.delete(tbCity).where(
    tbCity.c.region == "Capital"
)
print(deleteRegion)

try:
    with engine.connect() as connection:
        connection.execute(deleteRegion)
        connection.commit()
    print("Data updated")
except ValueError:
    ValueError()
