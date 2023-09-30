from typing import Dict,Any,List,Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionRespondToAPI(Action):
    def name(self):
        return "action_respond_to_api"
    

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Extract the message from the tracker
        message = tracker.latest_message.get('text')

        # Perform some logic (optional) and generate a response
        response = "You said: " + message

        # Send the response
        dispatcher.utter_message(text=response)

        return []
