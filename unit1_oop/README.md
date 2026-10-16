# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explored object-oriented programming concepts in Python, including inheritance, class and instance namespaces, encapsulation, and object copying.

## Implementation

I created a `Person` parent class with shared class data, validated instance data, display behavior, and a birthday method. I then created a `Student` child class that inherited from `Person`. The child added a shared school name, a student ID, an independently allocated course list, course enrollment behavior, and an overridden display method. The `course_count` property provided read-only access to derived state, while the `__str__` and `__len__` special methods made each object easier to inspect and use.

The namespace demonstration created two students, accessed a class variable through both the class and an object, and added a nickname to only one instance. It printed both instance dictionaries and selected class namespace data. It also changed `Student.school_name` and showed that the change was visible through both students.

The copying demonstration created shallow and deep copies of a student. After the original course list was changed, the shallow copy reflected the change because it shared the nested list. The deep copy remained independent because its nested list had also been copied.

## Edge Cases and Extension

The program displayed an empty course list safely. It rejected blank course names with a clear `ValueError`, prevented duplicate enrollment, and returned `False` when a nonexistent course was dropped. I added `drop_course` as my student-created extension and tested both successful and unsuccessful removals.

Each `Student` stored its own course list, so storage grew linearly with that student's number of courses, or O(n). Enrollment and duplicate checking used a list and therefore took O(n) time in the worst case. Appending a new course was amortized O(1) after the duplicate check. A set could make membership checking faster, but the list preserved enrollment order and produced readable output.

## Running the Program in VS Code

I ran the program from the repository root with:

```bash
python3 unit1_oop/unit1_discussion.py
```

No external packages were required. VS Code worked for this assignment because the submitted Python and Markdown files were independent of IntelliJ.

## Discussion Board Reflection

While completing this assignment, I learned how inheritance reused common behavior while allowing a child class to specialize it. The `Student` class reused the `Person` constructor and birthday method, added course data, and overrode the display method. I also learned that class variables belonged to the class namespace, while a nickname could exist only in one object's namespace. My main challenge was understanding why a shallow copy changed when the original course list changed. Identity comparisons showed that both objects referenced the same nested list, while `deepcopy` created an independent list.

Compared with procedural programming, OOP grouped related data and behavior into objects instead of passing data among separate functions. This organization added overhead because classes and validation required more planning, but it made the program easier to maintain and reuse. Another student type could inherit from `Student` without recreating its enrollment logic. The design resembled a school registration system, where shared rules stayed in reusable classes and invalid operations were handled without stopping the program. In future applications, I could apply the same structure to cybersecurity accounts or smart devices, using parent classes for shared behavior and child classes for specialized capabilities.

## Original Assignment Requirements

All TODO prompts remained visible in `unit1_discussion.py`, and their implementations were completed. The program included a parent class, a child class, namespace demonstrations, shallow and deep copying, object tests, edge-case handling, and a student-created extension.
