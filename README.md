
**Employee Salary Analysis Using NumPy**

 Description

This Python program uses the **NumPy** library to analyze employee salary data. The program stores employee details such as name, email, and salary in a list and performs the following operations:

1. Finds the employee with the highest salary.
2. Finds the employee with the lowest salary.
3. Calculates the average salary of all employees.

NumPy functions are used to perform these calculations efficiently.

---

## Requirements

* Python 3.x
* NumPy Library

## Employee Data Structure

The employee data is stored as a list of lists.

''' python
employees = [
    ["Omkar", "omkar@gmail.com", 80000],
    ["Parth", "parth@gmail.com", 60000],
    ["Ram", "ram@gmail.com", 55000],
    ["Rahul", "rahul@gmail.com", 70000],
    ["Madhav", "madhav@gmail.com", 45000]
]
''' 
### Fields

| Index | Description     |
| ----- | --------------- |
| 0     | Employee Name   |
| 1     | Employee Email  |
| 2     | Employee Salary |

---

## NumPy Functions Used

### `np.array()`

Converts salary values into a NumPy array.

```python
salaries = np.array([emp[2] for emp in employees])
```

### `np.max()`

Finds the highest salary.

```python
max_salary = np.max(salaries)
```

### `np.argmax()`

Returns the index of the highest salary.

```python
max_index = np.argmax(salaries)
```

### `np.min()`

Finds the lowest salary.

```python
min_salary = np.min(salaries)
```

### `np.argmin()`

Returns the index of the lowest salary.

```python
min_index = np.argmin(salaries)
```

### `np.mean()`

Calculates the average salary.

```python
average_salary = np.mean(salaries)
```

---

## Program Flow

1. Import NumPy library.
2. Create employee dataset.
3. Extract salary values into a NumPy array.
4. Find highest salary employee.
5. Find lowest salary employee.
6. Calculate average salary.
7. Display results.


## Advantages of Using NumPy

* Faster numerical computations.
* Efficient memory usage.
* Built-in statistical functions.
* Suitable for large datasets.
* Widely used in Data Science and Machine Learning.

## Conclusion

This project demonstrates how NumPy can be used to perform salary analysis on employee data. The program efficiently identifies the highest-paid employee, the lowest-paid employee, and computes the average salary using NumPy's optimized functions.
