

<a name="readme-top"></a>


  <h3 align="center">Intellihome</h3>

  <p align="center">
    Your AI-Powered Smart Home Companion
    <br />
    <a href="https://github.com/xXlyitemXx/Mira-Intellihome"><strong>Explore the Code »</strong></a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#features">Features</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

Intellihome is a Python-based smart home system designed to understand and respond to your needs through voice commands, gestures, and facial recognition. Powered by Google's Gemini flash and leveraging the power of OpenCV and Mediapipe, Intellihome seamlessly integrates into your daily life, making it easier and more comfortable.

### Features

* **Natural Language Processing:** Interact with Mira, your AI assistant, using natural language to get information, set reminders, and control smart devices.
* **Gesture Recognition:** Use simple hand gestures to control various aspects of your home environment.
* **Facial Recognition:** Intellihome can recognize you and personalize settings based on your preferences.
* **OpenWeatherMap Integration:**  Get real-time weather updates for your location.
* **Continuously Learning:** Intellihome adapts and learns your habits over time to provide a personalized experience. 

### Built With

* [Python](https://www.python.org/)
* [Gemini-url](https://aistudio.google.com)
* [OpenCV-url](https://opencv.org/)
* [Mediapipe-url](https://chuoling.github.io/mediapipe/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Python 3.6 or higher
* pip (package installer for Python)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/xxlyitemxx/Mira-Intellihome.git
content_copy
Use code with caution.
Markdown

Navigate to the project directory:

cd Intellihome
content_copy
Use code with caution.
Sh

2. Install required packages:
```sh
   pip install -r requirements.txt
```
Obtain API keys:

Google Gemini flash: [Gemini API key](https://aistudio.google.com)

OpenWeatherMap: [OpenWeatherMap API key](https://openweathermap.org/api)

Configure API keys:

Create a config.json file in the project's root directory.

Add the following lines, replacing placeholders with your actual keys:
```
{
    "api_key": "Your Gemini api key!",
    "city":"Your city!"
} 
```

(back to top)

Usage

Run the main script:
```
python main.py
```

Start interacting with Mira using voice commands.

Examples:

  "What time is it?"
  
  "How many fingers can you see?"
  
  "What's the weather like?"
  
  "Tell me a joke."

(back to top)

Roadmap

  * Integrate with smart home devices
  
  * Implement facial recognition for personalized user profiles
  
  * Expand gesture recognition capabilities
  
  * Develop a user interface for easier control and settings customization

(back to top)

Contributing

  * Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.
  
  * Fork the Project
  
  * Create your Feature Branch (git checkout -b feature/AmazingFeature)
  
  * Commit your Changes (git commit -m 'Add some AmazingFeature')
  
  * Push to the Branch (git push origin feature/AmazingFeature)
  
  * Open a Pull Request

(back to top)

License

  Distributed under the MIT License. See LICENSE for more information.


(back to top)

Acknowledgments

OpenWeatherMap API

Google Gemini Pro

OpenCV

Mediapipe

(back to top)

**Key points and things to fill in:**

* **Project Title and Description:**  Clearly state your project's name (Intellihome) and provide a concise, informative description.
* **Logo:**  Replace `images/logo.png` with the actual path to your project's logo. If you don't have a logo yet, you can create one or use a placeholder image.
* **Features:** Highlight the main features of your project.
* **Built With:** Showcase the key technologies used. I've added some badges for visual appeal.
* **Installation:** Provide clear, step-by-step instructions on how to install and set up your project locally, including how to obtain and configure API keys.
* **Usage:** Include examples of how to use your project after it's set up.
* **Roadmap:** Outline future plans and features you intend to implement.
* **Contact:**  Provide your team's names and a link to the GitHub repository. 
* **Acknowledgments:** Give credit to any external resources or libraries you've used.

