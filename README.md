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

## Scope

### Functional Requirements

#### Simple, Intuitive, and Engaging Interface

-   Users must be able to navigate, and interact with, the site with ease.
-   Ensure Interactivity and Gameplay is simple and intuitive.
-   Ensure users can obtain additional information on how to play, and that the
    instructions are easy to understand.
-   Ensure layout and design is responsive to all media sizes.

#### User Management

-   Allow a user to create an account, confirm their email address, change their
    password, log in, and log out.

#### Premium Content

-   Implement content which is available only to premium users.
-   Create a paywall between free and premium content, preventing free users
    from accessing the premium content.
-   Allow users to upgrade to a premium account through a one-off Stripe payment
    to obtain access to the premium content.
-   Prevent users from upgrading to a premium account more than once.

#### Codex Overview

-   Allow users to see an overview of all possible content in the game via the
    Codex.
-   Allow free users to see what Premium content is available within the Codex.
-   Allow users to filter and sort content within the Codex.
-   Allow Admins to create, update, and delete content from the Codex.

#### Character Creation

-   Allow a user to create a character if one does not already exist in their
    profile.
-   Allow users to have a transparent view of the difference between available
    classes.
-   Allow free users to create a character from the free characters available.
-   Allow premium users to create a character from all available characters.
-   Ensure that when a user creates a character, a random weapon of appropriate
    Tier, Premium Access, Level, and Rarity is created.

#### Profile

-   Allow users to visit their profile.
-   Allow users to see their gameplay statistics from their profile.
-   Allow users to create a character from their profile (if applicable).
-   Allow users to see their current character and weapon from their profile (if
    applicable).
-   Allow users to delete their current character from their profile (if
    applicable).

#### Battle Mechanics

-   Allow users to engage in combat with a random enemy of a relative level and
    Tier.
-   Allow real-time control of the battle through an [Active Time
    Battle](https://en.wikipedia.org/wiki/Turns,_rounds_and_time-keeping_systems_in_games#Active_Time_Battle)
    system.
-   Allow users to attack or retreat on their turn.
-   Allow users to understand the battle mechanics through an intuitive UI and a
    text-based battle log.
-   Prevent free users from fighting enemies higher than Tier 2.

#### Character Progression and Lifecycle

-   Clearly communicate to a user if they have won or lost a battle.
-   Generate random Loot for a user when they win a battle.
-   Allow a user to choose whether to keep their existing weapon or take the new
    loot.
-   Grant a character a relative amount of XP when they win a battle.
-   If a character levels up when they win a battle, their character’s
    statistics are increased.
-   If a character loses a battle, their character is removed from the database
    (akin to [permadeath](https://en.wikipedia.org/wiki/Permadeath)).
-   When a character loses a battle, their score is presented to them.
-   Prevent free users from exceeding Level 2.
-   Prevent free users from obtaining loot higher than Tier 2, or Rarity higher
    than Uncommon.

#### Leaderboard

-   Allow all users to view the Leaderboard.
-   Allow all users to view additional details regarding each individual
    Leaderboard entry.
-   Ensure there are only ever 10 Leaderboard entries.
-   Prevent free users from their score being added to the database.
-   Allow paid users to have their score and stats published on their
    Leaderboard if their score his higher than any of the existing 10 entries.

### Content Requirements

The “content” within this project relates to the entries within the Codex. Each
entry will either be a Character, and Enemy, or a Weapon, and will have a name,
and image, a unique set of stats, and an associated Tier. All game mechanics are
centred around these Codex entries and their associated stats.

#### Artwork

Content artwork will be commissioned, and will be in the style of
[Fantasy](https://en.wikipedia.org/wiki/Fantasy) / [Dungeons and
Dragons](https://en.wikipedia.org/wiki/Dungeons_%26_Dragons).

#### Characters

Characters will be entries within the Codex that only the User can select.

#### Enemies 

Enemies will be entries within the Codex that Characters will fight against
during a Battle.

#### Weapons

Weapons will be entries within the Codex that will be randomly generated for
both Characters and Enemies. A weapon’s stats will be combined with the
associated Character’s/Enemy’s stats.

#### Stats

-   Each entry within the Codex will have 4 stats:
    -   **HP**: Hit Points, which represent health. When a Character or Enemy’s
        total HP is reduced to Zero, they will be defeated.
    -   **Attack:** This will represent the amount of damage one inflicts on
        their opponent’s **HP** in the event of a successful attack.
    -   **Defence:** This value will be used to calculate **Dodge Chance**.
        -   A Character/Enemy’s chance of dodging an attack will be calculated
            through the following formula: **Defence**/**HP** (capped at 75%).
        -   Each time an attack is attempted, the opposition will attempt to
            dodge the attack based on their own Defence and HP.
    -   **Speed:** This value will be used to calculated who attacks first, and
        when they attack.
-   Each entry’s stats will be defined as **Base Stats**, as they are subject to
    modification.
    -   The higher the base stats, the bigger impact stat modification will
        have.

#### Tiers

-   Enemies and Weapons will have an associated Tier.
    -   Tiers represent what Level the Character must be in order for the entry
        to be available within the pool of content.
    -   Entries with a higher Tier will have higher **Base Stats**, which will
        make them substantially more powerful (on a logarithmic scale) based on
        how the stat modification intends to apply.

#### Level

When an enemy or weapon is generated from the Codex, it will be randomly
assigned a level. The level will only ever be less than or equal to the current
Character’s level.

For weapons, the level will affect the range of possible stat modifiers.

For enemies, the level will affect the number of times the stat modifier is
applied to the enemy’s stats.

#### Rarity

When a weapon is generated (either as Loot for the user, or for an enemy during
battle), it’s rarity will be randomly allocated based on the Character’s current
level:

-   Uncommon (Character Level 1+)
-   Common (Character Level 2+)
-   Rare (Character Level 3+)
-   Epic (Character Level 4+)
-   Mythic (Character Level 5+)

An item’s rarity affects how many times a stat modifier is applied to the
weapon’s stats.

## Structure

### Informational Architecture

In order to create a simple interface for the user, each of the project’s core
functions will be isolated into different pages. In an attempt to implement an
intuitive navigation system, a persistent Navigation Bar will be utilised, along
with carefully selected navigational aids on each page in an attempt to pre-empt
the user’s subsequent destination. This will allow a user to navigate the
project with ease, spending minimal time finding the next destination, hopefully
engaging and retaining their attention for longer periods of time.

#### Navbar

The Navbar will be a persistent element that will allows users to navigate to
any logical page (i.e any route the user is permitted to access manually).

<details>
  <summary>Show Details</summary>

>Applicable User Stories:
>-   1b, 2a, 2b, 2e, 3a, 4a, 4b, 4c, 5a, 6a
>
>Applicable Functional Requirements:
>-   Simple, Intuitive, and Engaging Interface
>-   User Management
>-   Premium Content
>-   Codex Overview
>-   Profile
>-   Character Creation
>-   Leaderboard
>
>Navigational Routes:
>-   All logical pages
  
</details>  
  

#### Home 

The home page is the initial landing page, and provides a brief overview of the
project’s concept and the appropriate CTAs.

<details>
  <summary>Show Details</summary>

>Applicable User Stories:
>-   1a, 1b, 1c, 2a, 2b, 2e, 6a, 6b
>
>Applicable Functional Requirements:
>-   Simple, Intuitive, and Engaging Interface
>-   User Management
>-   Codex Overview
>
>Navigational Routes:
>-   Codex (Pre-filtered)
>-   Log In (Logged Out)
>-   Register (Logged Out)
>-   Profile (Logged in)

</details>  
  

#### Account Management

Account Management will allow users to register, create an account, log in, log
out, and reset their password.

<details>
  <summary>Show Details</summary>

>Applicable User Stories:
>-   1b, 2b, 2c
>
>Applicable Functional Requirements:
>-   Simple, Intuitive, and Engaging Interface
>-   User Management
>
>Navigational Routes:
>-   Non-logical account verification
>-   Profile
>-   Login Redirect

</details>  
  

#### Help 

The help page will provide an in-depth breakdown of all content, gameplay
mechanics, and guidance.

<details>
  <summary>Show Details</summary>

>Applicable User Stories:
>-   1b, 1c
>
>Applicable Functional Requirements:
>-   Simple, Intuitive, and Engaging Interface
>
>Navigational Routes:
>-   N/A

</details>  
  

#### Codex

The codex will allow free and paid users to view all content in the game, and
sort/filter the content appropriately. Admins will be able to Create, Edit, and
Delete content from this page.

<details>
  <summary>Show Details</summary>

>Applicable User Stories:
>-   1b, 6a, 6b, 6c, 6d, 6e
>
>Applicable Functional Requirements:
>-   Simple, Intuitive, and Engaging Interface
>-   Codex
>
>Navigational Routes:
>-   N/A 

</details>  
  

#### Profile

The profile will allow users to see an overview of their long-term progress. If
the user has a current active character, this page will allow a user to see
their current character, proceed to a battle, or delete their current character.
If a user does not have an activate character, they can create a new character
from this page.

<details>
  <summary>Show Details</summary>

>Applicable User Stories:
>-   1b, 2e, 4a, 4b, 4c,
>
>Applicable Functional Requirements:
>-   Simple, Intuitive, and Engaging Interface
>-   User Management
>-   Character Creation
>-   Premium Content
>-   Profile
>-   Character Progression and Lifecycle
>
>Navigational Routes:
>-   Create
>-   Battle 

</details>  
  

#### Create

The create page will allow users to create a new Character.

<details>
  <summary>Show Details</summary>

>Applicable User Stories:
>-   1b, 4a, 4b, 4g
>
>Applicable Functional Requirements:
>-   Simple, Intuitive, and Engaging Interface
>-   Premium Content
>-   Character Creation
>-   Profile
>
>Navigational Routes:
>-   Profile

</details>  
  

#### Battle

Battle will consist of a logical route (Battle) and non-logical route
(Post-Battle). Users will manually navigate to the Battle page to engage in the
project’s main gameplay loop. Once a battle is finished, they will be routed to
the Post-Battle page, the content of which will change depending on multiple
factors including whether the user won the battle, whether they are premium
users, or whether their character levelled up.

<details>
  <summary>Show Details</summary>

>Applicable User Stories:
>-   1b, 2e, 3c, 4a, 4c, 4d, 4e, 4f, 4g, 5c, 5d
>
>Applicable Functional Requirements:
>-   Simple, Intuitive, and Engaging Interface
>-   Premium Content
>-   Battle Mechanics
>-   Character Progression and Lifecycle
>-   Leaderboard
>
>Navigational Routes:
>-   Profile
>-   Battle
>-   Create
>-   Premium
>-   Leaderboard

</details>  
  

#### Leaderboard

The Leaderboard will show the top 10 scoring premium users. Contained within
each entry will be detailed information surrounding that particular character’s
run.

<details>
  <summary>Show Details</summary>

>Applicable User Stories:
>-   1b, 5a, 5b, 5c, 5d
>
>Applicable Functional Requirements:
>-   Simple, Intuitive, and Engaging Interface
>-   Premium Content
>-   Leaderboard
>
>Navigational Routes:
>-   N/A

</details>  
  

#### Premium

The Premium page will allow users to upgrade their account from Free to Premium.
This page will display the benefits of upgrading, and will direct the user to an
external Stripe website upon requesting to upgrade. The redirect back from the
external page will change depending on whether the payment was successful or
not.

<details>
  <summary>Show Details</summary>

>Applicable User Stories:
>-   1b, 3b, 3c
>
>Applicable Functional Requirements:
>-   Simple, Intuitive, and Engaging Interface
>-   Premium Content
>-   Character Creation
>-   Profile
>-   Battle Mechanics
>-   Character Progression and Lifecycle
>-   Leaderboard
>
>Navigational Routes:
>-   Non-logical Success/Abort routes.
>-   Profile
>-   Premium
 
</details>  
  
  
### Interaction Design

The following considerations were made when planning the project’s Interaction
Design. Given this project is a game, is intended to entice a user to upgrade to
a premium account, the interaction design aims to keep a user engaged and
excited by the content.

#### Words

-   The main game mechanics focus on stats, whether they are individual stats of
    a new piece of loot, or whether they are the combined stats of a Character
    or their Enemy. Therefore, this information intends to be clearly
    communicated the user via text; all stats must be easily legible, and
    contained to their relative entry in the codex, allowing a user to clearly
    identify their relevance and relationship to the associated entry.
-   All instructional content within the project will be colloquial, yet simple,
    easy to understand, and easy to follow.
-   All text relating to navigation and authentication will be appropriately
    selected and positioned to allow a user to easily understand how to access
    and navigate the project.

#### Visual 

-   Each entry within the Codex will contain an associated image; the name of
    each entry will relate to the image (i.e. the entry “Ape King” will have a
    picture that resembles an Ape).
-   Each image will be appropriately sized and positioned, allowing a user to
    understand their relationship to the Codex entries, yet not overwhelm or
    misuse the available screen space.
-   Interactive elements will have visual effects tied to them in order to
    communicate their interactivity.
-   Visual effects will be applied to weapons, and relevant identifiers
    associated with weapons, in order to emphasise their rarity or the scale of
    their stats.

#### Physical

-   All features will be available to all screen sizes and devices.
-   Visual Effects on interactive elements will be adjusted whether the user is
    interacting with the site via a mouse or via touch.
-   Users will be able to access and engage with this project anywhere with an
    internet connection.

#### Time

-   One of the project’s objectives is to keep a user engaged for as long as
    possible, therefore it is important to respect a user’s time.
-   Animations will be implemented in the Battle section, albeit short and
    informative, and intend not to disrupt the flow of gameplay.
-   Each run will take anywhere between 5 seconds to over 5 minutes; this grants
    a user the choice as to whether they want to play once a day, or multiple
    times in a sitting.
-   A user will be able to log out of website at any point, and log back in on
    any other device and resume where they left off.

#### Behaviour

-   The core gameplay loop will require simple and repetitive user interaction;
    given the above interaction considerations, this will allow users of any
    prior gaming experience to enjoy the project.
-   Due to the random nature of the gameplay loop, users may be frustrated by
    the outcome of some battles, however this is an expected emotion. This is
    strongly counteracted by the excitement of progressing through the game,
    complimented by the combined interaction design discussed above, designed to
    invoke engagement and excitement.

## Skeleton

### Wireframes

**Due to the resolution of the wireframe documents, it is recommended that these PDFs 
are downloaded to be viewed in the browser, rather than using GitHub’s native PDF viewer.**

-   All Wireframes: [Link](.documentation/all-wireframes.pdf)
-   Navbar Wireframe: [Link](.documentation/navbar-wireframes.pdf)
-   Home Wireframe: [Link](.documentation/home-wireframes.pdf)
-   How To Wireframe: [Link](.documentation/how-to-wireframes.pdf)
-   Login/Register Wireframe: [Link](.documentation/login-register-wireframes.pdf)
-   Codex Wireframe: [Link](.documentation/codex-wireframes.pdf)
-   Upgrade Wireframe: [Link](.documentation/upgrade-wireframes.pdf)
-   Create Wireframe: [Link](.documentation/create-wireframes.pdf)
-   Profile Wireframe: [Link](.documentation/profile-wireframes.pdf)
-   Battle Wireframe: [Link](.documentation/battle-wireframes.pdf)
-   Post-Battle Wireframe: [Link](.documentation/post-battle-wireframes.pdf)
-   Leaderboard Wireframe: [Link](.documentation/leaderboard-wireframes.pdf)

### Database

This project utilises a Relational Database via PostgreSQL for storing User
Credentials, User Profiles, Codex entries, Active Characters, Active Enemies,
and Leaderboard entries. The Database went through 3 major iterations throughout
the planning phase of the project. This was as a result of the following:

-   A reduction in scope:
    -   The removal of the “Magic” stat from Codex Entries.
    -   The removal of Leaderboard Messages.
-   Refinement and Refactoring of DB:
    -   The removal of Orders model.
    -   Splitting “User” model into “User” and “Profiles”.
-   Developing a better understand of relational databases.
    -   Splitting “Active Characters” into “Active Characters” and “Active
        Enemies”
    -   Replacing the Leaderboard Foreign Key with required fields.

The first three DB concepts were completed manually, while the final DB Schema
is an actual representation of the deployed database.

**Schema**

<details>
  <summary>Iteration 1</summary>

![First DB Iteration](https://res.cloudinary.com/bak2k3/image/upload/v1628878126/CIRPG/DB_Version_1_kilnnx.jpg)

</details>

<details>
  <summary>Iteration 2</summary>

![Second DB Iteration](https://res.cloudinary.com/bak2k3/image/upload/v1628878126/CIRPG/DB_Version_2_mezz57.jpg)

</details>

<details>
  <summary>Iteration 3</summary>

![Third DB Iteration](https://res.cloudinary.com/bak2k3/image/upload/v1628878126/CIRPG/DB_Version_3_yfrcab.jpg)

</details>

<details>
  <summary>Final DB Schema</summary>

![Final DB Schema](https://res.cloudinary.com/bak2k3/image/upload/v1628878124/CIRPG/DB_Version_Final_rxptcv.jpg)

</details>

## Surface

This project utilises a
pseudo-[monochromatic](https://en.wikipedia.org/wiki/Monochromatic_color) colour
scheme, in order to align with the
[Fantasy](https://en.wikipedia.org/wiki/Fantasy) aesthetic and theme. By
implemented dark tonal colours, this prevents the colour scheme of the webpages
themselves from clashing with the vibrant image content utilised for the Codex
entries.

### Colour Scheme

The primary colour scheme, utilised for the layout, framework, and text of the
website, focuses on a white to black pseudo-monochromatic colour scheme.

![Primary Colour Scheme](https://res.cloudinary.com/bak2k3/image/upload/v1628878125/CIRPG/Primary_Colour_Scheme_id0qx0.jpg)

The variations of white were implemented in various aspects of the website
depending on the context, whether it is representing the Chalk style text, or
whether being used for outlines and glowing effects (see Typography).

The shades of black were used to differentiate between content layers, and
priority within the informational hierarchy of each individual page.

Regardless of which shade of white was used with which shade of black, all
combinations produced ideal contrast ratios.

<details>
  <summary>Contrast Results</summary>

**Chalk on Raisin**  

![Contrast – Chalk on Raisin](https://res.cloudinary.com/bak2k3/image/upload/v1628878126/CIRPG/Contrast_-_Chalk_on_Raisin_bejrgd.jpg)


**Chalk on Rich**  

![Contrast – Chalk on Rich](https://res.cloudinary.com/bak2k3/image/upload/v1628878126/CIRPG/Contrast_-_Chalk_on_Rich_bqfoal.jpg)

</details>

The [secondary colour scheme](https://coolors.co/fff8f0-208b3a-ffd100-e5383b),
implemented to represent Loot Rarity, was based on colour schemes synonymous for
[Color-Coded Loot](https://www.giantbomb.com/color-coded-loot/3015-4702/), and
therefore would be familiar to regular gamers.

![Secondary Colour Scheme](https://res.cloudinary.com/bak2k3/image/upload/v1628878125/CIRPG/Secondary_Colour_Scheme_vhr4bv.jpg)

The images utilised throughout the project for the Codex entries are vibrant and
colourful. Given the primary colour scheme is simple, monochromatic, and dark,
the allows the images to stand out and ultimately compliment the overall
aesthetic.

### Typography

#### Heading Font

The font [Mandhor](https://www.fontspace.com/mandhor-font-f57186) was used for
all headings within the project, intended to represent handwritten chalkboard
text. The use of a handwritten style font was chosen as this would complement
the theme of the project, given it handwritten text is synonymous with [Tabletop
RPGs](https://en.wikipedia.org/wiki/Tabletop_role-playing_game).

![Typography – Mandhor](https://res.cloudinary.com/bak2k3/image/upload/v1628878125/CIRPG/Typography_-_Mandhor_uz2iy3.jpg)

#### Body Font

The font [Titillium Web](https://fonts.google.com/specimen/Titillium+Web) was
chosen as the website’s body text as it is clear, legible, and strong. All text
is easy to read, identify, and given it has similarities with the sans-serif
font, would be easily recognisable by any user.

![Typography – Titillium Web](https://res.cloudinary.com/bak2k3/image/upload/v1628878125/CIRPG/Typography_-_Titillium_Web_v9gcmq.jpg)

### Visual Effects

Given the primary colour scheme is simple, and utilises a very limited colour
range, various visual effects were implemented in order to create an engaging,
interesting, and visually appealing aesthetic.

#### Box Shadows

Box shadows are heavily utilised throughout the project to ‘lift’ content off
the background. Whilst initially influenced by <https://neumorphism.io/>, custom
border shadows were created for the Navbar, Card Elements, Buttons, and the
Leaderboard/Help table.

#### Colour Gradients

In order to add a degree of texture to the colour filled elements, and to
prevent the overall aesthetic being stale, colour gradients were utilised. The
body’s background content utilises a diagonal colour gradient, while the
majority of Card elements use the same gradient reversed. The below example
demonstrates both the cohesion of using inverted gradients, and the
implementation of the aforementioned box shadows.

<details>
  <summary>View Gradient Effect</summary>

![Visual Effects – Gradients](https://res.cloudinary.com/bak2k3/image/upload/v1628878125/CIRPG/Visual_Effects_-_Gradients_nbnfc5.jpg)
</details>


#### Underlined Links

All links and buttons within the project produce an underlined effect when
hovered (desktop) or pressed (mobile). This helps communicate that the elements
are interactive, and produces appropriate user feedback when a user engages with
these elements.

![Visual Effects – Underline](https://res.cloudinary.com/bak2k3/image/upload/v1628878126/CIRPG/Visual_Effects_-_Underline_zf2m2p.jpg)

#### Button Effect 

All buttons are custom designed with a border radius, box shadow, and solid
colour fill. When a user hovers (desktop) or pressed (mobile) buttons, an
animation is produced which removes the button entirely, and evokes the
underlined effect discussed above.

![Visual Effects – Buttons](https://res.cloudinary.com/bak2k3/image/upload/v1628878125/CIRPG/Visual_Effects_-_Buttons_dioubt.jpg)

#### Character Select

When a user is creating a character, visual effects have been implemented in
order to produce responsive feedback to a user’s inputs, and to aid a user’s
understanding of how to interact with this page.

When a user hovers over a character, the container produces a “hover” effect,
lifting the highlighted content off the page.

When a user clicks (Desktop) or presses (Mobile) on a character, a green glow
effect is set to the selected element.


<details>
  <summary>View Character Select Animation</summary>

![Visual Effects – Char Select Selected](https://res.cloudinary.com/bak2k3/image/upload/v1628878124/CIRPG/Features_-_Char_Select_sthqy4.gif)

</details>

#### Rarity Effects

If, when a user wins a battle, they are presented with a new piece of Loot which
is of rarity “Uncommon” or higher, a glow effect will be presented on the new
piece of loot. The colour of the glow changes depending on the Rarity.

<details>
  <summary>View Rarity Glow</summary>

![Visual Effects – Rarity Glow](https://res.cloudinary.com/bak2k3/image/upload/v1628878126/CIRPG/Visual_Effects_-_Rarity_Glow_hkud1q.jpg)
</details>



In the above example, the weapon currently equipped is of “common” rarity, and
therefore does not have a glow effect. The new weapon awarded is of “rare”
rarity, and is therefore accompanied by a green glow effect.

This visual effect enhances the user experience by emphasising the value and
strength of the new Loot pulled. This helps build excitement and present a sense
of being rewarded as they progress through the game.

When in battle, the rarity of the weapon is communicated by the colour of the
weapon’s Tier rating (stars). This allows the communication of information
through the use of colour, without visually overloading the user.

<details>
  <summary>View Battle Rarity</summary>

  
![Visual Effects – Rarity Battle](https://res.cloudinary.com/bak2k3/image/upload/v1628878126/CIRPG/Visual_Effects_-_Rarity_Battle_sp3qf0.jpg)

</details>


The Rarity scope, and their associated colours, are explained within the game’s
How To section:


<details>
  <summary>View Rarity Scale</summary>

  
![Visual Effects – Rarity Scale](https://res.cloudinary.com/bak2k3/image/upload/v1628878126/CIRPG/Visual_Effects_-_Rarity_Scale_tbckf3.jpg)

</details>


##### Pulse Effect

Certain CTAs throughout the project have a pulse effect tied to them. As you
would assume, the CTAs are either important actions, or have the intention of
drawing the user’s attention. As such, specific aspects of the site implement
this pulse effect to help communicate importance. Examples of this include:

The Upgrade Now button on the Premium Page:

![Visual Effects – Pulse – Premium](https://res.cloudinary.com/bak2k3/image/upload/v1628878126/CIRPG/Visual_Effects_-_Pulse_-_Premium_oe9tb0.jpg)

The Attack button during battle when it is the user’s turn to act:

![Visual Effects – Pulse – Attack](https://res.cloudinary.com/bak2k3/image/upload/v1628878125/CIRPG/Visual_Effects_-_Pulse_-_Attack_wzrofb.jpg)

Login and Register buttons on the Home page:

![Visual Effects – Pulse – Home](https://res.cloudinary.com/bak2k3/image/upload/v1628878125/CIRPG/Visual_Effects_-_Pulse_-_Home_ph8kme.jpg)
