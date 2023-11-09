# ntizu-backend

## Setup Instructions

### Prerequisites


Before running the project, make sure you have the following installed:

-   Python (version 3.12.0)
-   Django (version 4.2.7)
-   Django Rest Framework (version 3.14.0)
   

### Installation


1. **Clone the repository:**

    ```bash
    git clone https://github.com/JersonCamara/ntizu-backend.git
    cd ntizu-backend

2.  **Create a Virtual Environment:**

    ```bash
    python -m venv venv

3.  **Activate the Virtual Environment:**

    -   On Windows:

        ```bash
        venv\Scripts\activate

    -   On Unix or MacOS:

        ```bash
        source venv/bin/activate

4.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt

5.  **Run Migrations:**

    ```bash
    python manage.py migrate

6.  **Create a Superuser (Optional):**

    ```bash
    python manage.py createsuperuser

7.  **Start the Development Server:**

    ```bash
    python manage.py runserver

   - The development server will be running at <http://localhost:8000/>.

8.  **Access the Admin Panel (Optional):**

    If you created a superuser, you can access the admin panel at <http://localhost:8000/admin/>.
