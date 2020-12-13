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
symptoms_filename = os.path.join(dirname, 'symptoms.json')
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
        medicine_name = None
        try:
            medicine_name = tracker.latest_message['entities'][0]['value']
            print(medicine_name)
        except:
            medicine_name = None
        # for e in entities:
        #     print(e)
        # with open(sideeffects_filename) as json_file: 
        #         data = json.load(json_file)
        # print(data[medicine_name])
        if medicine_name != None:
            try:
                with open(sideeffects_filename) as json_file: 
                    data = json.load(json_file) 
                dispatcher.utter_message(text="Side effects of the medicine "+medicine_name+" are "+data[medicine_name])
            except:
                dispatcher.utter_message(text="Sorry we could not find any side effects of "+medicine_name+" in our databse")
        else:
            dispatcher.utter_message(text="Sorry we could not recognize the medicine name")

        
            
        

        return []

class ActionMedicines(Action):

    def name(self) -> Text:
        return "action_medicines"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        symptom_name = tracker.latest_message['entities'][0]['value']
        print(symptom_name)

        # try:
        #     with open(sideeffects_filename) as json_file: 
        #         data = json.load(json_file) 
        #     dispatcher.utter_message(text="Symptoms of the disease "+disease_name+" are "+data[disease_name])
        # except:
        #     dispatcher.utter_message(text="Sorry we could not find any symptoms of "+disease_name+" in our databse")



        dispatcher.utter_message(text="Here are some medicine for "+symptom_name+ " - crocin, naprocin, advil. However if the headache persist or is accompnied with fever or nausea I recommend seeing the nearest doctor")

        return []

class ActionSymptoms(Action):

    def name(self) -> Text:
        return "action_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        disease_name = None
        try:
            disease_name = tracker.latest_message['entities'][0]['value']
            print(disease_name)
        except:
            disease_name = None

        if(disease_name!=None):
            try:
                with open(symptoms_filename) as json_file: 
                    data = json.load(json_file) 
                dispatcher.utter_message(text="Symptoms of the disease "+disease_name+" are "+data[disease_name])
            except:
                dispatcher.utter_message(text="Sorry we could not find any symptoms of "+disease_name+" in our databse")

        else:
            dispatcher.utter_message(text="Sorry we could not recognize the disease name")

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



