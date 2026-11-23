# CommunityConnect: AI-Powered Community Resource Navigator

## About the Project

I created CommunityConnect because I wanted to build something that could make finding community resources a little easier. There are many organizations that offer assistance with things like food, housing, and employment, but figuring out where to start or which resources are available can sometimes be overwhelming.

CommunityConnect is a website I built using Python, Streamlit, and Claude AI. Users can type in what they need help with, and the application searches through a list of community resources to find relevant options. Claude then explains those resources in simple terms and provides links to the organizations' official websites.

Right now, the project focuses on resources available in Virginia. It's still a work in progress, but my goal is to keep improving it and explore how AI can help make useful information more accessible.

## Why I Built It

With my background in psychology and data analytics, I've become interested in how technology can be used to solve problems that affect people's everyday lives. I wanted to work on a project that would challenge me technically while also having a meaningful purpose. Instead of building something that only demonstrates programming skills, I wanted to create a tool that could potentially be useful to people or organizations trying to navigate community assistance.

I also wanted to gain more hands-on experience working with AI, particularly learning how to integrate Claude into an application rather than simply using it as a chatbot.

## How It Works

CommunityConnect is designed to be simple and straightforward.

1. A user types a question explaining what they need help with.
2. The application searches for keywords related to food, housing, or employment.
3. It finds matching organizations in the resource directory.
4. Claude explains which resources might be helpful based on the information available.
5. Users can click links to visit the organizations' official websites.

For example, someone could type, "I lost my job and need help finding food."

CommunityConnect would recognize that the person may need both employment and food assistance, show matching resources, and provide a short explanation of how those organizations could help.

## Tools and Technologies

I used several tools to build and publish the application:

- **Python:** Wrote the code that processes questions and matches users with resources.
- **pandas:** Organized and managed the resource directory.
- **Streamlit:** Turned my Python code into an interactive website.
- **Claude API:** Added AI-generated explanations to make resource information easier to understand.
- **GitHub:** Stored and managed my project files.
- **Streamlit Community Cloud:** Published the application online.

This was also an opportunity for me to become more comfortable connecting different technologies and seeing how they work together.

## Community Resources Included

CommunityConnect currently includes three Virginia-based resources:

- **Virginia CommonHelp:** Information about applying for benefits, including food assistance.
- **211 Virginia:** Helps connect people with community services and assistance referrals, including housing-related resources.
- **Virginia Works:** Provides information about employment services and workforce development opportunities.

Each resource includes a link to its official website so users can learn more and verify information directly.

As I continue developing CommunityConnect, I hope to expand the resource directory to include more organizations and types of assistance.

## Testing the Application

One thing I learned while building CommunityConnect is that getting an application to run is only part of the process. I also needed to make sure it was responding appropriately. I tested the application with different questions to see whether it could identify the correct resources and avoid giving misleading information.

| Test | What I Wanted to Check | Result |
|---|---|---|
| Food and employment assistance | Could the application recognize two different needs in one question? | Passed |
| Request for a phone number | Would Claude avoid making up contact information that wasn't provided? | Passed |
| Transportation assistance | Would the application recognize when it didn't have a relevant resource? | Passed |
| Website links | Could users open the official resource websites? | Passed |

These were initial tests, so there's still more testing I want to do as I explore more for the project.

## Challenges I Ran Into

Building CommunityConnect wasn't plain and simple, I ran into a few problems along the way.

### Connecting to Claude

One of my first challenges was getting the Claude API to work with my Python code. I kept receiving an authentication error even though my API key appeared to be saved correctly. I went through the configuration, checked how the key was being accessed, and eventually created a replacement API key that worked. This helped me better understand how APIs connect to Python applications and how important it is to troubleshoot each part of the process.

### Getting the Website Online

After creating the first version of CommunityConnect, I tried running the Streamlit application through Google Colab. Although the application was running, the website wouldn't display correctly in my browser. After trying several ways to access it, I decided to move the project to GitHub and publish it using Streamlit Community Cloud. That ended up working and gave me a website I could access and share.

### Making Claude's Responses More Reliable

Another thing I wanted to focus on was making sure Claude didn't provide information that wasn't supported by the resource directory. I added instructions telling Claude to use only the organizations included in the application and avoid inventing phone numbers, addresses, or eligibility requirements. I also tested what happened when someone asked about a service that wasn't included in the directory. These experiences helped me see why testing and reviewing AI-generated information is just as important as getting the AI to produce a response.

## Responsible AI Use

Because CommunityConnect provides information about community assistance, I wanted to be thoughtful about how AI was being used.

I included a few safeguards:

- Claude is instructed to recommend only organizations listed in the resource directory.
- The application tells users that it's an educational prototype.
- Users are directed to official websites to confirm program details.
- API credentials are stored privately rather than included in the public code.
- The AI feature is protected by a demo password.

I also recognize that AI can make mistakes, even when instructions are in place. CommunityConnect is meant to help people find information, not replace official guidance or professional support.

## What I Still Want to Improve

Although CommunityConnect is working, there are several things I'd like to improve.

One limitation is that the application currently relies on keyword matching. This means it recognizes certain words, but it may not understand every way someone describes their situation. The resource directory is also small, and the application doesn't check whether programs currently have openings or whether someone meets their eligibility requirements.

As I continue working on the project, I'd like to:

1. Add more verified community resources across Virginia.
2. Improve how the application understands different types of questions.
3. Test more scenarios to identify errors and areas for improvement.
4. Make the website easier to navigate and more accessible.
5. Get feedback from people who work with community resources.
6. Create clearer instructions for maintaining and updating the application.

## What I Learned

CommunityConnect gave me the opportunity to take something from an idea to a working website.

I had previous experience programming in Python and working with data, but this project pushed me to use those skills differently. I learned more about connecting to an AI API, building a web application, troubleshooting technical issues, and testing whether a tool actually behaves the way I intended.

One of my biggest takeaways was that building an AI application isn't just about getting the technology to work. It's also about understanding the problem you're trying to solve, thinking about the people who might use the tool, and recognizing where the technology has limitations.

I'm proud of the progress I've made so far, and I'm looking forward to continuing to develop CommunityConnect as I learn more about AI and its potential applications in community-serving organizations.

## Project Status

**Working prototype — ongoing development**

CommunityConnect is an educational project and is not affiliated with the organizations listed. Information about assistance programs should always be verified through their official websites.
