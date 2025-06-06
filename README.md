## 📱💡 MINDSPACE – GENAI DIGITAL WELLNESS COMPANION (FULL PLAN)

## ✅ FUNCTIONAL OVERVIEW

### 🎯 Core Goals
Empower teens to monitor & understand screen time.

Use GenAI to provide mental wellness advice in a chill, relatable tone.

Offer mindfulness tools to reset stress levels.

Support balance, not banning—it’s a wellness buddy, not a watchdog.

### 🧩 FUNCTIONAL MODULES (Features)

Feature	Description
 - 📊 Digital Habit Tracker	Logs daily screen time, app usage patterns
 - 🤖 AI Wellness Buddy	GenAI-powered chatbot for real-time support
 - 🧘 Mindfulness Toolkit	Music, journaling prompts, creative breathing breaks
 - 🛡️ Content Detox Mode	AI filters out toxic content recommendations
 - 🎓 Teen Talks (AI Ed-Zone)	Quick educational GenAI content: "how tech hooks us", etc.
 - 👪 Parent Dashboard (Optional)	Trend summaries for parents, not micro-tracking

### 🔁 FUNCTIONAL FLOW (STEP BY STEP)
1. Onboarding
      - Teen sets mood baseline & usage goals
      - Chooses tone: chill, fun, serious, emoji-heavy, etc.
      - Can opt-in for mindfulness check-ins or detox mode
2. Daily Use Cycle
     - User Opens App
        - → Dashboard shows screen time, mood, usage streaks.
     - AI Chatbot Check-in
        - → Asks how user is feeling
        - → Suggests a tip, journaling prompt, or 2-min decompression task (via GenAI)
     - Mindfulness Toolkit
        - → Personalized recommendation: e.g., "Wanna vibe with a 1-minute calming breath?"
        - → Launches activity (timer, sound, sketch prompt)
    - Teen Talks Zone
        - → Optional: user taps into a feed of AI-generated learning bites
        - → Could be text, video, or voice-based
    - Logging & Reflection
        - → Mood after mindfulness?
        - → AI logs this + gives encouraging reinforcement.
3. Parent View (Optional)
        - Receives weekly digest: “Your teen has reduced screen spikes by 12% this week."
        - No direct monitoring or spying.

## 🔧 TECHNICAL FLOW (WITH PYTHON COMPONENTS)
Here’s the architecture with Python components at the heart 👇

### 🛠️ TECH STACK
- Layer	Technology
- Frontend (App UI)	React Native
- Backend (API + Logic)	Python (FastAPI or Flask)
- Azure Open AI Services ,AI/GenAI Services	OpenAI GPT API, HuggingFace Transformers
- Azure service
- Database	Firebase / MongoDB / PostgreSQL /Cosmos DB
- Analytics & Logs	SQLite (local) + Firebase Analytics
- Mobile Integration	Screen Time APIs (Android/iOS)
- Authentication	Firebase Auth (with Teen/Parent roles)
- **Currently using only Azure Open AI Services - gpt-4o ,streamlit and python**

## 🧠 PYTHON MODULES (Core Functions)

     
## 🧭 TECHNICAL ARCHITECTURE (FLOW DIAGRAM STYLE)


### 🎯 FUTURE EXPANSION IDEAS
  - Voice-based AI companion
  - “Detox Mode” that auto-hides social apps during peak stress hours
  - AI-generated meditations using GenAI voice synthesis
  - Gamify wellness: “Complete 3 mindfulness missions this week to unlock a theme”


## Sample screens with results for reference
Home
 ![image](https://github.com/user-attachments/assets/64956e4c-47b0-4a82-94d1-dc7bf354d702)
 After choosing hour of spend using mobile
 ![image](https://github.com/user-attachments/assets/866ad42a-47f5-4f1e-9219-0f04c9e778fa)
 Deployed in streamlit
 ![image](https://github.com/user-attachments/assets/c2ac2ade-64eb-41cf-89e2-4f633c54d9b9)
 Home
 ![image](https://github.com/user-attachments/assets/50acd1c1-e414-435b-951c-f7f49ca86653)
 After choosing hour of spend using mobile
 ![image](https://github.com/user-attachments/assets/5be99b24-5ca0-4130-8be2-58c43a3d0023)



 



