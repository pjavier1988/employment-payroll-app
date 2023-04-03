

# Employee Payroll System
## ACME Company

The Employee Payroll System is a Python program that calculates the amount that a company has to pay its employees based on the hours they worked and the times during which they worked. The program reads the employee schedules from a file and calculates the payroll based on the day of the week and time of day, according to a table of rates.

The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

| Day | Schedule | Rate |
| :----------- | :------------ | :----: |
| **Weekdays** | 00:01 - 09:00 | 25 USD |
| **Weekdays** | 09:01 - 18:00 | 15 USD |
| **Weekdays** | 18:01 - 00:00 | 20 USD |
| | | |
| **Weekends** | 00:01 - 09:00 | 30 USD |
| **Weekends** | 09:01 - 18:00 | 20 USD |
| **Weekends** | 18:01 - 00:00 | 25 USD |

The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:

| Abbreviation | Day |
| :----------- | :------------ |
| **MO** | Monday |
| **TU** | Tuesday |
| **WE** | Wednesday |
| **TH** | Thursday |
| **FR** | Friday |
| | | |
| **SA** | Saturday |
| **SU** | Sunday |


Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. The sample data used is as shows below:
```sh
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
PEDRO=TU01:00-03:00,SA12:00-14:00,SU19:00-21:00
JAVIER=MO10:00-15:00,TU10:00-13:00,TH01:00-04:00,SA14:00-18:00,SU20:00-21:00
LUIS=MO10:00-11:00,TH01:00-05:00,SA14:00-18:00,SU18:00-21:00
```
**The example file is location under the data directory**

Output: indicate how much the employee has to be paid
For example:

Case 1:
INPUT
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

OUTPUT:
The amount to pay RENE is: 215 USD

Case 2:
INPUT
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:
The amount to pay ASTRID is: 85 USD



## 2. Explanation of Architecture

The system is divided into several packages: src: domain, repositories, services; and tests.
That's a common convention to keep the tests in a separate directory or package. This separation helps to keep the production code and the testing code organized and maintainable.
By keeping the test code in a separate package, you can also easily exclude the test code when you distribute your application. You can use tools like setuptools to build a distribution package that excludes the test files. This can make the distribution smaller and more efficient.

- The domain package contains the classes that represent the core concepts of the system, such as Employee, Schedule, and Rate.
- The repositories package contains classes that handle data access, such as EmployeeScheduleRepository and RateRepository.
- The services package contains the main business logic of the system, such as the EmployeeScheduleService class, which calculates the pay for employees based on their work schedules and the rates that apply to each shift.
- The test package implements unittest over the distint functionalities implemented on the main code. You may note that the structure behind tests is the same as main code.
- Finally, the main class PayrollSystem contains the entry point for the application.
- The architecture follows the Dependency Inversion Principle, which means that high-level modules should not depend on low-level modules, but both should depend on abstractions. In this solution, the PayrollService class depends on abstractions of the EmployeeScheduleRepository and RateRepository classes, rather than directly on their implementations. This allows the system to easily switch between different data sources without affecting the higher-level logic of the PayrollService.

## 3. Approach

The approach used to implement the Employee Payroll System is object-oriented programming. The program uses classes and objects to encapsulate the logic of the program into reusable and testable components.

The program follows the SOLID principles of object-oriented design, which emphasize the importance of Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion.

The program also follows the Test-Driven Development (TDD) methodology, which involves writing automated tests before writing the code. This approach helps ensure that the code is correct and maintainable.

## 4. Pattern designs based on dependency injection

The solution uses the Dependency Inversion Principle and the Dependency Injection pattern to decouple the higher-level PayrollService class from the lower-level EmployeeScheduleRepository and RateRepository classes. By using abstractions of the data source, the system becomes more flexible and easier to maintain, since changes to the data source can be made without affecting the higher-level logic of the PayrollService.

## 5. Clean code, solid principles

The solution follows the SOLID principles of object-oriented design, including Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion. The code is organized into well-defined classes and packages, with each class having a single responsibility. The code also uses meaningful names for variables and functions, and follows a consistent style for formatting and indentation.
## 6. Methodology and instructions on how to run the program locally

To run the program locally, follow these steps:
1. Clone the repo
   ```sh
   git clone https://github.com/pjavier1988/employment-payroll-app.git
   ```
2. Open a terminal and navigate to the root directory of the project.
   ```sh
   cd /your/directory/employment-payroll-app
   ```
3. Create a virtual environment using the following command:
   ```sh
    python -m venv venv
   ```
4. Activate the virtual environment by running the command:
   ```sh
    source venv/bin/activate (on macOS/Linux)
    or
    venv\Scripts\activate (on Windows)
   ```
5. Run the program using the command:
   ```sh
    python3 src/main.py
    or
    venv\Scripts\activate (on Windows)
   ```

## Testing
Payroll System was developed based on TDD implementation.
The Payroll System is thoroughly tested using the unittest library and MagicMock for mocking. The tests covers repositories, and services. To run the tests, you can use the following command:
```sh
python3 -m unittest -v
```
This will run all the tests in the project and provide verbose output.

You should get an oputput as follows:
   ```sh
$ python3 -m unittest -v
test_when_read_file_returns_dict (tests.repositories.test_repositories.TestRepositories) ... ok
test_when_hours_worked_on_monday_betwwen_10_and_12_return30_dollars (tests.services.test_services.TestServices) ... ok
test_when_input_employee_is_astrid_pyament_value_is85 (tests.services.test_services.TestServices) ... ok
test_when_input_employee_is_rene_pyament_value_is215 (tests.services.test_services.TestServices) ... ok
----------------------------------------------------------------------
Ran 4 tests in 0.016s
OK
```

## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
