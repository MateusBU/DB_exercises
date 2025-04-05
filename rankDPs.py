import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import occurrences as oc

engine = sa.create_engine("sqlite:///DB/occurrences.db")
Session= orm.sessionmaker(bind=engine)
session = Session()
'''
Suppose that the Secretary of State for Civil Police asked you to present a
ranking of all Police Stations, located in the Capital, through the
number of occurrences.
'''
# check the table
rankDP = pd.DataFrame(
    session.query(
        oc.dp.name.label("DP"),
        sa.func.sum(oc.occurrences.qtde).label("Total")
    ).join(
        oc.occurrences,
        oc.occurrences.codeDP == oc.dp.codeDP
    ).join(
        oc.municipality,
        oc.occurrences.codeIBGE == oc.municipality.codeIBGE
    ).where(
        oc.municipality.region == "Capital"
    ).group_by(
        oc.dp.name
    ).order_by(
        sa.func.sum(oc.occurrences.qtde).label("Total").desc()
    ).all()
)

print(rankDP)