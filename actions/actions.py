# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.events import Restarted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
import csv
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionStoreCSV(Action):

     def name(self) -> Text:
         return "action_store_csv"
     

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        sname=tracker.get_slot("sname")
        pname=tracker.get_slot("pname")
        number=tracker.get_slot("number")
        board=tracker.get_slot("board")
        course=tracker.get_slot("course")
        location=tracker.get_slot("location")
        
        with open('info.csv', 'a') as info:
            fieldnames = ['sname', 'pname', 'number', 'board', 'course', 'location']
            
            csv_writer = csv.writer(info, delimiter='\t')
            
            row=[sname,pname,number,board,course,location]
            csv_writer.writerow(row)
        return []

class ActionHelloWorld(FormAction):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


