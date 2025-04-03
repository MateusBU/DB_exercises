import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import sales as sls

address = "\\seller.csv"

seller = pd.read_csv(address + "seller.csv", sep = ";")

tbSeller = pd.DataFrame(seller)

engine = sa.create_engine("sqlite:///DB/sales.db")

session = orm.sessionmaker(bind=engine)
session = session()

for i in range(len(tbSeller)):
    data_seller = sls.seller(
        register_supplier = int(tbSeller['register_supplier'][i]),
        register_supplier = int(tbSeller['register_supplier'][i]),
    )