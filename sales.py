import sqlalchemy as sa
import sqlalchemy.orm as orm

engine = sa.create_engine("sqlite:///DB/sales.db")

base = orm.declarative_base()

#client table
class client(base):
    __tablename__ = "client" #you must use tablename
    #columns        type of the columns "cpf"
    cpf = sa.Column(sa.VARCHAR(14), primary_key = True, index = True)
    name = sa.Column(sa.VARCHAR(100), nullable = False) #not null
    email_address = sa.Column(sa.VARCHAR(50), nullable = False)
    gender = sa.Column(sa.CHAR(1))
    salary = sa.Column(sa.DECIMAL(10,2))
    day_month_birthday = sa.Column(sa.CHAR(5)) #mm/dd
    neighborhood = sa.Column(sa.VARCHAR(50))
    city = sa.Column(sa.VARCHAR(50))
    uf = sa.Column(sa.CHAR(2))

#supplier table
class supplier(base):
    __tablename__ = "supplier"
    #columns
    register_supplier = sa.Column(sa.INTEGER, primary_key = True, index = True)
    name_supplier = sa.Column(sa.VARCHAR(50), nullable = False)
    official_name = sa.Column(sa.VARCHAR(100), nullable = False)
    city = sa.Column(sa.VARCHAR(50), nullable = False)
    uf = sa.Column(sa.CHAR(2), nullable = False)

#product table
class product(base):
    __tablename__ = "product"
    #columns
    code = sa.Column(sa.INTEGER, primary_key = True, index = True)
    
    #if I update/delete register_supplier, use ondelete can do an action,
    #CASCADE = if update in the mother table (this case is supplier)
    # update here (product)
    register_supplier = sa.Column(sa.INTEGER, sa.ForeignKey("supplier.register_supplier", 
                                                            ondelete = "NO ACTION", onupdate = "CASCADE"))
    dscProduct = sa.Column(sa.VARCHAR(100), nullable = False)
    gender = sa.Column(sa.CHAR(1), nullable = False)
    
#seller table
class seller(base):
    __tablename__ = "seller"
    #columns
    register_seller = sa.Column(sa.INTEGER, primary_key = True, index = True)
    cpf = sa.Column(sa.VARCHAR(14), nullable = False)
    name_seller = sa.Column(sa.VARCHAR(100), nullable = False)
    email_address = sa.Column(sa.VARCHAR(50), nullable = False)
    gender = sa.Column(sa.CHAR(1))

#sales table
class sales(base):
    __tablename__ = "sales"
    #columns
    idTransaction = sa.Column(sa.INTEGER, primary_key = True, index = True)
    cpf = sa.Column(sa.VARCHAR(14), sa.ForeignKey("client.cpf", ondelete = "NO ACTION", onupdate = "CASCADE"), index = True)
    register_supplier = sa.Column(sa.INTEGER, sa.ForeignKey("supplier.register_supplier", ondelete = "NO ACTION", onupdate = "CASCADE"), index = True)
    code = sa.Column(sa.INTEGER, sa.ForeignKey("product.code", ondelete = "NO ACTION", onupdate = "CASCADE"), index = True)

try:
    base.metadata.create_all(engine) #create tables
    print("Table created")
except ValueError:
    ValueError()