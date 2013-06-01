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
