import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import occurrences as oc

engine = sa.create_engine("sqlite:///DB/occurrences.db")
Session= orm.sessionmaker(bind=engine)
session = Session()


'''
Suppose that the Delegate of the Vehicle Robbery and Theft Police Station has asked you for a
analysis related to the ranking of all DPs, through the total amount of
occurrences related to Theft and theft of Vehicles, in the countryside of the State of RJ
• The result of this ranking must be sent in a table, containing the following
Columns:
•DP
•Total
'''

rankDP = pd.DataFrame(
    session.query(
        oc.dp.name.label("DP"),
        sa.func.sum(oc.occurrences.qtde).label("Amount of occurrences")
    ).join(
        oc.occurrences,
        oc.occurrences.codeDP == oc.dp.codeDP
    ).join(
        oc.municipality,
        oc.occurrences.codeIBGE == oc.municipality.codeIBGE
    ).where(
        oc.municipality.region == "Interior",
        sa.or_(oc.occurrences.occurence == "roubo_veiculo",
               oc.occurrences.occurence == "furto_veiculos")
    ).group_by(
        oc.dp.name
    ).order_by(
        sa.func.sum(oc.occurrences.qtde).label("Amount of occurrences").desc()
    ).all()
)

print(rankDP)