from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    """Initial operator that converts names or multi-word identifiers into initials."""

    def operate(self, text: str, params=None):
        if not text or not isinstance(text, str):
            return text

        words = text.strip().split()
        initials = []

        for word in words:
            prefix = ""
            first_alpha_num = None

            # Detect prefix and first alphanumeric character
            for ch in word:
                if ch.isalnum():
                    first_alpha_num = ch.upper()
                    break
                else:
                    prefix += ch

            if not first_alpha_num:
                continue  # Word has no alphanumeric chars

            initials.append(f"{prefix}{first_alpha_num}.")

        return " ".join(initials)

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize

    def validate(self, params: dict = None):
        return
