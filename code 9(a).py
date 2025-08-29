def count_file_stats(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        num_lines = len(lines)
        num_words = 0
        num_chars = 0

        for line in lines:
            num_chars += len(line)
            num_words += len(line.split())

        print(f"Total Lines: {num_lines}")
        print(f"Total Words: {num_words}")
        print(f"Total Characters: {num_chars}")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
count_file_stats('sample.txt')