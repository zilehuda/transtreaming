

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="documentation/logo.png" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">Transtreaming</h3>

  <p align="center">
    <a href="https://transtreaming-jupiter.herokuapp.com">View Demo</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
 * [Application Architecture](#application-architecture)
	 * [Jupiter](#jupiter)
	 * [Europa](#europa)
 * [Project Naming Convention](#project-naming-convention)
 * [Getting Started](#getting-started)
 * [TODO](#TODO)
 * [Acknowledgements](#acknowledgements)
 * [Contact](#contact)
 * [License](#license)
 
<!-- ABOUT THE PROJECT -->
## About The Project

![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)

Treamstreaming is a video calling application which is created for [**RTE2020 Hackaton**](https://rte.devpost.com/) by **Agora.io**. It helps two different people from different regions to communicate easily without any difficulty. It transcribe and translate the partner voice in a realtime. And agora give the power on realtime communication.

<!-- APPLICATION ARCHITECTURE -->
## Application Architecture
Application is divided into three major components.
  - Jupiter
  - Europa
  - Agora

[![Tramstreaming Architecture Diagram][architecture-diagram]](https://transtreaming-jupyter.herokuapp.com)
  
### Jupiter
Jupiter is the front end part of this application, it is created on reactjs. Which communicate directly with **Agora** for a realtime video calling feature. It also transcribe the data and send it back to Europa through socket connection.
- [Github Repository](https://github.com/zilehuda/transtreaming-jupiter)

### Europa
Europa is the back end of this application, it is created on Flask. It translate the text send emit the data to the jupiter.
- [Github Repository](https://github.com/zilehuda/transtreaming-europa)

<!-- APPLICATION ARCHITECTURE -->
## Project Naming Convention
Project naming convention is based on the planet **Jupiter** echo system. We named our main application as **Jupiter** the front part of the transtreaming. And **Europa** is the moon of **Jupiter** which is the backend part of the transtreaming.

<!-- Getting Started -->
## Getting Started

### Jupiter
To setup the ***Jupiter*** (frontend of transtreaming), please refer to Transtreaming Jupiter.
- [GitHub Repository](https://github.com/zilehuda/transtreaming-jupiter)

### Europa
To setup the ***Europa*** (backend of transtreaming), please refer toTranstreaming Europa.
- [Github Repository](https://github.com/zilehuda/transtreaming-europa)

<!-- TODO -->
## TODO

### Jupiter
  - Resolve the issue of reapting text due to the partner voice.
  - Resolve the issue first time permission allow.
  - Re-architect the code for better component communication.
  
### Europa
  - Use SqLite or a database for a user management.

<!-- Acknowledgements -->
## Acknowledgements

### Jupiter
* WebRTC powerd by [Agora](https://www.agora.io/en)
* [Agora React Template](https://github.com/AgoraIO-Community/OpenAgoraWeb-React)
* [React-Speech-Recognization](https://www.npmjs.com/package/react-speech-recognition)
* Socket.io

### Europa
*  [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Flask-SocketIO](https://flask-socketio.readthedocs.io/en/latest/)
* [Googletrans](https://py-googletrans.readthedocs.io/en/latest/)
* [Gunicorn](https://gunicorn.org/)

<!-- CONTACT -->
## Contact

Zilehuda - [LinkedIn/zilehuda](https://www.linkedin.com/in/zilehuda/) - zilehuda.tariq@gmail.com

Taimour - [LinkedIn/Taimour](https://www.linkedin.com/in/muhammadtaimour/) - muhammad.taimour95@gmail.com

Project Link: [https://transtreaming-jupiter.herokuapp.com](https://transtreaming-jupyter.herokuapp.com)


## License
This software is licensed under the MIT License (MIT). [View the license](LICENSE.md).


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[architecture-diagram]: documentation/architecture-diagram.png
