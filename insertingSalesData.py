import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import sales as sls

address = "C:\\Users\\mateu\\Documents\\PUCRS\\Pos-graduação\\BancodeDados\\"

seller = pd.read_csv(address + "seller.csv", sep = ";")

tbSeller = pd.DataFrame(seller)

engine = sa.create_engine("sqlite:///DB/sales.db")

session = orm.sessionmaker(bind=engine)
session = session()

for i in range(len(tbSeller)):
    data_seller = sls.seller(
        register_seller = int(tbSeller['register_seller'][i]),
        cpf = tbSeller['cpf'][i],
        name_seller = tbSeller['name_seller'][i],
        email_address = tbSeller['email_address'][i],
        gender = tbSeller['gender'][i],
    )
    try:
        session.add(data_seller)
        session.commit()
    except ValueError:
        ValueError()

print("Seller inserted on tbSeller")    