import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import occurrences as oc

engine = sa.create_engine("sqlite:///DB/occurrences.db")
Session= orm.sessionmaker(bind=engine)
session = Session()

'''
Suppose that the Governor of the State of Rio de Janeiro has called you and asked for an analysis
related to the ranking of all municipalities, through the total amount of
occurrences related to Vehicle Theft
'''

rankCity= pd.DataFrame(
    session.query(
        oc.municipality.city.label("City"),
        sa.func.sum(oc.occurrences.qtde).label("Amount of occurrences")
    ).join(
        oc.occurrences,
        oc.occurrences.codeIBGE == oc.municipality.codeIBGE #relationship btw foreing_key
    ).where(
        oc.occurrences.occurence == "furto_veiculos"
    ).group_by(
        oc.municipality.city
    ).order_by(
        sa.func.sum(oc.occurrences.qtde).label("Amount of occurrences").desc()
    ).all()
)

print(rankCity)