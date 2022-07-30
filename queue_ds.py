"""This module contains a queue data structure to contain pairs of currency codes from the history.txt file  """
# queue data structure class
class history_queue:
    def __init__(self):
        self.queue = list()

    # class method to modify the queue, if the amount of elements in the queue is less than 10, the new pair of codes will just
    # be added into the queue if it is not in the queue already, else, it will pop the last element and insert it as the first element
    def modify(self, add):
        if add not in self.queue:
            if len(self.queue) < 10:
                self.queue.insert(0, add)
            else:
                self.queue.insert(0, add)
                self.queue.pop()