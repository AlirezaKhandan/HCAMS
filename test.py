import os
import pprint
from pymongo import MongoClient
#shortcut to load the enviromenet variable file without leaking code or the file path!!!
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
#using environment variables to hide the password and access it in code
password = os.environ.get("MONGODB_PWD")
connection_string = f"mongodb+srv://ak714:{password}@hcams.jgxal.mongodb.net/?retryWrites=true&w=majority&appName=HCAMS"
#connect to my database through the link,
# mongo client is basically the door, client is just the short name for it
client = MongoClient(connection_string)
#list all databases i have
dbs = client.list_database_names()
#client access my database (testdb) and from now on call it test_db in the code for easier access
test_db = client.testdb
#list all collections inside testdb
collections = test_db.list_collection_names()

print(f"dbs: {dbs}")
print(f"collections: {collections}")#
#function to insert one document into a collection (testcollection)
def insertData():
    collection = test_db.testcollection
    test_doc = {
        "book":"secret garden",
        "pages":"202",
        "author": "me"
    }
    #basically the line was like this: collection.insert_one(test_doc)
    #but we added insert id on each side to give it an id and execute the line of command at the same time 
    insert_id = collection.insert_one(test_doc).inserted_id
    print(insert_id)

#if you try to access a database that doesnt exist, mongodb will create it for you!
production = client.production
#same logic, since it doesnt exist, mongodb creates it for you!
person_collection = production.person_collection
#if we dont insert a document the two lines above wont work!!!!!!!#

def create_docs():
    fnames = ["Tim","Kim","Tom","Ben","Cat","Ken"]
    lnames = ["Tims","Kims","Toms","Bens","Cats","Kens"]
    ages = [21, 22, 23, 24, 25, 26]
    #using insert on by using for loop or using insert many by storing everything into an array(docs)
    docs = []

    for fname, lname, age in zip(fnames, lnames, ages):
        doc = {"fname":fname, "Lname": lname, "age":age}
        docs.append(doc)
        #person_collection.insert_one(doc)

    person_collection.insert_many(docs)
    print("all done")

#adding pretty printer
printer = pprint.PrettyPrinter()

#function to find all elements of a table, to do so you just leave find() empty
def findAllPeople():
    people = person_collection.find()

    for person in people:
        printer.pprint(person)


def findSomeOne():
    someone = person_collection.find_one({"fname":"Tim", "Lname":"Tims"})
    printer.pprint(someone)

def countAll():
    count = person_collection.count_documents(filter={})
    print(f"number of people: {count}")
    print("number of people:", count)

