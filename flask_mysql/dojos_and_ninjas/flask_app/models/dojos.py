from flask_app.config.mysqlconnection import connectToMySQL 
from flask_app.models.ninja import Ninja
#since this is MODEL need to reach out to DB

# import tables from dojos_and_ninjas schema

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        # this will return all results from dojos table
        # BUT we want to iterate over the db results to create instaces of users within cls so we can manipulate later if needed
        dojos = []

        dojos.append(Dojo(results[0]))

        for row in results:
            #Ryan lectured on this, the idea here is that since we're LEFT JOIN-ing dojos -> ninjas there could be repeats of dojos if multiple ninjas are there. This is checking if the PREVIOUS instance in the dojos list has the SAME id as the one we're checking (if not add it)
            if row['id'] != dojos[-1].id:
                dojos.append(Dojo(row))
            #updating this to account for the LEFT JOIN - can pull user data and also get users at same time
            if row['ninjas.id'] != None:
                ninja_data = {
                    "id":row["ninjas.id"],
                    "first_name": row["first_name"],
                    "last_name": row["last_name"],
                    "age": row["age"],
                    "created_at": row["ninjas.created_at"],
                    "updated_at": row["ninjas.updated_at"],
                    "dojo_id": row["dojo_id"]
                }
                new_ninja = Ninja(ninja_data)
                dojos[-1].ninjas.append(new_ninja)

        return dojos

    @classmethod
    def add_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES(%(name)s);"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)
    
    @classmethod
    def show_one_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id=%(id)s"

        results=connectToMySQL('dojos_and_ninjas').query_db(query, data)
        dojo = Dojo(results[0])

        for row in results:
            #Ryan lectured on this, the idea here is that since we're LEFT JOIN-ing dojos -> ninjas there could be repeats of dojos if multiple ninjas are there. This is checking if the PREVIOUS instance in the dojos list has the SAME id as the one we're checking (if not add it)
            # if dojo['id'] != dojos[-1].id:
            #     dojos.append(Dojo(dojo))
            #updating this to account for the LEFT JOIN - can pull user data and also get users at same time
            if row['ninjas.id'] != None:
                ninja_data = {
                    "id":row["ninjas.id"],
                    "first_name": row["first_name"],
                    "last_name": row["last_name"],
                    "age": row["age"],
                    "created_at": row["ninjas.created_at"],
                    "updated_at": row["ninjas.updated_at"],
                    "dojo_id": row["dojo_id"]
                }
                new_ninja = Ninja(ninja_data)
                dojo.ninjas.append(new_ninja)
                print(dojo.ninjas)
        return dojo
        