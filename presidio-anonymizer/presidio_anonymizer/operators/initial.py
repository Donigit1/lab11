from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    """Initial operator that converts names to initials."""

    def operate(self, text: str, params=None):
        if not text or not isinstance(text, str):
            return text

        # Remove extra whitespace and split words
        words = text.strip().split()

        initials = []
        for word in words:
            # Get first alphanumeric character in the word
            first_char = None
            for ch in word:
                if ch.isalnum():
                    first_char = ch.upper()
                    break

            # If no alphanumeric char found, skip
            if not first_char:
                continue

            initials.append(f"{first_char}.")

        # Join with space
        return " ".join(initials)

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize

    def validate(self, params: dict = None):
        return
