import streamlit as st
import random
from enum import Enum
from abc import ABC, abstractmethod

clues = [
    "There is a faded photograph of a grand ball, the guests' faces blurred with time.",
    "There is a worn-out diary, its pages filled with tales of epic adventures.",
    "There is a shattered mirror, reflecting a room that doesn't quite match yours.",
    "There is a dusty old map, its edges frayed and locations unrecognizable.",
    "There is a cryptic inscription on the wall, its meaning lost to time.",
    "There is a single feather, its origin unknown, lying in the corner.",
    "There is a forgotten melody playing from an unseen source.",
    "There is a strange symbol etched into the floor, its purpose unclear.",
    "There is a peculiar scent in the air, reminiscent of a time long past.",
    "There is a mysterious light flickering intermittently from beneath the door."
]

sense_exp = [
    "You see a flickering candle casting long, dancing shadows on the stone walls.",
    "You hear the distant echo of footsteps, but can't tell where they're coming from.",
    "You smell the musty scent of old books and parchment.",
    "You touch the cold, rough stone of the wall, worn by centuries of history.",
    "You intuit a sense of foreboding, as if the castle itself is watching you.",
    "You see a tapestry, its colors faded, depicting a battle long past.",
    "You hear the soft rustling of a curtain in the breeze from a hidden window.",
    "You smell the faint aroma of a meal cooked hours, or perhaps days, ago.",
    "You touch a velvet drapery, its once vibrant color now dulled by dust and time.",
    "You intuit a presence in the room, though you see no one.",
    "You see a suit of armor, its metal tarnished and covered in cobwebs.",
    "You hear the distant tolling of a bell, its sound muffled and melancholic."
]


class RandomItemSelector:
    def __init__(self, items):
        self.items = items
        self.used_items = []

    def pull_random_item(self):
        unused = list(set(self.items) - set(self.used_items))
        if not unused:
            self.used_items = []
            unused = self.items.copy()
        item = random.choice(unused)
        self.used_items.append(item)
        return item

class SenseClueGenerator:
    def __init__(self, clues, sense_exp):
        self.clue_selector = RandomItemSelector(clues)
        self.sense_selector = RandomItemSelector(sense_exp)

    def get_senseclue(self):
        clue = self.clue_selector.pull_random_item()
        sense = self.sense_selector.pull_random_item()
        return f"{clue} {sense}"


class EncounterOutcome(Enum):
    CONTINUE = 1
    END = 2

class Encounter(ABC):
    @abstractmethod
    def run_encounter(self):
        pass

class DefaultEncounter(Encounter):
    def __init__(self):
        self.generator = SenseClueGenerator(clues, sense_exp)

    def run_encounter(self):
        return self.generator.get_senseclue(), EncounterOutcome.CONTINUE

class TreasureEncounter(Encounter):
    def run_encounter(self):
        return "🎉 Congratulations! You found the treasure and won the game!", EncounterOutcome.END

class RedWizardEncounter(Encounter):
    game_rules = {
        "Fireball": ["Ice Shard", "Lightning Bolt"],
        "Ice Shard": ["Wind Gust", "Earthquake"],
        "Wind Gust": ["Lightning Bolt", "Fireball"],
        "Lightning Bolt": ["Earthquake", "Ice Shard"],
        "Earthquake": ["Fireball", "Wind Gust"]
    }

    def run_encounter(self, user_spell):
        wizard_spell = random.choice(list(self.game_rules.keys()))
        if user_spell == wizard_spell:
            return f"🤝 It's a draw! Both cast {user_spell}. Try again.", EncounterOutcome.CONTINUE
        elif user_spell in self.game_rules[wizard_spell]:
            return f"💥 You cast {user_spell}, Red Wizard cast {wizard_spell}. You were defeated.", EncounterOutcome.END
        else:
            return f"⚡ You cast {user_spell}, Red Wizard cast {wizard_spell}. You countered it!", EncounterOutcome.CONTINUE


room_names = [
    "Throne Room", "Armory", "Library", "Dungeon", "Observatory", "Royal Chamber"
]

room_encounters = {
    name: DefaultEncounter() for name in room_names
}
room_encounters["Treasure Room"] = TreasureEncounter()
room_encounters["The Red Wizard's Lair"] = RedWizardEncounter()

rooms = list(room_encounters.keys())


st.title("🏰 Castle Quest")

if "state" not in st.session_state:
    st.session_state.state = "start"
    st.session_state.current_room = None
    st.session_state.wizard = RedWizardEncounter()
    st.session_state.msg = ""
    st.session_state.spell_result = ""
    st.session_state.room_selector = RandomItemSelector(rooms)
    st.session_state.outcome = EncounterOutcome.CONTINUE


if st.session_state.state == "start":
    st.write("Welcome, adventurer! Your mission is to find the treasure hidden within this castle.")
    if st.button("Enter the Castle"):
        st.session_state.state = "room"

elif st.session_state.state == "room":
    door_count = random.randint(2, 4)
    st.write(f"You see {door_count} doors. Choose one to proceed:")
    for i in range(1, door_count + 1):
        if st.button(f"🚪 Door {i}"):
            room_name = st.session_state.room_selector.pull_random_item()
            st.session_state.current_room = room_name
            st.session_state.state = "encounter"
            break

elif st.session_state.state == "encounter":
    room = st.session_state.current_room
    st.subheader(f"You have entered: {room}")
    encounter = room_encounters[room]

    if room == "The Red Wizard's Lair":
        st.write("🔥 You face the Red Wizard! Choose your spell:")
        spells = list(RedWizardEncounter.game_rules.keys())
        for spell in spells:
            if st.button(spell):
                msg, outcome = encounter.run_encounter(spell)
                st.session_state.msg = msg
                st.session_state.outcome = outcome
                if outcome == EncounterOutcome.END:
                    st.session_state.state = "end"
                break
        if st.session_state.msg:
            st.info(st.session_state.msg)

    else:
        msg, outcome = encounter.run_encounter()
        st.write(msg)
        st.session_state.outcome = outcome
        if outcome == EncounterOutcome.END:
            st.session_state.state = "end"
        else:
            if st.button("Continue Exploring"):
                st.session_state.state = "room"

elif st.session_state.state == "end":
    st.success("🏁 Game Over!")
    st.write(st.session_state.msg)
    if st.button("Play Again"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.experimental_rerun()
