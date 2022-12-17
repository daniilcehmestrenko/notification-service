from dataclasses import dataclass


@dataclass
class MailingListStats:
    mailinglist: str
    count_message: int
