from pymongo import MongoClient

connection_string = "mongodb+srv://ericcui:a3tgSg0tVBJ9bhg5@cluster0.r6ela.mongodb.net/"
client = MongoClient(connection_string)

db = client.test_DB
collection = db.test_collection

user_document = {
    "username": "john_doe",
    "email": "john.doe@example.com",
    "age": 28
}

inserted_id = collection.insert_one(user_document).inserted_id
print(f"Inserted document ID: {inserted_id}")
