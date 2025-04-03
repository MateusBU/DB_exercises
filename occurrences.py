import sqlalchemy as sa
import sqlalchemy.orm as orm

engine = sa.create_engine("sqlite:///DB/occurrences.db")

base = orm.declarative_base()

#responsible table
class responsibleSP(base):
    __tablename__ = "responsibleSP"
    #columns
    codeDP = sa.Column(sa.INTEGER, primary_key = True, index = True)
    delegate = sa.Column(sa.VARCHAR(100), nullable = False)

#dp table
class dp(base):
    __tablename__ = "dp"
    #columns
    codeDP = sa.Column(sa.INTEGER, primary_key = True, index = True)
    name = sa.Column(sa.VARCHAR(100), nullable = False)
    address = sa.Column(sa.VARCHAR(255), nullable = False)

#municipality table
class municipality(base):
    __tablename__ = "municipality"
    #columns
    codeIBGE = sa.Column(sa.INTEGER, primary_key = True, index = True)
    city = sa.Column(sa.VARCHAR(100), nullable = False)
    region = sa.Column(sa.VARCHAR(25), nullable = False)

#occurrences table
class occurrences(base):
    __tablename__ = "occurrences"
    #columns
    idRegister = sa.Column(sa.INTEGER, primary_key = True, index = True)
    codeDP = sa.Column(sa.INTEGER, sa.ForeignKey("dp.codeDP", ondelete = "NO ACTION", onupdate = "CASCADE"), index = True)
    codeIBGE = sa.Column(sa.INTEGER, sa.ForeignKey("municipality.codeIBGE", ondelete = "NO ACTION", onupdate = "CASCADE"), index = True)
    year = sa.Column(sa.CHAR(4), nullable = False)
    month = sa.Column(sa.VARCHAR(2), nullable = False)
    occurence = sa.Column(sa.VARCHAR(100), nullable = False)
    qtde = sa.Column(sa.INTEGER, nullable = False)


try:
    base.metadata.create_all(engine) #create tables
    print("Table created")
except ValueError:
    ValueError()