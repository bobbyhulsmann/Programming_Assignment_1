"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data


# Part 1: vowel_count
# Returns the number of vowels in text, treating uppercase and lowercase
# letters the same.
def vowel_count(text: str) -> int:
    total = 0 # Keeps track of how many vowels have been found.

    # Check each character in the input text.
    for char in text:
        # Convert the character to lowercase and check whether it is a vowel.
        if char.lower() in "aeiou":
            total = total + 1
    
    # Return the final number of vowels.
    return total
    
    raise NotImplementedError("Part 1: implement vowel_count")


# Part 2: short_lists
# Returns a new list containing only the inner lists that have exactly
# two integers, preserving their original order.
def short_lists(items: list[list[int]]) -> list[list[int]]:
    result = [] # Stores the inner lists that have a length of 2.

    # Check each inner list in items.
    for list in items:
        # Keep the list only if it contains exactly two elements.
        if len(list) == 2:
            result.append(list)
    
    # Return the filtered list.
    return result
    
    raise NotImplementedError("Part 2: implement short_lists")


# Part 3: ascending_pairs
# Returns a new list where every two-item inner list is in ascending order.
# Inner lists with a different length are included unchanged.
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    result = [] # Stores the processed inner lists.
    
     # Check each inner list in items.
    for list in items:
         # Lists that are not pairs do not need to be reordered.
        if len(list) != 2:
            result.append(list)

         # Keep an already ascending pair in its original order.
        elif list[0] <= list[1]:
            result.append(list)
    
        else:
            # Copy and reverse a descending pair so the original is unchanged.
            x = list.copy()
            x.reverse()
            result.append(x)

    # Return the list of processed inner lists.
    return result

    
    raise NotImplementedError("Part 3: implement ascending_pairs")


# Part 4: add_prices
# Returns a new Price object representing the sum of two Price objects.
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    # Add the dollar and cent amounts separately.
    dollar = first.dollars + second.dollars
    cent = first.cents + second.cents
    
    # Convert every group of 100 cents into one additional dollar.
    if cent >= 100:
        cent -= 100
        dollar += 1
    
    # Create and return a new Price object with the combined amount.
    return data.Price(dollar, cent)

    
    raise NotImplementedError("Part 4: implement add_prices")


# Part 5: rectangle_area
# Returns the area of the given Rectangle.
def rectangle_area(rectangle: data.Rectangle) -> float:
     # Find the horizontal distance between the rectangle's left and right sides.
    width = rectangle.bottom_right[0] - rectangle.top_left[0]
    
     # Find the vertical distance between the rectangle's top and bottom sides.
    height = rectangle.top_left[1] - rectangle.bottom_right[1]
    
    # Return the rectangle's area.
    return width * height
    
    
    raise NotImplementedError("Part 5: implement rectangle_area")


# Part 6: books_by_author
# Returns a new list of books written by the given author.
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    result = [] # Stores books that include author in their authors list.
    
    # Check each Book object in the input list.
    for book in books:
        # Add the book if the author is one of its authors.
        if author in book.authors:
            result.append(book)
    
    # Return the matching Book objects in their original order.
    return result
    
    
    raise NotImplementedError("Part 6: implement books_by_author")

from math import sqrt
# Part 7: circle_bound
# Returns the smallest Circle that encloses the given Rectangle.
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    # Find the midpoint of the rectangle, which becomes the circle's center.
    x_center = (rectangle.top_left[0] + rectangle.bottom_right[0])/2
    y_center = (rectangle.top_left[1] + rectangle.bottom_right[1])/2
    
    # Find the horizontal and vertical distances from the center to a corner.
    x_distance = rectangle.top_left[0] - x_center
    y_distance = rectangle.top_left[1] - y_center
    
    # Use the distance formula to find the radius from the center to a corner.
    radius = sqrt(x_distance**2 + y_distance**2)
    
    # Create and return a Circle with the calculated center and radius.
    return data.Circle((x_center, y_center), radius)
    
    
    raise NotImplementedError("Part 7: implement circle_bound")


# Part 8: below_pay_average
# Returns the names of employees whose pay rate is below the group's average.
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    # An empty list has no employees below its average.
    if len(employees) == 0:
        return [] # Stores names of employees paid below the average.
    total = 0
    result = []
    
     # Add all employee pay rates to find the total.
    for emp in employees:
        total += emp.pay_rate
    
     # Calculate the average pay rate.
    average = total/len(employees)
    
     # Add each qualifying employee's name, keeping the original order.
    for emp in employees:
        if emp.pay_rate < average:
                result.append(emp.name)
    
    return result
    
    
    raise NotImplementedError("Part 8: implement below_pay_average")
