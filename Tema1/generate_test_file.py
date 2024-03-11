def generate_large_file(filename, target_size_mb, message):
    target_size = target_size_mb * 1024 * 1024  # Convert MB to bytes
    message_size = len(message)
    num_messages = target_size // message_size # Number of times to repeat the message
    
    with open(filename, 'w') as f:
        for _ in range(num_messages):
            f.write(message + '\n')
    
    print(f"Generated file {filename} with size approximately {target_size_mb}MB.")

# Example usage
message = "This is a sample message for testing. " * 20  # Adjust this to change the message size
generate_large_file("test_file.txt", 200, message)


