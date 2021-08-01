// Initialise Popover
var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
    return new bootstrap.Popover(popoverTriggerEl, {
        html: true,
        container: "body",
        sanitize: false,
        placement: "auto",
        content: function() {
            contentId = $(this).attr("data-content-id");
            return $(contentId).html();
        }
    });
});

// Prevent Window Closure
window.addEventListener('beforeunload', preventClosure);

function preventClosure(event){
    // Cancel the event as stated by the standard.
    event.preventDefault();
    // Chrome requires returnValue to be set.
    event.returnValue = 'Are you sure you want to exit?';
}

// Global Declarations

// Extract JSON dumps - Needed to double parse and index to work properly
const characterJson = JSON.parse(JSON.parse(document.getElementById('id_character_json').textContent))[0];
const enemyJson = JSON.parse(JSON.parse(document.getElementById('id_enemy_json').textContent))[0];

// Remove these elements from the DOM
document.getElementById('id_character_json').remove();
document.getElementById('id_enemy_json').remove();

// Combine the required character stats for object creation
let characterStats = {
    'name': $(".character-container .battle-title")[0].innerText.split("-")[0].slice(0,-1),
    'level': characterJson.fields.current_level,
    'hp': characterJson.fields.char_hp + characterJson.fields.weapon_hp,
    'attack': characterJson.fields.char_attack + characterJson.fields.weapon_attack,
    'defense': characterJson.fields.char_defense + characterJson.fields.weapon_defense,
    'speed': characterJson.fields.char_speed+ characterJson.fields.weapon_speed,
};

// Combine the required enemy stats for object creation
let enemyStats = {
    'name': $(".enemy-container .battle-title")[0].innerText.split("-")[0].slice(0,-1),
    'level': enemyJson.fields.enemy_level,
    'hp': enemyJson.fields.enemy_hp + enemyJson.fields.weapon_hp,
    'attack': enemyJson.fields.enemy_attack + enemyJson.fields.weapon_attack,
    'defense': enemyJson.fields.enemy_defense + enemyJson.fields.weapon_defense,
    'speed': enemyJson.fields.enemy_speed + enemyJson.fields.weapon_speed,
};

// BattleObject class definition
class BattleObject {

    // Constructor for required stats
    constructor(stats) {
        this.name = stats.name; 
        this.level = stats.level;
        this.maxHP = stats.hp;
        this.hp = stats.hp;
        this.attack = stats.attack; 
        this.defense = stats.defense;
        this.speed = stats.speed;
        this.dodge = this.calculateDodge();
        this.turnMeter = 0;
        this.isTurn = false;
    }

    // Calculates dodge chance (capped at 75%)
    calculateDodge () {
        let dodgeChance = Math.floor((this.defense / this.hp) * 100);
        if (dodgeChance > 75){
            return 75;
        } else {
            return dodgeChance;
        }
    }

    // Randomly calculates whether an attack is successful
    // Based on opponents dodge attribute
    // Returns true/false depending on success
    attackOutcome (opponentDodge) {
        let successRoll = this.getRandomInt();
        if (successRoll >= opponentDodge){
            return true;
        } else {
            return false;
        }
    }

    // Random 0-100 generator for attackOutcome
    getRandomInt() {
        return Math.floor(Math.random() * 99);
      }

    // When called adds speed to turnmeter
    // If turnmeter exceeds 100, substract 100
    // And set isTurn bool to True
    calculateTurnMeter() {
        this.turnMeter += this.speed;
        if (this.turnMeter >= 1000) {
            this.turnMeter -= 1000;
            this.isTurn = true;
        } 
    }

    // Deducts enemy damage of current objects
    // HP. If exceeds HP remaining, set to 0.
    calculateDamage(enemyDamage){
        this.hp -= enemyDamage;
        if (this.hp < 0){
            this.hp = 0;
        }
    }

    // Function for updating battle log
    // Take in the logstring to be 
    // Written to the log and appends to existing
    // HTML.
    updateBattleLog(logString){
        let battleLog = document.getElementById("battleLog");
        battleLog.append(logString);
        battleLog.scrollTop = battleLog.scrollHeight;
    }

    // Prepares battle log string for successful attack
    attackHitLog(enemyName){
        let logString = `\n${this.name} hit ${enemyName} for ${this.attack} damage!`;
        this.updateBattleLog(logString);
    }
    
    // Prepares battle log string for missed attack
    attackMissLog(){
        let logString = `\n${this.name} missed their attack!`;
        this.updateBattleLog(logString);
    }

    // Function to be called when current object wins
    async declareWinner(result){
        let logString = `\n${this.name} wins the fight!`;
        this.updateBattleLog(logString);
        await new Promise(r => setTimeout(r, 1000));
        $("#postBattleForm #hiddenResult").val(result);
        window.removeEventListener("beforeunload", preventClosure);
        $("#postBattleForm").submit();
    }

    // Function to update Progress Bar %
    // Takes in targetted bar and value 
    updateBar(bar, percent, value){
        bar.style.width = `${percent}%`;
        bar.setAttribute('aria-valuenow', value);
    }

    // Function to calculate HP remaining %
    // To be passed to updateBar.
    calculateHPPercent(){
        return Math.floor((this.hp / this.maxHP) * 100);
    }

    calculateTurnPercent(){
        return Math.floor((this.turnMeter / 1000) * 100)
    }
}


// Declare user Character and Enemy objects
let characterObject = new BattleObject(characterStats);
let enemyObject = new BattleObject(enemyStats);

// Obtain required progress bars
let characterHPBar = document.getElementById("heroHp");
let characterTurnBar = document.getElementById("heroTurn");
let enemyHPBar = document.getElementById("enemyHp");
let enemyTurnBar = document.getElementById("enemyTurn");

// Function for starting the battle timer
function startBattleTimer() {
    // Swap button
    document.getElementById('startButton').remove();
    document.getElementById('attackButton').classList.remove('d-none');
    
    // Start Battle
    engageBattle();
}


// Game Logic Battle Loop
async function engageBattle(){

    // Disable attack button
    document.getElementById('attackButton').disabled = true;

    // While either char/enemy is alive
    while ((characterObject.hp > 0) || (enemyObject.hp > 0)) {

        await new Promise(done => setTimeout(() => done(), 5));

        // Character Turn
        if (characterObject.isTurn){
            // If the character hits
            if (characterObject.attackOutcome(enemyObject.dodge)){
                enemyObject.calculateDamage(characterObject.attack);
                enemyObject.updateBar(enemyHPBar, enemyObject.calculateHPPercent(), enemyObject.hp);
                characterObject.attackHitLog(enemyObject.name);
                // If enemy HP is 0
                if (enemyObject.hp == 0){
                    characterObject.declareWinner(true);
                    return true;
                }
            // If the character misses
            } else {
                characterObject.attackMissLog();
            }
            // De-active character's turn
            characterObject.isTurn = false;
            characterObject.updateBar(characterTurnBar, characterObject.calculateTurnPercent(), characterObject.turnMeter);
        // If not turn
        } else {
            // Calculate Character turn meter
            characterObject.calculateTurnMeter();
            if (characterObject.isTurn){
                characterObject.updateBar(characterTurnBar, 100, 1000);
                document.getElementById('attackButton').disabled = false;
                return true;
            }
            characterObject.updateBar(characterTurnBar, characterObject.calculateTurnPercent(), characterObject.turnMeter);
        }

        // Calculate enemy turn 
        enemyObject.calculateTurnMeter();

        // If the turn metre exceeds 100%
        if (enemyObject.isTurn){

            // Set turn meter bar to 100%
            enemyObject.updateBar(enemyTurnBar, 100);

            await new Promise(done => setTimeout(() => done(), 500));

            // Calculate attack hit and update bars
            if (enemyObject.attackOutcome(characterObject.dodge)) {
                characterObject.calculateDamage(enemyObject.attack);
                characterObject.updateBar(characterHPBar, characterObject.calculateHPPercent(), characterObject.hp);
                enemyObject.attackHitLog(characterObject.name);
                // Determine if character is dead
                if (characterObject.hp == 0){
                    enemyObject.declareWinner(false);
                    return true;
                } else {
                    // Update accurate turn meter display
                    enemyObject.updateBar(enemyTurnBar, enemyObject.calculateTurnPercent(), enemyObject.turnMeter);
                }
            
            // If the attack misses
            } else {
                enemyObject.attackMissLog();
            }

            // After turn reset turn bool
            enemyObject.isTurn = false;

        // If the turnmeter doesn't cause the turn to activate
        } else {
            enemyObject.updateBar(enemyTurnBar, enemyObject.calculateTurnPercent(), enemyObject.turnMeter);
        }
    }
}

// Set event listeners to Start Button and Attack Button
$('#startButton').click(startBattleTimer);
$('#attackButton').click(engageBattle);
