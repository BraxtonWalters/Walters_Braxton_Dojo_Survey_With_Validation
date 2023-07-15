from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.favorite_language = data["favorite_language"]
        self.comment = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # write
    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name, location, favorite_language, comment) VALUES (%(name)s, %(location)s, %(favorite_language)s, %(comment)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    # read
    @classmethod
    def get_dojo(cls, id):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, {"id": id})
        return results[0]
    
    @staticmethod
    def validator(data):
        is_valid = True
        if len(data["name"]) < 3:
            flash("Invalid", "error_dojos_name")
            is_valid = False
        if len(data["location"]) < 3:
            flash("Invalid", "error_dojos_location")
            is_valid = False
        if len(data["favorite_language"]) < 3:
            flash("Invalid", "error_dojos_favorite_language")
            is_valid = False
        if len(data["comment"]) < 3:
            flash("Invalid", "error_dojos_comment")
            is_valid = False
        return is_valid
