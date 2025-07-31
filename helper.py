def print_table(data, sample=False):
    if not data:
        print("No data to display.")
        return

    # Extract headers
    headers = list(data[0].keys())

    # Calculate column widths
    col_widths = {header: max(len(header), max(len(str(row.get(header, ''))) for row in data)) for header in headers}

    # Print header row
    header_row = " | ".join(f"{header:<{col_widths[header]}}" for header in headers)
    separator = "-+-".join("-" * col_widths[header] for header in headers)
    print(header_row)
    print(separator)

    counter = 0
    # Print data rows
    for row in data:
        counter += 1
        print(" | ".join(f"{str(row.get(header, '')):<{col_widths[header]}}" for header in headers))
        if sample and counter >= sample:
            break
