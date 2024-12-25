# Reddit Gen

This program generates a .mp4 video automatically by querying the top post on the
r/askreddit subreddit, and grabbing several comments. The workflow of this program is:

---
## Setup
---

#### Clone Repository

```
git clone https://github.com/rachan2005/reddit_gen.git
cd reddit_gen
```
---

#### Installation

1. **Set Up a Virtual Environment**:
   - It is recommended to use a virtual environment to manage your project dependencies. You can create and activate a virtual environment using the following commands:
     ```sh
     python -m venv venv
     ```
   - To **activate** the virtual environment:
     - On Windows:
       ```sh
       .\venv\Scripts\activate
       ```
     - On macOS and Linux:
       ```sh
       source venv/bin/activate
       ```

2. **Install Chocolatey** (Windows only):
   - Chocolatey is a package manager for Windows that simplifies the installation of software. To install Chocolatey, open a PowerShell terminal with administrative privileges and run the following command:
     ```sh
     Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
     ```

3. **Install ffmpeg and CMake**:
   - Ensure you have `ffmpeg` and `cmake` installed on your system. You can install them using Chocolatey:
     ```sh
     choco install ffmpeg
     choco install cmake
     ```

4. **Install Python Dependencies**:
   - Ensure you have Python and the required libraries installed. You can install the required Python libraries using:
     ```sh
     pip install -r requirements.txt
     ```

5. **Prepare Template Videos**:
   - Ensure you have template videos in the [BackgroundVideos](http://_vscodecontentref_/0) folder. The videos should be named as `ShortTemplate_0.mp4`, `ShortTemplate_1.mp4`, and so on.
---
#### Build

1. **Create Build Directory and Run CMake**:
   - Open a terminal in the project directory and run the following commands:
     ```sh
     cd build
     cmake .
     cmake --build . --target RunCommands
     ```

   - This will create the necessary directories and duplicate the [`config.example.ini`](config.example.ini ) file to [`config.ini`](config.ini ).

#### Register with Reddit

   To interact with Reddit's API, you need to create a Reddit application and obtain the necessary credentials. Follow these steps to set up your Reddit application:

   1. **Create a Reddit Account**:
      - If you do not already have a Reddit account, you will need to create one. You can sign up [here](https://www.reddit.com/register/).

   2. **Navigate to Reddit's App Preferences**:
      - Once you have a Reddit account, go to the [Reddit App Preferences](https://www.reddit.com/prefs/apps) page.

   3. **Create a New Application**:
      - Scroll down to the "Developed Applications" section and click on the "Create App" or "Create Another App" button.

   4. **Fill Out the Application Form**:
      - **Name**: Enter a name for your application. This can be anything you like.
      - **App Type**: Select "script" as the type of application.
      - **Description**: Optionally, provide a description for your application.
      - **About URL**: This can be left blank or you can provide a URL with more information about your application.
      - **Redirect URI**: Enter `http://localhost:8000` or any valid URL. This is required but not used for script-type applications.
      - **Permissions**: Select the necessary permissions your application will need. For this project, you typically need read access.

   5. **Save the Application**:
      - Click the "Create app" button to save your new application.

   6. **Copy the Credentials**:
      - After creating the application, you will see a "client ID" (you can find it under ***personal use script***) and a "client secret". Copy these credentials as you will need them for the next step.

   7. **Update [config.ini](http://_vscodecontentref_/1)**:
      - Open the [config.ini](http://_vscodecontentref_/2) file in your project directory.
      - Locate lines 22 to 24 and update them with the credentials you copied:
        ```ini
        client_id = YOUR_CLIENT_ID
        client_secret = YOUR_CLIENT_SECRET
        user_agent = YOUR_USER_AGENT
        ```
      - Replace `YOUR_CLIENT_ID` with the client ID you copied.
      - Replace `YOUR_CLIENT_SECRET` with the client secret you copied.
      - Replace `YOUR_USER_AGENT` with a user agent string (e.g., `my_reddit_app:v1.0 (by /u/your_reddit_username)`).

   By following these steps, you will have successfully registered a Reddit application and configured your project to use the Reddit API with the necessary credentials.

---
#### Running the Program

- Now, you can run the program using:
  ```sh
  python main.py
  ```

---
THANK YOU :)
---
