from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Category_Item


engine = create_engine('sqlite:///categories.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# result = session.query(Category).all()
# for catalog in result:
#     print(catalog.name+" "+"id:"+str(catalog.id))

result = session.query(Category_Item).all()
for item in result:
    print(item.name+" "+"id:"+str(item.id))


# You completely passed by the most clear and useful, the map method:
#
# print “{first} {last} is {age} years old.” format(first=fname, last=lname, age=age)
#
