from datetime import datetime, timedelta

class BorrowingRecord:
    def __init__(self, user_id: str, isbn: str, borrow_date: datetime, due_date: datetime):
        self.user_id = user_id
        self.isbn = isbn
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.return_date = None

    def is_overdue(self) -> bool:
        if self.return_date:
            return self.return_date > self.due_date
        return datetime.now() > self.due_date

    def calculate_fine(self, fine_per_day: float) -> float:
        if not self.is_overdue():
            return 0.0
        
        end_date = self.return_date if self.return_date else datetime.now()
        overdue_days = (end_date - self.due_date).days
        return max(0, overdue_days) * fine_per_day

    def __str__(self):
        status = "Returned" if self.return_date else "Borrowed"
        overdue = " (Overdue)" if self.is_overdue() else ""
        return f"{status}: {self.isbn} by {self.user_id} from {self.borrow_date.date()} to {self.due_date.date()}{overdue}"