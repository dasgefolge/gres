class Task:
    """
    This class represents tasks, the individual items on people's to-do lists.
    This class is an abstract superclass: instances of it can never be completed.
    """
    def __init__(self, title):
        self.title = title

    def progress(self):
        """
        Returns a value between 0.0 and 1.0 (both inclusive) representing the amount of work that has been done to complete the task.
        A task with a progress of 1 has been completed.
        A progress value which is less than 1, however, should not be used as anything but an estimate. For example, a checkbox task may be nearly finished but still have a progress value of 0.0, and a download task may have a progress value of 0.99 and still never be completed.
        This method always returns 0.0 and subclasses should usually override it.
        """
        return 0.0

class Checkbox(Task):
    """
    This class represents checkbox tasks: These tasks can be either checked (completed) or unchecked.
    """
    def __init__(self, title, checked=False):
        super().__init__(self, title)
        self.checked = checked
    
    def check(self, checked=True):
        """
        Checks the task (or unchecks if checked == False).
        """
        self.checked = checked
    
    def progress(self):
        """
        Returns 1.0 if the checkbox is checked, and 0.0 otherwise.
        """
        return 1.0 if self.checked else 0.0
