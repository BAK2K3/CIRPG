![CIRPG Light Logo](https://res.cloudinary.com/bak2k3/image/upload/v1629570329/CIRPG/CIRPG-Logo_tcbytz.jpg)

# **CIRPG**: Code Institute Role-Playing Game

This project is a Full Stack online Role-Playing Game. Users can sign up and
play for free, or upgrade to a premium account to access premium content.

View the deployed site on [Heroku](https://cirpg.herokuapp.com/).

# Table of contents

> 1.  [Overview](#overview)
> 2.  [Terminology](#terminology)
> 3.  [UX](#ux)
>     1.  [Strategy](#strategy)
>     2.  [Scope](#scope)
>     3.  [Structure](#structure)
>     4.  [Skeleton](#skeleton)
>     5.  [Surface](#surface)
> 4.  [Features](#features)
>     1.  [Existing Features](#existing-features)
>     2.  [Future Feature Considerations](#future-feature-considerations)
> 5.  [Technologies Used](#technologies-used)
> 6.  [Testing](#testing)
> 7.  [Deployment](#deployment)
> 8.  [Credits](#credits)
>     1.  [Content](#content)
>     2.  [Media](#media)
>     3.  [Code](#code)
> 9.  [Acknowledgements](#acknowledgements)
> 10.  [Disclaimer](#disclaimer)


# Overview

>   **CIRPG**: siː aɪ ɑː piː ʤiː | Noun  
>   Acronym: Code Institute Role Playing Game.  
>   A Full Stack Role-Playing Game, filled with loot fuelled endorphins, stunning hand drawn
>   graphics, and a Leaderboard to lose friends over.  
>   *“You should have seen the Mythic item I pulled on* **CIRPG** *last night!”*

**CIRPG** is browser-based Full Stack Role-Playing Game, which allows users to
create a character, embark on an endless adventure, and aim for a place on the
Leaderboard. As users progress through the game, they earn experience, level up,
and find new weapons to equip. Whilst the mechanics behind the gameplay are
complex, the gameplay itself is simple, fun, and intuitive.

The project was developed using **Python** (Django), **HTML**, **CSS**,
**JavaScript**, and utilises an SQL database via **PostreSQL**.

---

# Terminology

<details>
  <summary>View Terminology</summary>
 Throughout this documentation, certain terms will be used which either may not
be familiar to some, or may appear very similar and indistinguishable from one
another without any prior explanation. In order to avoid any confusion and for
the sake of clarity, I have defined these in relative terms to the project
below:

-   [**Loot**](https://en.wikipedia.org/wiki/Loot_(video_games)): A term
    used to describe weapons that are generated after a successful battle.

-   **Run**: A term used to describe user’s playthrough of the game, from
    starting a new character to losing that character.

-   **User**: An individual playing the game.

-   **Profile**: A user’s central hub, containing run statistics, their current
    character/loot (if applicable), and their corresponding stats.

-   **Character**: The playable entity chosen by a user at the beginning of a
    run, displayed in a user’s profile.

-   **Stats**: A character/enemy/weapon’s attributes (HP, Attack, Defence,
    Speed).

-   **XP**: Experience Points. Represents progression between Character Levels.

-   **Tier**: Weapons and Enemies are Tiered, which means they will only become
    available within the possible pool of content when a user reaches or exceeds
    that Tier.

-   [**Codex**](https://en.wikipedia.org/wiki/Codex_(Warhammer_40,000)): This
    term is used to refer to a library-like list of all content within the game.

-   [**Rarity**](https://en.wikipedia.org/wiki/Loot_(video_games)): This term is
    used to describe how ‘rare’ a weapon is. The higher the Rarity, the higher
    the item’s stats will be.
</details>

---

# UX

## Strategy

### Stakeholder Interview  

What would your ideal browser-based RPG look like?

*“I want a game that I can play in shorts bursts.”*

*“I want a game that I can stop playing and come back to later.”*

*“I want a game where I can compete with my friends.”*

*“I want a game where each play through feels unique.”*

*“I want a game where I can try it before I pay for it.”*

### User Stories  

| User Story ID                      | As A/An        | I want to be able to                                                                | So that I can                                                                                         |
|------------------------------------|----------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Viewing and Navigation**         |                |                                                                                     |                                                                                                       |
| 1a                                 | Site User      | Understand the purpose of the site immediately                                      | Decide whether I want to engage with it.                                                              |
| 1b                                 | Site User      | Navigate and interact with the site with ease on all viewports                      | Play the game on any device.                                                                          |
| 1c                                 | Site User      | Find out information about the game                                                 | Understand how to play.                                                                               |
| **Registration and User Accounts** |                |                                                                                     |                                                                                                       |
| 2a                                 | Site User      | Register for an account                                                             | Have a profile.                                                                                       |
| 2b                                 | Site User      | Log In and logout                                                                   | Access my profile and play the game.                                                                  |
| 2c                                 | Site User      | Recover my password                                                                 | Recover access to my account.                                                                         |
| 2e                                 | Free/Paid User | Access my profile                                                                   | See my statistics and status.                                                                         |
| **Premium**                        |                |                                                                                     |                                                                                                       |
| 3a                                 | Free User      | Access the upgrade offer from any page                                              | Choose to upgrade easily from any location on the site.                                               |
| 3b                                 | Free User      | Pay to upgrade to the full version                                                  | Have full access to premium features.                                                                 |
| 3c                                 | Paid User      | Navigate the site without upgrade offers                                            | Avoid paying for the product twice.                                                                   |
| **Game**                           |                |                                                                                     |                                                                                                       |
| 4a                                 | Free User      | Have basic access to the game                                                       | Decide whether I want to pay for the full game.                                                       |
| 4b                                 | Free/Paid User | Create a new character                                                              | Start playing the game.                                                                               |
| 4c                                 | Free/Paid User | Enter and engage in a battle                                                        | Enjoy the basic gameplay loop of the game.                                                            |
| 4d                                 | Free/Paid User | Level up my character                                                               | Make progress in the game.                                                                            |
| 4e                                 | Free/Paid User | Be presented with a choice of a new weapon after each win                           | Customise my character.                                                                               |
| 4f                                 | Free/Paid User | Leave a battle halfway through and return at a later time                           | Stop playing the game at any point without being penalised.                                           |
| 4g                                 | Paid User      | Have access to higher levels, additional characters, and additional weapons/enemies | Enjoy the benefits of premium content.                                                                |
| **Leaderboard**                    |                |                                                                                     |                                                                                                       |
| 5a                                 | Site User      | View the Leaderboard                                                                | See the High Scores of paid players.                                                                  |
| 5b                                 | Site User      | View individual Leaderboard entries                                                 | View the breakdown of a player's score.                                                               |
| 5c                                 | Paid User      | Add my score to the Leaderboard                                                     | Compete with other paid players.                                                                      |
| 5d                                 | Paid User      | See my score at the end of a game.                                                  | Find out where my position is on the Leaderboard, or see how close I was to reaching the Leaderboard. |
| **Codex**                          |                |                                                                                     |                                                                                                       |
| 6a                                 | Site User      | View the Codex                                                                      | See all available content in the game.                                                                |
| 6b                                 | Site User      | Sort and Filter the Codex                                                           | Find specific entries in the codex, and find out what content is available as a premium user.         |
| 6c                                 | Admin          | Add entries to the Codex                                                            | Add content to the game.                                                                              |
| 6d                                 | Admin          | Update entries to the Codex                                                         | Update content in the game.                                                                           |
| 6e                                 | Admin          | Delete entries in the Codex                                                         | Remove content to the game.                                                                           |

### Project Strategy Summary

**Ideal User:** An individual who likes Role-Playing Games, and wants a game
that is easy to play, accessible, and can be plaid in short stints.

**Project Goal:** Create a game that is intuitive, addictive, competitive, yet
rewarding and easy to play.

**User Needs:**

-   To be able to navigate the site with ease.

-   To be able to register, log in and log out.

-   To be able to try the game without paying for it.

-   To be able to pay for premium access for content not available to free
    users.

-   To be able to play the game easily.

-   To be able to compete with other players.

**Project Objectives:**

-   To create a game that is easy to play, addictive, and rewarding.

-   To paywall content between free/premium users.

-   To incentivise users to upgrade to premium.

-   To add a degree of competition to encourage users to continue playing.

-   To create a game where every run is unique.

-   To allow the user to navigate and control the application with ease on all
    platforms and devices.
