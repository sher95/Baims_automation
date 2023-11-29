# Configuration of project steps:

1. >**Make sure python 3.5 above version installed**
2. >**Make clone of project from version control(GitHub), unzip and open in IDE**
3. >**Create new environment and make it as environment of project:**
python -m venv myenv
4. >**Activate env by typing command:**
+ >source myenv/bin/activate    # on Linux/Mac
+ >myenv\Scripts\activate.bat  # on Windows
5. >**Run command in terminal to install dependencies:**
   >pip install -r requirements.txt
6. >**Run test command:**
+  > pytest -s -v --disable-pytest-warnings --alluredir="../reports" --clean-alluredir
+  >**Or to run specific test: move to test directory and run command:**
+  > cd test_cases
+  > pytest -s -v test_biams_auto.py --disable-pytest-warnings --alluredir="../reports" --clean-alluredir
7. >**To run allure report in command line: In current path(e.g. /Project_name/test_cases:) run this command:**
   > allure serve "../reports"


# Jenkins command:
+ >**Install the latest LTS version: brew install jenkins-lts**
+ >**Start the Jenkins service: brew services start jenkins-lts**
+ >**Restart the Jenkins service: brew services restart jenkins-lts**
+ >**Update the Jenkins version: brew upgrade jenkins-lts**
