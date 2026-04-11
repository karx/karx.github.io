---
published: true
title: "Art of Intent"
tags:
  - interface
  - reference
description: "Technical overview and architecture of 'Art of Intent', an AI-powered word puzzle game exploring the boundaries of prompt engineering."
---

Art of Intent is a project that explores prompt engineering through an elegant word puzzle game where users learn to guide an AI
       bot through careful prompt crafting - a perfect metaphor for the "art of intent" in AI interaction.
  1. PROJECT OVERVIEW

       Art of Intent is a sophisticated AI-powered word puzzle game that teaches prompt engineering through
       gameplay. Players guide "Arty the Haiku Bot" to generate haikus that include target words while avoiding
       blacklisted words.

       Key Metadata:
       - Project: art-of-intent
       - Version: 1.1.0-alpha
       - License: MIT
       - Repository: https://github.com/karx/art-of-intent.git
       - Homepage: https://art-of-intent.netlify.app

       ---
       2. OVERALL PROJECT STRUCTURE

       /d/src/art-of-intent/
       ├── index.html                           # Main game interface
       ├── about.html / aboutV2.html           # About pages
       ├── history.html                         # Game history view
       ├── firebase.json                        # Firebase deployment config
       ├── .firebaserc                          # Firebase project config
       ├── firestore.rules                      # Firestore security rules
       ├── firestore.indexes.json               # Firestore index config
       ├── package.json                         # Root dependencies
       ├── package-lock.json                    # Locked dependencies
       │
       ├── functions/                           # Firebase Cloud Functions
       │   ├── index.js                        # Main function implementations
       │   ├── package.json                    # Function dependencies
       │   ├── .env.example                    # Environment template
       │   ├── README.md                       # Function documentation
       │   ├── test-local.js                   # Local testing script
       │   └── node_modules/                   # npm dependencies
       │
       ├── src/
       │   ├── js/
       │   │   ├── firebase-config.js          # Firebase initialization (exports httpsCallable, functions)
       │   │   ├── game.js                     # Main game logic (~2000 lines)
       │   │   ├── firebase-auth.js            # Authentication handlers
       │   │   ├── firebase-db.js              # Database operations
       │   │   ├── firebase-integration.js     # Firebase integration layer
       │   │   ├── analytics.js                # Game analytics tracking
       │   │   ├── prompt-purify.js            # Security/injection prevention
       │   │   ├── share-card-generator.js     # Game result sharing
       │   │   ├── leaderboard-*.js            # Leaderboard functionality
       │   │   ├── theme-*.js                  # Theme management
       │   │   └── other UI/UX utilities
       │   ├── css/
       │   │   ├── styles.css                  # Main styles
       │   │   ├── dos-theme.css               # DOS-style theme
       │   │   └── themes.css                  # Additional themes
       │   └── assets/
       │       ├── og_image.png                # Open Graph image
       │       └── other icons/images
       │
       ├── docs/                                # Documentation directory
       ├── tests/                               # Test files
       ├── .env                                 # Environment variables (actual)
       ├── .env_example                         # Environment template
       ├── .gitignore                           # Git ignore rules
       ├── site.webmanifest                     # PWA manifest
       ├── favicon-*.svg/png                    # Favicon files
       ├── android-chrome-*.svg                 # Android icons
       ├── apple-touch-icon.svg                 # iOS icon
       │
       └── Documentation Files (numerous MD files):
           ├── README.md
           ├── FINAL_DEPLOYMENT_SUMMARY.md
           ├── SERVICES_AND_APIS_GUIDE.md
           ├── DEPLOYMENT_*.md
           ├── SECURITY_*.md
           ├── FIREBASE_FUNCTIONS_*.md
           └── [15+ additional docs]

       ---
       3. DEPLOYMENT STRATEGY: Firebase Full Stack

       Hosting

       - Platform: Firebase Hosting
       - Configuration: firebase.json
         - Public directory: . (root)
       - Rewrites: Single-page app rewrite to /index.html
       - Ignores: node_modules/, tests/, docs/, functions/, *.md files

       Backend Services

       - Cloud Functions v2 (Node.js 20)
         - Runtime: nodejs20
         - Region: us-central1
         - Memory: 256 MiB per function
         - CORS: Enabled
       - Firestore Database (Alpha)
         - Database ID: alpha
         - Rules: Configured in firestore.rules
         - Indexes: Defined in firestore.indexes.json

       11 Google Cloud APIs Enabled

       1. Cloud Functions API - Core serverless compute
       2. Cloud Build API - Builds function containers
       3. Artifact Registry API - Stores container images
       4. Cloud Scheduler API - Schedules daily word generation
       5. Cloud Run API - Executes Cloud Functions v2
       6. Eventarc API - Routes scheduled events
       7. Cloud Pub/Sub API - Message queue for events
       8. Cloud Storage API - Stores source code & artifacts
       9. Firebase Extensions API - Firebase extensions
       10. Cloud Billing API - Tracks costs
       11. Firestore API - Database operations

       Cost: $0/month (all within free tier limits)

       ---
       12. HOW "ARTY" (GEMINI API) IS CALLED

       Architecture Overview

       ┌──────────────┐
       │   Browser    │
       │  (game.js)   │
       └──────┬───────┘
              │ httpsCallable(functions, 'artyGenerateHaiku')
              │ with: userPrompt, systemInstruction, sessionId
              ▼
       ┌─────────────────────────────────┐
       │   Firebase Cloud Function       │
       │   artyGenerateHaiku             │
       │   (functions/index.js:102-209)  │
       └──────┬────────────────────────────┘
              │ GEMINI_API_KEY (server-side secret)
              │ fetch() to Gemini API
              ▼
       ┌──────────────────────────────────┐
       │   Google Gemini API              │
       │ generativelanguage.googleapis.com│
       │ /v1beta/models/gemini-2.0-flash │
       └──────────────────────────────────┘

       Call Flow in game.js

       File: /d/src/art-of-intent/src/js/game.js (lines 598-630)

       async function callArtyAPI(userPrompt) {
           const systemInstruction = generateSystemInstruction();

           try {
               // Get the Cloud Function reference
               const artyGenerateHaiku = httpsCallable(functions, 'artyGenerateHaiku');

               // Call the function with user's prompt
               const result = await artyGenerateHaiku({
                   userPrompt,                    // User's input prompt
                   systemInstruction,             // AI system instructions
                   sessionId: gameState.sessionId  // Session tracking
               });

               // Handle response
               return result.data.data.fullResponse;
           } catch (error) {
               // User-friendly error handling
               throw new Error('Failed to generate haiku...');
           }
       }

       Cloud Function Implementation

       File: /d/src/art-of-intent/functions/index.js (lines 102-209)

       Function: artyGenerateHaiku
       - Type: HTTPS Callable (requires Firebase authentication)
       - Max Instances: 10
       - Timeout: 30 seconds
       - Memory: 256 MiB

       Request Validation:
       - Requires authentication: if (!request.auth)
       - Max prompt length: 500 characters
       - Validates userPrompt and systemInstruction parameters

       API Call:
       const geminiApiUrl = process.env.GEMINI_API_URL ||
           'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent';

       const response = await fetch(geminiApiUrl, {
           method: 'POST',
           headers: {
               'Content-Type': 'application/json',
               'x-goog-api-key': geminiApiKey  // Server-side secret
           },
           body: JSON.stringify({
               system_instruction: { parts: [{text: systemInstruction}] },
               contents: [{ parts: [{text: userPrompt}] }]
           })
       });

       Response Processing:
       - Extracts: responseText, usageMetadata, fullResponse
       - Logs for monitoring: session ID, prompt length, token count
       - Returns formatted response to client

       System Instruction Generation

       File: /d/src/art-of-intent/src/js/game.js (lines 632-692)

       Creates detailed prompt instruction that:
       - Tells ARTY to respond only with haikus (5-7-5 syllables)
       - Lists forbidden (blacklist) words
       - Defines "violation protocol" - respond with specific haiku if forbidden words detected
       - Includes examples of valid and violation responses
       - Ensures consistent behavior across sessions

       Daily Word Generation

       Function: generateDailyWords (Scheduled)
       - Schedule: 0 0 * * * (daily at midnight UTC)
       - Trigger: Cloud Scheduler → Pub/Sub → Eventarc
       - Storage: /firestore/dailyWords/{YYYY-MM-DD}

       Word Selection:
       - Uses deterministic seeded random from date (ensures same words for all users)
       - Selects 3 target words (from 13 categories)
       - Selects 5-7 blacklist words
       - Stores in Firestore with seed for reproducibility

       Word Pools (13 categories × 32 words each):
       - nature, weather, time, seasons, emotions, elements, creatures, plants, cosmos, structures, abstract,
       textures (1152 total words)

       ---
       5. FIRESTORE STRUCTURE & SECURITY

       Collections

       ┌────────────────┬───────────────────────────────────┬───────────────────────┐
       │   Collection   │              Access               │        Purpose        │
       ├────────────────┼───────────────────────────────────┼───────────────────────┤
       │ users/         │ Public read, owner write          │ User profiles & stats │
       ├────────────────┼───────────────────────────────────┼───────────────────────┤
       │ sessions/      │ Public read, owner write          │ Game sessions         │
       ├────────────────┼───────────────────────────────────┼───────────────────────┤
       │ sessionEvents/ │ Auth read, owner write            │ Detailed game logs    │
       ├────────────────┼───────────────────────────────────┼───────────────────────┤
       │ dailyWords/    │ Public read, functions-only write │ Daily word pairs      │
       ├────────────────┼───────────────────────────────────┼───────────────────────┤
       │ leaderboard/   │ Public read, auth write           │ Real-time rankings    │
       ├────────────────┼───────────────────────────────────┼───────────────────────┤
       │ leaderboards/  │ Public read, functions-only write │ Historical data       │
       └────────────────┴───────────────────────────────────┴───────────────────────┘

       Firestore Rules Highlights (firestore.rules)

       - All reads require isAuthenticated() except for public collections
       - Write operations restricted to owners or Cloud Functions service account
       - Aggregation queries allowed for statistics
       - No deletes permitted (data preservation)

       ---
       6. CLIENT-SIDE FIREBASE CONFIGURATION

       File: /d/src/art-of-intent/src/js/firebase-config.js

       Imports:
       - Firebase Auth (anonymous, Google OAuth)
       - Firestore (with offline persistence)
       - Cloud Functions (httpsCallable)
       - Analytics

       Public API Key: AIzaSyCbjBSXYA75T7RWByOk3d10ofoMps145-M (safe - Firebase config is public)

       Database: alpha (non-default Firestore database)

       Features:
       - Offline persistence enabled (IndexedDB)
       - Fallback error handling for multiple tabs
       - Exports modular Firebase functions

       ---
       7. DEPLOYMENT PROCESS

       Deployment Config (firebase.json)

       {
         "functions": {
           "source": "functions",
           "runtime": "nodejs20",
           "codebase": "default"
         },
         "firestore": {
           "rules": "firestore.rules",
           "indexes": "firestore.indexes.json",
           "database": "alpha"
         },
         "hosting": {
           "public": ".",
           "rewrites": [{"source": "**", "destination": "/index.html"}]
         }
       }

       Firebase Project (.firebaserc)

       - Default project: art-of-intent

       Functions Dependencies (functions/package.json)

       - firebase-admin@^13.5.0 - Backend SDK
       - firebase-functions@^6.6.0 - Function framework
       - dotenv@^17.2.3 - Environment config

       Deployment Steps

       firebase deploy --only functions      # Deploy Cloud Functions
       firebase deploy --only firestore      # Deploy Firestore rules
       firebase deploy --only hosting        # Deploy web app
       firebase deploy                       # Deploy everything

       Recent Deployment History (Git commits)

       - 3907a12 - Update wordPool (latest)
       - c7181d4 - Add final deployment summary
       - c4b968a - Fix: Update game.js to use modular Firebase SDK
       - d3bea47 - Successfully deploy Firebase Cloud Functions
       - 4753ca0 - Migrate LLM calls to Firebase Cloud Functions

       Migration Timeline: Functions deployed Nov 3, 2025 (production-ready)

       ---
       8. KEY SECURITY FEATURES

       API Key Security (Major improvement)

       - Before: Gemini API key exposed in client-side code
       - After: Key stored server-side in functions/.env - never exposed to browser

       Authentication

       - All artyGenerateHaiku calls require Firebase authentication
       - Anonymous login allowed (no email required)
       - Google OAuth supported

       Input Validation

       - Max prompt length: 500 characters
       - System instruction validation
       - Type checking on all inputs

       Rate Limiting

       - Cloud Functions auto-scaling (max 10 instances)
       - Gemini API free tier: 15 req/min, 1M tokens/day

       XSS & Prompt Injection Protection

       - prompt-purify.js validates inputs
       - Security signals system
       - Separate test files for security validation

       ---
       9. IMPORTANT FILES SUMMARY

       ┌───────────────────────────┬─────────┬─────────────────────────────────┐
       │         File Path         │  Size   │             Purpose             │
       ├───────────────────────────┼─────────┼─────────────────────────────────┤
       │ src/js/game.js            │ ~83KB   │ Main game logic, AI integration │
       ├───────────────────────────┼─────────┼─────────────────────────────────┤
       │ functions/index.js        │ ~11.7KB │ Cloud Functions implementation  │
       ├───────────────────────────┼─────────┼─────────────────────────────────┤
       │ index.html                │ ~27KB   │ Main UI with schema.org markup  │
       ├───────────────────────────┼─────────┼─────────────────────────────────┤
       │ src/js/firebase-config.js │ ~2.9KB  │ Firebase init & exports         │
       ├───────────────────────────┼─────────┼─────────────────────────────────┤
       │ firestore.rules           │ ~3.9KB  │ Database security rules         │
       ├───────────────────────────┼─────────┼─────────────────────────────────┤
       │ firebase.json             │ ~553B   │ Deployment configuration        │
       ├───────────────────────────┼─────────┼─────────────────────────────────┤
       │ package.json              │ ~1.8KB  │ Project dependencies            │
       ├───────────────────────────┼─────────┼─────────────────────────────────┤
       │ functions/package.json    │ ~780B   │ Function dependencies           │
       └───────────────────────────┴─────────┴─────────────────────────────────┘

       ---
       10. KEY TECHNICAL INSIGHTS

       11. Single-Page Application (SPA): All routes rewrite to /index.html
       12. Modular Firebase SDK: Uses v9+ modular imports (modern approach)
       13. Offline-First: IndexedDB persistence for offline gameplay
       14. Serverless Architecture: No traditional backend server - pure Firebase
       15. Deterministic Daily Challenges: Seeded random ensures same words for all users on a given day
       16. Gemini Integration: Uses gemini-2.0-flash-exp model for fast, creative responses
       17. Custom Database ID: Uses non-default alpha database (allows experimentation)
       18. Comprehensive Logging: Game analytics, security signals, function metrics
       19. Theme System: DOS aesthetic with multiple theme options
       20. Progressive Web App: Manifest file, icons, offline support

       ---
       SUMMARY

       Art of Intent is a fully cloud-native game hosted on Firebase with:
       - Frontend: Static HTML/CSS/JS hosted on Firebase Hosting
       - Backend: Serverless Cloud Functions (Node.js 20)
       - Database: Firestore with custom security rules
       - AI Engine: Google Gemini API via secure Cloud Function proxy
       - Authentication: Firebase Auth (anonymous + OAuth)
       - Deployment: Firebase CLI with git-based version control
       - Cost: $0/month (free tier)
       - Status: Production-ready, deployed to Netlify CDN

       The project teaches prompt engineering through an elegant word puzzle game where users learn to guide an AI
       bot through careful prompt crafting - a perfect metaphor for the "art of intent" in AI interaction.