<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F2027,50:203A43,100:2C5364&height=250&section=header&text=QuickBite%20QA%20Automation&fontSize=50&fontColor=ffffff&animation=fadeIn"/>

# 🚀 QuickBite QA Automation

### 🧪 Web Automation Testing using Python, Selenium & Pytest

<p>
<img src="https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python"/>
<img src="https://img.shields.io/badge/Selenium-WebDriver-green?style=for-the-badge&logo=selenium"/>
<img src="https://img.shields.io/badge/Pytest-Testing-orange?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Browser-Chrome-yellow?style=for-the-badge&logo=googlechrome"/>
<img src="https://img.shields.io/badge/Tests-10-success?style=for-the-badge"/>
</p>

### ⚡ Automated functional and navigation testing for the QuickBite food ordering website

</div>

---

# 📖 Overview

This project is a **Web UI Automation Testing project** created using **Python, Selenium WebDriver, and Pytest**.

The project automates important user-facing functionalities of the **QuickBite food ordering website**, including homepage verification, navigation, search, restaurant sorting, cart navigation, and food ordering navigation.

The goal is to demonstrate practical **QA Automation**, including:

- 🌐 Web UI Testing
- 🧪 Functional Testing
- 🔄 Navigation Testing
- ✅ Assertion & Validation
- 🤖 Selenium WebDriver Automation
- 📋 Pytest Test Execution

---

# 🌐 Application Under Test

**QuickBite – Food Ordering Website**

🔗 https://quickbite-varshith.netlify.app/

QuickBite is a food ordering web application that provides functionality such as:

- Restaurant browsing
- Food item browsing
- Search
- Cart
- Ordering
- Restaurant sorting
- User profile functionality

---

# ✨ Test Coverage

The project currently contains **10 automated Selenium tests**.

| # | Test Scenario | Status |
|---|---------------|:------:|
| 1 | Verify QuickBite homepage title | ✅ |
| 2 | Verify homepage elements and content | ✅ |
| 3 | Verify Order Now button | ✅ |
| 4 | Verify Search visibility and click | ✅ |
| 5 | Verify restaurant sorting option | ✅ |
| 6 | Verify Cart visibility and click | ✅ |
| 7 | Verify Search navigation | ✅ |
| 8 | Verify Cart navigation | ✅ |
| 9 | Verify Home navigation | ✅ |
| 10 | Verify Order Now navigation | ✅ |

---

# 🏗️ Automation Architecture

```text
                  QuickBite Website
                         │
                         ▼
                  Selenium WebDriver
                         │
                         ▼
                  Browser Interaction
                         │
                         ▼
                  Element Identification
                         │
                         ▼
                    User Actions
                         │
                         ▼
                   Assertions
                         │
                         ▼
                    Pytest Result


```

---

# 📂 Project Structure

```text
qa-automation-project/
│
├── 📂 tests/
│   └── test_quickbite.py
│
├── 📂 scripts/
│   └── scripts/
│       └── test_login.py
│
├── 📂 screenshots/
│
├── 📜 README.md
├── 📜 project-notes.md
├── 📜 requirements.txt
└── 📜 .gitignore
```

---

# 💻 Tech Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python 3.13 | Test Automation Programming |
| 🧪 Selenium WebDriver | Browser Automation |
| ⚙️ Pytest | Test Framework |
| 🌐 Google Chrome | Browser Testing |
| 🔧 Git | Version Control |
| 🐙 GitHub | Source Code Management |

---

# 🔍 Testing Approach

The automation framework uses Selenium WebDriver to interact with the QuickBite web application through a Chrome browser.

The tests follow this process:

```text
Open Application
       ↓
Locate Web Element
       ↓
Verify Element
       ↓
Perform User Action
       ↓
Wait for Page Update
       ↓
Validate Expected Result
       ↓
Pass / Fail
```

The tests use **Pytest fixtures** to create and close the Selenium WebDriver instance.

---

# 🧩 Pytest Fixture

The project uses a Pytest fixture for browser setup and teardown.

```python
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
```

This ensures that:

- Chrome starts before each test
- The browser window is maximized
- The WebDriver is available to the test
- Chrome closes after the test completes

---

# 🧪 Example Automation Test

```python
def test_search_navigation(driver):
    driver.get("https://quickbite-varshith.netlify.app/landing_page")

    search = driver.find_element(
        By.XPATH, "//a[normalize-space()='Search']"
    )

    assert search.is_displayed()
    assert search.is_enabled()

    search.click()

    time.sleep(3)

    assert "/searchpage/search" in driver.current_url
```

This test verifies that the **Search** navigation link is available and successfully navigates to the Search page.

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone https://github.com/varshith525/quickbite-qa-automation.git
```

## 2. Navigate to the project

```bash
cd quickbite-qa-automation
```

## 3. Create a virtual environment

### macOS / Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Tests

Run the QuickBite automation suite:

```bash
pytest tests/test_quickbite.py
```

Run tests with detailed information:

```bash
pytest tests/test_quickbite.py -v
```

Run tests with printed output:

```bash
pytest tests/test_quickbite.py -s
```

---

# 📊 Test Execution

The current test suite contains **10 automated tests**.

```text
10 Automated Tests
        ↓
Selenium WebDriver
        ↓
Chrome Browser
        ↓
QuickBite Website
        ↓
Pytest Assertions
        ↓
Test Result
```

Example successful execution:

```text
============================= test session starts =============================

collected 10 items

tests/test_quickbite.py ..........                         [100%]

============================== 10 passed ==============================
```

---

# 🧪 QA Skills Demonstrated

### Functional Testing

Automating and validating important user-facing functionality of the QuickBite application.

### UI Testing

Verifying that buttons, links, page content, and navigation elements are displayed and usable.

### Navigation Testing

Validating navigation between:

- Home
- Search
- Cart
- Food Items

### Assertions

Using Pytest assertions to validate expected application behavior.

### Browser Automation

Using Selenium WebDriver to automate Google Chrome.

### Pytest Fixtures

Using fixtures for reusable WebDriver setup and teardown.

### Element Locators

Using Selenium locators such as:

- XPath
- Tag Name

---

# 📸 Screenshots

Screenshots from test execution can be stored in:

```text
screenshots/
```

Future improvements can include automatically capturing screenshots whenever a test fails.

---

# 🔄 Future Improvements

The current project focuses on functional and navigation automation.

Future improvements may include:

- 🔄 Page Object Model (POM)
- ⏱️ Selenium Explicit Waits
- 📊 HTML Test Reports
- 📸 Automatic Screenshot Capture on Failure
- 🌐 Cross-Browser Testing
- ⚡ Parallel Test Execution
- 🔄 Data-Driven Testing
- 🤖 GitHub Actions CI/CD
- 📈 Allure Reporting

---

# 🎯 Project Objectives

The main objectives of this project are:

```text
Python
   +
Selenium WebDriver
   +
Pytest
   +
Web UI Testing
   +
Functional Testing
   +
Navigation Testing
   +
Git & GitHub
```

This project demonstrates hands-on experience in creating, executing, and maintaining automated browser tests for a real-world web application.

---

# 📈 Testing Workflow

```text
Requirement
     ↓
Identify Test Scenario
     ↓
Identify Web Elements
     ↓
Create Selenium Test
     ↓
Run with Pytest
     ↓
Verify Expected Result
     ↓
Fix / Improve Test
     ↓
Commit to Git
     ↓
Push to GitHub
```

---

# 🌟 Why This Project?

✔ Real web application testing

✔ Selenium WebDriver automation

✔ Python-based test development

✔ Pytest test execution

✔ Functional and UI testing

✔ Navigation validation

✔ Browser automation

✔ Git and GitHub version control

✔ Practical QA automation experience

---

# 👨‍💻 Author

<div align="center">

# BUPANA VARSHITH

### QA Automation | Python | Selenium | Pytest

<p>
<a href="https://github.com/varshith525">
<img src="https://img.shields.io/badge/GitHub-Profile-black?style=for-the-badge&logo=github">
</a>
</p>

### 🚀 QA Automation Portfolio Project

⭐ If you find this project useful, feel free to star the repository!

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2C5364,100:0F2027&height=120&section=footer"/>

</div>
