import time
from pymongo import MongoClient
from transformers import AutoModelForQuestionAnswering, AutoTokenizer
from rich.console import Console
from rich.progress import Progress
from rich.table import Table
import pyfiglet
from rich.live import Live
from rich.text import Text
from difflib import get_close_matches
import re

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://root:root2026@cluster1.xjqwm4a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1")
db = client["commands"]
collection = db["linux_commands"]

# Load model and tokenizer
model_name = "Ragaspace20041/bot"
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Function to handle user inputs and retrieve command details from the database or model
def get_command_details(user_input):
    user_input_lower = user_input.lower()

    # Check if the input directly matches a command
    command_data = list(collection.find({"command": {"$regex": f"^{user_input_lower}$", "$options": "i"}}))
    if command_data:
        return command_data

    # Check if the input matches a description (case-insensitive)
    description_data = list(collection.find({"description": {"$regex": f"{user_input_lower}", "$options": "i"}}))
    if description_data:
        return description_data

    # If input is not a direct command or description, use the model to find the best match
    question = f"What command is used for {user_input}?"
    inputs = tokenizer(question, return_tensors="pt")
    outputs = model(**inputs)
    answer_start = outputs.start_logits.argmax()
    answer_end = outputs.end_logits.argmax()
    command = tokenizer.decode(inputs.input_ids[0][answer_start:answer_end + 1]).strip()

    # Convert the predicted command to lowercase
    command_lower = command.lower()

    # Retrieve command details from the database (case-insensitive)
    command_data = list(collection.find({"command": {"$regex": f"^{command_lower}$", "$options": "i"}}))
    return command_data

def find_similar_commands(user_input):
    all_commands = [command["command"] for command in collection.find()]
    similar_commands = get_close_matches(user_input, all_commands, n=3, cutoff=0.6)
    return list(set(similar_commands))  # Convert to set to remove duplicates, then back to list

def generate_response(user_input):
    user_input = user_input.strip()

    # Check if the user is requesting examples or options for a specific command
    if user_input.startswith("examples for "):
        command_name = user_input.replace("examples for ", "").strip()
        command = collection.find_one({"command": command_name})
        if command:
            console.print(f"Examples for {command_name}:")
            for example in command['examples']:
                console.print(f"  - {example}")
        else:
            console.print(f"I couldn't find examples for '{command_name}'.")
        return
    elif user_input.startswith("options for "):
        command_name = user_input.replace("options for ", "").strip()
        command = collection.find_one({"command": command_name})
        if command:
            console.print(f"Options for {command_name}:")
            if command.get('options'):
                for option in command['options']:
                    console.print(f"  - {option}")
            else:
                console.print("No options available.")
        else:
            console.print(f"I couldn't find options for '{command_name}'.")
        return

    command_details = get_command_details(user_input)
    if command_details:
        for cmd in command_details:
            cmd.pop('_id', None)
        display_result_in_table(command_details[0])
    else:
        similar_commands = find_similar_commands(user_input)
        if similar_commands:
            console.print("Did you mean one of these commands?")
            for cmd in similar_commands:
                console.print(f"  - {cmd}")
        else:
            console.print(f"I couldn't find an exact match for '{user_input}'.")

def display_animated_project_name(project_name, duration=5):
    fig = pyfiglet.Figlet(font='slant')
    colors = ["green", "yellow", "magenta", "cyan", "white"]
    start_time = time.time()

    with Live(console=console, refresh_per_second=10) as live:
        while time.time() - start_time < duration:
            for color in colors:
                rendered_text = fig.renderText(project_name)
                colorful_text = Text(rendered_text, style=f"bold {color}")
                live.update(colorful_text)
                time.sleep(0.2)

def show_progress(task_description, total_steps=10):
    with Progress() as progress:
        task = progress.add_task(f"[cyan]{task_description}", total=total_steps)
        for step in range(total_steps):
            time.sleep(0.5)  # Simulating a task
            progress.update(task, advance=1)

def display_result_in_table(result):
    table = Table(title="Command Details")
    table.add_column("Attribute", style="cyan", no_wrap=True)
    table.add_column("Value")

    for key, value in result.items():
        table.add_row(key.capitalize(), str(value))

    console.print(table)

# CLI elements
console = Console()

# Main loop
if __name__ == "__main__":
    project_name = "Linux CommandBot"
    display_animated_project_name(project_name)

    prompt_text = "CommandBot >>"
    formatted_prompt = f"[bold green]{prompt_text}[/bold green]"

    while True:
        console.print(formatted_prompt, style="bold bright_yellow", end=" ")
        user_input = console.input()

        if user_input.lower() == "exit":
            console.print("[bold cyan]Exiting CommandBot. Goodbye![/bold cyan]")
            break

        console.print(f"[bold yellow]Processing input: {user_input}[/bold yellow]")
        show_progress("Processing input")

        generate_response(user_input)
