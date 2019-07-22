# Copenhacks 2019

<pre>
    __ __  _               _____                           __  
   / //_/ (_)____ ___     / ___/ ____   ___   ___   _____ / /_      IIIIII
  / ,<   / // __ `__ \    \__ \ / __ \ / _ \ / _ \ / ___// __ \    ( ͡° ͜ʖ ͡°)
 / /| | / // / / / / /   ___/ // /_/ //  __//  __// /__ / / / /     ------
/_/ |_|/_//_/ /_/ /_/   /____// .___/ \___/ \___/ \___//_/ /_/     ///  \\\
                             /_/                                  /________\   
</pre>

## Project Description
Cognitive Service Project Copenhacks 2019.

Application for training presentation and explanation of a topic of your choice.
Just lean back and have a nice conversation with dear Kim.


Much swag...


We wanted to solve(education).

Looking at the learning pyramid, we see that teaching others is the most efficient way of mastering a subject.
Combining that with gamification and a personal assistant, we’ve utilised Cognitive Services from the Azure toolbox resources to create an interactive tool to enhance learning and get continuous feedback.

We call our tool Kim, the Learning Panda.

Kim is basically a stupid, but sweet and curious, personal assistant, that will interact with you in order to become smarter and evolve. It will prompt you to teach it a subject of your choice.

Much a like a tamagotchi, just with knowledge as it’s core requirement.

So we utilised the “Language Understanding” from Azure Cognitive Systems.
Doing that:
We build a speech to text system, integrated with a language analyser which finds keywords. The keywords is used to find a teaching curriculum, in this prototype, a Wikipedia page.

Next, analysing the content of the Wikipedia page, Kim will ask intelligent questions within the topic, with a text to speech system, based on the users next input.

The user input and curriculum is weighed against each other with language analysis and a Sequence Matcher to give a correctness response, through either a prompt for elaboration or an appraise.

We tried to integrate the azure web bot for natural language processing, but the resource was unavailabile for azure student accounts.

Our next step in development is to categorise the saved ‘knowledge’, so as you study, it learns how well you know each topic, then prioritizes them for you, and asks you to go through old topics again so you study the things you don't know, without wasting precious time on the things you already do. Basically like Anki Flashcards.
