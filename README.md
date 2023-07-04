<p align="center">
  <img src="https://github.com/PORTUNO-SMD/portuno-api/assets/86852231/cc09cfb8-8599-4fc0-94ae-f990a5487514" width="100px">
</p>

# PORTUNO API

The **PORTUNO API** is a Python API that implements CRUD _(Create, Read, Update, Delete)_ endpoints for the entities and tables of the `PostgreSQL` database: Classroom, Occupancy, Permission, User, Professor, SchoolClass, and Semester. The API is built using `Flask`, which is a lightweight and modular web framework.

The PORTUNO project was conceived as part of the Integrated Project I course and developed as part of the Database I course in the Systems and Digital Media program at UFC (Federal University of Ceará).

# Getting started

Before starting to use the API, please follow the configuration steps below:

**Clone the repository to your local environment:**

   ```
   git clone https://github.com/your-username/portuno-api.git
   ```

**Create a `.env` file in the project's root directory and set the required environment variables. These variables include the database credentials and other environment-specific configurations. A basic example of the `.env` file content is shown below:**

   ```
   USER
   PASSWORD
   HOST
   PORT
   DATABASE
   ```

**Install the project dependencies. In the project's root directory, run the following command:**

   ```
   pip install -r requirements.txt
   ```

**After completing the above steps, you are ready to start the API.**

# Endpoints

The API follows an architecture with entity, DAO (Data Access Object), and controller layers. Each entity corresponds to a table in the database and has dedicated endpoints for CRUD operations. Below is the table with the available endpoints for each entity:

### Class

| Method  | Endpoint           | Description                                 |
|---------|--------------------|---------------------------------------------|
| GET     | /classes           | Get all classes                              |
| GET     | /classes/{id}      | Get a specific class                         |
| POST    | /classes           | Create a new class                           |
| PUT     | /classes/{id}      | Update an existing class                     |
| DELETE  | /classes/{id}      | Delete a specific class                      |

**Request Body to POST:**

```
{
    "day_week": "segunda",
    "subject": "xxxxxxxxx",
    "hour": "10:00:00"
}
```

### Classroom

| Method  | Endpoint           | Description                                 |
|---------|--------------------|---------------------------------------------|
| GET     | /classrooms        | Get all classrooms                           |
| GET     | /classrooms/{id}   | Get a specific classroom                     |
| POST    | /classrooms        | Create a new classroom                       |
| PUT     | /classrooms/{id}   | Update an existing classroom                 |
| DELETE  | /classrooms/{id}   | Delete a specific classroom                  |

**Request Body to POST:**

```
{
        "floor": 1,
        "id": 100,
        "name": "Laboratório XX",
        "professor": null,
        "short_name": "Lab. XX",
        "type": "laboratório de informática"
}
```

### Occupancy

| Method  | Endpoint           | Description                                 |
|---------|--------------------|---------------------------------------------|
| GET     | /occupancies       | Get all occupancies                          |
| GET     | /occupancies/{id}  | Get a specific occupancy                     |
| POST    | /occupancies       | Create a new occupancy                       |
| PUT     | /occupancies/{id}  | Update an existing occupancy                 |
| DELETE  | /occupancies/{id}  | Delete a specific occupancy                  |

**Request Body to POST:**

```
{
    "goal": "Dar aula",
    "classroom": 11,
    "user": 98765,
    "semester": "2023.1",
    "class": null
}
```

### Permission

| Method  | Endpoint           | Description                                 |
|---------|--------------------|---------------------------------------------|
| GET     | /permissions       | Get all permissions                          |
| GET     | /permissions/{id}  | Get a specific permission                    |
| POST    | /permissions       | Create a new permission                      |
| PUT     | /permissions/{id}  | Update an existing permission                |
| DELETE  | /permissions/{id}  | Delete a specific permission                 |

**Request Body to POST:**

```
{
    "beginning_date_time": "2023-06-22",
    "ending_date_time": "2023-06-30",
    "classroom": 4,
    "user": 527898,
    "professor": 556891
}
```

### User

| Method  | Endpoint           | Description                                 |
|---------|--------------------|---------------------------------------------|
| GET     | /users             | Get all users                                |
| GET     | /users/{id}        | Get a specific user                          |
| POST    | /users             | Create a new user                            |
| PUT     | /users/{id}        | Update an existing user                      |
| DELETE  | /users/{id}        | Delete a specific user                       |


**Request Body to POST:**

```
{
    "ddd": 85,
    "id": 509697,
    "name": "João Victor",
    "number": 987560857,
    "password": "sE0724"
}
    
```

### Professor

| Method  | Endpoint           | Description                                 |
|---------|--------------------|---------------------------------------------|
| GET     | /professors        | Get all professors                           |
| GET     | /professors/{id}   | Get a specific professor                     |
| POST    | /professors        | Create a new professor                       |
| PUT     | /professors/{id}   | Update an existing professor                 |
| DELETE  | /professors/{id}   | Delete a specific professor                  |

**Request Body to POST:**

```
 {
    "ddd": 85,
    "id": 98765,
    "name": "George Gomes",
    "number": 1111111111,
    "password": "george123"
}
    
```

### Semester

| Method  | Endpoint           | Description                                 |
|---------|--------------------|---------------------------------------------|
| GET     | /semesters         | Get all semesters                            |
| GET     | /semesters/{id}    | Get a specific semester                      |
| POST    | /semesters         | Create a new semester                        |
| PUT     | /semesters/{id}    | Update an existing semester                  |
| DELETE  | /semesters/{id}    | Delete a specific semester                   |

**Request Body to POST:**

```
{
    "beginning_date": "2023-08-03",
    "ending_date": "2023-06-13",
    "name": "2023.1"
}
```
