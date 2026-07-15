import re


class IntentService:

    @staticmethod
    def detect(message: str):

        text = message.lower()

        complaint = re.search(
            r"(CP\d{6})",
            message,
            re.IGNORECASE
        )

        complaint_number = (
            complaint.group(1).upper()
            if complaint
            else None
        )

        if complaint_number and text.strip() == complaint_number.lower():

            return {
                "intent": "select_complaint",
                "complaint_number": complaint_number
            }

        if "status" in text or "progress" in text:

            return {
                "intent": "complaint_status",
                "complaint_number": complaint_number
            }

        if (
            "policy" in text
            or "resolution" in text
            or "working days" in text
        ):

            return {
                "intent": "policy_query",
                "complaint_number": None
            }

        if (
            "register" in text
            or "report" in text
            or "complaint" in text
        ):

            return {
                "intent": "complaint_registration",
                "complaint_number": None
            }

        return {
            "intent": "general",
            "complaint_number": None
        }