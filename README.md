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
