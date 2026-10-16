"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Person:
    """Represent a person with a name and age."""

    category = "Person"

    def __init__(self, name, age):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name cannot be empty.")
        if not isinstance(age, int) or isinstance(age, bool) or age < 0:
            raise ValueError("Age must be a nonnegative integer.")

        self.name = name.strip()
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def have_birthday(self):
        """Increase the person's age by one."""
        self.age += 1

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class Student(Person):
    """Represent a student and the courses in which the student is enrolled."""

    school_name = "Generic University"

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        if not isinstance(student_id, (str, int)) or not str(student_id).strip():
            raise ValueError("Student ID cannot be empty.")

        self.student_id = student_id
        # This list is created per instance, so students do not share courses.
        self.courses = []

    def enroll_course(self, course_name):
        """Enroll in a nonempty course unless it is already in the list."""
        if not isinstance(course_name, str) or not course_name.strip():
            raise ValueError("Course name cannot be empty.")

        course_name = course_name.strip()
        if course_name in self.courses:
            return False

        self.courses.append(course_name)
        return True

    # Student-created extension: remove a course and report whether it existed.
    def drop_course(self, course_name):
        if course_name not in self.courses:
            return False
        self.courses.remove(course_name)
        return True

    @property
    def course_count(self):
        """Provide read-only access to the number of enrolled courses."""
        return len(self.courses)

    def display_info(self):
        """Override Person.display_info with student-specific details."""
        course_list = ", ".join(self.courses)
        print(
            f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}, "
            f"School: {self.school_name}, Courses: [{course_list}]"
        )

    def __str__(self):
        course_list = ", ".join(self.courses)
        return (
            f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}, "
            f"School: {self.school_name}, Courses: [{course_list}]"
        )

    def __len__(self):
        return self.course_count


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    first_student = Student("Ben", 20, "S1234")
    second_student = Student("Eli", 21, "S2222")
    first_student.enroll_course("Math 101")

    print(f"Class access: {Student.school_name}")
    print(f"Object access: {first_student.school_name}")

    # A nickname is added only to first_student's instance namespace.
    first_student.nickname = "Benny"
    print(f"First student's namespace: {first_student.__dict__}")
    print(f"Second student's namespace: {second_student.__dict__}")

    class_items = {
        key: value
        for key, value in Student.__dict__.items()
        if (
            not key.startswith("__")
            and not callable(value)
            and not isinstance(value, property)
        )
    }
    print(f"Student class namespace data: {class_items}")

    # Changing the class variable is visible through both instances.
    Student.school_name = "Tech Institute"
    print(f"After class update, first student: {first_student.school_name}")
    print(f"After class update, second student: {second_student.school_name}")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    original = Student("Ava", 27, "S3000")
    original.enroll_course("Programming I")

    # A shallow copy creates a new Student but shares the nested courses list.
    shallow_copy = copy(original)
    # A deep copy creates a new Student and a separate nested courses list.
    deep_copy = deepcopy(original)

    original.enroll_course("Data Structures")

    print(f"Original:     {original}")
    print(f"Shallow copy: {shallow_copy}")
    print(f"Deep copy:    {deep_copy}")
    print(
        "Original and shallow copy share courses: "
        f"{original.courses is shallow_copy.courses}"
    )
    print(
        "Original and deep copy share courses: "
        f"{original.courses is deep_copy.courses}"
    )


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n=== Parent Object ===")
    person = Person("Cleo", 45)
    person.display_info()

    print("\n=== Child Object and Inheritance ===")
    student = Student("Dana", 22, "S9876")
    student.enroll_course("Biology")
    student.enroll_course("Chemistry")
    student.have_birthday()  # This method was inherited from Person.
    student.display_info()
    print(f"Course count using len(): {len(student)}")

    print("\n=== Edge Cases and Student-Created Extension ===")
    empty_schedule = Student("Noah", 19, "S4000")
    empty_schedule.display_info()
    print(f"Duplicate Biology enrollment added: {student.enroll_course('Biology')}")
    print(f"Dropped Chemistry: {student.drop_course('Chemistry')}")
    print(f"Dropped missing Art course: {student.drop_course('Art')}")
    try:
        student.enroll_course("   ")
    except ValueError as error:
        print(f"Invalid course handled: {error}")
    student.display_info()

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
