import couchdb

# Connect to the CouchDB server
server = couchdb.Server("http://tireni:tireni123@localhost:5984/")

# Create a database if it does not exist, or use the existing database
db_name = "db434"
try:
    db = server.create(db_name)
except couchdb.http.PreconditionFailed as e:
    db = server[db_name]

# Write data to the database
data = {
    "Name": "Oluwafemi Tireni",
    "Matriculation Number": "20CJ027477",
    "Programme": "Computer Engineering",
}

# Save the document to the database and get the document ID and revision
doc_id, doc_rev = db.save(data)

# Read the document from the database
doc = db.get(doc_id)

# Print the document to the console
# print(doc)

# Update the document
doc= db.get(doc_id)
# doc["Name"] = "Victor Elikwu"
# db.save(doc)

# Modify the document using a function
# def modify_data(doc_id, new_data):
#     doc = db.get(doc_id)
#     doc.update(new_data)
#     db.save(doc)

# Set the new data to be updated
# new_data = {"level": "500level"}

# Modify the document using the function
# modify_data(doc_id, new_data)

# Delete the document from the database
doc = db.get(doc_id)
db.delete(doc)