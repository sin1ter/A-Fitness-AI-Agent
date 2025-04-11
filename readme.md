# Fitness Advisor AI Agent

## Overview

The **Fitness Advisor AI Agent** is built using `pydantic_ai` and integrates with OpenAI's GPT-3.5-turbo model to create personalized fitness plans, workout schedules, meal plans, and motivational quotes based on user profiles.

This system leverages a `FitnessProfile` and generates a detailed `FitnessReportResult`, including workout and meal plans, as well as motivational quotes to encourage fitness progress.

## Requirements

Before running the code, we have the following dependencies installed:

```bash
pip install pydantic_ai openai python-dotenv
```

### To run this

```bash
docker build -t fastapi-app .
```

```bash
docker run -d -p 8000:80 fastapi-app:latest
```


### AI Agent Setup

#### Fitness Agent

```
fitness_agent = Agent(
    'gpt-3.5-turbo', 
    deps_type=FitnessProfile,
    result_type=FitnessReportResult,
    result_retries=3,
    system_prompt="Create personalized FitnessReportResult base on user's information provided."
    "for motivational quotes call the get_motivation tool and pick the single best one from the list"
)
```
The `fitness_agent` is set up to use the OpenAI GPT-3.5-turbo model, receiving `FitnessProfile` data and returning a `FitnessReportResult`.

#### Motivational Agent

```
motivational_agent = Agent(
    'gpt-3.5-turbo', 
    result_type=list[str],
    system_prompt="Give motivational quotes based on the user's fitness goals and current status."
)
```
This tool interacts with the `motivational_agent` to generate 5 motivational quotes related to fitness.
