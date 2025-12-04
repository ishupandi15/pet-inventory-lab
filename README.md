# AWS Learner Lab – Pet Inventory Project  
**Author:** Ishwariya pandi
**Course:** ABD – AWS Learner Lab  
**Assignment:** Lab #3 – DynamoDB Pet Inventory  
**Date:** September 2025  

---

# 📌 Abstract

This lab demonstrates how to build a fully serverless application on AWS using Cloud9, DynamoDB, S3, and Python (Boto3).  
The project implements table creation, data insertion, CRUD operations, and exporting DynamoDB data to S3.

---

# 🧰 AWS Services Used

| Service | Purpose |
|--------|---------|
| **Cloud9** | Cloud-based IDE to run Python scripts |
| **DynamoDB** | NoSQL database to store pet data |
| **S3** | Storage location for JSON export |
| **Lambda** | Automates DynamoDB → S3 export |
| **Boto3** | Python SDK to interact with AWS |

---

# 📘 Required Rubric Answers

## ✔ **1. Difference Between Partition Key and Sort Key**

### **Partition Key**
- Determines how DynamoDB distributes data across partitions  
- All items with the same partition key value go into the same partition  
- Must be unique *if there is no sort key*

### **Sort Key**
- Used to order items within the same partition  
- Allows storing multiple rows under the same partition key  
- Enables efficient querying and sorting

### **Example From This Lab**
- Partition Key → `pet_species` (“Dog”, “Cat”, “Bird”)  
- Sort Key → `pet_id` (1, 2, 3…)  

This means all `"Dog"` pets are grouped together, sorted by `pet_id`.

---

## ✔ **2. Meaning of `s3_key = "IshwariyaPandiDynamoDbFolder-export/pets.json"`**

This line sets the **file path inside the S3 bucket** where exported data will be stored.

Breakdown:

- `IshwariyaPandiDynamoDbFolder-export/` → folder (prefix) created inside S3  
- `pets.json` → actual JSON file name created during export  

So your file ends up in:
s3://your-bucket-name/YourNameDynamoDbFolder-export/pets.json


