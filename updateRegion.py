import sqlalchemy as sa
import occurrences as oc

engine = sa.create_engine("sqlite:///DB/occurrences.db")

metadata = sa.MetaData()
sa.MetaData.reflect(metadata, bind=engine) #access data from the metadata (important to change some data)

#it is possible, because reflect was used
tbCity = metadata.tables[oc.municipality.__tablename__] 
print(tbCity.c.city)

updateRegion = sa.update(tbCity).values(
    {"region":"Rio de Janeiro"}
).where(
    tbCity.c.city == "Rio de Janeiro"
)
print(updateRegion)
try:
    with engine.connect() as connection:
        connection.execute(updateRegion)
        connection.commit()
    print("Data updated")
except ValueError:
    ValueError()
