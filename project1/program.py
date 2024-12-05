class CoolProg:
    def __init__(self):
        self.list = ["tuth", "two", "three"]

    def bubblesort(self):
        # Outer loop to iterate through the list n times
        for n in range(len(self.list) - 1, 0, -1):
            # Initialize swapped to track if any swaps occur
            swapped = False

            # Inner loop to compare adjacent elements
            for i in range(n):
                if self.list[i] > self.list[i + 1]:
                    # Swap elements if they are in the wrong order
                    self.list[i], self.list[i + 1] = self.list[i + 1], self.list[i]

                    # Mark that a swap has occurred
                    swapped = True

            # If no swaps occurred, the list is already sorted
            if not swapped:
                break
