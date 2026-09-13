from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Footer, Header, Static


class PyChronicleUI(App):
    """Day 1 prototype of the PyChronicle Textual interface."""

    CSS_PATH = "styles.tcss"

    BINDINGS = [
        ("left", "previous_event", "Previous"),
        ("right", "next_event", "Next"),
        ("q", "quit", "Quit"),
    ]

    current_event = 3
    total_events = 5

    def compose(self) -> ComposeResult:
        yield Header()

        with Horizontal(id="main-container"):

            # Execution timeline
            with Vertical(id="timeline-panel"):
                yield Static(
                    "EXECUTION TIMELINE",
                    classes="panel-title"
                )

                yield Static(
                    "● Event 1   Line 1\n"
                    "● Event 2   Line 2\n"
                    "● Event 3   Line 3  ← CURRENT\n"
                    "● Event 4   Line 4\n"
                    "● Event 5   Line 5",
                    id="timeline",
                )

            # Source code
            with Vertical(id="source-panel"):
                yield Static(
                    "SOURCE CODE",
                    classes="panel-title"
                )

                yield Static(
                    "01  def calculate():\n"
                    "02      x = 10\n"
                    "03      y = 20\n"
                    "04      z = x + y\n"
                    "05      print(z)\n\n"
                    "Current execution:\n"
                    "→ Line 4: z = x + y",
                    id="source-code",
                )

            # State inspector
            with Vertical(id="state-panel"):
                yield Static(
                    "STATE INSPECTOR",
                    classes="panel-title"
                )

                yield Static(
                    "Local Variables\n\n"
                    "x = 10\n"
                    "y = 20\n"
                    "z = 30",
                    id="state",
                )

        with Horizontal(id="navigation"):
            yield Static(
                "← Previous State     "
                "Current: Event 3     "
                "Next State →",
                id="navigation-text",
            )

        yield Footer()

    def action_previous_event(self) -> None:
        if self.current_event > 1:
            self.current_event -= 1

        self.update_navigation()

    def action_next_event(self) -> None:
        if self.current_event < self.total_events:
            self.current_event += 1

        self.update_navigation()

    def update_navigation(self) -> None:
        navigation = self.query_one(
            "#navigation-text",
            Static
        )

        navigation.update(
            f"← Previous State     "
            f"Current: Event {self.current_event}     "
            f"Next State →"
        )


if __name__ == "__main__":
    PyChronicleUI().run()
