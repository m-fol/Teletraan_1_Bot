# Teletraan 1 Bot

**Teletraan 1 Bot** is an educational chatbot developed in Python, designed to help users, especially students, learn about our solar system. It provides information about planets, distances between them, and other fascinating space facts, leveraging Python's `re` library for pattern recognition. The chatbot simulates a conversational experience while educating users on various aspects of space.

## Table of Contents
- [Background](#background)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Design and Implementation](#design-and-implementation)
- [Sample Interactions](#sample-interactions)
- [Future Improvements](#future-improvements)
- [License](#license)

## Background

### Origin of Teletraan 1
Teletraan 1 is a fictional supercomputer from the Transformers universe, originally featured in the Transformers comic books and animated series. It serves as the central intelligence hub for the Autobots, a group of sentient robots from the planet Cybertron. Teletraan 1 is responsible for monitoring global events, providing critical data, and controlling various systems within the Autobots' base, known as the Ark. This supercomputer is integral to the Autobots' operations, offering strategic guidance and storing vast amounts of knowledge about the universe.

## Features
- **Planet Information**: Get details about planets including their distance from the Sun, average temperature, and other interesting facts.
- **Dynamic Calculations**: Compute the distance between two planets or from the Sun.
- **Space Facts**: Provides random, interesting facts about space.
- **ELIZA Effect**: Simulates a realistic conversation to make the interaction feel more natural.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/teletraan_space_bot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd teletraan_space_bot
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To start interacting with Teletraan Space Bot:
```bash
python Teletraan_Space_Bot.py
```
Once launched, you can ask questions about planets, distances, temperatures, or simply request a random space fact. To exit the chatbot, type `bye` or `goodbye`.

## Design and Implementation
### Scope
Teletraan Space Bot is aimed at educating users about the solar system. It is primarily designed for students, but can be used by anyone interested in space.

### Code Structure
- **Patterns and Responses**: The chatbot uses regex patterns to match user input with predefined responses. 
- **Data Structures**: Key information about planets and space facts are stored in dictionaries and lists, making data retrieval efficient.
- **Main Function**: The core logic includes handling user input, matching patterns, and returning the appropriate response.

### Key Functions
- `get_random_space_fact()`: Returns a random fact about space.
- `calculate_distance(planet1, planet2)`: Calculates the distance between two planets.
- `chatbot(input_text)`: The main function that processes user input and provides responses.

## Sample Interactions
Here are a few examples of how users can interact with Teletraan Space Bot:

- **Greeting**:
  ```
  User: Hello
  Teletraan Space Bot: Hello! What can I help you with today?
  ```

- **Planet Information**:
  ```
  User: What is Mars?
  Teletraan Space Bot: Mars is the fourth planet from the Sun, often called the "Red Planet" due to its reddish appearance.
  ```

- **Distance Calculation**:
  ```
  User: Find the distance between Earth and Mars
  Teletraan Space Bot: The distance between Earth and Mars is 78 million kilometers.
  ```

- **Random Space Fact**:
  ```
  User: Tell me a space fact
  Teletraan Space Bot: Sure! Did you know that Jupiter has the shortest day of all the planets?
  ```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
