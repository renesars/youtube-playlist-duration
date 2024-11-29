# 🎶 YouTube Playlist Duration Calculator 🎬
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A Python script that calculates the total duration of a YouTube playlist by leveraging the YouTube Data API v3. This tool retrieves all the videos in a playlist, calculates their total duration, and displays it in minutes. ⏳

## 📚 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Project Structure](#project-structure)
- [API Key Setup](#api-key-setup)
- [Contributing](#contributing)
- [License](#license)

## 🚀 Project Overview

The **YouTube Playlist Duration Calculator** is a Python-based solution to help YouTube creators, researchers, or users calculate the cumulative time of all the videos in a specific playlist. By providing the playlist URL, this tool fetches all the videos, aggregates their individual durations, and presents the total playlist length in a clear and concise format. 🎧

The project uses the **YouTube Data API v3** to fetch the data of the videos in the playlist. This script takes the playlist link as input, retrieves video metadata like the duration of each video, and adds them up to give the total playlist duration. 🧮

## ✨ Features

- **Playlist Duration Calculation**: Automatically fetches all videos in a YouTube playlist and calculates the total playlist duration in minutes. 📊
- **Easy-to-Use Interface**: Simple input for the playlist link and quick calculation of the playlist's total duration. ⏱️
- **Error Handling**: Handles potential errors such as invalid playlist links, API issues, or quota errors gracefully. 🚨

## 🛠️ Technologies Used

- **Python 3.x**: The main programming language for the script. 🐍
- **Google API Client**: For accessing the YouTube Data API v3 to fetch playlist data. 🌐
- **isodate**: For parsing video durations in ISO 8601 format. 📅
- **YouTube Data API v3**: The API used to access information about the videos in the playlist. 📹


## 🏗️ Installation


To use the YouTube Playlist Duration Calculator, follow these steps:

1. **Clone the repository**:
   ```bash
       git clone https://github.com/your-username/youtube-playlist-duration.git
   

2. **🗂 Navigate to the Project Folder**
    ```bash
        cd youtube-playlist-duration


3. **💻 Create a Virtual Environment (Optional but Recommended)**


Creating a virtual environment helps to manage dependencies and keep your project isolated.

  For macOS/Linux:
   ```bash
        python3 -m venv venv
```
  ```bash
        source venv/bin/activate  # For macOS/Linux
```

  For Windows:
  ```bash
        venv\Scripts\activate
```

4. **🛠️ Install the Required Dependencies**


  Once the virtual environment is activated, install the required dependencies from the `requirements.txt` file.

```bash
        pip install -r requirements.txt
```

  If **requirements.txt** doesn't exist yet, you can manually install the following libraries:
```bash
        pip install google-api-python-client isodate
```

## 📝 How to Use

  **Step 1: 🗝️ Obtain a YouTube Data API Key**


  To access the YouTube Data API v3, you'll need to create an API key.


  -Go to the **Google Cloud Console**.

  -Create a new project or use an existing one.

  -Enable the **YouTube Data API v3**.

  -Navigate to **APIs & Services > Credentials**.

  -Click on **Create Credentials**, and select **API Key**.

  -Copy the generated **API Key**.


**Step 2: 🚀 Run the Script**


  Open the terminal or command prompt in the project directory and run the script:

```bash
        python youtube_playlist_duration.py
```

  The script will prompt you for the YouTube playlist ***URL***. Enter the playlist ***URL***, and the script will calculate and display the total playlist duration in minutes. 🎥


**Example:**

```bash
Enter the YouTube playlist URL: https://www.youtube.com/playlist?list=PLid4wTCw-WDWaXg0RWAzwk-fgpPPr9OgQ

Total duration of the playlist: 123.45 minutes
```

## 🗂️ Project Structure

  The project contains the following files:


```bash
youtube-playlist-duration/
│
├── youtube_playlist_duration.py       # The Python script that calculates the playlist duration.
├── requirements.txt                  # A list of required libraries for the project.
├── README.md                         # The README file (this one).
└── .gitignore                        # Git ignore file to avoid committing unnecessary files.
```


## 🔑 API Key Setup

  To use the script, make sure your API key is set up correctly in the code.


Replace the **YOUR_API_KEY_HERE** placeholder in the script with your own **API key**:

```python
          youtube = build("youtube", "v3", developerKey="YOUR_API_KEY_HERE")
```

Alternatively, you can store your API key in a .env file and load it using a library like *python-dotenv* (optional).


## 🤝 Contributing

  We welcome contributions to the project! If you'd like to contribute:


  -Fork the repository.

  -Create a new branch (git checkout -b feature-name).

  -Make your changes.

  -Commit your changes (git commit -am 'Add new feature').

  -Push to the branch (git push origin feature-name).

  -Open a pull request.


  Please make sure your changes are well-documented and your code adheres to the style guide of the project.


## License

  This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

  ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

  ### Summary of the MIT License

  The MIT License is a permissive free software license that allows you to:

  - Use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.

  - Modify the Software and incorporate it into other works.

  - Use the Software in both open-source and proprietary projects.


However, it comes with no warranty. The software is provided "as is," without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, or non-infringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

For the full text of the MIT License, refer to the [LICENSE](./LICENSE) file.
