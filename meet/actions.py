# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any,Union, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
#
#
class ActionHelloWorld(FormAction):
    def name(self) -> Text:
        return "meeting_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        print("required slots(tracker: Tracker)")
        return  ["count", "data_time"]
    
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "count": [self.from_entity(entity="count"),
                     self.from_text()],
            "data_time": [self.from_entity(entity="data_time"),
                     self.from_text()],
        }
    
    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(template="utter_submit")
        return []
