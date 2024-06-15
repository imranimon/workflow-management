# Workflow Management

## Setup Instructions

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.x**
- **pip**: This is the Python package installer, which comes bundled with Python.

### Installation Process

Follow these steps to set up the project on your local machine:

1. **Clone the repository**:

   Open your terminal or command prompt and run the following command to clone the repository:

   ```sh
   git clone https://github.com/imranimon/workflow-management.git
   cd workflow-management
   ```

2. **Create a virtual environment** :

   A virtual environment helps isolate your project's dependencies. Run the following commands to create and activate a virtual environment:

   2.1 On Windows

   ```
   python -m venv env
   .\env\Scripts\activate
   ```

   2.2 On Mac

   ```
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install project dependencies** :

   With the virtual environment activated, install the project dependencies listed in `requirements.txt`:

   ```
   pip install -r requirements.txt
   ```

4. **Run the FastAPI application** :

   Use the following command to start the FastAPI application: The `--reload` flag ensures that the server automatically reloads when you make changes to your code.

   ```
   uvicorn main:app --reload
   ```

5. **Access the application** :

   Open your web browser and navigate to `http://127.0.0.1:8000` to see the application running.

6. **Explore the interactive API documentation** :

   FastAPI provides interactive API documentation. You can access it at the following URLs:

- **Swagger UI** : [http://127.0.0.1:8000/docs]()
- **ReDoc** : [http://127.0.0.1:8000/redoc]()
