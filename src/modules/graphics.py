def print_boxed_code(output):
    output_lines = output.split("\n")
    width = max(len(line) for line in output_lines) +2  

    print("┌" + "─" * width + "┐")
    for line in output_lines:
        print(f"│ {line.ljust(width - 2)} │")  
    print("└" + "─" * width + "┘")

