import pandas as pd
from pyparsing import anyOpenTag #biblioteca de manipulação de dados
import sqlalchemy as sa
import sqlalchemy.orm as orm
import occurrences as occurr

address = "C:\\Users\\mateu\\Documents\\PUCRS\\Pos-graduação\\BancodeDados\\"

dp = pd.read_csv(address + "DP.csv", sep=",")
responsible = pd.read_excel(address + "responsibleSP.xlsx")
city = pd.read_csv(address + "Municipio.csv", sep=",")
occurrences = pd.read_excel(address + "occurrences.xlsx")

tbDP = pd.DataFrame(dp)
tbResponsible = pd.DataFrame(responsible)
tbCity = pd.DataFrame(city)
tbOccurrences = pd.DataFrame(occurrences)

engine = sa.create_engine("sqlite:///DB/occurrences.db")

conn = engine.connect()

# Create MetaData instance
metadata = sa.MetaData()

Session = orm.sessionmaker(bind=engine)
session = Session()

#dp
DataDP = tbDP.to_dict(orient="records")
tableDPt = sa.Table(occurr.dp.__tablename__, metadata, autoload_with=engine)

try:
    conn.execute(tableDPt.insert(), DataDP)
    session.commit()
except Exception as e:
    print(f"Error inserting dp: {e}")
    session.rollback()  # Rollback if there’s an error
print("dp inserted on dp")
        
#Responsibledp
DataResponsible = tbResponsible.to_dict(orient="records")
tableResponsible = sa.Table(occurr.responsibleSP.__tablename__, metadata, autoload_with=engine)

try:
    conn.execute(tableResponsible.insert(), DataResponsible)
    session.commit()
except Exception as e:
    print(f"Error inserting dp: {e}")
    session.rollback()  # Rollback if there’s an error
print("Responsibledp inserted on tbResponsible")
        
#Municipality
DataMunicipality = tbCity.to_dict(orient="records")
tableMunicipality = sa.Table(occurr.municipality.__tablename__, metadata, autoload_with=engine)

try:
    conn.execute(tableMunicipality.insert(), DataMunicipality)
    session.commit()
except Exception as e:
    print(f"Error inserting dp: {e}")
    session.rollback()  # Rollback if there’s an error
        
print("city inserted on tbCity")
        
#occurrences
DataOccurrences = tbCity.to_dict(orient="records")
tableOccurrences = sa.Table(occurr.occurrences.__tablename__, metadata, autoload_with=engine)

try:
    conn.execute(tableOccurrences.insert(), DataOccurrences)
    session.commit()
except Exception as e:
    print(f"Error inserting dp: {e}")
    session.rollback()  # Rollback if there’s an error
        
print("occurrences inserted on tbOccurrences")
session.close()