import calendar
from rich.console import Console
from rich.table import Table

def colorful_calendar(year):
    console = Console()
    
    # Loop through all months
    for month in range(1, 13):
        month_name = calendar.month_name[month]
        month_data = calendar.monthcalendar(year, month)
        
        table = Table(title=f"[bold cyan]{month_name} {year}[/bold cyan]", show_lines=True)
        
        # Days of the week
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        styles = ["green", "green", "green", "green", "green", "red", "red"]
        
        for day, style in zip(days, styles):
            table.add_column(day, justify="center", style=style)
        
        # Add the weeks
        for week in month_data:
            table.add_row(*[str(day) if day != 0 else "" for day in week])
        
        console.print(table)
        console.print("\n")

# Call the function for 2025
colorful_calendar(2025)
