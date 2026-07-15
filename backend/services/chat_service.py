from ai.agent.agent import CivicPulseAgent


class ChatService:

    @staticmethod
    def chat(
        current_user,
        message: str
    ):

        return CivicPulseAgent.invoke(

            citizen_id=current_user.id,

            current_user=current_user,

            message=message

        )