# Employees_server

**Setup**

## Create a virtul env 
`python3.6 -m venv empenv`

# Activate the virtual environment

For Windows:

venv\Scripts\activate

# For Linux or macOS:
source empenv/bin/activate

## Run Migrations

python manage.py makemigrations

python manage.py migrate


## API Documentation

### Create Employee

#### Endpoint

- **URL**: `/api/employee/create/`
- **Method**: `POST`

- **Body**: JSON
  ```json
  {
    "name": "xyzpk",
    "email": "kumar@gmail.com",
    "age": 25,
    "gender": "male",
    "phone_no": "1234567890",
    "address_details": {
        "hno": "123",
        "street": "xyz",
        "city": "xyz",
        "state": "xyz"
    },
    "work_experience": [
        {
            "companyName": "xyz",
            "fromDate": "20-05-2019",
            "toDate": "20-09-2021",
            "address": "xyz"
        }
    ],
    "qualifications": [
        {
            "qualificationName": "ssc",
            "fromDate": "20-05-2012",
            "toDate": "20-05-2013",
            "percentage": 85
        }
    ],
    "projects": [
        {
            "titile": "xyz",
            "description": "description of the project"
        }
    ]
}


### Get Employee Details

#### Endpoint

- **Get Employee Details by ID:**
  - `GET /api/employees/?regid=123`: Details of the employee with ID 123.
  - **Method**: `GET`

- **Get Details of All Employees:**
  - `GET /api/employees/`: Details of all employees.
  - **Method**: `GET`

### Delete Employee

#### Endpoint

- **URL**: `/api/employee/delete_employee/`
- **Method**: `DELETE`

#### Request

- **Body**: JSON
  ```json
  {
      "regid": 2
  }


### Update Employee

#### Endpoint

- **URL**: `/api/employee/id/update_employee/`
- **Method**: `PUT`

- **Body**: JSON
  ```json
  {
    "name": "xyzpk",
    "email": "kumar@gmail.com",
    "age": 25,
    "gender": "male",
    "phone_no": "1234567890",
    "address_details": {
        "hno": "123",
        "street": "xyz",
        "city": "xyz",
        "state": "xyz"
    },
    "work_experience": [
        {
            "companyName": "xyz",
            "fromDate": "20-05-2019",
            "toDate": "20-09-2021",
            "address": "xyz"
        }
    ],
    "qualifications": [
        {
            "qualificationName": "ssc",
            "fromDate": "20-05-2012",
            "toDate": "20-05-2013",
            "percentage": 85
        }
    ],
    "projects": [
        {
            "titile": "xyz",
            "description": "description of the project"
        }
    ]
}
