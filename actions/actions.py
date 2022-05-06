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
        asname=tracker.get_slot("asname")
        bnumber=tracker.get_slot("bnumber")
        cboard=tracker.get_slot("cboard")
        dcutoff=tracker.get_slot("dcutoff")
        elocation=tracker.get_slot("elocation")
        
        with open('info.csv', 'a') as info:
            fieldnames = ['asname', 'bnumber', 'cboard', 'dcutoff', 'elocation']
            
            csv_writer = csv.writer(info, delimiter='\t')
            
            row=[asname,bnumber,cboard,dcutoff,elocation]
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


