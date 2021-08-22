# CIRPG - Testing Documentation

The Main README documentation can be found under [README.md](README.md)

# Table of contents

> 1.  [User Story and Feature Testing](#user-story-and-feature-testing)
> 2.  [Automated View Testing](#automated-view-testing)
> 3.  [Browser Testing](#browser-testing)
> 4.  [Code Validation](#code-validation)
> 5.  [Significant Bugs](#significant-bugs)

# User Story and Feature Testing

The User Story testing was completed manually; each user story had an acceptance
criteria defined, and a summary is provided as to how the acceptance criteria
was met, and the outcome of each test. This section also encapsulates the manual
testing of the features associated with the User Story Testing.

## Viewing and Navigation

## 

**User Story:** 1a – As a Site User, I want to be able to understand the purpose
of the site immediately, so that I can decide whether I want to engage with it.

**Acceptance Criteria:** A site user must be able to identify the website's name
and understand its purpose on first visit.

**Summary:**

-   When a user first visits the website, they are presented with the name of
    the website.
-   The name of the website is contained in a **Navbar** which is persistent
    across each webpage, and is positioned centrally at all times.
-   When a user first visits the website, they are presented with a clear
    overview which contains:
    -   Three **feature callouts**, which relate to the different aspect of the
        games content. These callouts contain links to the Codex, pre-filtered
        to the type of content interacted with.
    -   A **call-to-action**, which explains the concept of the project, and the
        initial pricing point for the project.
    -   If a user is not logged in, they are prompted to **register** or **sign
        in.**
    -   If a user is logged in, they are prompted to access their **profile**.
-   It is therefore clear, from first visit, the name of the website, what its
    purpose is, and how to engage with it.

**Outcome: Pass**

**User Story:** 1b – As a Site User, I want to be able to navigate and interact
with the site with ease on all viewports, so that I can play the game on any
device.

**Acceptance Criteria:** A site user should be able to benefit from all features
on the website, regardless of viewport.

**Summary:**

-   As the project utilises **Bootstrap**, most of the structure natively adapts
    to a user’s viewport, allowing native compatibility on any screen size; all
    aspects of the site have been designed to be responsive, allowing the
    appropriate font sizing and spacing on all viewports.
-   All **features** have been specifically designed to adapt to the user’s
    viewport, with the structure and layout changing when appropriate.
-   All **interactive elements** work with touch screen devices, and are large
    enough to target using touch.
-   All **text** is legible on all screen sizes.
-   All **forms** respond appropriately to on-screen keyboards.
-   As such, all website functionality works innately on all screen devices,
    regardless of viewport.

**Outcome: Pass**

**User Story:** 1c – As a Site User, I want to be able to find out information
about the game, so that I can understand how to play.

**Acceptance Criteria:** A site user must be able to navigate to and utilise the
How To section from any location within the project.

**Summary:**

-   On larger viewports, an icon is available in the top right corner **(?)**.
-   On smaller viewports, an additional entry is added to the collapsible navbar
    called “**How To**”.
-   As this is part of the persistent navbar, this is accessible from all pages.
-   The content on this page is legible, and can be scrolled where applicable.
-   Each **How-To** section is contained within an accordion, each element of
    which can be expanded and collapsed individually.
-   The **How-To** section contains information about every aspect of the game,
    from high level to low level concepts.
-   As such, users can access additional information regarding the game,
    including instructions, from any location within the site.

**Outcome: Pass**

## Registration and User Accounts

## 

**User Story:** 2a – As a Site User, I want to be able to Register for an
account, so that I can have a profile.

**Acceptance Criteria:** A site user must be able to successful register for an
account.

**Summary:**

-   Users can access the **Registration** page from any location.
-   Users who are not logged in are presented with the **Register** button on
    the navbar, and a registration **CTA** on the landing page.
-   Users who try and access content that requires logged in access are
    redirected to the login page, which contains a link for registering.
-   The registration form on the registration page contains validation, and
    cannot be submitted without fully completing the form.
-   Once a user registers, they are sent a validation email which they are
    required to interact with, confirming their email address.
-   Once a user confirms their email address, a profile is set up for their user
    account.
-   A user cannot access their account until they have validated their email.

**Outcome: Pass**

**User Story:** 2b – As a Site User, I want to be able to log In and log out, so
that I can access my profile and play the game.

**Acceptance Criteria:** A site user who has validated their account must be
about to log in and log out of the site.

**Summary:**

-   Users who are not logged in are presented with the **Log In** link within
    the Navbar (both desktop and mobile), and can therefore **Log In** from any
    location on the project.
-   Users who are not logged in are presented with a **Log In** link on the home
    page.
-   Features of the project which require logged in access redirect the user to
    the **Log In** page, and subsequently navigates them to their initially
    requested location.
-   The **Log In** form validates all user input, and provides the appropriate
    feedback when invalid information has been provided.
-   A successful log in attempt redirects the user to the **home** page unless
    the user was redirected to the **Log In** page from another route.
-   Logged in users are presented with **Log Out** within the Navbar.
-   Logged in users who interact with the **Log Out** link are taken to a
    confirmation page, which allows a user to confirm they would like to log
    out.
    -   By navigating away from this page manually, users remain logged in.
    -   By confirming they would like to log out, users are successfully logged
        out.
    -   Once logged out, all prior access is revoked, and requires logging in
        again.

**Outcome: Pass**

**User Story:** 2c – As a Site User, I want to be able to recover my password,
so that I can recover access to my account.

**Acceptance Criteria:** A site user should be able to reset their password
using their email address.

**Summary:**

-   On the Log In page, there is a button which states “**Forgot Password**?”
    which redirects the user to a password reset page.
-   Users can submit their email address, and subsequently receive a unique link
    which they can use to re-set their existing password associated with their
    email address.
-   The password reset form is fully validated before submission, and all errors
    are clearly communicated to the user.
-   Once the password has been reset, a user cannot log into the site using
    their previous password.

**Outcome: Pass**

**User Story:** 2d – As a Free/User, I want to be able to access my profile, so
that I can see my statistics and status.

**Acceptance Criteria:** A logged in user must be able to access their profile
from any page to view stats and interact with the profile.

**Summary:**

-   Users who are logged in are presented with the **Profile** link within the
    Navbar (both desktop and mobile).
-   If a user who is **not logged in** attempts to access the profile, they are
    re-directed to the **Log In** page.
-   Logged in users can access the **Profile** from any page, and this page
    always shows the following information:
    -   **Username**
    -   **Total Runs**
    -   **Longest Run**
    -   **Current Streak**
    -   **Account Type**
-   If a user does not have an **Active Character:**
    -   They are presented with a **“Create New Character”** button which takes
        them to the **Character Creation** page.
-   If a user has an **Active Character**:
    -   They are presented with their **Active Character**, **Weapon**, and
        their associated **Statistics**.
    -   They are presented with their **Active Character’s** XP progress to
        their next level.
    -   They are prompted to **Delete Hero**, which removes the user’s **Active
        Character**.
    -   They are prompted to proceed to **Start Battle**, which takes them to
        **Battle**.

**Outcome: Pass**

## Premium

## 

**User Story:** 3a – As a Free User, I want to be able to access the upgrade
offers from any page, so that I can choose to upgrade easily from any location
on the site.

**Acceptance Criteria:** A free user should be able to access the premium page
and be presented with the option to upgrade.

**Summary:**

-   All users can access the **Premium** page, regardless of viewport, from any
    page.
-   When a free user hits the **Active Character** level limit of 2, they are
    presented with a link to the **Premium** page after every battle.
-   When on the **Premium** page, if a user is not logged in, they are
    instructed to log in.
-   When on the **Premium** page, if a user is logged in and not premium, a
    button is presented which states **Upgrade Now**. This initiates the upgrade
    process.

**Outcome: Pass**

**User Story:** 3b – As a Free User, I want to be able to pay to upgrade to the
full version, so that I can have full access to premium features

**Acceptance Criteria:** A free user should be able to make a one-off payment to
permanently add the paid status to their profile, unlocking the benefits of
premium.

**Summary:**

-   Users who are not logged in, and users who are already paid users, are
    unable to interact with the **Upgrade Now** button on the **Premium** page.
-   Users who are logged in, but have not upgraded to premium, are able to
    interact with the **Upgrade Now** button on the **Premium** page.
-   Interacting with the **Upgrade Now** button directs users to a **Stripe
    Checkout** interface.
-   If a user pressed the ‘back’ button whilst on the **Stripe Checkout**
    interface, the user is directed to a **Abort** page, confirming the payment
    was not successful.
-   Three payment types were tested on the **Stripe Checkout** interface:
    -   Failed Payment Test: 4000000000009995:
        -   The interface confirms the card has insufficient funds.
    -   Requires Authentication Test: 4000002500003155:
        -   Authentication pop-up appears. Failing authorisation communicates a
            failed payment to the user. Successful authorisation directs the
            user to the **Payment Success** page.
    -   Successful Payment Test: 4242424242424242:
        -   User is directed to the **Payment Success** page.
-   From the **Stripe Checkout** interface, or any other domain page, a user
    cannot manually navigate to:
    -   **Premium/success**
    -   **Premium/process**
    -   These attempts redirect the user to the **Premium Page.**
-   Upon successful payment, the users are sent a confirmation email.
-   Upon successful payment, users’ profile **Account Type** states Premium.
-   Upon successful payment, paid users have access to all content within the
    Codex.

**Outcome: Pass**

**User Story:** 3c – As a Paid User, I want to be able to navigate the site
without any upgrade offers, so that I can avoid paying for the product twice.

**Acceptance Criteria:** Paid users must not be prompted to upgrade, and must
not be able to access the **Stripe Checkout** page.

**Summary:**

-   When a paid user accesses the **Premium** page, they are presented with a
    message stating *“You are already a premium user!”.*
-   Paid users are unable to access the **Stripe Checkout** page.
-   Paid users are not presented with any additional prompts to upgrade to
    premium.

**Outcome: Pass**

## 

## Game

**User Story:** 4a – As a Free User, I want to be able to have basic access to
the game, so that I can decide whether I want to pay for the full game.

**Acceptance Criteria:** A free user must be able to have limited access to all
features of the game.

**Summary:**

-   Free users, once having their account validated, have the following access:
    -   They can create a character, out of the reduced choice available.
    -   They can access their **Profile**, which confirms their account type as
        **Free**.
        -   When a free user has no **Active Character**, the profile prompts
            them to create one.
        -   When a free user has an **Active Character**, the profile displays
            all character and weapon stats, and provides the option to **Delete
            Character** or **Start Battle**.
    -   They can access **Battle:**
        -   They can only fight enemies which are not tagged as **Paid**.
        -   They can only obtain loot which is not tagged as **Paid.**
    -   They can view the **Leaderboard**, however they are not presented with a
        score after battle, nor are they capable of having their score added to
        the **Leaderboard.**

**Outcome: Pass**

**User Story:** 4b – As a Free/Paid User, I want to be able to create a new
character, so that I can start playing the game.

**Acceptance Criteria:** A user must be able to create a new character, and
access features associated with a profile having an Active Character**.**

**Summary:**

-   Any logged in user can navigate to the **Create** page.
-   Any logged in user can hover over selectable **Heroes**.
-   Any logged in user can select a **Hero,** which highlights the chosen
    **Hero.**
-   If a character has not been selected, the navigational aid at the bottom of
    the screen states **Select a Character**.
    -   While in this state, the user cannot interact with this, and it appears
        disabled.
-   Once a character has been selected, the navigational aid at the bottom of
    the screen states **Create Character**.
    -   While in this state, users can hover (desktop) on this button, which
        provides the required visual feedback.
    -   Users can interact with this, which confirms the **Hero** selection.
-   Once a logged in user has confirmed their **Hero** selection, an **Active
    Character** is created in the relevant database for the respective user, and
    the user is redirected to their **Profile**.
-   When an **Active Character** has been created for the user, a random weapon
    is generated, relevant to the user’s Premium status and **Character Level**.
-   When an **Active Character** has been created for the user, and they visit
    the **Profile** page, their **Active Character** is displayed along with
    their associated weapon.
-   Any logged in user with an **Active Character** can delete their character
    from their **Profile.**
    -   This completely removes the **Active Character** from the relevant
        database.
    -   This **Active Character** can no longer be accessed from the user’s
        **Profile.**
    -   Once the **Active Character** is deleted, the user is redirected to the
        **Profile** page, which now prompts the user to **Create a new
        character.**
-   Any logged in user with an **Active Character** cannot access the **Create**
    page, to create a new character.
-   Any logged in user with an **Active Character** can access **Battle**
    through the Navbar (which replaces **Create** with **Battle**, when a user
    has an **Active Character**), through their Profile, or by manually
    navigating to **/battle/.**

**Outcome: Pass**

**User Story:** 4c – As a Free/Paid User, I want to be able to enter and engage
in a battle, so that I can enjoy the basic gameplay loop of the game.

**Acceptance Criteria:** Any user with an Active Character must be able to
participate in a Battle.

**Summary:**

-   Any logged in user with an **Active Character** can access **Battle**
    through the Navbar through their Profile, or by manually navigating to
    **/battle/.**
-   If a logged in user **without** an **Active Character** attempts to access
    **Battle** (for example by manually navigating to **/battle/**), the user is
    redirected to their **Profile**, which prompts them to **Create a new
    character.**
-   When a logged in user with an **Active Character** accesses a **Battle**:
    -   They are presented with their **Active Character** and associated
        weapon.
    -   They are presented with a randomly generated **Active Enemy** and their
        associated weapon.
    -   The combined statistics of each respective party is displayed for the
        user to view.
        -   On smaller viewports, these are condensed into a **popover** that
            can be accessed by interacting with the **Stats** button.
    -   Details on either the **Active Character’s** or **Active Enemy’s**
        weapon can be obtained by clicking/touching on the star rating of the
        respective weapon.
-   The **Active Time Battle** does not commence until a user clicks on **Start
    Battle.**
-   When a user clicks **Start Battle:**
    -   The **Battle Log** states **Battle Commenced!**
    -   The **Start Battle** button is replaced with an **Attack** and a
        **Retreat** button.
    -   The **Active Time Battle** commences.
    -   While it is not the **Active Character’s** turn, both **Attack** and
        **Retreat** buttons are disabled.
    -   The turn meters respond and animate according to the relationship
        between the **Active Character’s** and the **Active** **Enemy’s Speed**.
        -   If the **Active Character** has twice the speed of the **Active
            Enemy**, the user’s **Turn Meter** will fill twice as fast, and as
            such have two turns before the enemy takes their turn.
        -   If the **Active Enemy** has twice the speed of the **Active
            Character**, the enemy’s **Turn Meter** will fill twice as fast, and
            as such have to turns before the user takes their turn.
-   When the **Active Character’s** turn meter fills fully, the gameplay is
    paused, and does not proceed until the user chooses an action.
    -   When it is the **Active Character’s** turn, the **Attack** and
        **Retreat** buttons are enabled.
    -   When it is the **Active Character’s turn**, the **Attack** button
        pulses.
    -   When the user presses the **Attack** button, a calculation is performed
        to determine:
        -   Whether the attack hits.
        -   How much damage is deducted off the opponents HP.
        -   Whether the attack kills the **Active Enemy**.
        -   The outcome of the attack is communicated to the user in the
            **Battle Log**.
        -   The **Active Enemy’s** HP bar is updated accordingly.
    -   When the user presses the **Retreat** button, a modal is presented which
        gives the user the option to **Retreat, Retry,** or **Continue** (See
        User Story 4f).
-   When the **Active Enemy’s** turn meter fills fully, the gameplay is **not
    paused**, instead, they automatically attempt an attack, the aforementioned
    calculations are performed, and the outcome of the attack is communicated to
    the user in the **Battle Log**.
-   At any time, the user can scroll through the **Battle Log** to read historic
    entries.
-   If the **Active Character’s** HP is reduced to zero, the user loses the
    battle.
-   If the **Active Enemy’s** HP is reduced to zero, the enemy loses the battle.
-   The outcome of the battle is communicated to the user in the **Battle Log**.
-   Following the conclusion of a battle, after a short delay, the user is
    directed to the **Post-Battle** page, where the outcome of the battle is
    communicated along with the features discussed in 4d, 4e, and 4g (where
    applicable).

**Outcome: Pass**

**User Story:** 4d – As a Free/Paid User, I want to be able to level up my
character, so that I can make progress in the game.

**Acceptance Criteria:** A user must be able to level up, and compare statistics
of their previous level and current level.

**Summary:**

-   At the end of a successful battle, **Active Characters** gain an amount of
    XP relative to both their own level and the **Active Enemy’s** level.
    -   XP is granted as a percentage of the **Active Enemy’s** Level to the
        **Active Character’s** Level.
    -   If a Level 2 **Active Character** defeats a Level 1 **Active Enemy**,
        they are awarded 50XP.
    -   If a Level 2 **Active Character** defeats a Level 2 **Active Enemy**,
        they are awarded 100XP.
-   At any point, a user can visit the **Profile** page to see their **Active
    Character’s** current level, and their relative progression towards the next
    level.
-   If the user’s XP exceeds their current **Max XP**, which is calculated based
    on their **Active Character**’s current Level, they subsequently level up.
    -   Upon Levelling Up, the **Active Character’s** **Min XP** and **Max XP**
        are updated accordingly to reflect the new thresholds required to Level
        Up, and this scales exponentially.
-   If, following a successful **Battle,** an **Active Character** levels up,
    the **Post Battle** screen confirms this to the user.
    -   A heading reads **Level Up**.
    -   The user is displayed their previous character (and the associated
        stats) and their newly levelled up character (and the associated stats).
-   Any loot obtained from a **Battle** where the **Active Character** has
    levelled up is subject to randomisation based on the **Active Characters**
    new level.
-   Free Users cannot obtain XP or Level Up past Level 2.
    -   Free users who continue to play the game are presented with a message in
        the **Post-Battle** screen informing them they have reached the level
        limit.
    -   Free users who continue to play the game can see from the **Profile**
        page that the XP progress bar does not move after reaching max level.
-   Paid users can continue to Level Up indefinitely.

**Outcome: Pass**

## 

**User Story:** 4e – As a Free/Paid User, I want to be presented with a choice
of a new weapon after each win, so that I can customize my character.

**Acceptance Criteria:** Users must be presented with a new weapon after every
successful battle, and they must be provided with the choice to take the new
weapon or keep their existing weapon.

**Summary:**

-   For any user, at the end of each successful **Battle**, a random weapon is
    generated (subject to Stat, Tier, and Rarity randomisation).
-   The user is presented with their existing weapon, along with the newly
    generated weapon.
-   Each weapon is clearly separated within their isolated container, and
    clearly communicate the following:
    -   The weapon’s image.
    -   The weapon’s name.
    -   The weapons Tier (Star Rating).
    -   The weapon’s Rarity (via both text and visual effects).
    -   The stats of the weapon (HP, Attack, Defence, and Speed).
-   A button is presented under each item:
    -   The existing weapon has the button **Keep Old Weapon** underneath it,
        and pressing this button dismisses the newly generated weapon.
    -   The newly generated weapon has the button **Take New Weapon** underneath
        it, and pressing this button dismisses the old weapon, and inserts the
        data of the new weapon into the **Active Character**’s relative database
        entry.
    -   After choosing the required Loot, the chosen item remains on screen, and
        the user is presented with two new options:
        -   **Profile**: This takes the user to their **Profile**.
        -   **Battle:** This takes the user to a new **Battle.**
-   If the user decides to take the new weapon, this can be immediately seen in
    both the user’s **Profile** and in the next **Battle** they commence.
-   The two weapons, their stats, and their rarity, are clearly distinguishable.
-   The weapon that is generated is always relative to the **Active
    Character’s** level.

**Outcome: Pass**

**User Story:** 4f – As a Free/Paid User, I want to be able to leave a battle
halfway through and return at a later time, so that I can stop playing the game
at any point without being penalised.

**Acceptance Criteria:** Users should be able to retreat or retry a battle with
no consequence, and and/or subsequently return to the battle at a later time.

**Summary:**

-   When a user first engages in **Battle**, an **Active Enemy** is created.
-   When an **Active Enemy** is created, this enemy is retained in the relevant
    database until:
    -   The **Activate Character** is deleted by the user.
    -   The **Active Character** wins the battle against the **Active Enemy.**
    -   The **Active Character** loses the battle against the **Active Enemy.**
-   Therefore, if a user decides to **Retreat** during a **Battle**, when they
    return to **Battle**, they will be presented with the **Active Enemy** they
    retreated from.
-   When a user presses the **Retreat** button during their turn in **Battle**,
    they have the following three choices:
    -   **Retreat**: This directs the user to their **Profile** If they return
        to **Battle** at any point, they will be raced against the existing
        **Active Enemy** as discussed.
    -   **Retry:** This restarts the **Battle.**
    -   **Continue**: This dismisses the modal, and allows the user to continue
        with the **Battle.**
-   If the user tries to navigate away from the **Battle** (or refreshes the
    page) without interacting with the **Retreat** button, they will be
    presented with a browser-native **Confirmation**. There are **no** penalties
    for retreating or retrying a battle through this method, however this
    prevents a user from accidentally exiting.
-   If a user retreats during a battle, logs off, and logs back in with a
    different device, they will be presented with the same **Active Enemy** they
    retreated from.

**Outcome: Pass**

**User Story:** 4g – As a Paid User, I want to have access to higher levels,
additional characters, and additional weapons/enemies, so that I can enjoy the
benefits of premium content.

**Acceptance Criteria:** A paid user must be able to access premium content, and
be able to exceed level 2 in order to access content which is paywalled from
this level.

**Summary:**

-   Free users are only able to choose out of 3 **Heroes** when creating an
    **Active Character.**
-   Paid users can choose out of 10 **Heroes** when creating an **Active
    Character.**
-   Paid users can exceed past level 2, with no max limit; at the time of
    documenting the highest level achieved by a user is Level 7.
-   As weapons’ **Tiers** are tied to **Active Character Level,** Tier 3, Tier
    4, and Tier 5 weapons become available in the pool of loot (for any given
    run) when the **Active Character** reaches these levels accordingly.
    -   At no point has a weapon been generated that is of higher Tier than the
        **Active Character’s** current level.
-   As the max **Level** of a weapon is tied to the **Active Character Level**,
    the highest possible weapon **Level** that can be generated at any given
    time is limited by the **Active Character’s Level.**
    -   At no point has the level of a generated weapon been higher than the
        **Active Character’s** current level.
-   As enemies’ **Tiers** are tied to **Active Character Level,** Tier 3, Tier
    4, and Tier 5 enemies become available in the pool of loot (for any given
    run) when the **Active Character** reaches these levels accordingly.
    -   At no point has an enemy been generated that is of higher **Tier** than
        the **Active Character’s** current level.
-   As weapon **Rarity** is tied to **Active Character Level**:
    -   Free users can only generate the following rarity weapons:
        -   **Common** (from Character Level 1)
        -   **Uncommon** (from Character Level 2)
    -   Paid users can generate the following rarity weapons:
        -   **Rare** (from Character Level 3)
        -   **Epic** (from Character Level 4)
        -   **Mythic** (from Character Level 5)
    -   At no point has a Free user been able to generate a weapon with a rarity
        higher than **Uncommon,** due to the Level 2 cap.
    -   Paid users have generated content of all rarities.
-   Certain Tier 1 and Tier 2 enemies and weapons within the **Codex** contain
    **Paid** tags, and as such are programmatically prevented from being
    instanced from the **Codex** database for enemy and weapon generation.
    -   At no point has **Premium** **Codex** content been generated for a Free
        User.
    -   Paid users have generated Premium Codex content for **Tier 1**  and
        **Tier 2** enemies/weapons.

**Outcome: Pass**

## Leaderboard

## 

**User Story:** 5a – As a Site User, I want to be able to view the Leaderboard,
so that I can see the High Scores of paid players.

**Acceptance Criteria:** Site users should be able to access the Leaderboard
page from any page, in order to a summary of the Leaderboard.

**Summary:**

-   As the Navbar contains a link to the **Leaderboard,** site users can access
    the **Leaderboard** from any location (regardless of viewport).
-   When visiting the Leaderboard, all 10 entries within the **Leaderboard** are
    visible from the outset, in the format of an accordion.
-   Each **Leaderboard** entry’s heading contains the **Position, Username**,
    and **Score.**
-   The **Leaderboard** always appears in descending order, with 1st position
    (highest scorer) at the top.
-   Site users can scroll through the list of all **Leaderboard** entries (if
    applicable, due to viewport).
-   If no scores are on the **Leaderboard**, the accordion is replaced with a
    heading which confirms there are currently no **Leaderboard** entries.

**Outcome: Pass**

**User Story:** 5b – As a Site User, I want to be able to view individual
Leaderboard entries, so that I can view the breakdown of a player’s score.

**Acceptance Criteria:** Site users should be able to interact with each
Leaderboard entry to obtain more information on each entry.

**Summary:**

-   Within the **Leaderboard** page, site users can interact with each
    individual **Leaderboard** entry.
-   Interacting with an entry will reveal additional information and statistics
    regarding that particular entry.
-   The statistics contained within each entry relate to the relevant user’s
    **Activate Character** database entry at the time in which they were
    defeated.
-   The statistics present for each entry are:
    -   Character Name
    -   Character Level
    -   Character Image
    -   Character HP
    -   Character Attack
    -   Character Defence
    -   Character Speed
    -   Weapon Name
    -   Weapon Level
    -   Weapon Image
    -   Weapon HP
    -   Weapon Attack
    -   Weapon Defence
    -   Weapon Speed
    -   Weapon Rarity
    -   Date of entry within the **Leaderboard**
    -   The **Active Character’s** total kills
-   Site users can interact with every **Leaderboard** entry.
    -   Interacting with the same entry for a second time collapses it.
    -   Interacting with a different entry, while an entry is currently open,
        collapses the currently open entry, and opens the new entry selected.
-   Site users can easily distinguish and understand the statistics presented.

**Outcome: Pass**

**User Story:** 5c – As a Paid User, I want to be able to add my score to the
Leaderboard, so that I can compete with other paid players.

**Acceptance Criteria:** If a Paid User’s score is high enough, following a
battle loss, it is added to the Leaderboard and the user is informed of this.

**Summary:**

-   Free users cannot compete in the **Leaderboard.**
    -   When Free Users lose a battle, they are informed they must upgrade to
        **Premium** in order to compete in the **Leaderboard.**
    -   With an empty **Leaderboard** database, a Free User’s score is not added
        to the database.
-   Paid users can compete in the **Leaderboard.**
    -   When Paid users lose a battle, they are informed whether or not their
        score has been added to the **Leaderboard.**
    -   With an empty **Leaderboard** database, the first 10 scores are
        submitted to the **Leaderboard.**
    -   With a full **Leaderboard** database, the score will only be added to
        the **Leaderboard** database if it is higher than the lowest scoring
        **Leaderboard** entry.
    -   If a new score is added to the **Leaderboard**, the
-   If a paid user delete’s their **Active Character** from the **Profile,**
    their score is not calculated and therefore is not considered for entry into
    the **Leaderboard**.

**Outcome: Pass**

**User Story:** 5d – As a Paid User, I want to be able to see my score at the
end of a game, so that I can find out where my position is on the Leaderboard,
or see how close I was to reaching the Leaderboard.

**Acceptance Criteria:** Paid users must be presented with their score on the
Post-Battle screen, and this must match the score on the Leaderboard if
successful.

**Summary:**

-   Free users are not presented with a score on the **Post-Battle** screen on
    defeat.
    -   Free users are directed to upgrade to **Premium** for this feature.
-   Paid users are presented with their score on the **Post-Battle.**
    -   Paid users are informed whether or not the score has made it to the
        **Leaderboard.**
    -   Paid users are always provided their score, regardless of whether the
        score has made the **Leaderboard.**
-   If a paid user’s score is successfully added to the Leaderboard, their
    position on the **Leaderboard** can be determined by matching the score
    shown on the **Post-Battle** screen.
    -   When applicable, the score presented to apaid user, on the
        **Post-Battle** screen, matches the score saved within the
        **Leaderboard.**
-   If a paid user delete’s their **Active Character** from the **Profile,**
    their score is not calculated and therefore is not considered for entry into
    the **Leaderboard**.

## Codex

**User Story:** 6a – As a Site User, I want to be able to view the Codex, so
that I can see all available content in the game.

**Acceptance Criteria:** Site Users must be able to access the Codex from any
page, and navigate through all content available.

**Summary:**

-   As the Navbar contains a link to the **Codex,** site users can access the
    **Codex** from any location (regardless of viewport).
-   Within the **Codex**, the site user is presented with every item within the
    **Codex**.
-   Each **Codex** entry is clearly differentiated and containerised.
-   Each **Codex** entry contains the following information:
    -   Image
    -   Name
    -   Type (Enemy/Weapon/Hero)
    -   HP (Stat)
    -   Attack (Stat)
    -   Defence (Stat)
    -   Speed (Stat)
    -   Premium (Paid Tag)
    -   Tier (Star Rating)
-   All information within a **Codex Entry** is clear and legible.
-   At the bottom of the screen is a **Back to Top** button, which contains the
    number of entries visible, and when interacted with navigates the user back
    to the top of the screen (if applicable).
-   The number of entries visible adjusts dynamically to the site user’s
    viewport.

**Outcome: Pass**

**User Story:** 6b – As a Site User, I want to be able to sort and filter the
Codex, so that I can find specified entries in the codex, and find out what
content is available as a paid user.

**Acceptance Criteria:** Site Users must be able to filter and sort the Codex
entries.

**Summary:**

-   Site users can interact with the **Filters** button at the top of the
    **Codex**.
-   The **Filters** button reveals a container which contains multiple filtering
    and sorting options:
    -   **Premium Content:** This filters entries by **Free, Premium,** or
        **Both.**
    -   **Type:** This filters entries by **Enemy, Hero, Weapon,** or **Both.**
    -   **Tier:** This filters entries by the **Tiers** selected (1 – 5).
    -   **Sort By:** This sorts entries by **Name, Type, HP, Attack,** 
        **Defence, Speed,** or **Default.**
        -   The **Default** sort parameter is a special alphabetized version of
            the entries name, and is not visible to the site user.
    -   **Direction**: This sorts the selected value in either **Ascending**
        (default) or **Descending** order.
-   After selecting the requested filters and sorting options, site users can
    select the **Apply Filters** link, which requests the sorted and filtered
    content.
    -   A user can press **Clear Filters** at any time to reset all filters.
-   If a site user selects a combination of parameters that produces no results
    (for example **Free** content of **Tier 3 and above)**, a messages is
    presented to the user confirming **No codex entries found for these
    parameters.**
-   The **Back to Top** button shows the correct number of results presented for
    any combination of filters (including those that produce no results).

**Outcome: Pass**

**User Story:** 6c – As an Admin, I want to be able to add entries to the Codex,
so that I can add content to the game.

**Acceptance Criteria:** Admins must be able to add full Codex entries without
relying on the Django admin interface.

**Summary:**

-   Admins have access to an additional **Create** button on **Codex** page,
    next to **Filters**, which allows Admins to add new entries to the **Codex**
    database.
-   Interacting with the **Create** button directs the user to a new **Create**
    page, which contains a blank form.
-   This form contains all the required feels to add a new entry to the
    **Codex** database.
    -   All required fields are marked with an asterisk.
    -   All fields within the form are validated on submission.
        -   Invalid fields prevent the form from being submitted.
    -   Images are uploaded via the form are uploaded to the relevant storage
        (local for development, AWS for deployment).
    -   The form contains a **Create** button which submits the form.
-   On valid submission of a **Codex** entry, the Admin is directed to the
    **Codex** page, and the new entry appears within the list.
-   All fields for the new **Codex** entry are correctly populated, and the
    image uploaded correctly display.

**Outcome: Pass**

**User Story:** 6d – As an Admin, I want to be able to update entries to the
Codex, so that I can update content in the game.

**Acceptance Criteria:** Admins must be able to edit full Codex entries without
relying on the Django admin interface.

**Summary:**

-   Admins have access to an additional **Edit** button on **Codex** page, at
    the bottom of each **Codex** entry, which allows Admins to edit existing
    **Codex** entries within the database.
-   Interacting with the **Edit** button directs the user to an **Edit** page,
    which contains a form prepopulated with the given entry’s information.
-   This form contains all the required fields to edit every aspect of a given
    Codex entry (other than Primary Key).
    -   All required fields are marked with an asterisk.
    -   All fields within the form are validated on submission.
        -   Invalid fields prevent the form from being submitted.
    -   Images are uploaded via the form are uploaded to the relevant storage
        (local for development, AWS for deployment).
    -   The form contains an **Edit** and **Delete** button. The **Edit** button
        submits the form for editing the entry with the new details.
-   On valid submission of a **Codex** entry modification, the Admin is directed
    to the **Codex** page, and the edited entry appears within the list.
-   All edited fields for the existing **Codex** entry are correctly populated,
    and the image uploaded correctly display (if amended).

**Outcome: Pass**

## 

**User Story:** 6e – As an Admin, I want to be able to delete entries in the
Codex, so that I can remove content from the game.

**Acceptance Criteria:** Admins must be able to delete full Codex entries
without relying on the Django admin interface.

**Summary:**

-   Within the **Edit** page, accessible only to admins, a **Delete** button is
    available.
    -   This button **Deletes** the entry the admin is currently editing.
-   Interacting with this button prompts a modal, which requests confirmation of
    the admin’s request to **delete** the entry.
-   When an admin confirms their request to **delete** the entry, the admin is
    redirected to the **Codex**.
-   **Codex** entries which are deleted are removed from the **Codex** database,
    and as such are no longer present on the **Codex** page.

**Outcome: Pass**

## Additional Manual Testing

**Error Handling**

-   Ensure that **404 HTTP** errors are appropriately routed to the custom
    404.html.
    -   **Stress Test:** Input an unfamiliar route in the URL
-   Ensure that **500 HTTP** errors are appropriately routed to the custom
    500.html.
    -   **Stress Test:** Set debug to disabled, and intentionally break a route
        before attempting to access it.

**Interface Interaction**

-   Ensure all interactive elements respond appropriately:
    -   **Desktop:**
        -   All navigational links correctly respond to hovering.
        -   All buttons correctly respond to hovering.
    -   **Mobile:**
        -   All navigational links correctly respond to touch.
        -   All buttons correctly respond to touch.

**Links**

-   Ensure the external link within the **How To** opens up in a new tab.

# Automated View Testing  


This project was developed using **Test Driven Development.** As such, Unit
Tests were written for the majority of views within Django before the respective
view was written.


## Testing Overview

| **Django App**                                                                    | Unit Test Number | Unit Test Summary                                          | Related User Stories                                   | Outcome |
|-----------------------------------------------------------------------------------|------------------|------------------------------------------------------------|--------------------------------------------------------|---------|
| [**Home**](https://github.com/BAK2K3/CIRPG/blob/main/home/tests.py)               | UT01             | Test home page renders correct page.                       | 1a                                                     | Pass    |
|                                                                                   | UT02             | Test help page renders correct page.                       | 1c                                                     | Pass    |
| [**Profiles**](https://github.com/BAK2K3/CIRPG/blob/main/profiles/tests.py)       | UT03             | Test Current Profile Context being passed to any page.     | 2b, 2e, 3a, 3b, 3c, 4a, 4b, 4c, 4d, 4e, 4f, 4g, 5c, 5d | Pass    |
|                                                                                   | UT04             | Test Active Character is rendered to Profile page.         | 2e, 4d, 4f                                             | Pass    |
|                                                                                   | UT05             | Test Hero list Context being passed to Create page.        | 4a, 4b                                                 | Pass    |
|                                                                                   | UT06             | Test Create page redirects if user has active character.   | 2e, 4a, 4b                                             | Pass    |
|                                                                                   | UT07             | Test Create route filtering paid from current profile.     | 4a, 4b, 4g                                             | Pass    |
|                                                                                   | UT08             | Test Create Character post submission route.               | 2e, 4a, 4b                                             | Pass    |
|                                                                                   | UT09             | Test Delete Character route deletes active Char.           | 2e, 4a                                                 | Pass    |
| [**Battle**](https://github.com/BAK2K3/CIRPG/blob/main/battle/tests.py)           | UT10             | Tests battle route is rendered with correct context.       | 4a, 4c, 4g                                             | Pass    |
|                                                                                   | UT11             | Tests context for successful post-battle route.            | 4a, 4d, 4e, 5d                                         | Pass    |
|                                                                                   | UT12             | Tests whether Ajax Loot route updates active character.    | 2e, 4a, 4e                                             | Pass    |
| [**Leaderboard**](https://github.com/BAK2K3/CIRPG/blob/main/leaderboard/tests.py) | UT13             | Test Leaderboard view renders correct page.                | 5a                                                     | Pass    |
|                                                                                   | UT14             | Test empty Leaderboard context in page rendering.          | 5a                                                     | Pass    |
|                                                                                   | UT15             | Test single Leaderboard context entry in page rendering.   | 5b, 5c                                                 | Pass    |
| [**Premium**](https://github.com/BAK2K3/CIRPG/blob/main/premium/tests.py)         | UT16             | Test premium page renders correct page.                    | 3a                                                     | Pass    |
|                                                                                   | UT17             | Test AJAX config view returns stripe public key.           | 3a, 3b                                                 | Pass    |
|                                                                                   | UT18             | Test AJAX checkout session view returns sessionId.         | 3b                                                     | Pass    |
|                                                                                   | UT19             | UT19 - Test AJAX checkout returns error for premium users. | 3c                                                     | Pass    |
|                                                                                   | UT20             | Test successful payment page renders correct page.         | 3b                                                     | Pass    |
|                                                                                   | UT21             | Test process invalid session_id redirects to premium.      | 3b                                                     | Pass    |
|                                                                                   | UT22             | Test aborted payment page renders correct page             | 3b                                                     | Pass    |
| [**Codex**](https://github.com/BAK2K3/CIRPG/blob/main/codex/tests.py)             | UT23             | Test codex route renders correct page.                     | 6a                                                     | Pass    |
|                                                                                   | UT24             | Test codex route queries DB.                               | 6a                                                     | Pass    |
|                                                                                   | UT25             | Test codex DB entry structure.                             | 6a                                                     | Pass    |
|                                                                                   | UT26             | Test codex filtering for premium products.                 | 6b                                                     | Pass    |
|                                                                                   | UT27             | Test codex filtering for free products.                    | 6b                                                     | Pass    |
|                                                                                   | UT28             | Test codex filtering for weapons.                          | 6b                                                     | Pass    |
|                                                                                   | UT29             | Test codex filtering for enemies.                          | 6b                                                     | Pass    |
|                                                                                   | UT30             | Test codex filtering for heroes.                           | 6b                                                     | Pass    |
|                                                                                   | UT31             | Test codex filtering for rating.                           | 6b                                                     | Pass    |
|                                                                                   | UT32             | Test codex filtering for multiple ratings.                 | 6b                                                     | Pass    |
|                                                                                   | UT33             | Test codex filtering for multiple parameters.              | 6b                                                     | Pass    |
|                                                                                   | UT34             | Test codex sorting direction params.                       | 6b                                                     | Pass    |
|                                                                                   | UT35             | Test codex sort by parameters.                             | 6b                                                     | Pass    |
|                                                                                   | UT36             | Test codex Edit view.                                      | 6c                                                     | Pass    |
|                                                                                   | UT37             | Test codex Create view.                                    | 6d                                                     | Pass    |
|                                                                                   | UT38             | Test codex Delete view                                     | 6e                                                     | Pass    |

## Test Coverage

In order to assess **Test Coverage,**
[Coverage](https://coverage.readthedocs.io/en/coverage-5.5/) was used. The test
coverage resulted in an **89%** coverage (also taking into consideration the
default Django files). For full results, please see the **Coverage Results.**

The following steps were taken to generate the above report:

-   Enter `pip install coverage`
-   Create a Coverage Debug launch file:

```

{

    "name": "Python: Django Coverage",

    "type": "python",

    "request": "launch",

    "module": "coverage",

    "args": [

        "run",

        "--source='.'",

        "manage.py",

        "test"

        ],

    "django": true,

    "env": {

        "DJANGO_SECRET_KEY": "<variable>",

        "DEVELOPMENT": "Yes",

        "STRIPE_PUBLISHABLE_KEY": "<variable>",

        "STRIPE_SECRET_KEY": "<variable>",

        "STRIPE_PRICE_ID": "<variable>",

        "STRIPE_WH_SECRET": "<variable>",

        "DOMAIN_URL": "<variable>",

    }
}
```

-   Launch Python: Django Coverage debug (`F5`).
    -   This runs the script: `coverage run --source=’,’ manage.py test` with
        environment variables.
-   Enter `coverage report`
-   Enter `coverage html`
-   From within the produced `htmlcov` folder, open `index.html`.
-   Copy and paste the values into an Excel spreadsheet, and format accordingly.

Please note that the test coverage files (`htmlcov`) have **not** been
included in the GitHub repository.
