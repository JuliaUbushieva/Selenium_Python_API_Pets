# Selenium API Testing with Swagger 🛠️

### Project Overview
This project focuses on API testing using **Selenium** and **Swagger**. It validates RESTful API endpoints with tests designed to ensure that core functionalities, such as CRUD operations, work as expected. Test results are documented using **Allure** reports.

### Project Structure
- **tests/**: Contains test cases for various API endpoints, including CRUD operations, error handling, and response validation.
- **results/**: Stores generated **Allure** reports after running the tests, providing detailed insights into test execution and results.

### Key Features
- Comprehensive **API testing** with automated validation of requests and responses.
- Use of **Swagger** to validate API schema and request/response formats.
- Integrated **Allure reports** for detailed test results.
- Coverage of **negative testing** to ensure API robustness.

### Tech Stack
- **Python**
- **Selenium** (for API interaction testing)
- **pytest** (for running tests)
- **Allure** (for generating reports)
- **requests** (for making HTTP API calls)

### Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/JuliaUbushieva/PyTests.git
    cd PyTests
    ```

2. **Install dependencies**:
    Ensure you have Python and pip installed, then install the necessary libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the tests**:
    To execute all API tests:
    ```bash
    pytest --alluredir=results/
    ```

4. **View Allure reports**:
    After running the tests, generate and open the Allure report:
    ```bash
    allure serve results/
    ```

### How It Works
- **tests/**: This folder contains test scripts for various API endpoints. Each script performs operations like sending requests (GET, POST, PUT, DELETE) and validating the responses.
- **results/**: After tests are executed, Allure reports are generated here. The reports provide detailed test logs, results, and visualizations.

### Example Usage

To run a specific API test, such as a test for the `GET` method:
```bash
pytest tests/test_get_user.py --alluredir=results/
```
This command will run the specified test and generate the Allure report in the `results/` folder.

### Continuous Integration

You can set up CI/CD with **GitHub Actions** to automate running the tests and generating reports on each code push or pull request.

### Contributing

To contribute to this project:
- Fork the repository.
- Create a new branch (`git checkout -b feature-branch`).
- Commit your changes (`git commit -m 'Add feature'`).
- Push to your branch (`git push origin feature-branch`).
- Open a pull request for review.

---

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Future Enhancements
- Expand the test coverage to include more complex API workflows.
- Integrate **performance testing** for APIs.
- Add tests for **authentication** and **authorization** mechanisms.

---
