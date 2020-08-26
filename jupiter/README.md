# Transtreaming Documentation

Please refer to main github reposity for a complete transtreaming documentation
 - [Github Reposity](https://github.com/zilehuda/transtreaming)
 
# Transtreaming (Translated Subtitles Using AgoraRTC SDK)

This tutorial describes how to run this app that translates voice of a person in a meeting with respect to other persons preferred language.

With this app, you can:

- Join a meeting room
- Select your preffered Language (You will shown subtitles with respect to the language selected)
- Leave the meeting room
- Apply two layouts views
- Hide a remote window

## Prerequisites

- Node.js 6.9.1+


## Quick Start

This section shows you how to prepare, build, and run this application.

- [Create an Account and Obtain an App ID](#create-an-account-and-obtain-an-app-id)
- [Update and Run the Sample Application](#update-and-run-the-sample-application) 


### Create an Account and Obtain an App ID
To build and run the sample application, you must obtain an app ID: 

1. Create a developer account at [agora.io](https://dashboard.agora.io/signin/). Once you finish the sign-up process, you are redirected to the dashboard.
2. Navigate in the dashboard tree on the left to **Projects** > **Project List**.
3. Copy the app ID that you obtained from the dashboard into a text file. You will use this when you launch the app.

### Getting Started
1. Copy the [.env.example](.env.example) and rename it to **.env**
```JavaScript
REACT_APP_EUROPA_BASE_URL=
REACT_APP_AGORA_APP_ID=
```

2. In **.env** set **REACT_APP_AGORA_APP_ID** with your app id.

```JavaScript
REACT_APP_AGORA_APP_ID = 'Your App ID'
```

3. In **.env** set **REACT_APP_EUROPA_BASE_URL** with the europa base url.
```JavaScript
REACT_APP_EUROPA_BASE_URL = 'Your Europa Base url'
```
The code for the back end of the project is located on the following repo  [Transtreaming Back End](https://github.com/zilehuda/transtreaming-europa)

4. Open the terminal and navigate to your project folder.
``` bash
cd path/to/project
```
5. Use `npm` to install the dependencies:

``` bash
# install dependency
npm install
```
6. Build and run the project:

Use `start` for a local build. View the application in your browser with the URL `http://localhost:3000`

```bash
# serve with hot reload at localhost:3000
npm run start
```
Use `build` for a production version with minification.

```bash
# build for production with minification
npm run build
```

## Application Flow
1. After setting up the application as described in the previous step open the application in the desired browser and Enter the room id.

![User Page][user-page]

2. Select your prefered language (You will recieve translated subtitles of the language you choose).
3. Repeat step 1 and 2 on the other attendee browser.
4. Now as both the attendees speak they will see translated text of the other attendee on thier screen.


## Resources
- Find full API documentation in the [Document Center](https://docs.agora.io/en/).


## License
This software is licensed under the MIT License (MIT). [View the license](LICENSE.md).

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[user-page]: user-page.PNG
[room]: room.png
