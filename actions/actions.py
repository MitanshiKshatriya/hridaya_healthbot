# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
import json 
import os
dirname = os.path.dirname(__file__)
sideeffects_filename = os.path.join(dirname, 'sideeffects.json')
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

class ActionSideEffects(Action):

    def name(self) -> Text:
        return "action_side_effects"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        medicine_name = tracker.latest_message['entities'][0]['value']
        print(medicine_name)
        # for e in entities:
        #     print(e)
        # with open(sideeffects_filename) as json_file: 
        #         data = json.load(json_file)
        # print(data[medicine_name])
        try:
            with open(sideeffects_filename) as json_file: 
                data = json.load(json_file) 
            dispatcher.utter_message(text="Side effects of the medicine "+medicine_name+" are "+data[medicine_name])
        except:
            dispatcher.utter_message(text="Sorry we could not find any side effects of "+medicine_name+" in our databse")

        
            
        

        return []

class ActionMedicines(Action):

    def name(self) -> Text:
        return "action_medicines"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="action medecine is running!!")

        return []

class ActionSymptoms(Action):

    def name(self) -> Text:
        return "action_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="action symptoms is running!!")

        return []

# class ValidateSideEffectForm(Action):
#     def name(self) -> Text:
#         return "user_side_effect_form"
    
#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         required_slots = ["medicine_name"]
#         # mention utter for it utter_ask_medicine_name utter_ask_nameofslot
#         for slot_name in required_slots:
#             if tracker.slots.get(slot_name) is None:
#                 return [SlotSet("requested_slot", slot_name)]

#         return [SlotSet("requested_slot",None)]


# class ActionSubmitSideEffect(Action):
#     def name(self)-> Text:
#         return "action_submit_side_effect"

#     def run(
#         self,
#         dispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text,Any]]:
#         text = "ACTION: here is ur med: " + tracker.get_slot("medicine_name")
#         dispatcher.utter_message(text=text)



