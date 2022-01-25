from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name,location,language,comment,created_at,updated_at) VALUES (%(name)s,%(location)s,%(language)s,%(comment)s,NOW(),NOW())"
        return connectToMySQL('dojo_survey').query_db(query,data)


    @classmethod
    def get_one(cls):
        query ="SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
        result = connectToMySQL('dojo_survey').query_db(query)
        return cls(result[0])

    @staticmethod
    def is_valid(dojo):
        is_valid = True
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
        if len(dojo['location']) < 1:
            flash("Must choose a Dojo location")
        if len(dojo['language']) < 1:
            flash("Must choose a language")
        if len(dojo['comment']) < 3:
            is_valid = False
            flash("Comments must be at least 3 characters")
        return is_valid