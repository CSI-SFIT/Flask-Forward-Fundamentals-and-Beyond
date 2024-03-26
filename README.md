# FLASK FORWARD FUNDAMENTALS AND BEYOND

<p align="center">
  <img src="static/assets/img.png" width="200" />
</p>

> ## Introduction

Flask is a micro web framework for Python. It allows developers to build web applications quickly and easily. It is known for its simplicity and flexibility, making it a popular choice for both beginners and experienced developers.

> ## Pre-Requisites

**(Depending on your project, these software may or may not be required. Install accordingly)**

You can follow with Automatic Installation or Manual Installation!

### Automatic Installation:

To know how this script works, you can check by visiting this [repository](https://github.com/Tetroner9/CSI).

1. Open this [link](https://raw.githubusercontent.com/Tetroner9/CSI/main/run.bat) and right click, save as run.bat
2. Create a folder anywhere in your system and paste the bat file there.
3. Run the run.bat file just by double clicking it. <span style="color:red">DO NOT RUN AS ADMINISTRATOR.</span>
If prompted for UAC (yes or no), press Yes.
4. After the first file is executed successfully without any errors. Run the file.bat from same directory by double clicking.
5. A folder called Flask-Project must be created and VS Code opened in that directory.

***If any issues occur during installation you can post the issue [here](https://github.com/Tetroner9/CSI/issues/new).***
### Manual Installation:

**(Follow default installation steps. Make sure to tick add .PATH for python)**

- Softwares:
  - <span style="color:red">[Python](https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe) - REQUIRED</span>
  - [Git](https://github.com/git-for-windows/git/releases/download/v2.44.0.windows.1/Git-2.44.0-64-bit.exe) - To clone the repository
  - Any code editor of your choice, preferably [VS Code](https://code.visualstudio.com/docs/?dv=win64user)
  - [XAMPP Control Center](https://sourceforge.net/projects/xampp/files/latest/download)
  - [MongoDB Server](https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-7.0.7-signed.msi)

 - Python packages used for this project
   ```shell
   pip install blinker certifi charset-normalizer click colorama dnspython Flask Flask-Mail Flask-MySQLdb idna itsdangerous Jinja2 MarkupSafe mysql-connector-python passlib pymongo razorpay requests urllib3 Werkzeug
   ```

> ## Steps to be followed

- Clone The Repo:
  ```shell
  git clone https://github.com/CSI-SFIT/Flask-Forward-Fundamentals-and-Beyond.git
  ```
  - Paste the above command in your cmd.

- Flask Mail:
  - Set MAIL_USERNAME as your SFIT email account
  - Set MAIL_PASSWORD as your email id password
  - Visit this [link](https://myaccount.google.com/lesssecureapps?pli=1) >> Select your SFIT account >> Allow less secure apps
  (Make sure you have 2FA disabled for this to work)

- XAMPP:
  - Open XAMPP Control Center and Start both Apache & MySQL:
  ![XAMPP Control Center](/screenshots/1.png)
  ![XAMPP Control Center](/screenshots/2.png)
  - After the admin page is opened click on new database and type database name as portfolio
  ![MySQL admin page](/screenshots/3.png)
  ![MySQL create database](/screenshots/4.png)
  - Select the portfolio database and paste the following lines in the SQL tab
      ```sql
      CREATE TABLE projects (
        sno INT AUTO_INCREMENT PRIMARY KEY,
        title TEXT,
        description TEXT,
        link VARCHAR(255),
        img_file VARCHAR(255),
        date DATE
      );

      CREATE TABLE contacts (
        sno INT AUTO_INCREMENT PRIMARY KEY,
        name TEXT,
        phone VARCHAR(20),
        msg TEXT,
        date DATE,
        email VARCHAR(255)
      );
      ```
    ![MySQL tables](/screenshots/5.png)

- Sessions:
  - Replace every instance of **YOUR_NAME** with your actual name in the [main.py](main.py) file.

- Add you emailID to following [line](https://github.com/CSI-SFIT/Flask-Forward-Fundamentals-and-Beyond/blob/bb0507ef0a22601b667a256cdecbecd35f121205/main.py#L48)
  ```python
  sender='',
  #sender='youremail@example.com';
  ```

> ## Acknowledgements

CSI SFIT Tech Team 2023 - 2024

- Tech Head: [Yogiraj](https://github.com/yogiiieee)
- Joint Tech Head: [Ojas]()
- Tech Executives:-
  - [Vijet](https://github.com/avogadronuggies)
  - [Prathamesh](https://github.com/PrathameshDesai0409)
  - [Reuben](https://github.com/ReubenMatrix)
  - [Om](https://github.com/Tetroner9)
  - [Tanmay](https://github.com/tannmayy14)
  - [Viraj]()

<p align="center">
  <a href="https://www.csi.sfit.ac.in/">
    <img src="static/assets/img_1.png" width="250" />
  </a>
</p>
