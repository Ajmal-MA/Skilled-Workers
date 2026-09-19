\# Skilled Workers



A Django-based web platform that connects customers with skilled workers for different services such as plumbing, electrical work, painting, welding, and fabrication.



\## Features



\### Customer Features



\* Customer registration and login

\* Browse available services

\* Submit service requests

\* View worker profiles

\* Contact workers for services



\### Worker Features



\* Worker registration and login

\* Create and manage worker profiles

\* Add skills and service details

\* Upload work/project images

\* View available service requests



\### Admin Features



\* Manage customers

\* Manage workers

\* Manage service requests

\* Manage website content



\## Services



The platform can support different skilled services, including:



\* Plumbing

\* Electrical work

\* Painting

\* Welding

\* Fabrication

\* Other skilled services



\## Technologies Used



\* Python

\* Django

\* HTML

\* CSS

\* JavaScript

\* Bootstrap

\* SQLite

\* REST API



\## Project Structure



```text

Skilled-Workers/

│

├── Skilled\_workers\_project/

│   ├── Accounts/

│   ├── customers/

│   ├── workers/

│   ├── main/

│   ├── templates/

│   ├── static/

│   ├── media/

│   ├── manage.py

│   └── requirements.txt

│

├── .gitignore

└── README.md

```



\## Installation



\### 1. Clone the repository



```bash

git clone https://github.com/Ajmal-MA/Skilled-Workers.git

cd Skilled-Workers

```



\### 2. Create a virtual environment



```bash

python -m venv venv

```



\### 3. Activate the virtual environment



Windows:



```bash

venv\\Scripts\\activate

```



\### 4. Install dependencies



```bash

pip install -r Skilled\_workers\_project/requirements.txt

```



\### 5. Configure environment variables



Create a `.env` file inside the `Skilled\_workers\_project` folder and add:



```env

SECRET\_KEY=your-secret-key

```



Do not upload the `.env` file to GitHub.



\### 6. Run migrations



```bash

cd Skilled\_workers\_project

python manage.py migrate

```



\### 7. Start the development server



```bash

python manage.py runserver

```



Open the application in your browser:



```text

http://127.0.0.1:8000/

```



\## Future Improvements



\* Online worker/customer chat

\* Worker ratings and reviews

\* Location-based worker search

\* Online payment integration

\* Email/SMS notifications

\* Advanced search and filtering



\## Author



\*\*Ajmal MA\*\*



GitHub: https://github.com/Ajmal-MA



