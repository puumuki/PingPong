# -*- coding: utf-8 *-*

class EntityManager(object):

    def __init__(self):
        self.game_objects_list = []
        self.game_objects_dictionary = {}

    def add(self,name, entity):
        self.game_objects_list.append(entity)
        self.game_objects_dictionary[name] = entity

    def get(self, name):
        return self.game_objects_dictionary[name]

    def as_list(self):
        return self.game_objects_list
