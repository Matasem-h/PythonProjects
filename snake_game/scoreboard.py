from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            # Open the file and check for valid content
            with open("data.txt", mode="r") as data:
                content = data.read().strip()  # Strip whitespace
                self.high_score = int(content) if content.isdigit() else 0
        except (FileNotFoundError, ValueError):  # Handle missing or invalid file
            self.high_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard display."""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        """Reset the current score and update the high score if necessary."""
        if self.score > self.high_score:
            self.high_score = self.score
            # Save the new high score to the file
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """Increase the current score and update the display."""
        self.score += 1
        self.update_scoreboard()
