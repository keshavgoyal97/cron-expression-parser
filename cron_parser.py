import sys

from cron_field import Minute, Hour, DayOfMonth, Month, DayOfWeek, Command
from cron_operation import CronExpOperation
from rich.console import Console
from rich.table import Table, Column
from rich.panel import Panel

cron_expression_order = [Minute, Hour, DayOfMonth, Month, DayOfWeek, Command]


def render_table(result):
    console = Console()
    table = Table(title="Cron Parsing Results:", title_style="bold magenta")
    table.add_column("Cron Fields", style="bold cyan", header_style="bold blue", width=20)
    table.add_column("Expanded Values", style="bold green", header_style="bold blue")

    for item in result:
        name, times = item.__dict__()
        table.add_row(name, times)

    panel = Panel.fit(table, title="Parsed Cron Fields", title_align="left", border_style="bright_yellow")
    console.print(panel)


def cron_expression_parser(cron_expr_string):
    cron_expressions = cron_expr_string.split(" ")
    if len(cron_expressions) != len(cron_expression_order):
        print("Invalid input length")

    result = []

    for idx, exp in enumerate(cron_expressions[:-1]):
        cron_field = cron_expression_order[idx]
        if "/" in exp:
            result.append(CronExpOperation.range_step_operation(exp, cron_field))
        elif "*" in exp:
            result.append(CronExpOperation.asterisk_operation(cron_field))
        elif "-" in exp:
            result.append(CronExpOperation.range_operation(exp, cron_field))
        elif "," in exp:
            result.append(CronExpOperation.comma_operation(exp, cron_field))
        else:
            result.append(CronExpOperation.single_value_operation(exp, cron_field))

    result.append(Command(cron_expressions[-1]))
    render_table(result)

    return result


if __name__ == "__main__":
    print(sys.argv)
    cron_expression_parser(sys.argv[1])
