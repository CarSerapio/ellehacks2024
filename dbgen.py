# MongoDB database to upload user records 
import os 
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi 
import random 

load_dotenv() 

password = os.environ.get("MONGODB_PASSWORD")

uri = f"mongodb+srv://CarolineSerapio:{password}@cluster0.lep8bak.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))

db = client["user"]
collection = db["volunteer"]
collection1 = db["senior"]

sample_vdata = { 
    "fname": ["Joe", "Alice", "Bob", "Emma", "John", "Sophia", "Michael", "Olivia", "Daniel", "Emily"],
    "lname": ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"],
    "gender": ["male", "female"],
    "certification": ["First Aid", "CPR", "Fire Safety", "Life Guard", "EMT"],
    "license": ["G1", "G2", "G"],
}

sample_sdata = {
    "fname": ["Eleanor", "Liam", "Emma", "Noah", "Olivia", "William", "Ava", "James", "Isabella", "Alexander"],
    "lname": ["Brown", "Davis", "Garcia", "Jones", "Martinez", "Miller", "Smith", "Taylor", "Wilson", "Young"],
    "gender": ["male", "female"],
    "health_problems": ["Arthritis", "Osteoporosis", "Hypertension", "Diabetes", "Heart disease", "Dementia", "Alzheimer's disease", "Stroke", "Cancer", "Depression"],
    "provinces": {
        "Alberta": ["Calgary", "Edmonton"],
        "British Columbia": ["Vancouver", "Victoria"],
        "Manitoba": ["Winnipeg"],
        "New Brunswick": ["Fredericton", "Moncton"],
        "Newfoundland and Labrador": ["St. John's"],
        "Nova Scotia": ["Halifax"],
        "Ontario": ["Toronto", "Ottawa", "Hamilton"],
        "Prince Edward Island": ["Charlottetown"],
        "Quebec": ["Montreal", "Quebec City"],
        "Saskatchewan": ["Regina", "Saskatoon"]
    }
}

# Global variable to track the `_id`
current_id = (collection.count_documents({}) + collection1.count_documents({})) - 1 
#print(current_id) 

# Function to generate a random volunteer 
def generate_random_volunteer(): 
    global current_id 
    post = {"_id" : current_id} 
    current_id += 1 
    full_name = random.choice(sample_vdata["fname"]) + " " + random.choice(sample_vdata["lname"])
    post["full_name"] = full_name
    post["age"] = random.randint(18, 30)
    post["gender"] = random.choice(sample_vdata["gender"])
    post["certification"] = random.choice(sample_vdata["certification"])
    post["license"] = random.choice(sample_vdata["license"])
    return post

"""" # Generate 15 random volunteer records to add to MongoDB 
for _ in range(15): 
    result = generate_random_volunteer() 
    collection.insert_one(result)
"""

#random_volunteers = [generate_random_volunteer() for _ in range(15)]

# Function to generate a random senior
def generate_random_senior(): 
    global current_id 
    post = {"_id" : current_id}
    current_id += 1 
    full_name = random.choice(sample_sdata["fname"]) + " " + random.choice(sample_sdata["lname"])
    post["full_name"] = full_name
    post["age"] = random.randint(60, 100)
    post["gender"] = random.choice(sample_sdata["gender"])
    post["medical_conditions"] = random.sample(sample_sdata["health_problems"], random.randint(0,5))
    post["phone_number"] = ''.join(random.choices('0123456789', k=10))
    province = random.choice(list(sample_sdata["provinces"].keys())) 
    post["province"] = province
    post["city"] = random.choice(sample_sdata["provinces"][province])
    return post

#random_seniors = [generate_random_senior() for _ in range(15)]

"""# Generate 15 random customer records to add to MongoDB 
for _ in range(15): 
    result = generate_random_senior() 
    collection1.insert_one(result)
"""

#print(random_volunteers)
#print(random_seniors)


#collection.insert_one(post) 

# Count the amount of documents in a collection 
#post_count = collection.count_documents({})
#print(post_count)

pipeline = [ 
    {"$sample": {"size": 4}}
]

random_records = collection1.aggregate(pipeline)

for record in random_records: 
    print(record)