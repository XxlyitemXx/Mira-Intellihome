

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
* [Gemini](https://aistudio.google.com)
* [OpenCV](https://opencv.org/)
* [Mediapipe](https://chuoling.github.io/mediapipe/)

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

Navigate to the project directory:

2. ```cd Intellihome```

3. Install required packages:
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

<p align="right">(<a href="#readme-top">back to top</a>)</p>

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

<p align="right">(<a href="#readme-top">back to top</a>)</p>

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
<p align="right">(<a href="#readme-top">back to top</a>)</p>

License

  Distributed under the MIT License. See LICENSE for more information.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

Acknowledgments

OpenWeatherMap API

Google Gemini Pro

OpenCV

Mediapipe

<p align="right">(<a href="#readme-top">back to top</a>)</p>


