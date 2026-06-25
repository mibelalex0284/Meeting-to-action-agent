# MeetIQ Problem Description

## Overview
Describe the core problem or requirements that the system aims to solve.

## Use Cases
Detail specific scenarios or user flows.

## Core Challenges
Identify key technical or business challenges to address.
# Problem Statement: Meeting-to-Action AI Agent

## Background

In modern organizations, meetings generate important discussions, decisions, tasks, and deadlines. However, participants often spend significant time manually taking notes, preparing summaries, assigning action items, and tracking follow-ups. This process is inefficient and can lead to missed responsibilities, forgotten decisions, and poor accountability.

An intelligent system is needed to automatically transform meeting conversations into structured, actionable outcomes.

---

## Challenge

Design and develop an AI-powered Meeting-to-Action Agent that can analyze meeting recordings or transcripts and automatically generate summaries, identify decisions, extract action items, assign responsibilities, and track deadlines.

The system should help teams reduce manual effort, improve productivity, and ensure that important information from meetings is captured accurately.

---

## Objectives

Build a solution capable of:

1. Processing meeting audio, video, or text transcripts.
2. Generating concise and accurate meeting summaries.
3. Identifying key discussion points and decisions.
4. Extracting action items from conversations.
5. Detecting task owners and assignees.
6. Recognizing deadlines, dates, and priorities.
7. Producing structured meeting reports.
8. Allowing users to search and query meeting content using natural language.

---

## Functional Requirements

### 1. Meeting Ingestion

* Upload audio recordings.
* Upload video recordings.
* Upload text transcripts.
* Support multiple meeting formats.

### 2. Speech-to-Text Conversion

If audio/video is uploaded:

* Convert speech into text.
* Identify speakers when possible.

### 3. Meeting Summarization

Generate:

* Executive summary
* Discussion highlights
* Key outcomes
* Important observations

### 4. Decision Extraction

Identify:

* Approved decisions
* Rejected proposals
* Pending decisions

Example:

**Transcript**

> The team agreed to launch the mobile application on August 15.

**Output**

> Decision: Launch mobile application on August 15.

### 5. Action Item Extraction

Example:

**Transcript**

> John will complete the quarterly report by Friday.
>
> Sarah should contact the client regarding pricing updates.
>
> Mike will schedule the product demonstration next week.

**Expected Output**

| Task                                     | Owner | Deadline      |
| ---------------------------------------- | ----- | ------------- |
| Complete quarterly report                | John  | Friday        |
| Contact client regarding pricing updates | Sarah | Not Specified |
| Schedule product demonstration           | Mike  | Next Week     |

### 6. Deadline Detection

Identify:

* Explicit dates
* Relative dates
* Time references

Examples:

* Tomorrow
* Next Week
* August 15
* End of Month

### 7. Priority Classification

Classify tasks into:

* High Priority
* Medium Priority
* Low Priority

### 8. Meeting Report Generation

Generate a report containing:

* Meeting summary
* Key decisions
* Action items
* Assigned owners
* Deadlines
* Risks
* Next steps

---

## Bonus Features

### AI Meeting Assistant

Users can ask questions such as:

* What decisions were made?
* What tasks were assigned to Sarah?
* What is due this week?
* What was discussed about the budget?

### Calendar Integration

Automatically create calendar events from extracted deadlines.

### Email Generation

Generate follow-up emails containing:

* Summary
* Decisions
* Assigned tasks
* Due dates

### Progress Tracking

Track completion status of action items.

### Multi-Language Support

Support meetings conducted in different languages.

---

## Technical Requirements

Suggested Components:

* Speech Recognition Model
* Large Language Model (LLM)
* Named Entity Recognition (NER)
* Retrieval-Augmented Generation (RAG)
* Vector Database
* Task Management Backend

---

## Evaluation Criteria

| Criteria                        | Weight |
| ------------------------------- | ------ |
| Action Item Extraction Accuracy | 30%    |
| Summary Quality                 | 20%    |
| Decision Detection Accuracy     | 15%    |
| User Experience                 | 15%    |
| Innovation                      | 10%    |
| Scalability & Architecture      | 10%    |

---

## Deliverables

1. Working application.
2. Source code repository.
3. Architecture diagram.
4. Demo video.
5. Technical documentation.
6. Presentation deck.

---

## Expected Outcome

The final system should automatically convert unstructured meeting conversations into clear, organized, and actionable outputs, enabling teams to spend less time on administrative work and more time executing decisions.
