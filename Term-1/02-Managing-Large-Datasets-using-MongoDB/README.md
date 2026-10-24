# Module 02: Managing Large Datasets using MongoDB

![MongoDB](https://img.shields.io/badge/MongoDB-8.0-47A248?logo=mongodb&logoColor=white) ![mongosh](https://img.shields.io/badge/mongosh-2.x-13AA52?logo=mongodb&logoColor=white) ![Compass](https://img.shields.io/badge/Compass-GUI-00684A?logo=mongodb&logoColor=white) ![Atlas](https://img.shields.io/badge/Atlas-Cloud-00ED64?logo=mongodb&logoColor=black) ![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white) ![PyMongo](https://img.shields.io/badge/PyMongo-4.x-47A248) ![Level](https://img.shields.io/badge/Level-Beginner-2EA44F)

> Diploma in AI / Data Science · Term 1 · 16 sessions × 2 hours · [⬅ Term Home](../README.md)

Much of the data used in AI and data science does not fit neatly into tables: app logs, product catalogues, sensor readings, social media posts, chatbot conversations. **MongoDB** stores this kind of data as flexible JSON-like **documents**. In this module you will install MongoDB, create and query data, summarise it with the aggregation pipeline, make queries fast with indexes, keep data safe with replication and transactions, move it to the cloud with **MongoDB Atlas**, and finally read and write it from **Python**, the main language of data science.

All examples use one small practice database called **shopdb**: an online store in Pakistan with `products`, `customers` and `orders`. Because the data is tiny, you can see every result with your own eyes and focus on learning the commands.

## 🎯 What You Will Learn

- Explain the difference between relational (SQL) and NoSQL databases, and when MongoDB is a good fit
- Install MongoDB Server, the MongoDB Shell (`mongosh`) and MongoDB Compass, and connect to a server
- Create databases and collections, and insert, query, update and delete documents (CRUD)
- Filter and change data with query, projection and update operators
- Summarise data with the aggregation pipeline (`$match`, `$group`, `$sort`, `$lookup` ...)
- Run database commands and shell methods, and manage users and roles
- Create and drop indexes, and check them with `explain()`
- Understand replica sets, sharding and multi-document transactions
- Use Compass, the BI Connector, Excel and MongoDB Atlas (cloud)
- Connect Python to MongoDB with PyMongo and run CRUD from a script

## 📋 Prerequisites

- Module 01 (T-SQL): you should know what a table, row, column and primary key are
- Basic computer skills: installing software, using a terminal / command prompt
- No JavaScript is required. `mongosh` uses a JavaScript-like syntax, and every line is explained
- For Session 15 only: basic Python (variables, lists, dictionaries, loops)

## 🛠 Tools to Install

| Tool | Why you need it | Official link |
|---|---|---|
| MongoDB Community Server 8 | the database server (`mongod`) on your PC | [https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community) |
| MongoDB Shell (`mongosh`) | type commands and run `.js` scripts | [https://www.mongodb.com/try/download/shell](https://www.mongodb.com/try/download/shell) |
| MongoDB Compass | free graphical tool to browse and edit data | [https://www.mongodb.com/try/download/compass](https://www.mongodb.com/try/download/compass) |
| MongoDB Database Tools | `mongoimport`, `mongoexport`, `mongodump`, `mongorestore` | [https://www.mongodb.com/try/download/database-tools](https://www.mongodb.com/try/download/database-tools) |
| MongoDB Atlas (free M0 cluster) | MongoDB in the cloud (Session 14) | [https://www.mongodb.com/cloud/atlas/register](https://www.mongodb.com/cloud/atlas/register) |
| Python 3.12 | for PyMongo (Session 15) | [https://www.python.org/downloads/](https://www.python.org/downloads/) |
| Visual Studio Code (optional) | edit `.js` and `.py` files | [https://code.visualstudio.com/](https://code.visualstudio.com/) |

> 💡 **First step for every student:** after installing, open a terminal in the [Session 02 folder](./Session-02-Working-with-MongoDB-Databases/README.md) and run `mongosh --file shopdb-setup.js`. It builds the **shopdb** practice database used from Session 02 onwards. Run it again any time you want a fresh copy.

### How to run the example files

| File type | How to run it |
|---|---|
| `something.js` (mongosh script) | `mongosh --file something.js` from a terminal, or `load("something.js")` inside mongosh |
| `something.py` (Python) | `python something.py` (after `pip install pymongo`) |
| `something.json` (data) | `mongoimport --db shopdb --collection products --jsonArray --file products.json` |

## 📚 Session Index

| Session | Topic | Link |
|---|---|---|
| 01 | Introduction to MongoDB | [Open notes](./Session-01-Introduction-to-MongoDB/README.md) |
| 02 | Working with MongoDB Databases (CRUD) | [Open notes](./Session-02-Working-with-MongoDB-Databases/README.md) |
| 03 | MongoDB Operators | [Open notes](./Session-03-MongoDB-Operators/README.md) |
| 04 | Practice Lab: Basics, CRUD and Operators | [Open notes](./Session-04-Practice-Lab-CRUD-and-Operators/README.md) |
| 05 | The Aggregation Pipeline | [Open notes](./Session-05-Aggregation-Pipeline/README.md) |
| 06 | Database Commands | [Open notes](./Session-06-Database-Commands/README.md) |
| 07 | MongoDB Shell Methods, Users and Roles | [Open notes](./Session-07-MongoDB-Shell-Methods/README.md) |
| 08 | Practice Lab: Aggregation, Commands and Shell Methods | [Open notes](./Session-08-Practice-Lab-Aggregation-Commands-and-Shell-Methods/README.md) |
| 09 | MongoDB Indexing | [Open notes](./Session-09-MongoDB-Indexing/README.md) |
| 10 | Replication and Sharding | [Open notes](./Session-10-Replication-and-Sharding/README.md) |
| 11 | Transaction Management | [Open notes](./Session-11-Transaction-Management/README.md) |
| 12 | Practice Lab: Indexes, Replication and Transactions | [Open notes](./Session-12-Practice-Lab-Indexes-Replication-and-Transactions/README.md) |
| 13 | MongoDB Tools: Compass, BI Connector and Excel | [Open notes](./Session-13-MongoDB-Tools-Compass-BI-Connector-and-Excel/README.md) |
| 14 | MongoDB in the Cloud with Atlas | [Open notes](./Session-14-MongoDB-Cloud-with-Atlas/README.md) |
| 15 | MongoDB Connectivity with Python (PyMongo) | [Open notes](./Session-15-MongoDB-Connectivity-with-Python/README.md) |
| 16 | Practice Lab: Tools, Atlas and Python | [Open notes](./Session-16-Practice-Lab-Tools-Atlas-and-Python/README.md) |

Sessions 04, 08, 12 and 16 are **practice labs**: no new theory, only hands-on tasks with a full solution file so you can check your work.

## 🚀 Module Mini-Project

**Student Feedback Analytics Store** - a small NoSQL back end that a data science team could later analyse:

1. Create a database `feedbackdb` with collections `students`, `courses` and `feedback` (each feedback document has a rating 1-5, a comment, a list of tags and a date).
2. Insert at least 10 students, 5 courses and 40 feedback documents (a `.js` seed script or a JSON file loaded with `mongoimport`).
3. Write queries with operators: low ratings (`$lt`), feedback with a given tag (`$in`), feedback without a comment (`$exists`).
4. Build aggregation reports: average rating per course, number of feedback per month, top 3 courses (use `$lookup` to show course names).
5. Create indexes for your two most common queries and prove them with `explain("executionStats")`.
6. Create a read-only user `analyst` that can only read `feedbackdb`.
7. Move the database to a free Atlas cluster and write a Python script (PyMongo) that prints the average rating per course.
8. Submit your scripts plus a short README with screenshots of the results.

## 🔗 Resources (official documentation)

- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [MongoDB Shell (mongosh)](https://www.mongodb.com/docs/mongodb-shell/)
- [CRUD operations](https://www.mongodb.com/docs/manual/crud/)
- [Query and projection operators](https://www.mongodb.com/docs/manual/reference/operator/query/)
- [Aggregation](https://www.mongodb.com/docs/manual/aggregation/)
- [Indexes](https://www.mongodb.com/docs/manual/indexes/)
- [Replication](https://www.mongodb.com/docs/manual/replication/) · [Sharding](https://www.mongodb.com/docs/manual/sharding/)
- [Transactions](https://www.mongodb.com/docs/manual/core/transactions/)
- [MongoDB Compass](https://www.mongodb.com/docs/compass/current/)
- [MongoDB Atlas](https://www.mongodb.com/docs/atlas/)
- [PyMongo documentation](https://pymongo.readthedocs.io/en/stable/)
- [MongoDB University (free courses)](https://learn.mongodb.com/)

---

[⬅ Term Home](../README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
